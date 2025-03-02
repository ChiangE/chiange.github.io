---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<span class='anchor' id='about-me'></span>

<!-- I am a final-year Ph.D. student at Zhejiang University (ZJU), will soon be joining the Independent Cyber Security Lab (ICSL) at Huawei, having been selected for the "[Top Minds](https://career.huawei.com/reccampportal/portal5/topminds.html)" program. -->

I obtained my Ph.D. in 2024 and my B.Eng. in 2019 from the College of Electrical Engineering at Zhejiang University, and I currently work as a security researcher.

My doctoral research is under the guidance of <a href='https://scholar.google.com/citations?user=FCsdj0YAAAAJ'>Prof. Wenyuan Xu</a> and <a href='https://scholar.google.com/citations?user=ax6CbMgAAAAJ'>Prof. Yanjiao Chen</a> at ZJU. Recently, I successfully defended my Ph.D. thesis. My research interests revolve around AI (for) security and privacy, with a particular focus on the security and safety of (multimodal) large language models (LLMs) recently. I have contributed to several publications in leading security conferences such as IEEE S&P, USENIX Security, ACM CCS, and NDSS. I am open to academic collaborations and welcome discussions regarding potential research partnerships.

<!-- I received my B.E. degree in the College of Electrical Engineering at Zhejiang University in 2019. -->

The template for this page is credited to [AcadHomepage](https://github.com/RayeRen/acad-homepage.github.io).

<!-- <a href='https://scholar.google.com/citations?user=AE7d_1QAAAAJ'><img src="https://img.shields.io/endpoint?url={{ url | url_encode }}&logo=Google%20Scholar&labelColor=f6f6f6&color=9cf&style=flat&label=citations"></a> -->


# 🔥 News
- *2024.08.31*: &nbsp;🎉🎉 Accepted paper for presentation at the NDSS Symposium 2025!
- *2024.08.24*: &nbsp;🎉🎉 Accepted paper for presentation at the ACM Conference on Computer and Communications Security 2024!
- *2024.05.31*: &nbsp;🎉🎉 Successfully defended my Ph.D. thesis!
- *2024.05.24*: &nbsp;🎉🎉 One paper is accepted by ACM CCS 2024!
- *2024.05.20*: &nbsp;🎉🎉 Attended the 45th IEEE Symposium on Security and Privacy in San Francisco, CA, from May 20th to 23rd.
- *2024.04.04*: &nbsp;🎉🎉 One paper is accepted by ACM CCS 2024!
- *2024.03.09*: &nbsp;🎉🎉 Accepted paper for presentation at the 45th IEEE Symposium on Security and Privacy!


# 📝 Publications 
<div class='paper-box'><div class='paper-box-image'><div><div class="badge">CCS 2024</div><img src='images/legilimens-img.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Legilimens: Practical and Unified Content Moderation for Large Language Model Services](https://arxiv.org/pdf/2408.15488)

Jialin Wu, **Jiangyi Deng** (co-first), Shengyuan Pang, Yanjiao Chen, Jiayang Xu, Xinfeng Li, Wenyuan Xu

[**Code**](https://github.com/lin000001/Legilimens) <strong><span class='show_paper_citations' data='DhtAFkwAAAAJ:ALROH1vI_8AC'></span></strong>
- In this paper, we reveal for the first time that effective and efficient content moderation can be achieved by extracting conceptual features from chat-oriented LLMs, despite their initial fine-tuning for conversation rather than content moderation. We propose a practical and unified content moderation framework for LLM services, named Legilimens, which features both effectiveness and efficiency.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">S&P 2024</div><img src='images/sophon-img.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[SOPHON: Non-Fine-Tunable Learning to Restrain Task Transferability For Pre-trained Models](https://arxiv.org/pdf/2404.12699)

**Jiangyi Deng**, Shengyuan Pang, Yanjiao Chen, Liangming Xia, Yijie Bai, Haiqin Weng, Wenyuan Xu

[**Code**](https://github.com/ChiangE/Sophon) <strong><span class='show_paper_citations' data='DhtAFkwAAAAJ:ALROH1vI_8AC'></span></strong>
- In this paper, we introduce a pioneering learning paradigm, *non-fine-tunable learning*, which prevents the pre-trained model from being fine-tuned to indecent tasks while preserving its performance on the original task.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">USENIX 2023</div><img src='images/revelio-img.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Catch You and I Can: Revealing Source Voiceprint Against Voice Conversion](https://www.usenix.org/system/files/usenixsecurity23-deng-jiangyi-voiceprint.pdf)

**Jiangyi Deng**, Yanjiao Chen, Yinan Zhong, Qianhao Miao, Xueluan Gong, Wenyuan Xu

[**Presentation**](https://www.youtube.com/watch?v=sz7kKZRT5sg) <strong><span class='show_paper_citations' data='DhtAFkwAAAAJ:ALROH1vI_8AC'></span></strong>
- In this paper, we make the first attempt to restore the source voiceprint from audios synthesized by voice conversion methods with high credit. This technique may assist investigations of voice conversion-based phone scam.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">USENIX 2023</div><img src='images/vcloak-img.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[V-Cloak: Intelligibility-, Naturalness- & Timbre-Preserving Real-Time Voice Anonymization](https://www.usenix.org/system/files/usenixsecurity23-deng-jiangyi-v-cloak.pdf)

**Jiangyi Deng**, Fei Teng, Yanjiao Chen, Xiaofu Chen, Zhaohui Wang, Wenyuan Xu

[**Demo**](https://v-cloak.github.io/) [**Code**](https://github.com/V-Cloak/V-Cloak) [**Presentation**](https://www.youtube.com/watch?v=bDVgfSyjPDo) <strong><span class='show_paper_citations' data='DhtAFkwAAAAJ:ALROH1vI_8AC'></span></strong>
- In this paper, we develop a voice anonymization system, named V-Cloak, which attains real-time voice anonymization while preserving the intelligibility, naturalness and timbre of the audio.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">CCS 2022</div><img src='images/fencesitter-img.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[FenceSitter: Black-box, Content-Agnostic, and Synchronization-Free Enrollment-Phase Attacks on Speaker Recognition Systems](https://dl.acm.org/doi/10.1145/3548606.3559357)

**Jiangyi Deng**, Yanjiao Chen, Wenyuan Xu

[**Presentation**](https://dl.acm.org/doi/10.1145/3548606.3559357) <strong><span class='show_paper_citations' data='DhtAFkwAAAAJ:ALROH1vI_8AC'></span></strong>
- In this paper, we explore a new attack surface of SRSs by presenting an enrollment-phase attack paradigm, named FenceSitter, where the adversary poisons the SRS using imperceptible adversarial ambient sound when the legitimate user registers into the SRS.
</div>
</div>


- [SafeGen: Mitigating Unsafe Content Generation in Text-to-Image Models](https://arxiv.org/abs/2404.06666). Xinfeng Li, Yuchen Yang, **Jiangyi Deng** (co-first), Chen Yan, Yanjiao Chen, Xiaoyu Ji, Wenyuan Xu. *ACM CCS*, 2024.

- [Alchemy: Data-Free Adversarial Training](). Yijie Bai, Zhongming Ma, Yanjiao Chen, **Jiangyi Deng**, Shengyuan Pang, Yan Liu, Wenyuan Xu. *ACM CCS*, 2024.

- [Dr. Defender: Proactive Detection of Autopilot Drones based on CSI](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=10239182). **Jiangyi Deng**, Xiaoyu Ji, Beibei Wang, Bin Wang, Wenyuan Xu. *IEEE TIFS*, 2023.

- [A Nonlinearity-based Secure Face-to-Face Device Authentication for Mobile Devices](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=9200789). Xiaoyu Ji, Xinyan Zhou, Chen Yan, **Jiangyi Deng**, Wenyuan Xu. *IEEE TMC*, 2020.

- [Nauth: Secure face-to-face device authentication via nonlinearity](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=8737572). Xinyan Zhou, Xiaoyu Ji, Chen Yan, **Jiangyi Deng**, Wenyuan Xu. *IEEE INFOCOM*, 2019.


# 🎖 Honors and Awards
- *2024.09*: ACM SIGSAC China Doctoral Dissertation award, ACM SIGSAC China
- *2024.03*: Sun Youxian Scholarship, Zhejiang University
- *2024.03*: Outstanding Graduate, Zhejiang University
- *2023.10*: National Scholarship, Zhejiang University
- *2023.09*: Outstanding Graduate Student Cadre, Zhejiang University
- *2023.09*: Outstanding Graduate Student, Zhejiang University
- *2022.09*: Outstanding Graduate Student Cadre, Zhejiang University
- *2020.09*: Outstanding Graduate Student, Zhejiang University

<!-- # 📖 Educations
- *2019.09 - 2024.06 (present)*, Ph.D.
- *2015.09 - 2019.09*, Undergraduate-->

<!-- # 💬 Invited Talks
- *2021.06*, Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet. 
- *2021.03*, Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet.  \| [\[video\]](https://github.com/) -->

# 📖 Services
- Reviewer of *IEEE Transactions on Information Forensics and Security*
- Reviewer of *ACM Transactions on Privacy and Security*
- External Reviewer of "Big Four", *i.e.*, *IEEE S&P*, *USENIX Security*, *ACM CCS*, and *NDSS*
- Teaching Assistant of *AI and IOT*, at Zhejiang University, *2021.9 - 2022.1*, *2022.9 - 2023.1*
- Teaching Assistant of *Computer Networking*, at Zhejiang University, *2020.9 - 2021.1*, *2021.2 - 2021.6*

# 💻 Internships
- *2023.05 - 2024.02*, Department of Fundamental Security, [Ant Group](https://www.antgroup.com/), China.

<!-- # 🗺️ Visitor Map

<script type="text/javascript" src="//rf.revolvermaps.com/0/0/6.js?i=5kfn1jf6u04&amp;m=7&amp;c=e63100&amp;cr1=ffffff&amp;f=arial&amp;l=0&amp;bv=90&amp;lx=-420&amp;ly=420&amp;hi=20&amp;he=7&amp;hc=a8ddff&amp;rs=80" async="async"></script> -->