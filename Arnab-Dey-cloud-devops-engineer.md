<div align="center">
	<h1><b>Arnab Dey</b></h1>
	<p>
		Cloud DevOps Engineer — Landing Zones · Governance · Security Baselines · Terraform · Python<br>
		Solna, Stockholm, Sweden | +46 76 451 60 92 | <a href="mailto:arnabdey009@gmail.com">arnabdey009@gmail.com</a><br>
		<a href="https://www.linkedin.com/in/arnabdey73">LinkedIn</a> | <a href="https://github.com/arnabdey73">GitHub</a> | <a href="https://arnabdey.dev">arnabdey.dev</a>
	</p>
</div>

---

## Professional Summary

Cloud engineer with **15+ years in IT** and **9+ years operating production cloud platforms** for enterprise clients, with the last year on the central Cloud Office (Governance) of a **mature Azure CAF Enterprise Scale estate — ~100 subscriptions across a multi-management-group hierarchy**. Track record of shipping landing-zone-aligned Terraform, custom RBAC role definitions enforcing separation-of-duties, tenant-wide Key Vault and Service Principal compliance audits, and Python/PowerShell automation against cloud control planes. Multi-cloud Terraform experience across **Azure and AWS** (plus OpenStack on a 5G commercial pilot). Stockholm-based, working in EU timezone.

---

## Core Skills

**Landing zones** — Azure **CAF Enterprise Scale / Landing Zones** on a ~100-subscription estate with multi-management-group hierarchy; archetype-driven deployment via Terraform and Azure DevOps pipelines; AWS account-vending patterns (VPC / IAM / KMS / ECR / EKS) for Cisco's CD 2.0 continuous-delivery platform.

**Governance** — Custom Azure RBAC role definitions enforcing separation-of-duties (ransomware-resilience control); tenant-wide Key Vault compliance audit (soft-delete retention, purge protection, RBAC authorisation) via KQL across Azure Resource Graph; Azure Policy; cost-allocation tagging across landing zones; subscription budget automation.

**Security baselines** — Service Principal lifecycle and credential rotation (Logic Apps + Microsoft Graph `addPassword`); KQL-driven expiring-credential inventory; SAML 2.0 federation (Azure AD / ADFS → AWS IAM) replacing long-lived IAM keys; Key Vault hardening (soft-delete, purge protection, RBAC authorisation); secrets management with sealed-secrets and AWS Secrets Manager via Terraform.

**Infrastructure as Code** — **Terraform** (AzureRM, AWS, OpenStack, Databricks providers); reusable module libraries with opinionated, sensible defaults; remote state in Azure Blob / S3 with backend config injected from CI environment secrets; two-workflow `validate-on-PR` / `apply-on-merge` contract; module versioning, drift handling, state inspection. **Native cloud IaC**: ARM templates, AWS CloudFormation-adjacent patterns. Ansible roles for legacy + on-prem.

**Cloud platforms** — **Azure** (primary, ~100-sub CAF estate at Stena Metall) and **AWS** (CD 2.0 platform at Cisco — VPC, EC2, EKS, IAM, ECR, ALB, KMS, CloudWatch, Route53, Auto Scaling Groups; AEM web platform on AWS for Channel 7 at ICF Next). Also OpenStack (DT 5G commercial pilot).

**Python / scripting for automation** — **Python** (REST/SCM automation, CLI tooling — including a Python migration tool against the Bitbucket REST API at Cisco with retry/rate-limit handling), **PowerShell** (Azure governance — Service Principal lifecycle, runtime audits, subscription budget automation, ACR token expiry inventory), **Bash**.

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
- PowerShell tooling: subscription budget automation, ACR token expiry inventory, .NET runtime enumeration across App Services, Hybrid Benefit enablement, cost-allocation tagging across landing zones.
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
- **Hindi**, **Bengali** — Native
