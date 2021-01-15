---
title: "About"
date: 2018-08-13T23:48:25-04:00
lastmod: 2021-01-14T21:39:21-04:00
description: Engineering manager in Boston, Massachusetts. Interested in product development and data visualization.
name: Renzo Francesco Lucioni
---

<p class="noprint">
  I'm an engineering manager in Boston, Massachusetts. I'm interested in product development and data visualization. I like <a href="https://github.com/rlucioni/recipes">cooking</a> and playing <a href="https://github.com/rlucioni/courtbot">squash</a>.
</p>

<p class="noprint">
  Want to get in touch? Email me at <code>location.hostname.replace('.', '@gmail.')</code>.
</p>

<p class="print">
  Engineering manager in Boston, Massachusetts. Interested in product development and data visualization.
</p>

## Contact

- **Web:** https://renzolucioni.com
- **Email:** renzolucioni@gmail.com
- **GitHub:** https://github.com/rlucioni

## Skills

- **Languages:** Python, JavaScript/Node.js
- **Frameworks:** Django, Express, Flask, React, Redux, Pandas
- **Ops:** Docker, Kubernetes, Helm, Terraform, AWS, GCP, Azure
- **Other Tools:** Postgres, Redis, Elasticsearch, Bigtable, Protobuf, GraphQL, OIDC, Git, Bash

## Experience

**Engineering Manager at [LogRocket](https://logrocket.com/)** (_January 2021 to present_)

- Transitioned from individual contributor to orchestrating and organizing, setting us up to work together as a larger team
- Pushed to split the engineering team into smaller teams
- Led one of those teams, planning work, sharing context, and advancing careers (planning, standups, 1-1s, retros, reviews)
- Put frameworks in place to spread knowledge, teaching others how to interview and how to handle ops-related incidents

**Lead Software Engineer at [LogRocket](https://logrocket.com/)** (_January 2020 to January 2021_)

- Worked to scale LogRocket, cutting costs, making our system more robust, expanding our feature set, increasing MRR, and growing our team
- Introduced dynamic data deletion policies to account for customers with shorter retention. Required developing a way to do fast streaming Bigtable deletes. Let us shed hundreds of TiBs and tens of nodes.
- Simplified user activity tracking, replacing a complex, expensive Redis-backed buffering system with a simple event-based approach involving Elasticsearch
- Cut cloud costs with GCP committed use discounts, E2 VMs, and AWS reservations
- Built support for backing up Bigtable, our 500+ TiB primary datastore, several times a day
- Made data ingestion cheaper by bypassing Pub/Sub where possible and more reliable by adding separate ingestion paths for high volume customers
- Stopped a Redis memory leak from taking down part of our system by finding large, previously-unknown, unused, and non-expiring Celery pidbox keys with RedisInsight, stopping them from being written, then unlinking them
- Identified SDK ingestion problems due to Cloudflare DDoS protection and negotiated with Cloudflare support to mitigate
- Implemented a "path analysis" algorithm for building trees used to visualize overlapping user flows from many sessions
- Integrated LogRocket with New Relic APM distributed tracing, linking from network requests in LogRocket sessions to corresponding backend traces in New Relic
- Increased maximum data retention from 3 months to 2 years, an exercise in reevaluating long-standing assumptions - decoupling video and search data retention, being smarter about ES index use and data retention - and a useful price anchoring tool for the sales team
- Rooted out flaky tests to pave the way for requiring passing tests on PRs and Kodiak PR automerge
- Helped build a great team through referrals, active involvement in the hiring process, and willingness to teach new engineers about the system and our processes
- Promoted a culture of rigorous, valuable code review. Set an example of what it means to give a good code review.

**Software Engineer at [LogRocket](https://logrocket.com/)** (_August 2017 to January 2020_)

- Developed web applications using JavaScript and Python, helping to lay the groundwork for growth
- Improved JavaScript SDK performance and memory usage
- Built error reporting product. Initially called Errors, later became the more general Issues.
- Got LogRocket listed on the GitHub Marketplace
- Reduced cloud costs by optimizing Bigtable, Pub/Sub, GKE, and GCS use
- Built support for deploying the LogRocket backend "on-prem" (on customer-controlled infrastructure) using Terraform, Kubernetes, and Helm
- Secured enterprise contracts by developing, installing, and maintaining our nascent on-prem/self-hosted offering, often working directly with customers
- Researched new product opportunities with Dataflow and Pandas, focusing on finding user frustration
- Increased trial to conversion rate and ACV by planning, building, and shipping new products that became LogRocket's Pro plan (Metrics, retroactive filters)

**Senior Software Engineer at [edX](https://www.edx.org/)** (_July 2017 to August 2017_)

- Implemented GoCD continuous delivery pipelines used to deploy daily
- Automated translation of application text using Jenkins and Transifex

**Software Engineer at [edX](https://www.edx.org/)** (_July 2014 to July 2017_)

- Developed open-source web applications using Python and JavaScript
- Built ecommerce service handling millions of orders
- Maintained services supporting edX programs (grouped courses)
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
