<div align="center">
	<h1><b>Arnab Dey</b></h1>
	<p>
		Stockholm, Sweden | +46 0764516092 | <a href="mailto:arnabdey009@gmail.com">arnabdey009@gmail.com</a><br>
		<a href="https://www.linkedin.com/in/arnabdey73">LinkedIn</a> | <a href="https://github.com/arnabdey73">GitHub</a>
	</p>
</div>

---

## Professional Summary

Cloud & Platform Engineer with **15+ years in IT** and **9+ years building and operating Azure platforms** that real product teams depend on — most recently a **GitOps self-service Azure Databricks platform at Volvo Cars** (PR-driven Terraform via GitHub Actions, lead time days → same-day) and a **~100-subscription Azure CAF Enterprise Scale governance estate at Stena Metall** delivered through the production Terraform + Azure DevOps pipeline. SRE-aligned by practice: KQL-driven monitoring at Stena that contributed to a **~20% reduction in downtime**, 24×7 incident handling on customer-critical Linux estates at HP, and observability stacks (ELK, Prometheus/Grafana, Azure Monitor) built for production. Deep on Azure compute / networking / identity / storage, Terraform module-library patterns, **GitHub Actions and Azure DevOps**, and security-first delivery (custom RBAC, Key Vault compliance, SP rotation design). Stockholm-based, fluent in English.

---

## Core Skills

**Microsoft Azure (primary)** — CAF Enterprise Scale / Landing Zones (~100-subscription estate), **Compute** (VM/VMSS, App Services), **Networking** (VNet, NSG, Private Endpoints), **Identity** (Entra ID, RBAC including custom role definitions, Service Principals), **Storage** (Blob, ADLS, disk-encryption-sets), Key Vault, AKS, ACR, Azure Monitor, Log Analytics / KQL, Azure Resource Graph, Azure Policy.

**CI/CD — GitHub Actions and Azure DevOps (both)** — **GitHub Actions** with reusable workflows for Volvo Cars Terraform delivery (`tf-validate` on PR, `tf-deploy` on merge); **Azure DevOps Pipelines** for Stena governance Terraform and Greenstone .NET microservices; reusable templates, automated quality gates (`fmt/validate/plan` separated from `apply`).

**Infrastructure as Code** — Terraform (AzureRM, AWS, OpenStack, Databricks providers): reusable module libraries with opinionated, governance-friendly defaults; archetype-driven CAF deployment; remote state in Azure Blob with backend config injected from CI environment secrets; module versioning, drift handling, state inspection. **ARM templates** (closest analogue to Bicep — same resource model, transpilation target — comfortable picking up Bicep on the job).

**Site Reliability practices** — Observability (Azure Monitor, Log Analytics / KQL, Prometheus, Grafana, ELK Stack); **KQL-driven monitoring contributed to ~20% downtime reduction at Stena**; production ELK stack with X-Pack security and snapshot repositories at Volvo; 24×7 incident handling at HP across customer-critical Unix/Linux estates; reliability-by-design via autoscale + auto-termination defaults baked into Terraform modules.

**DevSecOps & compliance** — **Custom Azure RBAC role definitions** (separation-of-duties for ransomware resilience); **tenant-wide Key Vault compliance audit** (soft-delete, purge protection, RBAC authorisation); **Service Principal lifecycle + credential-rotation design** (Logic Apps + Graph `addPassword`); SAML 2.0 federation replacing long-lived IAM keys; Azure Backup compliance reporting; cost-allocation tagging across landing zones.

**Backend language familiarity** — **C# / .NET**: Azure DevOps pipelines for .NET microservices at Greenstone Financial Services (Docker Swarm + ACR + Azure Monitor); PowerShell **App Service .NET runtime enumeration** across the Stena CAF estate.

**Kubernetes & containers** — AKS, EKS, **Rancher RKE**, K3s; Docker, Helm, Kubeflow, ArgoCD; container registries (ACR, ECR, Nexus).

**Cloud (other)** — AWS (EC2, S3, VPC, EKS, IAM, ECR, ALB, KMS); OpenStack (Deutsche Telekom 5G commercial pilot).

**Scripting** — Python (REST/SCM automation, CLI tooling), PowerShell (Azure governance — SP lifecycle, ACR token expiry, runtime audits, budget automation), Bash.

**Languages** — English (fluent), Swedish (SFI C-level).

---

## Professional Experience

### DevOps Engineer — AFRY Digital Solutions AB
*May 2025 – Present  |  Stockholm, Sweden*

**Assignment: Ericsson AB — CI Engineer, Tiger Test Tools (Sep 2025 – Present)**
- Maintain and support the end-to-end **CI flow for radio-communication smoke and regression testing** — Git, Gerrit, Jenkins, Docker, Linux. Close the loop between pipeline failures and physical lab state when test rigs misbehave.

**Platform engineering (internal reference project — public on GitHub)**
- Designed and operate a **GitOps Kubernetes platform**: K3s + ArgoCD + Prometheus + Grafana + cert-manager + sealed-secrets. Live demonstration of declarative platform foundations.

---

### Cloud Engineer — Stena Metall AB
*Aug 2024 – Jan 2025  |  Gothenburg, Sweden*

Cloud Infrastructure Engineer on the central Cloud Office (Governance) of a mature **Azure CAF Enterprise Scale** estate — **~100 subscriptions, multi-management-group hierarchy**, production workloads for a multi-billion-SEK industrial group. All infrastructure delivered as **Terraform via Azure DevOps pipelines**.

- **Authored two custom Azure RBAC role definitions** — a "Backup Remover" role and a Contributor variant with explicit `notActions` — to enforce **separation-of-duties** between resource management and backup deletion (a ransomware-resilience control missing from Azure's built-in Contributor). **Wired into the CAF archetype framework** and shipped through the production Terraform + Azure DevOps pipeline. **38 commits across the core-governance repo.**
- **Tenant-wide Key Vault compliance audit** — KQL against Azure Resource Graph for soft-delete retention, purge protection, and RBAC authorisation; CSV inventories and a documented review for architecture leadership.
- Built **Service Principal lifecycle tooling** — KQL audit + PowerShell expiring-credential inventory + a Logic Apps / Graph `addPassword` rotation design.
- Implemented **Azure Backup policy compliance reporting** with per-VM exempt-rationale tracking.
- PowerShell tooling: subscription budget automation, ACR token expiry inventory, .NET runtime enumeration across App Services, Hybrid Benefit enablement, cost-allocation tagging across landing zones.
- **KQL-based monitoring contributed to a ~20% reduction in downtime** across supported services.
- Published sanitised sister repos on GitHub: <a href="https://github.com/arnabdey73/iac-azure-core-governance">`iac-azure-core-governance`</a> (CAF Enterprise Scale governance), reusable Terraform module library, and Azure cost-optimisation templates.

---

### Senior Software Engineer (DevOps) — Capgemini Sverige AB
*Sep 2021 – Jul 2024  |  Gothenburg, Sweden*

**Assignment: Volvo Cars — Car Safety R&D (Abakus MLOps / AI Platform)**

*Self-service compute platform via GitOps — supporting product (data science) teams*
- Designed and owned a **GitOps self-service pattern for Azure Databricks**: data scientists request compute via a GitHub issue → YAML manifest PR → **GitHub Actions runs `terraform fmt/validate/plan`** for review → merge triggers `terraform apply`.
- Authored the **Terraform module** with opinionated, governance-friendly defaults baked in: single-user security mode, **30-minute auto-termination, autoscale 1→3 workers**, cluster-log shipping to DBFS, `CAN_RESTART` permissions — **reliable and cost-efficient by construction**.
- Remote state in **Azure Blob Storage** with backend config injected at init from GitHub environment secrets; two-workflow contract (`tf-validate` on PR, `tf-deploy` on merge).
- **Outcome:** provisioning lead time fell from days to same-day; every cluster traceable to a PR, manifest, and named owner; long-tail idle-cluster spend eliminated.

*Kubernetes platform modernisation*
- Contributed to modernising a ~36-node CAE/HPC cluster: OS migration SLES → Ubuntu LTS; stand-up of **Rancher-managed Kubernetes (RKE)**; **Kubeflow** via Helm.
- Built a **production-grade ELK stack** (Elasticsearch, Logstash, Kibana) on LXD with X-Pack security, SSL, and snapshot repositories for observability.

*Dual-cloud benchmarking*
- Built **two matched Terraform stacks** (AWS: EC2 + S3 + KMS + IAM | Azure: VM + Premium BlockBlobStorage) as identically-shaped, disposable test rigs for object-storage benchmarking.

---

### Senior Business Consultant (DevOps) — Tech Mahindra
*Feb 2017 – Sep 2021  |  Bangalore, India  |  Sydney, Australia*

**Assignment: Greenstone Financial Services — Insurance Portal**
- Led DevOps transformation for **.NET / C# microservices**: **Azure DevOps pipelines**, **Terraform for Azure infrastructure**, Docker + Docker Swarm with **Azure Container Registry**, Azure Monitor for observability.

**Assignment: Cisco Systems — CD 2.0 Continuous-Delivery Platform on AWS**
- **Authored the Terraform** for Cisco's CD 2.0 platform on AWS — VPC, subnets, security groups, **EKS cluster, IAM roles, Jenkins on EKS, ECR integration, build-agent fleet, ALB, DNS** — extending an internal reference architecture.
- Wrote a separate **Terraform stack for an AWS observability environment** (EKS + Prometheus Operator via Helm + Grafana + persistent storage + ingress).
- Closed out Cisco's long-running SVN-to-Git migration via Python automation against the Bitbucket REST API — with retry logic and batching for SCM rate limits.

**Assignment: Deutsche Telekom — 5G BSS Slicing Pilot on OpenStack**
- Owned the **DevOps platform side** of DT's 5G Network Slicing commercial pilot, delivering Blue Marble's ~30-microservice BSS suite.
- **Terraform against the OpenStack provider** provisioning the Jenkins / Nexus / Tuleap / Rancher / Keycloak / ELK estate.
- **~46 Jenkins jobs** building BMP microservices, tagging build number + short git SHA, pushing to internal Nexus, updating Kubernetes manifests, triggering Rancher rolling updates.
- Owned a **cross-tenant migration weekend** rehoming 54 Tuleap repositories, Jenkins jobs, Nexus artifacts, Keycloak realm, and live Kubernetes workloads via Python/shell automation.

---

### Senior AEM Administrator (Cloud) — ICF Next
*Sep 2015 – Jan 2017  |  Bangalore, India*

**Assignment: Channel 7 (Australia) — AEM web platform on AWS**
- Built and operated a production AEM web platform on AWS for a national broadcaster — VPC, EC2 lifecycle, Apache HTTPD + Dispatcher hardening, SSL termination, **SAML 2.0 federation (Azure AD / ADFS → AWS IAM)** replacing long-lived IAM user keys.
- Authored **Ansible roles** for AEM install, Apache/Dispatcher deployment, SSL, and base OS — turning instance rebuilds into a runbook rather than a discovery exercise.

---

### Unix / Linux Systems Administrator — HP Enterprise Services
*Nov 2011 – Aug 2015  |  Bangalore, India*

Three-and-a-half years on HP's Global Operations Center under Best Shore Services, rotating across enterprise outsourcing customers (HUL, E.ON, Con-way Inc.) — **24×7 incident handling on customer-critical Linux/Unix estates** (140+ servers), LVM/SAN, kernel tuning, SOP authorship for production runbooks, HP Service Manager / OpenView / Server Automation.

---

## Education

**B.Tech in Computer Science** — West Bengal University of Technology, Kolkata, India (2005 – 2009)

---

## Certifications

- **Microsoft Certified: Azure Fundamentals (AZ-900)** — Mar 2023 *(Credential ID: 801D970BAA49297)*
- **AWS Certified Solutions Architect – Associate (SAA-C03)** — *in progress*
