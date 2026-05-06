<div align="center">
	<h1><b>Arnab Dey</b></h1>
	<p>
		Senior Cloud Engineer — Azure · AKS · Terraform · Multi-Cloud · Security-First Infrastructure<br>
		Stockholm, Sweden — remote-from-Sweden (existing right to work, no sponsorship required)<br>
		+46 76 451 60 92 | <a href="mailto:arnabdey009@gmail.com">arnabdey009@gmail.com</a><br>
		<a href="https://www.linkedin.com/in/arnabdey73">LinkedIn</a> | <a href="https://github.com/arnabdey73">GitHub</a> | <a href="https://arnabdey.dev">arnabdey.dev</a>
	</p>
</div>

---

## Professional Summary

Cloud and Platform Engineer with **15+ years in IT** and **9+ years building cloud infrastructure that engineering teams depend on** — Azure-primary across the past four years, with substantial AWS and OpenStack experience. **Designed and built from the ground up** in every recent role: a custom Azure RBAC governance pattern at Stena Metall (CAF Enterprise Scale, ~100 subscriptions), a GitOps self-service Azure Databricks platform at Volvo Cars, and **the Terraform for Cisco's CD 2.0 platform on AWS** — VPC, EKS, IAM, ALB, ECR, Jenkins on EKS — alongside a separate Prometheus + Grafana observability stack. Security-first is the recurring thread: custom RBAC separation-of-duties (ransomware control), tenant-wide Key Vault compliance audit, Service Principal credential-rotation design, **SAML 2.0 federation eliminating long-lived IAM keys**, sealed-secrets + cert-manager on a live K3s reference platform, X-Pack SSL on production Elasticsearch. Three and a half years of **24×7 shift-based Linux operations** at HP Enterprise Services is where on-call instincts come from. Stockholm-based, remote-friendly across European time zones.

---

## Core Skills

**Azure (production)** — **AKS, Azure Databricks, App Services, VNets, Key Vault, Azure Monitor / Log Analytics / KQL, RBAC (including custom role definitions), Azure Policy, Service Principal lifecycle, Entra ID, Azure Backup**; Terraform-driven Azure estate at Stena Metall (CAF Enterprise Scale, ~100 subscriptions); Azure DevOps Pipelines as CI/CD; subscription budget automation, Hybrid Benefit enablement, cost-allocation tagging across landing zones.

**AWS (production)** — EC2 (Auto Scaling Groups), S3 (with KMS), VPC + subnets + security groups, IAM (roles, **SAML federation**), **EKS, ECR, ALB**, KMS, CloudWatch; Terraform-driven AWS estate at Cisco CD 2.0; high-availability AEM platform on AWS at Channel 7.

**Kubernetes (operator, not tourist)** — **AKS** (Greenstone insurance portal; Volvo MLOps); **EKS** at Cisco (CD 2.0 platform); **Rancher-managed Kubernetes (RKE)** on bare-metal CAE/HPC fleet at Volvo (~36 nodes); **K3s** (live single-node GitOps reference platform with ArgoCD + cert-manager + sealed-secrets); Helm, Kubeflow, ingress, networking, rolling-update orchestration, on-call.

**Terraform / Infrastructure as Code** — Multi-provider (AzureRM, AWS, OpenStack, Databricks); reusable module libraries with opinionated, governance-friendly defaults; **archetype-driven CAF Enterprise Scale** at Stena; remote state in object storage with backend config injected from CI; module versioning, drift handling. **Designs from scratch, not template tourism.**

**Security & hardening** — Custom Azure RBAC role definitions (separation-of-duties for ransomware resilience); tenant-wide Key Vault compliance audit (KQL against Resource Graph: soft-delete, purge protection, RBAC); Service Principal credential-rotation design (Logic Apps + Microsoft Graph `addPassword`); **SAML 2.0 federation eliminating long-lived IAM user keys**; sealed-secrets + cert-manager on K3s; X-Pack security with SSL on production Elasticsearch; SSL-terminating ALB at Cisco; custom Sonatype Nexus 3 SSL Dockerfile at Deutsche Telekom.

**Multi-region & multi-cloud** — Dual-cloud Terraform stacks at Volvo (AWS S3 + KMS + IAM and Azure Premium BlockBlobStorage as identically-shaped object-storage benchmarking rigs); OpenStack at Deutsche Telekom alongside Azure / AWS work; cross-tenant migration weekend rehoming live Kubernetes workloads, repos, artifacts, and identity systems with no rebuild-from-scratch.

**GitOps & CI/CD** — **GitHub Actions** (Volvo Databricks self-service, K3s reference platform), **ArgoCD** (K3s reference platform), **Azure DevOps Pipelines** (Stena CAF), **Jenkins** (CD 2.0 platform on EKS at Cisco; ~46 Jenkins jobs at Deutsche Telekom), GitLab CI; reusable workflows, two-workflow contracts (validate on PR, deploy on merge), automated quality gates.

**Observability** — **Prometheus + Grafana** (AWS observability stack at Cisco, K3s reference platform), production **ELK Stack** (Elasticsearch, Logstash, Kibana on LXD with X-Pack security, SSL, snapshot repositories at Volvo), **Azure Monitor / Log Analytics / KQL** (~20% downtime reduction at Stena Metall via KQL-based monitoring).

**Reliability & on-call** — **24×7 shift-based Linux operations** at HP Enterprise Services on customer-critical estates (E.ON Germany/UK, HUL ~140 servers); cross-tenant migration weekend at Deutsche Telekom rehoming live workloads; storage / SAN / LVM / kernel-tuning fluency; **Linux engineering depth** that translates to KTLO and incident-response work.

**Scripting & systems languages** — **Python** (REST/SCM automation, CLI tooling, batched migrations with retry logic), **Bash**, PowerShell.

**Languages** — English (fluent, working language), Hindi and Bengali (native), Swedish (SFI C-level basic).

---

## Professional Experience

### DevOps Engineer — AFRY Digital Solutions AB
*May 2025 – Present  |  Stockholm, Sweden*

**Assignment: Ericsson AB — CI Engineer, Tiger Test Tools (Sep 2025 – Present)**
- Maintain and support the end-to-end **CI flow for radio-communication smoke and regression testing** — Git, Gerrit, Jenkins, Docker, Linux. Triage failures across pipeline state and physical lab hardware.

**Platform engineering** — designed and operate a **GitOps Kubernetes platform** (K3s + ArgoCD + Prometheus + Grafana + cert-manager + sealed-secrets), provisioned via Terraform from scratch. Live demonstration of declarative platform foundations — public reference repo `single-node-gitops` on GitHub.

---

### Cloud Engineer — Stena Metall AB
*Aug 2024 – Jan 2025  |  Gothenburg, Sweden*

Cloud Infrastructure Engineer on the central Cloud Office of a mature **Azure CAF Enterprise Scale** estate — ~100 subscriptions, multi-management-group hierarchy, production workloads for a multi-billion-SEK industrial group. All infrastructure delivered as **Terraform via Azure DevOps pipelines**.

- **Authored two custom Azure RBAC role definitions** — a "Backup Remover" role and a Contributor variant with explicit `notActions` — to enforce **separation-of-duties** between resource management and backup deletion (ransomware-resilience control). Wired into the CAF archetype framework and shipped through the production pipeline. **Designed the control from scratch.**
- Delivered a **tenant-wide Key Vault compliance audit** (KQL against Azure Resource Graph) and **Service Principal lifecycle tooling** — KQL audit + PowerShell expiring-credential inventory + Logic Apps / Microsoft Graph `addPassword` rotation design.
- **KQL-based monitoring contributed to a ~20% reduction in downtime** across supported services.
- Sanitised public reference repo: <a href="https://github.com/arnabdey73/iac-azure-core-governance">`iac-azure-core-governance`</a> (CAF Enterprise Scale governance platform), reusable Terraform module library, Azure cost-optimisation templates.

---

### Senior Software Engineer (DevOps) — Capgemini Sverige AB
*Sep 2021 – Jul 2024  |  Gothenburg, Sweden*

**Assignment: Volvo Cars — Car Safety R&D (Abakus MLOps / AI Platform)**

- **Designed and owned a GitOps self-service pattern for Azure Databricks** — built from scratch: data scientists request compute via a GitHub issue → YAML manifest PR → **GitHub Actions** validates the change → merge applies it. Lead time fell from days to same-day; idle-cluster spend eliminated; every cluster traceable to a PR and a named owner.
- Authored the **Terraform module** with reliability and cost defaults baked in: single-user security mode, **30-minute auto-termination, autoscale 1→3 workers**, cluster-log shipping to DBFS, `CAN_RESTART` permissions. Remote state in Azure Blob Storage with backend config injected at init from GitHub environment secrets.
- Built **two matched Terraform stacks** as identically-shaped, disposable test rigs for **MLCommons-style object-storage benchmarking** — AWS (EC2 + S3 + KMS + IAM) on one side, Azure (VM + Premium BlockBlobStorage) on the other — multi-cloud platform engineering as the control variable.
- Modernised a **~36-node bare-metal CAE/HPC cluster** for ML research: OS migration SLES → Ubuntu LTS; stand-up of **Rancher-managed Kubernetes (RKE)**; **Kubeflow** via Helm; production-grade **ELK stack** on LXD with X-Pack security, SSL, and snapshot repositories.

---

### Senior Business Consultant (DevOps) — Tech Mahindra
*Feb 2017 – Sep 2021  |  Bangalore, India · Sydney, Australia*

**Assignment: Cisco Systems — CD 2.0 Continuous-Delivery Platform on AWS**
- **Authored the Terraform from scratch** for Cisco's CD 2.0 platform on **AWS** — VPC, subnets, security groups, **EKS cluster, IAM roles, Jenkins on EKS, ECR integration, build-agent fleet, ALB with SSL termination, DNS** — extending an internal reference architecture originally built on on-prem OpenShift.
- Wrote a separate **Terraform stack for an AWS observability environment** — EKS + **Prometheus Operator via Helm + Grafana** + persistent storage + ingress.
- Closed out Cisco's long-running SVN-to-Git migration via **Python automation** against the Bitbucket REST API — enumeration, history extraction, batched push with retry logic.

**Assignment: Deutsche Telekom — 5G BSS Slicing Pilot on OpenStack (Apr 2020 – Jul 2021)**
- Owned the **DevOps platform side** of DT's 5G Network Slicing commercial pilot on **PAN-NET (OpenStack)**, delivering Blue Marble's ~30-microservice BSS suite plus the Phenom UI.
- **Terraform against the OpenStack provider** provisioned the Jenkins / Nexus / Tuleap / Rancher / Keycloak / **ELK** estate; **Ansible playbooks** for all service configuration.
- Owned a **cross-tenant migration weekend** rehoming 54 Tuleap repositories, Jenkins jobs, Nexus artifacts, **Keycloak realm**, and live Kubernetes workloads via Python/shell automation — incident-grade coordination, single weekend cutover, **nothing rebuilt from scratch**.

**Assignment: Greenstone Financial Services — Insurance Portal**
- Led DevOps transformation for **.NET microservices** on **Azure**: Azure DevOps pipelines, **Terraform for Azure infrastructure (incl. AKS)**, Docker + Docker Swarm with Azure Container Registry, Azure Monitor.

---

### Senior AEM Administrator (Cloud) — ICF Next
*Sep 2015 – Jan 2017  |  Bangalore, India*

**Assignment: Channel 7 (Australia) — AEM web platform on AWS**
- Built and operated a production AEM web platform on AWS for a national broadcaster — VPC, **EC2 lifecycle (m3 family, Auto Scaling Groups)**, Apache HTTPD + Dispatcher hardening, **SSL termination**, **SAML 2.0 federation (Azure AD / ADFS → AWS IAM) replacing long-lived IAM user keys**.
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
