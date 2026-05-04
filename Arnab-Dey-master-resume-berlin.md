<div align="center">
	<h1><b>Arnab Dey</b></h1>
	<p>
		Cloud &amp; DevOps Engineer — Kubernetes · Terraform · AWS &amp; Azure · GitOps<br>
		Stockholm, Sweden — open to relocation to Berlin | +46 76 451 60 92 | <a href="mailto:arnabdey009@gmail.com">arnabdey009@gmail.com</a><br>
		<a href="https://www.linkedin.com/in/arnabdey73">LinkedIn</a> | <a href="https://github.com/arnabdey73">GitHub</a> | <a href="https://arnabdey.dev">arnabdey.dev</a><br>
		<i>Open to relocation to Berlin under EU Blue Card sponsorship.</i>
	</p>
</div>

---

## Professional Summary

Cloud and Platform Engineer with **15+ years in IT** and **9+ years in cloud and platform engineering** across Azure, AWS, OpenStack, and hybrid environments. I design and build with code — Terraform for infrastructure, Python and Bash for automation, GitOps for delivery — and favour reviewable, repeatable patterns over manual operations. Hands-on across CAF Enterprise Scale, Kubernetes (Rancher RKE, AKS, EKS, K3s), GitHub Actions, Azure DevOps, GitLab, Jenkins, ArgoCD, Prometheus/Grafana, and Azure Policy / RBAC. Includes a **15-month engagement with Deutsche Telekom on a 5G BSS commercial pilot** running on PAN-NET (DT's OpenStack-based private cloud). Consistent track record of moving platform teams off manual ClickOps toward self-service, audited, cost-aware infrastructure.

---

## Core Skills

**Infrastructure as Code** — Terraform (AzureRM, AWS, OpenStack, Databricks providers), reusable module libraries, ARM templates, Ansible, archetype-driven CAF Enterprise Scale

**Cloud Platforms** — Microsoft Azure (primary), AWS (EC2, S3, VPC, EKS, IAM, CloudWatch), OpenStack, hybrid and on-prem

**Scripting** — Python (automation, CLI tooling), Bash, PowerShell

**CI/CD &amp; GitOps** — GitHub Actions, Azure DevOps Pipelines, GitLab CI, Jenkins, ArgoCD, Git / Gerrit, trunk-based and GitFlow workflows

**Containers &amp; Orchestration** — Kubernetes (Rancher RKE, K3s, EKS, AKS), Docker, Helm, Kubeflow

**Identity, Security &amp; Governance** — Entra ID, Azure RBAC (including custom role definitions), Azure Policy, IAM, SAML federation, Key Vault, least-privilege patterns, backup-integrity by RBAC

**Observability** — Prometheus, Grafana, Azure Monitor, Log Analytics / KQL, ELK Stack, CloudWatch, cert-manager, sealed-secrets

**Ways of Working** — Agile / SAFe, cross-team platform enablement, technical documentation, stakeholder workshops, mentoring

---

## Professional Experience

### DevOps Engineer — AFRY Digital Solutions AB
*May 2025 – Present  |  Stockholm, Sweden*

**Assignment: Ericsson AB — CI Engineer, Tiger Test Tools (Sep 2025 – Present)**
- Maintain and support the end-to-end CI flow for radio-communication smoke and regression testing — Git, Gerrit, Jenkins, Docker, Linux.
- Support radio-communication hardware and test servers; troubleshoot issues across daily delivery and validation workflows.

**Assignment: AFRY Internal — True Demand Initiative, RPA Developer (Jul 2025 – Sep 2025)**
- Built a hybrid Power Automate (Desktop + cloud) solution that processes Tendsign procurement emails end-to-end, extracts document links, and automates browser-based login and download with secure credential handling.

**Platform engineering (ongoing, internal project)**
- Designed and deployed a **GitOps-based single-node Kubernetes platform** (K3s + ArgoCD + Prometheus + Grafana + cert-manager + sealed-secrets) as a reference for cloud-native delivery patterns — maintained as a live public demo.

---

### Cloud Engineer — Stena Metall AB
*Aug 2024 – Jan 2025  |  Gothenburg, Sweden*

Cloud Infrastructure Engineer on the central Cloud Office (Governance side) of a mature **Azure CAF Enterprise Scale** estate — ~100 subscriptions, multi-management-group hierarchy, production workloads for a multi-billion-SEK industrial group.

- **Authored two custom Azure RBAC role definitions** (a "Backup Remover" role and a modified Contributor with explicit `notActions`) to enforce separation-of-duties between resource management and backup deletion — a ransomware-resilience control missing from Azure's built-in Contributor role. Wired into the CAF archetype framework and deployed via the existing Terraform + Azure DevOps pipeline.
- Delivered a **tenant-wide Key Vault compliance audit** — KQL against Azure Resource Graph for soft-delete retention, purge protection, and RBAC authorisation — producing CSV inventories and a documented review for architecture leadership.
- Built **Service Principal lifecycle tooling** — KQL audit for 30-day create/update/delete events, PowerShell for expiring-credential inventory, and a design for client-secret rotation via Logic Apps + Graph API `addPassword`.
- Implemented **Azure Backup policy compliance reporting** with per-VM exempt-rationale tracking; contributed PowerShell tooling for subscription budget automation, ACR token expiry inventory, and Hybrid Benefit enablement.
- KQL-based monitoring contributed to a **~20% reduction in downtime** across supported services.
- Published sanitized sister repos on GitHub: <a href="https://github.com/arnabdey73/iac-azure-core-governance">`iac-azure-core-governance`</a> (CAF Enterprise Scale governance platform), reusable Terraform module library, and Azure cost-optimisation templates.

---

### Senior Software Engineer (DevOps) — Capgemini Sverige AB
*Sep 2021 – Jul 2024  |  Gothenburg, Sweden*

**Assignment: Volvo Cars — Car Safety R&amp;D (Abakus MLOps / AI ART)**

*Self-service Databricks platform via GitOps*
- Designed and owned a **GitOps self-service pattern for Azure Databricks**: data scientists request compute via a GitHub issue template → a YAML manifest PR → GitHub Actions runs `terraform fmt/validate/plan` for review → merge triggers `terraform apply`.
- Authored the **Terraform module** with opinionated, governance-friendly defaults baked in: single-user security mode, 30-minute auto-termination, autoscale 1→3 workers, cluster-log shipping to DBFS, `CAN_RESTART` permissions — making clusters cheap and safe by construction.
- **Outcome:** provisioning lead time dropped from days to same-day; every cluster traceable to a PR, a manifest, and a named owner; eliminated long-tail idle-cluster spend.

*CAE HPC platform modernization (on-prem)*
- Contributed to modernising a ~36-node CAE/HPC cluster supporting ML research: OS migration from SLES to Ubuntu LTS; stand-up of **Rancher-managed Kubernetes (RKE)** with worker fleet; **Kubeflow** installation via Helm for ML engineers.
- Built a **production-grade ELK stack** (Elasticsearch, Logstash, Kibana) on LXD with X-Pack security, SSL, and snapshot repositories for observability. Authored Ansible roles within the shared GitLab-managed codebase.

*Dual-cloud ML storage benchmarking*
- Built **two matched Terraform stacks** (AWS: EC2 + S3 + KMS + IAM  |  Azure: Linux VM + Premium BlockBlobStorage) as identically-shaped, disposable test rigs so data scientists could run MLCommons-style object-storage benchmarks on equal footing.

---

### Senior Business Consultant (DevOps) — Tech Mahindra
*Feb 2017 – Sep 2021  |  Bangalore, India · Sydney, Australia*

**Assignment: Deutsche Telekom — 5G BSS Slicing Pilot on OpenStack (Apr 2020 – Jul 2021)**
- Owned the **DevOps platform side** of DT's 5G Network Slicing commercial pilot on **PAN-NET (OpenStack)**, delivering Blue Marble's ~30-microservice BSS suite plus the Phenom UI.
- Wrote **Terraform against the OpenStack provider** — networks, subnets, security groups, VMs, floating IPs — provisioning the Jenkins / Nexus / Tuleap / Rancher / Keycloak / ELK estate; **Ansible playbooks** for all service configuration.
- Designed and ran **~46 Jenkins jobs** building BMP microservices, tagging with build number + short git SHA, pushing to internal Nexus registry, updating Kubernetes manifests, and triggering Rancher rolling updates.
- Owned the **cross-tenant migration** when the pilot moved PAN-NET tenants: wrote Python/shell automation to clone 54 Tuleap repositories at correct branches, re-seed Jenkins jobs, and rehome Nexus artifacts, Keycloak realm, and running Kubernetes workloads — cutover completed over a weekend, nothing rebuilt from scratch.
- Built a **Logstash pipeline** ingesting 5G UDR (Usage Data Record) CSV feeds into Elasticsearch for the billing emulator. Authored operational SOPs and architectural documentation used by DT and Tech Mahindra teams across multiple European regions.

**Assignment: Cisco Systems — CD 2.0 on AWS (Oct 2019 – Mar 2020)**
- **Authored the Terraform** for Cisco's CD 2.0 continuous-delivery platform on AWS — VPC, subnets, security groups, EKS cluster, IAM roles, Jenkins on EKS, ECR integration, build-agent fleet, ALB, DNS — extending an internal reference architecture originally built on on-prem OpenShift.
- Wrote a separate **Terraform stack for an AWS observability environment** (EKS, Prometheus Operator via Helm, Grafana, persistent storage, ingress).
- **Closed out Cisco's long-running SVN-to-Git migration** with a **Python automation** that enumerated SVN repositories, extracted history, provisioned Bitbucket repos via REST API, pushed converted Git history, and produced CSV migration reports — with retry logic and batching to work around SCM rate limits.

**Assignment: Greenstone Financial Services — Insurance Portal (Sep 2019 – Jan 2020)**
- Led DevOps transformation for .NET microservices: Azure DevOps pipelines, **Terraform for Azure infrastructure**, Docker + Docker Swarm with Azure Container Registry, Azure Monitor for observability.

**Assignment: CA ANZ (Sep 2019 – Jan 2020)**
- Architected the GitLab-based CI and source-control model — defined branching strategy, repository standards, pipeline conventions; supported team adoption through documentation and knowledge transfer.

---

### Senior AEM Administrator (Cloud) — ICF Next
*Sep 2015 – Jan 2017  |  Bangalore, India*

- Built and operated a production Adobe Experience Manager platform on AWS for a national Australian broadcaster (Channel 7) — VPC design, EC2 lifecycle, Apache HTTPD + AEM Dispatcher hardening, SSL termination, and **SAML 2.0 federation** (Azure AD / ADFS → AWS IAM) replacing long-lived IAM user keys.
- Authored **Ansible roles** for AEM install, Apache/Dispatcher deployment, SSL, and system baseline — making instance rebuilds a runbook rather than a discovery exercise.

---

### Unix / Linux Systems Administrator — HP Enterprise Services
*Nov 2011 – Aug 2015  |  Bangalore, India*

Three-and-a-half years on HP's Global Operations Center (Unix Service Delivery Unit), rotating across three large outsourcing customers including **E.ON (multi-site German / UK operations)** — storage, DNS, console management, SOP authoring. Authored a substantial portion of the BSS-ITO Con-way Linux procedure library covering LVM filesystem resizes, Veritas SAN migration, and kernel-parameter tuning.

---

## Public Projects (GitHub)

- **single-node-gitops** — Single-node GitOps Kubernetes platform (K3s + ArgoCD + Prometheus + Grafana + cert-manager + sealed-secrets), provisioned via Terraform.
- **iac-azure-core-governance** — Sanitized CAF Enterprise Scale governance platform (Terraform + Azure DevOps).
- **resume-builder-agent**, **weather-app**, **go-url-shortener** — Reference applications and tooling.

---

## Education

**B.Tech in Computer Science** — West Bengal University of Technology, Kolkata, India (2005 – 2009)

---

## Certifications

- **Microsoft Certified: Azure Fundamentals (AZ-900)** — Mar 2023 *(Credential ID: 801D970BAA49297)*
- **AWS Certified Solutions Architect – Associate (SAA-C03)** — *in progress*

---

## Languages

- **English** — Native / bilingual proficiency (working language)
- **Swedish** — SFI C-level (basic professional)
- **Hindi** — Native
- **Bengali** — Native
