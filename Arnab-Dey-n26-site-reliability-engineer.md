<div align="center">
	<h1><b>Arnab Dey</b></h1>
	<p>
		Site Reliability Engineer — AWS · Kubernetes · Terraform · Stateful Platforms · Observability<br>
		Stockholm, Sweden — open to relocation to Berlin under EU Blue Card sponsorship<br>
		+46 76 451 60 92 | <a href="mailto:arnabdey009@gmail.com">arnabdey009@gmail.com</a><br>
		<a href="https://www.linkedin.com/in/arnabdey73">LinkedIn</a> | <a href="https://github.com/arnabdey73">GitHub</a> | <a href="https://arnabdey.dev">arnabdey.dev</a>
	</p>
</div>

---

## Professional Summary

Cloud and Platform Engineer with **15+ years in IT** and **9+ years building and operating platforms** across AWS, Azure, and OpenStack — with a recurring focus on **the stateful side of the stack**: Elasticsearch with snapshot repositories and X-Pack security at Volvo, dual-cloud object-storage benchmarking on AWS S3 and Azure Blob, Logstash → Elasticsearch ingestion pipelines for 5G usage records at Deutsche Telekom, and three-and-a-half years of **24×7 shift-based Linux operations** (storage, LVM, SAN, kernel tuning, on-call) at HP Enterprise Services. **Authored the Terraform for Cisco's CD 2.0 platform on AWS** — VPC, EKS, IAM, ALB, ECR — alongside a separate **Prometheus Operator + Grafana observability stack**. Comfortable in incident-response and SLO-driven work; happy to ramp on Datadog and OpenTelemetry against the Prometheus/Grafana baseline.

---

## Core Skills

**AWS (production)** — EC2 (Auto Scaling Groups), **S3 (object storage operations, lifecycle, KMS)**, VPC + subnets + security groups, IAM (roles, SAML federation), **EKS, ECR, ALB**, KMS, CloudWatch; Terraform-driven AWS estate at Cisco; high-availability AEM platform on AWS at Channel 7. Operational exposure to RDS-class workloads via Tuleap/Keycloak/Nexus PostgreSQL backends in production.

**Stateful systems & data infrastructure** — Production **Elasticsearch on LXD** with **X-Pack security, SSL, snapshot repositories** at Volvo; Logstash ingestion pipelines for 5G UDR CSV feeds at Deutsche Telekom; **dual-cloud object-storage benchmarking** (S3 + KMS vs. Azure Premium BlockBlobStorage) for ML workloads; Linux storage / LVM / Veritas SAN migration / filesystem operations from HP Enterprise Services; cross-tenant migration of Tuleap (PostgreSQL-backed), Keycloak (realm/database), and Nexus artifact stores in a single weekend.

**Kubernetes (operator, not tourist)** — **EKS** at Cisco (CD 2.0 platform), **Rancher-managed Kubernetes (RKE)** on bare-metal CAE/HPC fleet at Volvo (~36 nodes), AKS, **K3s** (live single-node GitOps reference platform), Helm, Kubeflow, ArgoCD; cluster bootstrap, ingress, networking, rolling-update orchestration.

**Terraform** — Multi-provider (AWS, AzureRM, OpenStack, Databricks); reusable module libraries with opinionated, governance-friendly defaults; archetype-driven CAF deployment; remote state in object storage with backend config injected from CI; module versioning, drift handling. CloudFormation reading-knowledge.

**Observability** — **Prometheus + Grafana** (AWS observability stack at Cisco, K3s reference platform), production **ELK Stack** (Elasticsearch, Logstash, Kibana on LXD with X-Pack, SSL, snapshot repositories at Volvo), Azure Monitor / Log Analytics / KQL; **Datadog and OpenTelemetry** are a quick ramp against the Prometheus/Grafana baseline. SLO-driven thinking from incident-response work.

**CI/CD** — **GitHub Actions** (Volvo Databricks self-service, K3s reference platform), **Jenkins** (CD 2.0 platform on EKS at Cisco; ~46 Jenkins jobs at Deutsche Telekom), **ArgoCD** (K3s reference platform), Azure DevOps Pipelines, GitLab CI; reusable workflows, two-workflow contracts (validate on PR, deploy on merge), automated quality gates.

**Reliability & on-call** — **24×7 shift-based Linux operations** at HP Enterprise Services (incident handling, SOP authorship, customer-critical estates); cross-tenant migration weekend at Deutsche Telekom rehoming live Kubernetes workloads, repos, artifacts, and identity systems with no rebuild-from-scratch; KQL-based monitoring contributing to **~20% downtime reduction** at Stena Metall.

**Scripting & systems languages** — **Python** (REST/SCM automation, CLI tooling, batched migrations with retry logic), **Bash**, PowerShell.

**Security & networking** — Custom Azure RBAC (separation-of-duties for ransomware resilience), tenant-wide Key Vault compliance audit, Service Principal lifecycle and credential-rotation design, **SAML 2.0 federation replacing long-lived IAM keys**, VPC subnetting and security-group design.

**Languages** — English (fluent, working language), Hindi and Bengali (native), Swedish (SFI C-level basic).

---

## Professional Experience

### DevOps Engineer — AFRY Digital Solutions AB
*May 2025 – Present  |  Stockholm, Sweden*

**Assignment: Ericsson AB — CI Engineer, Tiger Test Tools (Sep 2025 – Present)**
- Maintain and support the end-to-end **CI flow for radio-communication smoke and regression testing** — Git, Gerrit, Jenkins, Docker, Linux. Triage failures across pipeline state and physical lab hardware.

**Platform engineering** — designed and operate a **GitOps Kubernetes platform** (K3s + ArgoCD + Prometheus + Grafana + cert-manager + sealed-secrets), provisioned via Terraform. Live demonstration of declarative platform foundations — public reference repo `single-node-gitops` on GitHub.

---

### Cloud Engineer — Stena Metall AB
*Aug 2024 – Jan 2025  |  Gothenburg, Sweden*

Cloud Infrastructure Engineer on the central Cloud Office of a mature **Azure CAF Enterprise Scale** estate — ~100 subscriptions, multi-management-group hierarchy, production workloads for a multi-billion-SEK industrial group. All infrastructure delivered as **Terraform via Azure DevOps pipelines**.

- **Authored two custom Azure RBAC role definitions** — a "Backup Remover" role and a Contributor variant with explicit `notActions` — to enforce **separation-of-duties** between resource management and backup deletion (ransomware-resilience control). Wired into the CAF archetype framework and shipped through the production pipeline.
- Delivered a **tenant-wide Key Vault compliance audit** (KQL against Azure Resource Graph) and **Service Principal lifecycle tooling** (KQL audit + PowerShell expiring-credential inventory + Logic Apps / Graph `addPassword` rotation design).
- **KQL-based monitoring contributed to a ~20% reduction in downtime** across supported services.
- Sanitised public reference repo: <a href="https://github.com/arnabdey73/iac-azure-core-governance">`iac-azure-core-governance`</a> (CAF Enterprise Scale governance platform), reusable Terraform module library, Azure cost-optimisation templates.

---

### Senior Software Engineer (DevOps) — Capgemini Sverige AB
*Sep 2021 – Jul 2024  |  Gothenburg, Sweden*

**Assignment: Volvo Cars — Car Safety R&D (Abakus MLOps / AI Platform)**

- Modernised a **~36-node bare-metal CAE/HPC cluster** for ML research: OS migration SLES → Ubuntu LTS; stand-up of **Rancher-managed Kubernetes (RKE)**; **Kubeflow** via Helm.
- Built a **production-grade ELK stack** on LXD — Elasticsearch with **X-Pack security, SSL, and snapshot repositories** for backup and restore — as the observability and search backbone for the platform.
- Built **two matched Terraform stacks** (AWS: EC2 + S3 + KMS + IAM | Azure: VM + Premium BlockBlobStorage) as disposable test rigs for **MLCommons-style object-storage benchmarking** — operational comparison of S3 and Azure Blob under identical workload shape.
- Designed and owned a **GitOps self-service pattern for Azure Databricks**: data scientists request compute via a GitHub issue → YAML manifest PR → **GitHub Actions** validates the change → merge applies it. Lead time fell from days to same-day; idle-cluster spend eliminated; every cluster traceable to a PR and a named owner.

---

### Senior Business Consultant (DevOps) — Tech Mahindra
*Feb 2017 – Sep 2021  |  Bangalore, India · Sydney, Australia*

**Assignment: Cisco Systems — CD 2.0 Continuous-Delivery Platform on AWS**
- **Authored the Terraform** for Cisco's CD 2.0 platform on **AWS** — VPC, subnets, security groups, **EKS cluster, IAM roles, Jenkins on EKS, ECR integration, build-agent fleet, ALB, DNS** — extending an internal reference architecture originally built on on-prem OpenShift.
- Wrote a separate **Terraform stack for an AWS observability environment** — EKS + **Prometheus Operator via Helm + Grafana** + persistent storage + ingress.
- Closed out Cisco's long-running SVN-to-Git migration via **Python automation** against the Bitbucket REST API — enumeration, history extraction, batched push with retry logic — a real codebase, not glue.

**Assignment: Deutsche Telekom — 5G BSS Slicing Pilot on OpenStack (Apr 2020 – Jul 2021)**
- Owned the **DevOps platform side** of DT's 5G Network Slicing commercial pilot on **PAN-NET (OpenStack)**, delivering Blue Marble's ~30-microservice BSS suite plus the Phenom UI.
- **Terraform against the OpenStack provider** provisioned the Jenkins / Nexus / Tuleap / Rancher / Keycloak / **ELK** estate; **Ansible playbooks** for all service configuration.
- Built a **Logstash pipeline ingesting 5G UDR (Usage Data Record) CSV feeds into Elasticsearch** for the billing emulator — operational data ingestion at production rates.
- Owned a **cross-tenant migration weekend** rehoming 54 Tuleap repositories (PostgreSQL-backed), Jenkins jobs, Nexus artifacts, **Keycloak realm**, and live Kubernetes workloads via Python/shell automation — incident-grade coordination, single weekend cutover, **nothing rebuilt from scratch**.

**Assignment: Greenstone Financial Services — Insurance Portal**
- Led DevOps transformation for **.NET microservices**: Azure DevOps pipelines, Terraform for Azure infrastructure, Docker + Docker Swarm with Azure Container Registry, Azure Monitor.

---

### Senior AEM Administrator (Cloud) — ICF Next
*Sep 2015 – Jan 2017  |  Bangalore, India*

**Assignment: Channel 7 (Australia) — AEM web platform on AWS**
- Built and operated a production AEM web platform on AWS for a national broadcaster — VPC, **EC2 lifecycle (m3 family, Auto Scaling Groups)**, Apache HTTPD + Dispatcher hardening, **SSL termination**, **SAML 2.0 federation (Azure AD / ADFS → AWS IAM)** replacing long-lived IAM user keys.
- Authored **Ansible roles** for AEM install, Apache/Dispatcher deployment, SSL, and base OS — turning instance rebuilds into a runbook rather than a discovery exercise.

---

### Unix / Linux Systems Administrator — HP Enterprise Services
*Nov 2011 – Aug 2015  |  Bangalore, India*

Three-and-a-half years on HP's Global Operations Center under Best Shore Services, rotating across enterprise customers including **E.ON (multi-site German / UK operations)** and **HUL (~140-server SAP-heavy estate)** — **24×7 incident handling on customer-critical Linux/Unix estates**.
- **Storage and filesystem operations**: LVM filesystem resizes, **Veritas SAN migration**, kernel-parameter tuning, NIM provisioning.
- DNS, console management, ITO/OpsBridge agent management; **authored a substantial portion of the BSS-ITO Con-way Linux procedure library** used as team reference material.
- Tooling fluency: HP Service Manager, HP OpenView / OpsBridge, HP Server Automation (Opsware).

---

## Education

**B.Tech in Computer Science** — West Bengal University of Technology, Kolkata, India (2005 – 2009)

---

## Certifications

- **Microsoft Certified: Azure Fundamentals (AZ-900)** — Mar 2023 *(Credential ID: 801D970BAA49297)*
- **AWS Certified Solutions Architect – Associate (SAA-C03)** — *in progress*
