---
title: About
description: Director of Research Engineering at LogRocket. Interested in product development and data visualization.
date: 2018-08-13T23:48:25-04:00
lastmod: 2024-07-30T23:08:00-04:00
layout: about.liquid
---

<p class="noprint">
  I'm Director of Research Engineering at LogRocket. I'm interested in product development and data visualization. I like gardening, <a href="https://github.com/rlucioni/recipes">cooking</a>, and playing squash.
</p>

<p class="noprint">
  Want to get in touch? Email me at <code>location.hostname.replace('.', '@gmail.')</code>.
</p>

<p class="print">
  Director of Research Engineering at LogRocket. Interested in product development and data visualization.
</p>

## Contact

- **Web:** https://renzolucioni.com
- **Email:** renzolucioni@gmail.com
- **GitHub:** https://github.com/rlucioni

## Skills

- **Languages:** Python, JavaScript/Node.js, Bash
- **Web Frameworks:** Django, Flask, Express, React
- **Ops:** Kubernetes, Docker, Helm, Terraform, GCP, AWS
- **Data Science/AI/ML:** Jupyter, LLMs and embeddings (OpenAI, Google, Anthropic, etc.), Pandas, BigQuery, Vertex AI
- **Other:** Pub/Sub, Bigtable, Postgres, Redis, Elasticsearch, GraphQL, OIDC, Git

## Experience

### Director of Research Engineering at [LogRocket](https://logrocket.com/) (July 2024-present)

- Leading development of new features that make it faster and easier for customers to benefit from the data LogRocket collects. Visibility into the user experience shouldn't require customers to spend hours watching sessions or learning to navigate a complex UI.
- Shipped Highlights in collaboration with our Replay engineering team. Highlights accelerates review of LogRocket sessions by summarizing them in natural language, individually and in aggregate, complete with inline links to key moments.
- Shipped a modified version of Highlights capable of using user-submitted content from support tickets to guide summarization and discover relevant user experience details, reducing ticket handle time by contextualizing users' requests for support agents. Fixed long-standing issues with LogRocket's Intercom and Zendesk integrations at the same time.
- Improved Issue classification and description capabilities, increasing precision without sacrificing too much recall. Explored multiclass classification to account for problems like UI/UX issues that don't fit neatly into binary severity buckets.
- Shipped Funnel Insights in collaboration with our Analytics engineering team. Funnel Insights guides customers towards ideas that could improve conversion by using natural language to explain how the behavior of users who don't complete a conversion funnel differs from that of converting users, providing supporting examples and estimating frequency for each pattern identified.
- Applied for a patent covering techniques for automatically summarizing digital experiences (63/760090)
- Managing LogRocket's relationship with OpenAI and Google to ensure that generative AI API spend or usage limits will accommodate our growth
- Promoting eval-based development of new AI features
- Developing Ask Galileo, an AI agent that autonomously operates LogRocket's product to answer customer queries

### Senior Engineering Manager at [LogRocket](https://logrocket.com/) (September 2021-July 2024)

- Advocated strongly for use of machine learning in LogRocket's product, specifically to improve Issues. Our AI-based "Galileo" suite of features became the most highly anticipated product launch in company history with over 500 customers on the waiting list.
- Established a small research team focused on training an in-house issue classification model that could be used to automatically recommend important issues to our customers, accelerating the triage process and increasing engagement with Issues
- Developed tools and processes needed to train and continuously improve machine learning models for predicting issue severity. Included collecting and preparing training data, feature engineering, getting familiar with Vertex AI, BigQuery, Jupyter, and Pandas, measuring model performance, and transforming probabilities output by the model into a metric that made sense in the context of the product.
- Validated model quality while enabling our small Proactive Insights team to punch above their weight by using the model to produce early, human-in-the-loop issue recommendations for customers (e.g., Issues Digest)
- Integrated the model with LogRocket's production systems in collaboration with our Issues engineering team. Our issue classification pipeline serves predictions for millions of sessions a day from all LogRocket Pro customers.
- Continued to spearhead work on Galileo by researching, developing, and deploying a method for using LLMs to generate natural language issue descriptions, reducing false positive issue classifications at the same time. This work grew Galileo into a collection of AI-based features that reshaped our product roadmap by generating significant customer interest and setting us apart from competitors.
- Patented our approach to automatic triage and description of software issues ([US12332767B2](https://patents.google.com/patent/US12332767B2))
- Broke ground on multimodal (text and image-based) session summarization, work that formed the basis of future Galileo features. Developed a "usage summaries" proof of concept demonstrating the feasibility of - and customer excitement around - using LLMs to summarize and query LogRocket sessions in natural language.

### Engineering Manager at [LogRocket](https://logrocket.com/) (January 2021-September 2021)

- Supported growth of LogRocket's single engineering team into smaller teams focused on different parts of the product
- Led and grew an engineering team of 8-10 people. We delivered limited-lookback conditional recording, new Issue types, a major redesign of the LogRocket dashboard, the vertical event timeline in session replay, improved iframe recording support, and integrations with NPS tools.
- Acting as tech lead, shipped changes to improve performance and make our system more robust. Added incremental timeseries caching using Redis. Removed Kubernetes CPU limits unnecessarily throttling our containers. Removed Cloudflare's proxy from our event ingestion endpoint, preventing our SDK's request rate from triggering Cloudflare's DDoS protection and taking down this critical endpoint; simultaneously switched to use of Let's Encrypt TLS certificates via cert-manager. Added a dedicated asset caching worker to help stabilize backend event processing. Significantly reduced an internal exception processing service's Redis usage, improving stability and cutting that service's costs by 3 orders of magnitude.
- Wrote handbooks for the rest of the engineering team to unsilo knowledge, specifically guides to the entire engineering interview process and handling ops-related incidents

### Lead Software Engineer at [LogRocket](https://logrocket.com/) (January 2020-January 2021)

- Scaled LogRocket, controlling costs, making our system more robust, expanding our feature set, increasing MRR, and growing our team
- Introduced dynamic data deletion policies to account for customers with shorter retention. Required developing a way to do fast streaming Bigtable deletes. Let us shed hundreds of tebibytes and tens of nodes.
- Simplified user activity tracking, replacing a complex and expensive Redis-backed buffering system with a simple event-based approach involving Elasticsearch
- Reduced cloud costs by organizing for GCP committed use discounts, E2 VMs, and AWS reservations
- Built support for backing up Bigtable, our 500+ TiB primary datastore, several times a day
- Made data ingestion cheaper by bypassing Pub/Sub where possible, and more reliable by adding separate ingestion pathways for high volume customers
- Stopped a Redis memory leak from taking down part of our system by finding large, previously-unknown, unused, and non-expiring Celery pidbox keys with RedisInsight, stopping them from being written, then unlinking them
- Identified SDK ingestion problems due to Cloudflare DDoS protection and negotiated with Cloudflare's support team to mitigate
- Implemented a "path analysis" algorithm for building trees used to visualize overlapping user flows from many sessions
- Integrated LogRocket with New Relic APM distributed tracing, linking from network requests in LogRocket sessions to corresponding backend traces in New Relic
- Increased maximum data retention we could sell from 3 months to 2 years, an exercise in reevaluating long-standing assumptions - decoupling video and search data retention, being smarter about ES index use and data archival - and a useful price anchoring tool for the sales team
- Rooted out flaky tests to pave the way for requiring passing tests on PRs and Kodiak PR automerge
- Helped build a great team through referrals, active involvement in the hiring process, and willingness to teach new engineers about the system and our processes
- Promoted a culture of rigorous, valuable code review. Set an example of what it means to give a good code review.

### Software Engineer at [LogRocket](https://logrocket.com/) (August 2017-January 2020)

- Developed web applications using JavaScript and Python
- Improved JavaScript SDK performance and memory usage
- Built error reporting product. Initially called Errors, later became Issues.
- Listed LogRocket on GitHub Marketplace
- Reduced cloud spend by optimizing use of Bigtable, Pub/Sub, GKE, and GCS
- Built support for customer self-hosted deployment of the LogRocket backend using Terraform, Kubernetes, and Helm
- Secured enterprise contracts by developing, installing, and maintaining our self-hosted offering, working directly with customers
- Researched new product opportunities with Dataflow and Pandas, focused on finding user frustration
- Increased trial to conversion rate and ACV by planning, building, and shipping new products that became LogRocket's Pro plan (e.g., Metrics, retroactive filters)

### Senior Software Engineer at [edX](https://www.edx.org/) (July 2017-August 2017)

- Implemented GoCD continuous delivery pipelines used to deploy daily
- Automated translation of application text using Jenkins and Transifex

### Software Engineer at [edX](https://www.edx.org/) (July 2014-July 2017)

- Developed open-source web applications using Python and JavaScript
- Built ecommerce service handling millions of orders
- Maintained services supporting edX Programs (grouped courses)
- Scaled metadata service underpinning edX products
- Load tested new applications and features with Locust

### Freelancer at [The Economist](https://www.economist.com/) (December 2013-November 2014)

- Created data visualizations for use by the paper, online and in print

### Intern at [edX](https://www.edx.org/) (May 2013-June 2014)

- Implemented inline problem scoring
- Built lightweight A/B testing framework using Django Waffle
- Instrumented platform with Google Analytics and Mixpanel

## Education

### Harvard University (September 2010-May 2014)

Bachelor of Arts in Computer Science, secondary field in Government
