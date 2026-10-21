"""Fetch Google Scholar citation data and write it to results/*.json.

The GitHub Actions workflow (.github/workflows/google_scholar_crawler.yaml) commits
results/gs_data.json and results/gs_data_shieldsio.json to the google-scholar-stats
branch, which the site reads through jsDelivr.
"""

import json
import os
import sys
import time
from datetime import datetime

from scholarly import scholarly

SCHOLAR_ID = os.environ.get("GOOGLE_SCHOLAR_ID")
MAX_ATTEMPTS = 3


def fetch_author(scholar_id: str) -> dict:
    author = scholarly.search_author_id(scholar_id)
    scholarly.fill(author, sections=["basics", "indices", "counts", "publications"])
    return author


def main() -> int:
    if not SCHOLAR_ID:
        print("GOOGLE_SCHOLAR_ID is not set", file=sys.stderr)
        return 1

    author = None
    for attempt in range(1, MAX_ATTEMPTS + 1):
        try:
            author = fetch_author(SCHOLAR_ID)
            break
        except Exception as exc:  # noqa: BLE001 - Google Scholar is flaky, we retry
            print(f"[attempt {attempt}/{MAX_ATTEMPTS}] {type(exc).__name__}: {exc}", file=sys.stderr)
            if attempt == MAX_ATTEMPTS:
                print("giving up after repeated failures", file=sys.stderr)
                return 1
            time.sleep(15 * attempt)

    author["updated"] = str(datetime.now())
    author["publications"] = {v["author_pub_id"]: v for v in author["publications"]}

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

    print(
        f"{author.get('name')}: citedby={author.get('citedby')} "
        f"hindex={author.get('hindex')} publications={len(author['publications'])}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
