<div align="center">
	<h1><b>Arnab Dey</b></h1>
	<p>
		Senior Cloud Engineer — Azure · Terraform · Kubernetes · GitOps · Data Platforms<br>
		Stockholm, Sweden — open to relocation to Berlin (EU Blue Card) | +46 76 451 60 92 | <a href="mailto:arnabdey009@gmail.com">arnabdey009@gmail.com</a><br>
		<a href="https://www.linkedin.com/in/arnabdey73">LinkedIn</a> | <a href="https://github.com/arnabdey73">GitHub</a> | <a href="https://arnabdey.dev">arnabdey.dev</a>
	</p>
</div>

---

## Professional Summary

Senior Cloud Engineer with **15+ years in IT** and **9+ years designing and operating production-grade Azure platforms** for enterprise clients. Most recent work directly relevant to a data studio: **GitOps self-service Azure Databricks platform at Volvo Cars** plus Kubeflow on Rancher Kubernetes and dual-cloud benchmarking rigs for ML. Senior technical voice in cross-functional consulting engagements at Stena Metall (~100-subscription Azure CAF estate) and Deutsche Telekom (15-month 5G BSS commercial pilot, German enterprise client). Stockholm-based today, fully open to relocating to Berlin.

---

## Core Skills

**Microsoft Azure** — CAF Enterprise Scale / Landing Zones (~100-subscription estate), Virtual Machines, AKS, App Services, Entra ID + RBAC (custom role definitions), Key Vault, Storage (Blob, ADLS), Networking (VNet, NSG, Private Endpoints), Azure Monitor, Log Analytics / KQL, Azure Resource Graph, Azure Policy, Azure Backup.

**Infrastructure as Code** — Terraform (AzureRM, AWS, OpenStack, Databricks providers), reusable module libraries, archetype-driven CAF deployment, ARM templates.

**CI/CD** — Azure DevOps Pipelines, GitHub Actions, GitLab CI, Jenkins, ArgoCD, Gerrit; reusable workflow templates, two-stage `validate-on-PR` / `apply-on-merge` contracts.

**Containers & orchestration** — AKS, EKS, Rancher RKE, K3s; Docker, Helm, Kubeflow.

**Cloud security & governance** — Custom Azure RBAC, Key Vault compliance auditing, Service Principal lifecycle (Logic Apps + Microsoft Graph), SAML 2.0 federation, separation-of-duties controls.

**Scripting** — Python, PowerShell, Bash.

**Observability** — Azure Monitor, Application Insights, Log Analytics / KQL, Prometheus, Grafana, ELK Stack.

**FinOps** — Subscription budget automation, cost-allocation tagging, idle-cluster elimination, Hybrid Benefit, published Azure cost-optimisation Terraform templates.

**Data platform adjacency** — Azure Databricks (self-service GitOps), Kubeflow on Rancher RKE, dual-cloud Terraform rigs for MLCommons-style benchmarking.

**Other** — AWS (EC2, S3, EKS, IAM, ECR, KMS, ALB), OpenStack (DT 5G commercial pilot).

---

## Professional Experience

### DevOps Engineer — AFRY Digital Solutions AB
*May 2025 – Present  |  Stockholm, Sweden*

**Assignment: Ericsson AB — CI Engineer, Tiger Test Tools (Sep 2025 – Present)**
- Maintain end-to-end **CI flow for radio-communication smoke and regression testing** — Git, Gerrit, Jenkins, Docker, Linux.

**Internal platform engineering (public on GitHub)**
- Designed and operate a **GitOps Kubernetes reference platform**: K3s + ArgoCD + Prometheus + Grafana + cert-manager + sealed-secrets.

---

### Cloud Engineer — Stena Metall AB
*Aug 2024 – Jan 2025  |  Gothenburg, Sweden*

Cloud Infrastructure Engineer on the central Cloud Office (Governance) of a mature **Azure CAF Enterprise Scale** estate — **~100 subscriptions, multi-management-group hierarchy**, production workloads for a multi-billion-SEK industrial group. All infrastructure delivered as **Terraform via Azure DevOps pipelines**.

- Collaborated with **architecture leadership** on a tenant-wide **Key Vault compliance audit** — KQL across Azure Resource Graph for soft-delete retention, purge protection, and RBAC authorisation.
- **Authored two custom Azure RBAC role definitions** enforcing separation-of-duties between resource management and backup deletion (a ransomware-resilience control missing from Azure's built-in Contributor). Wired into the CAF archetype framework and shipped through the production pipeline. **38 commits across the core-governance repo.**
- Built **Service Principal lifecycle tooling** integrating Azure Resource Graph (KQL audit), PowerShell (expiring-credential inventory), and a Logic Apps + Microsoft Graph `addPassword` rotation design.
- PowerShell tooling: subscription budget automation, ACR token expiry inventory, .NET runtime enumeration across App Services, Hybrid Benefit enablement.
- **KQL-based monitoring contributed to a ~20% reduction in downtime** across supported services.
- Public sister repos: <a href="https://github.com/arnabdey73/iac-azure-core-governance">`iac-azure-core-governance`</a>, reusable Terraform module library, Azure cost-optimisation templates.

---

### Senior Software Engineer (DevOps) — Capgemini Sverige AB
*Sep 2021 – Jul 2024  |  Gothenburg, Sweden*

**Assignment: Volvo Cars — Car Safety R&D (Abakus MLOps / AI Platform)**

- Designed and owned a **GitOps self-service pattern for Azure Databricks** for Car Safety data scientists (GitHub issue → manifest PR → GitHub Actions → `terraform apply`) with governance and cost defaults — auto-termination, autoscale, single-user mode — baked into the Terraform module. **Outcome:** provisioning lead time fell from days to same-day; every cluster traceable to a PR and named owner; idle-cluster spend eliminated.
- Modernised a ~36-node CAE/HPC cluster: SLES → Ubuntu LTS migration, **Rancher-managed Kubernetes (RKE)** stand-up, **Kubeflow** via Helm; production ELK stack with X-Pack security.
- Built **two matched Terraform stacks** (AWS + Azure) as identically-shaped test rigs for MLCommons-style ML object-storage benchmarking.

---

### Senior Business Consultant (DevOps) — Tech Mahindra
*Feb 2017 – Sep 2021  |  Bangalore, India · Sydney, Australia*

**Assignment: Deutsche Telekom — 5G BSS Slicing Pilot on OpenStack (15 months, Apr 2020 – Jul 2021)**
- Owned the **DevOps platform side** of DT's 5G Network Slicing commercial pilot on **PAN-NET (OpenStack)**, delivering Blue Marble's ~30-microservice BSS suite plus the Phenom UI.
- **Terraform against the OpenStack provider** provisioning the Jenkins / Nexus / Tuleap / Rancher / Keycloak / ELK estate; **Ansible playbooks** for all service configuration.
- **~46 Jenkins jobs** building BMP microservices, tagging build number + short git SHA, pushing to Nexus, updating Kubernetes manifests, triggering Rancher rolling updates.
- Built a **Logstash pipeline** ingesting 5G UDR feeds into Elasticsearch for the billing emulator. Authored operational SOPs and architectural documentation used by DT and Tech Mahindra teams across multiple European regions.

**Other Tech Mahindra assignments**
- **Cisco Systems — CD 2.0 on AWS:** authored the Terraform for Cisco's CD 2.0 continuous-delivery platform (VPC, EKS, IAM, Jenkins, ECR, ALB) and the AWS observability stack; closed out a long-running SVN-to-Git migration via Python automation against the Bitbucket REST API.
- **Greenstone Financial Services & CA ANZ:** DevOps transformation for .NET microservices on Azure DevOps + Terraform + ACR; architected GitLab-based CI and source-control model.

---

### Senior AEM Administrator (Cloud) — ICF Next
*Sep 2015 – Jan 2017  |  Bangalore, India*

Built and operated a production AEM web platform on AWS for Channel 7 (national Australian broadcaster) — VPC, EC2 lifecycle, Apache HTTPD + Dispatcher hardening, **SAML 2.0 federation (Azure AD / ADFS → AWS IAM)** replacing long-lived IAM keys; Ansible roles for AEM, Apache, SSL, and base OS.

---

### Unix / Linux Systems Administrator — HP Enterprise Services
*Nov 2011 – Aug 2015  |  Bangalore, India*

Three-and-a-half years on HP's Global Operations Center (Unix Service Delivery Unit), rotating across enterprise outsourcing customers including **E.ON (multi-site German / UK operations)** — 24×7 incident handling, storage, DNS, console management, SOP authoring on customer-critical Unix/Linux estates.

---

## Education

**B.Tech in Computer Science** — West Bengal University of Technology, Kolkata, India (2005 – 2009)

---

## Certifications

- **Microsoft Certified: Azure Fundamentals (AZ-900)** — Mar 2023 *(801D970BAA49297)*
- **AWS Certified Solutions Architect – Associate (SAA-C03)** — *in progress*

---

## Languages

- **English** — Fluent (working language)
- **Swedish** — SFI C-level (basic professional)
- **Hindi**, **Bengali** — Native
