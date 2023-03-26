---
title: "About"
date: 2018-08-13T23:48:25-04:00
lastmod: 2021-01-14T21:39:21-04:00
description: Senior engineering manager in Boston, Massachusetts. Interested in product development and data visualization.
name: Renzo Francesco Lucioni
---

<p class="noprint">
  I'm a senior engineering manager in Boston, Massachusetts. I'm interested in product development and data visualization. I like <a href="https://github.com/rlucioni/recipes">cooking</a> and playing squash.
</p>

<p class="noprint">
  Want to get in touch? Email me at <code>location.hostname.replace('.', '@gmail.')</code>.
</p>

<p class="print">
  Senior engineering manager in Boston, Massachusetts. Interested in product development and data visualization.
</p>

## Contact

- **Web:** https://renzolucioni.com
- **Email:** renzolucioni@gmail.com
- **GitHub:** https://github.com/rlucioni

## Skills

- **Languages:** Python, JavaScript/Node.js, Bash
- **Web Frameworks:** Django, Express, Flask, React
- **Ops:** Kubernetes, Docker, Helm, Terraform, GCP, AWS
- **Data Science:** Jupyter, Pandas, BigQuery, Vertex AI
- **Other:** Pub/Sub, Bigtable, Postgres, Redis, Elasticsearch, GraphQL, OIDC, Git

## Experience

**Senior Engineering Manager at [LogRocket](https://logrocket.com/)** (_September 2021 to present_)

- Advocated strongly for use of machine learning in LogRocket's product, specifically to improve Issues. Our ML-based "Galileo" suite of features later became the most highly anticipated product launch in company history with over 500 companies on the waiting list.
- Established a small data science/ML team focused on developing an issue classification model that could be used to automatically recommend important issues to our customers, accelerating the triage process and increasing engagement with Issues.
- Led development of tools and processes needed to train and continuously improve machine learning models for predicting issue severity. This included collecting and preparing training data, feature engineering, getting familiar with Vertex AI, BigQuery, Jupyter, and Pandas, measuring model performance, and transforming raw model output into a metric that made sense in the context of the product.
- Validated model quality while helping the Proactive Insights team punch above their weight by using the model to deliver early, human-in-the-loop issue recommendations to customers (e.g., Proactive Insights, Issues Digest).
- Integrated the model with LogRocket's production system in collaboration with the Issues engineering team. Our issue classification pipeline was capable of serving predictions for all LogRocket Pro customers (i.e., millions of sessions a day).
- Worked on a patent application for automatic issue triage.

**Engineering Manager at [LogRocket](https://logrocket.com/)** (_January 2021 to September 2021_)

- Helped organize LogRocket's engineering team into smaller teams focused on different parts of the product.
- Led and grew an engineering team. We delivered substantial new product to customers, including limited-lookback conditional recording, new Issue types, a major redesign of the LogRocket dashboard, the vertical event timeline in session replay, improved iframe recording support, and integrations with NPS tools.
- Acting as tech lead, shipped changes to improve performance and make our system more robust. Added incremental timeseries caching using Redis. Removed Kubernetes CPU limits unnecessarily throttling our containers. Removed the Cloudflare proxy from our event ingestion endpoint, preventing our SDK's request rate from triggering Cloudflare's DDoS protection and taking down this critical endpoint; simultaneously switched to use of Let's Encrypt TLS certificates via cert-manager. Added a dedicated asset caching worker to help stabilize event processing. Significantly reduced an internal exception processing service's Redis usage, improving stability and cutting costs by 3 orders of magnitude.
- Wrote handbooks for the rest of the engineering team to help spread siloed knowledge, specifically guides to the entire engineering interview process and handling ops-related incidents.

**Lead Software Engineer at [LogRocket](https://logrocket.com/)** (_January 2020 to January 2021_)

- Worked to scale LogRocket, keep costs under control, make our system more robust, expand our feature set, increase MRR, and grow our team
- Introduced dynamic data deletion policies to account for customers with shorter retention. Required developing a way to do fast streaming Bigtable deletes. Let us shed hundreds of tebibytes and tens of nodes.
- Simplified user activity tracking, replacing a complex and expensive Redis-backed buffering system with a simple event-based approach involving Elasticsearch
- Reduced cloud costs with GCP committed use discounts, E2 VMs, and AWS reservations
- Built support for backing up Bigtable, our 500+ TiB primary datastore, several times a day
- Made data ingestion cheaper by bypassing Pub/Sub where possible, and more reliable by adding separate ingestion pathways for high volume customers
- Stopped a Redis memory leak from taking down part of our system by finding large, previously-unknown, unused, and non-expiring Celery pidbox keys with RedisInsight, stopping them from being written, then unlinking them
- Identified SDK ingestion problems due to Cloudflare DDoS protection and negotiated with Cloudflare's support team to mitigate
- Implemented a "path analysis" algorithm for building trees used to visualize overlapping user flows from many sessions
- Integrated LogRocket with New Relic APM distributed tracing, linking from network requests in LogRocket sessions to corresponding backend traces in New Relic
- Increased maximum supported data retention from 3 months to 2 years, an exercise in reevaluating long-standing assumptions - decoupling video and search data retention, being smarter about ES index use and data archival - and a useful price anchoring tool for the sales team
- Rooted out flaky tests to pave the way for requiring passing tests on PRs and Kodiak PR automerge
- Helped build a great team through referrals, active involvement in the hiring process, and willingness to teach new engineers about the system and our processes
- Promoted a culture of rigorous, valuable code review. Set an example of what it means to give a good code review.

**Software Engineer at [LogRocket](https://logrocket.com/)** (_August 2017 to January 2020_)

- Developed web applications using JavaScript and Python
- Improved JavaScript SDK performance and memory usage
- Built error reporting product. Initially called Errors, later became the more general Issues.
- Listed LogRocket on the GitHub Marketplace
- Reduced cloud spend by optimizing our use of Bigtable, Pub/Sub, GKE, and GCS
- Built support for on-prem (i.e., on customer-controlled infrastructure) deployment of the LogRocket backend using Terraform, Kubernetes, and Helm
- Secured enterprise contracts by developing, installing, and maintaining our on-prem/self-hosted offering, often working directly with customers
- Researched new product opportunities with Dataflow and Pandas, focused on finding user frustration
- Increased trial to conversion rate and ACV by planning, building, and shipping new products that became LogRocket's Pro plan (e.g., Metrics, retroactive filters)

**Senior Software Engineer at [edX](https://www.edx.org/)** (_July 2017 to August 2017_)

- Implemented GoCD continuous delivery pipelines used to deploy daily
- Automated translation of application text using Jenkins and Transifex

**Software Engineer at [edX](https://www.edx.org/)** (_July 2014 to July 2017_)

- Developed open-source web applications using Python and JavaScript
- Built ecommerce service handling millions of orders
- Maintained services supporting edX Programs (grouped courses)
- Scaled metadata service underpinning edX products
- Load tested new applications and features with Locust

**Freelancer at [The Economist](https://www.economist.com/)** (_December 2013 to November 2014_)

- Created data visualizations for use by the paper, online and in print

**Intern at [edX](https://www.edx.org/)** (_May 2013 to June 2014_)

- Implemented inline problem scoring
- Built lightweight A/B testing framework using Django Waffle
- Instrumented platform with Google Analytics and Mixpanel

## Education

**Harvard College** (_September 2010 to May 2014_)

Bachelor of Arts in Computer Science, secondary field in Government
