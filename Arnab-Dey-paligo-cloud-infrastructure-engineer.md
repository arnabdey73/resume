<div align="center">
	<h1><b>Arnab Dey</b></h1>
	<p>
		Stockholm, Sweden | +46 0764516092 | <a href="mailto:arnabdey009@gmail.com">arnabdey009@gmail.com</a><br>
		<a href="https://www.linkedin.com/in/arnabdey73">LinkedIn</a> | <a href="https://github.com/arnabdey73">GitHub</a>
	</p>
</div>

---

## Professional Summary

Cloud Infrastructure Engineer with **9+ years focused on cloud and platform engineering** and deep hands-on AWS experience — EKS, EC2, S3, IAM, KMS, VPC, CloudWatch — built and operated as code with Terraform, Ansible, and Python. I design infrastructure around reliability, security, and developer self-service: version-controlled, reviewable, reproducible, and cheap to rebuild. Comfortable owning the full lifecycle of a SaaS platform — provisioning, CI/CD, observability, on-call. Based in Stockholm, fluent in English, Swedish at SFI C-level.

---

## Core Skills

**AWS** — EC2, EKS, S3, VPC, IAM, ECR, ALB, CloudWatch, KMS; production platform design, cost optimisation, least-privilege IAM, multi-environment delivery

**Infrastructure as Code** — Terraform (AWS, Azure, OpenStack providers), reusable module libraries, Ansible; fluent with IaC patterns transferable to CloudFormation / AWS CDK

**Scripting & Automation** — Python (automation, CLI tooling, REST API integration), Bash, PowerShell; day-to-day use of AI coding assistants (Claude Code, Copilot) as part of the development loop

**CI/CD & GitOps** — GitHub Actions, GitLab CI, Jenkins, ArgoCD, Azure DevOps Pipelines; PR-driven `plan`/`apply` workflows, trunk-based delivery

**Containers & Orchestration** — Kubernetes (EKS, K3s, Rancher RKE, AKS), Docker, Helm

**Observability** — Prometheus, Grafana, ELK Stack (Elasticsearch, Logstash, Kibana), CloudWatch, Azure Monitor / Log Analytics; dashboards, alerting design, log aggregation

**Security & Governance** — IAM least-privilege, RBAC, encryption at rest (KMS / Key Vault), secret management (sealed-secrets, Key Vault), credential rotation, compliance auditing

**Languages** — English (fluent), Swedish (SFI C-level)

---

## Professional Experience

### DevOps Engineer — AFRY Digital Solutions AB
*May 2025 – Present  |  Stockholm, Sweden*

**Assignment: Ericsson AB — CI Engineer, Tiger Test Tools (Sep 2025 – Present)**
- Maintain and support end-to-end CI for radio-communication smoke and regression testing — Git, Gerrit, Jenkins, Docker, Linux.
- Troubleshoot cross-cutting pipeline and hardware issues across daily delivery and validation workflows.

**GitOps Platform (internal reference project)**
- Designed and deployed a GitOps-based Kubernetes platform (K3s + ArgoCD + Prometheus + Grafana + cert-manager + sealed-secrets) as a live cloud-native operations reference — publicly maintained on GitHub.

---

### Cloud Engineer — Stena Metall AB
*Aug 2024 – Jan 2025  |  Gothenburg, Sweden*

Cloud Infrastructure Engineer on the central Cloud Office of a production Azure estate — ~100 subscriptions across a multi-management-group hierarchy supporting a multi-billion-SEK industrial group.

- **Designed and shipped a ransomware-resilience RBAC control** — custom role definitions enforcing separation-of-duties between resource management and backup deletion, closing a gap in Azure's built-in Contributor role. Delivered through the CAF archetype framework via Terraform + Azure DevOps across ~100 subscriptions.
- Delivered a **tenant-wide Key Vault compliance audit** — KQL against Azure Resource Graph for soft-delete retention, purge protection, and RBAC authorisation — producing CSV inventories and a documented review for architecture leadership.
- **Service Principal lifecycle tooling** — KQL audit for 30-day create/update/delete events, PowerShell for expiring-credential inventory, and a design for client-secret rotation via Logic Apps + Graph API `addPassword`.
- Implemented **Backup policy compliance reporting** with per-VM exempt-rationale tracking.
- KQL-based monitoring contributed to a **~20% reduction in downtime** across supported services.
- Published sanitized sister repos on GitHub including [`iac-azure-core-governance`](https://github.com/arnabdey73/iac-azure-core-governance) (CAF Enterprise Scale governance platform).

---

### Senior Software Engineer (DevOps) — Capgemini Sverige AB
*Sep 2021 – Jul 2024  |  Gothenburg, Sweden*

**Assignment: Volvo Cars — Car Safety R&D (MLOps / AI Platform)**

*Self-service Databricks platform via GitOps*
- Designed and owned a **GitOps self-service pattern for Azure Databricks**: data scientists request compute via an issue template → YAML manifest PR → GitHub Actions validates and plans changes for review → merge triggers deployment.
- Authored the Terraform module with governance-friendly defaults baked in: single-user security mode, 30-minute auto-termination, autoscale, cluster-log shipping, restricted permissions — making clusters cheap and safe by construction.
- **Outcome:** provisioning lead time dropped from days to same-day; every cluster traceable to a PR and named owner; eliminated idle-cluster spend.

*Dual-cloud ML storage benchmarking*
- Built **two matched Terraform stacks** — AWS (EC2 + S3 + KMS + IAM) and Azure (Linux VM + Premium BlockBlobStorage) — as identically-shaped, disposable test rigs for MLCommons-style object-storage benchmarks. Owned Terraform, IAM, dataset storage, and tear-down.

*CAE HPC platform modernisation (on-prem)*
- Contributed to modernising a ~36-node CAE/HPC cluster supporting ML research: OS migration from SLES to Ubuntu LTS, stand-up of **Rancher-managed Kubernetes (RKE)** with worker fleet, **Kubeflow** installation via Helm for ML engineers.
- Built a **production-grade ELK stack** (Elasticsearch, Logstash, Kibana) on LXD with X-Pack security, SSL, and snapshot repositories — full-fleet observability for ML workload monitoring and log aggregation.
- Authored **Ansible roles** within the shared GitLab-managed codebase.

*Other*
- Led the internal **AI-powered Resume Builder Agent** as a side project — [`sanitized public repo`](https://github.com/arnabdey73/resume-builder-agent).

---

### Senior Business Consultant (DevOps) — Tech Mahindra
*Feb 2017 – Sep 2021 | Bangalore, India | Sydney, Australia*

**Assignment: Cisco Systems — CD 2.0 on AWS** *(Technical Lead from mid-2019)*
- **Authored the Terraform** for Cisco's CD 2.0 continuous-delivery platform on AWS — VPC, subnets, security groups, **EKS cluster, IAM roles, Jenkins on EKS, ECR, ALB, DNS** — extending an internal reference architecture originally built on on-prem OpenShift.
- Built a separate **AWS observability environment** — EKS, Prometheus Operator via Helm, Grafana, persistent storage, ingress.
- **Closed out Cisco's long-running SVN-to-Git migration** by writing a Python automation that enumerated SVN repos, extracted history, provisioned Bitbucket repos via REST API, and pushed converted Git history — with retry logic and batching around SCM rate limits.
- Onboarded application teams to the platform through CI engagement templates, Bitbucket provisioning, and Jenkinsfile adaptation.

**Assignment: Deutsche Telekom — 5G BSS Slicing Pilot on OpenStack** *(Technical Lead, mid-2020 – Aug 2021)*
- Owned the **DevOps platform side** of DT's 5G Network Slicing commercial pilot — accountable for operational reliability of a ~30-microservice BSS suite.
- Wrote **Terraform against the OpenStack provider** for networks, subnets, security groups, VMs, floating IPs — provisioning the Jenkins / Nexus / Tuleap / Rancher / Keycloak / ELK estate.
- Designed and ran **~46 Jenkins jobs** building microservices, tagging with build number + short git SHA, pushing to internal Nexus registry, updating Kubernetes manifests, and triggering Rancher rolling updates.
- Owned the **cross-tenant migration** when the pilot moved tenants: Python/shell automation to clone 54 Tuleap repos, re-seed Jenkins jobs, and rehome Nexus artifacts, Keycloak realm, and running Kubernetes workloads — cutover completed over a weekend.

**Assignment: Greenstone Financial Services — Insurance Portal** *(Technical Lead, late 2019)*
- DevOps delivery for .NET microservices: Azure DevOps pipelines, Terraform for Azure, Docker + Docker Swarm with Azure Container Registry, Azure Monitor.

---

### Senior AEM Administrator (Cloud) — ICF Next
*Sep 2015 – Jan 2017  |  Bangalore, India*

**Assignment: Channel 7 (Australia) — AEM on AWS**

Operated a **high-availability public-facing AWS platform** for a national Australian broadcaster.

- VPC design, EC2 lifecycle, Apache HTTPD + AEM Dispatcher hardening, SSL termination, **SAML 2.0 federation** (Azure AD / ADFS → AWS IAM) replacing long-lived IAM user keys.
- Evolved the architecture from separate Dispatcher VMs to Publish tier in an **Auto Scaling Group**.
- Authored **Ansible roles** for AEM install, Apache/Dispatcher deployment, SSL, and system baseline — making instance rebuilds a runbook rather than a discovery exercise.

---

### Unix / Linux Systems Administrator — HP Enterprise Services
*Nov 2011 – Aug 2015  |  Bangalore, India*

Three and a half years on HP's Global Operations Center (Unix Service Delivery Unit) running **24×7 shift-based operations** — where my on-call and incident discipline comes from.

- **HUL** (~18 months, L1/L2) — 24×7 incident handling on a SAP-heavy Linux/Unix estate (140+ servers).
- **E.ON** (~12 months, L2/L3) — multi-site German/UK operations; storage, DNS, console management.
- **Con-way Inc.** (~13 months, L2/L3) — authored a significant portion of the BSS-ITO Con-way Linux procedure library (LVM filesystem resizes, Veritas SAN migration, kernel-parameter tuning). Procedures adopted as team reference material.

---

## Education

**B.Tech in Computer Science** — West Bengal University of Technology, Kolkata, India (2005 – 2009)

---

## Certifications

- **Microsoft Certified: Azure Fundamentals (AZ-900)** — Mar 2023
- **AWS Certified Solutions Architect – Associate (SAA-C03)** — *in progress*
