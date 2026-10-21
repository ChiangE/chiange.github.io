"""Fetch Google Scholar citation data and write it to results/*.json.

The GitHub Actions workflow (.github/workflows/google_scholar_crawler.yaml) commits
results/gs_data.json and results/gs_data_shieldsio.json to the google-scholar-stats
branch, which the site reads through jsDelivr.

Reliability notes: Google Scholar regularly answers GitHub runner IPs with 403/429 or
a CAPTCHA. ``scholarly`` handles that badly -- its retry loop sleeps 60-120s per
iteration and does not count those iterations against its retry budget, which is how
this job used to spend ~36 minutes before failing. An in-process alarm does not help
either, because that same loop swallows every exception. So the fetch runs in a child
interpreter that is killed by a hard timeout, and the parent decides the outcome.
"""

import json
import os
import signal
import subprocess
import sys
import tempfile
import time
from datetime import datetime

SCHOLAR_ID = os.environ.get("GOOGLE_SCHOLAR_ID")
MAX_ATTEMPTS = int(os.environ.get("CRAWL_ATTEMPTS", "2"))
ATTEMPT_TIMEOUT = int(os.environ.get("CRAWL_ATTEMPT_TIMEOUT", "150"))
SECTIONS = ["basics", "indices", "counts", "publications"]


class FetchFailed(RuntimeError):
    """Raised when one fetch attempt does not produce data."""


class FetchTimeout(FetchFailed):
    """Raised when one fetch attempt exceeds its time budget."""


def fetch_author(scholar_id: str) -> dict:
    """Query Google Scholar. Runs inside the child interpreter."""
    from scholarly import scholarly

    try:
        scholarly.set_retries(2)
    except Exception as exc:  # noqa: BLE001 - best effort, older versions differ
        print(f"could not lower scholarly retries: {exc}", file=sys.stderr)

    author = scholarly.search_author_id(scholar_id)
    scholarly.fill(author, sections=SECTIONS)
    return author


def run_child(out_path: str) -> None:
    author = fetch_author(SCHOLAR_ID)
    with open(out_path, "w", encoding="utf-8") as outfile:
        json.dump(author, outfile, ensure_ascii=False)


def fetch_once() -> dict:
    """Run one fetch in a child process that can be killed at any moment."""
    handle, out_path = tempfile.mkstemp(prefix="gs_data_", suffix=".json")
    os.close(handle)
    env = dict(os.environ, CRAWL_CHILD_OUTPUT=out_path)
    proc = subprocess.Popen(
        [sys.executable, os.path.abspath(__file__), "--fetch-once"],
        env=env,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        start_new_session=True,
    )
    timed_out = False
    try:
        stdout, stderr = proc.communicate(timeout=ATTEMPT_TIMEOUT)
    except subprocess.TimeoutExpired:
        timed_out = True
        try:
            os.killpg(os.getpgid(proc.pid), signal.SIGKILL)
        except ProcessLookupError:
            pass
        stdout, stderr = proc.communicate()

    try:
        if timed_out:
            raise FetchTimeout(f"no response from Google Scholar within {ATTEMPT_TIMEOUT}s")
        if proc.returncode != 0:
            tail = (stderr or stdout or "").strip().splitlines()[-3:]
            raise FetchFailed(f"fetch failed (exit {proc.returncode}): {' / '.join(tail)}")
        with open(out_path, encoding="utf-8") as infile:
            return json.load(infile)
    finally:
        try:
            os.unlink(out_path)
        except OSError:
            pass


def write_results(author: dict) -> None:
    os.makedirs("results", exist_ok=True)
    with open("results/gs_data.json", "w", encoding="utf-8") as outfile:
        json.dump(author, outfile, ensure_ascii=False)

    shieldsio_data = {
        "schemaVersion": 1,
        "label": "citations",
        "message": f"{author['citedby']}",
    }
    with open("results/gs_data_shieldsio.json", "w", encoding="utf-8") as outfile:
        json.dump(shieldsio_data, outfile, ensure_ascii=False)


def main() -> int:
    if "--fetch-once" in sys.argv:
        out_path = os.environ["CRAWL_CHILD_OUTPUT"]
        run_child(out_path)
        return 0

    if not SCHOLAR_ID:
        print("GOOGLE_SCHOLAR_ID is not set", file=sys.stderr)
        return 1

    author = None
    for attempt in range(1, MAX_ATTEMPTS + 1):
        try:
            author = fetch_once()
            break
        except Exception as exc:  # noqa: BLE001 - Google Scholar is flaky, we retry
            print(
                f"[attempt {attempt}/{MAX_ATTEMPTS}] {type(exc).__name__}: {exc}",
                file=sys.stderr,
            )
            if attempt == MAX_ATTEMPTS:
                print(
                    "giving up: Google Scholar did not return data "
                    "(usually 403/429 rate limiting or a CAPTCHA for the runner IP)",
                    file=sys.stderr,
                )
                return 1
            time.sleep(20 * attempt)

    author["updated"] = str(datetime.now())
    author["publications"] = {v["author_pub_id"]: v for v in author["publications"]}
    write_results(author)

    print(
        f"{author.get('name')}: citedby={author.get('citedby')} "
        f"hindex={author.get('hindex')} publications={len(author['publications'])}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
