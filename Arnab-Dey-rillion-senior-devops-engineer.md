<div align="center">
	<h1><b>Arnab Dey</b></h1>
	<p>
		Stockholm, Sweden | +46 0764516092 | <a href="mailto:arnabdey009@gmail.com">arnabdey009@gmail.com</a><br>
		<a href="https://www.linkedin.com/in/arnabdey73">LinkedIn</a> | <a href="https://github.com/arnabdey73">GitHub</a>
	</p>
</div>

---

## Professional Summary

Senior DevOps / Platform Engineer with **15+ years in IT** and **9+ years building shared platform foundations** that product teams actually use — most recently a **GitOps self-service Azure Databricks platform at Volvo Cars** (PR-driven Terraform via GitHub Actions, cluster lead time days → same-day) and a **~100-subscription Azure CAF Enterprise Scale governance estate at Stena Metall** delivered through the production Terraform + Azure DevOps pipeline. Deep on Kubernetes (AKS, EKS, Rancher RKE, K3s), Terraform at module-library scale, Azure across the full stack, and the security-first patterns — custom RBAC, Key Vault, SAML federation, separation-of-duties — that keep platforms compliant as they grow. Maintain a live public **K3s + ArgoCD + Prometheus + cert-manager + sealed-secrets** GitOps reference platform on GitHub. Stockholm-based, fluent in English.

---

## Core Skills

**Kubernetes (production, multi-flavour)** — AKS, EKS, **Rancher RKE**, K3s; cluster operations, networking, RBAC, ingress, persistent storage, rolling updates against live workloads; Helm, Kubeflow, **ArgoCD** (GitOps reference platform), cert-manager, sealed-secrets.

**GitOps & platform engineering** — Public reference platform: <a href="https://github.com/arnabdey73">K3s + ArgoCD + Prometheus + Grafana + cert-manager + sealed-secrets</a>; Volvo Databricks GitOps self-service (issue → PR → `plan` → merge → `apply`); shared module libraries with opinionated, governance-friendly defaults that make the right thing the easy thing.

**Microsoft Azure (primary)** — CAF Enterprise Scale / Landing Zones (~100-subscription estate, multi-management-group hierarchy), AKS, App Services, Compute (VM/VMSS), Networking (VNet, NSG, Private Endpoints), Storage (Blob, ADLS, disk-encryption-sets), Key Vault (soft-delete, purge protection, RBAC authorisation), Entra ID, Azure Policy, Azure RBAC (including custom role definitions), Azure Monitor, Log Analytics / KQL, Azure Resource Graph, ACR.

**Infrastructure as Code** — Terraform (AzureRM, AWS, OpenStack, Databricks providers); reusable module libraries; archetype-driven CAF deployment; remote state in Azure Blob with backend config injected from CI environment secrets; two-workflow `validate-on-PR` / `apply-on-merge` contract; module versioning, drift handling, state inspection.

**CI/CD — both stacks the JD calls for** — **GitHub Actions** (Volvo Terraform delivery on PR/merge), **Azure DevOps Pipelines** (Stena governance Terraform; Greenstone .NET microservices), GitLab CI, Jenkins (declarative + scripted, EKS-hosted, on-prem), Gerrit, ArgoCD.

**Security-first thinking** — **Authored two custom Azure RBAC role definitions** at Stena (separation-of-duties between resource management and backup deletion — a ransomware-resilience control missing from Azure's built-in Contributor); tenant-wide Key Vault compliance audits; Service Principal lifecycle + credential-rotation design (Logic Apps + Graph `addPassword`); SAML 2.0 federation (Azure AD / ADFS → AWS IAM) replacing long-lived keys; least-privilege patterns; network security via NSG / Private Endpoints.

**SaaS / web workload support** — Production AEM web platform on AWS for a national broadcaster (Channel 7 — VPC, EC2, Apache HTTPD + Dispatcher, SSL termination, SAML SSO); .NET / C# microservices on Azure DevOps + Docker Swarm + ACR (Greenstone); ~30-microservice BSS suite for Deutsche Telekom 5G pilot. Comfortable supporting web/SaaS product teams from the platform side.

**Cloud (other)** — AWS (EC2, S3, VPC, EKS, IAM, ECR, ALB, KMS, CloudWatch); OpenStack (Deutsche Telekom 5G commercial pilot).

**Scripting & automation** — Python (REST/SCM automation, CLI), PowerShell (Azure governance — SP lifecycle, ACR token expiry, App Service .NET runtime audits, budget automation), Bash.

**Observability** — Azure Monitor, Log Analytics / KQL, Prometheus, Grafana, ELK Stack, CloudWatch.

**Languages** — English (fluent), Swedish (SFI C-level).

---

## Professional Experience

### DevOps Engineer — AFRY Digital Solutions AB
*May 2025 – Present  |  Stockholm, Sweden*

**Assignment: Ericsson AB — CI Engineer, Tiger Test Tools (Sep 2025 – Present)**
- Maintain and support the end-to-end **CI flow for radio-communication smoke and regression testing** — Git, Gerrit, Jenkins, Docker, Linux.

**Platform engineering (internal reference project — public on GitHub)**
- Designed and operate a **GitOps Kubernetes platform**: K3s + **ArgoCD** + Prometheus + Grafana + cert-manager + sealed-secrets. Live demo of the platform pattern — declarative cluster state in Git, ArgoCD reconciling, secrets sealed at rest, ingress and certificates automated, observability built in. Maintained as a working reference for shared platform foundations.

---

### Cloud Engineer — Stena Metall AB
*Aug 2024 – Jan 2025  |  Gothenburg, Sweden*

Cloud Infrastructure Engineer on the central Cloud Office (Governance) of a mature **Azure CAF Enterprise Scale** estate — **~100 subscriptions, multi-management-group hierarchy**, production workloads for a multi-billion-SEK industrial group. All infrastructure delivered as **Terraform via Azure DevOps pipelines**.

- **Authored custom Azure RBAC role definitions** — a "Backup Remover" role and a Contributor variant with explicit `notActions` — to enforce **separation-of-duties** between resource management and backup deletion (a ransomware-resilience control missing from Azure's built-in Contributor). **Wired into the CAF archetype framework** and shipped through the production Terraform + Azure DevOps pipeline. 
- **Tenant-wide Key Vault compliance audit** — KQL against Azure Resource Graph for soft-delete retention, purge protection, and RBAC authorisation; CSV inventories and a documented review for architecture leadership.
- Built **Service Principal lifecycle tooling** — KQL audit + PowerShell expiring-credential inventory + a Logic Apps / Graph `addPassword` rotation design.
- Implemented **Azure Backup policy compliance reporting** with per-VM exempt-rationale tracking.
- PowerShell tooling: subscription budget automation, ACR token expiry inventory, .NET runtime enumeration across App Services, Hybrid Benefit enablement, cost-allocation tagging across landing zones.
- KQL-based monitoring contributed to a **~20% reduction in downtime** across supported services.
- Published sanitised sister repos on GitHub: <a href="https://github.com/arnabdey73/iac-azure-core-governance">`iac-azure-core-governance`</a> (CAF Enterprise Scale governance), reusable Terraform module library, and Azure cost-optimisation templates.

---

### Senior Software Engineer (DevOps) — Capgemini Sverige AB
*Sep 2021 – Jul 2024  |  Gothenburg, Sweden*

**Assignment: Volvo Cars — Car Safety R&D (Abakus MLOps / AI Platform)**

*Self-service compute platform via GitOps — supporting product (data science) teams*
- Designed and owned a **GitOps self-service pattern for Azure Databricks** used by Car Safety data scientists: request compute via a GitHub issue → YAML manifest PR → **GitHub Actions runs `terraform fmt/validate/plan`** for review → merge triggers `terraform apply`.
- Authored the **Terraform module** with opinionated, governance-friendly defaults baked in: single-user security mode, **30-minute auto-termination, autoscale 1→3 workers**, cluster-log shipping to DBFS, `CAN_RESTART` permissions — making clusters cheap and safe by construction.
- Remote state in **Azure Blob Storage** with backend config injected at init from GitHub environment secrets; two-workflow contract (`tf-validate` on PR, `tf-deploy` on merge).
- **Outcome:** provisioning lead time dropped from days to same-day; every cluster traceable to a PR, a manifest, and a named owner; long-tail idle-cluster spend eliminated.

*Kubernetes platform modernisation*
- Contributed to modernising a ~36-node CAE/HPC cluster: OS migration SLES → Ubuntu LTS; stand-up of **Rancher-managed Kubernetes (RKE)** with worker fleet; **Kubeflow** via Helm.
- Built a **production-grade ELK stack** for observability with X-Pack security, SSL, and snapshot repositories.

*Dual-cloud benchmarking*
- Built **two matched Terraform stacks** (AWS: EC2 + S3 + KMS + IAM | Azure: VM + Premium BlockBlobStorage) as identically-shaped, disposable test rigs for object-storage benchmarking on equal footing.

---

### Senior Business Consultant (DevOps) — Tech Mahindra
*Feb 2017 – Sep 2021  |  Bangalore, India  |  Sydney, Australia*

**Assignment: Cisco Systems — CD 2.0 Continuous-Delivery Platform on AWS**
- **Authored the Terraform** for Cisco's CD 2.0 platform on AWS — VPC, subnets, security groups, **EKS cluster, IAM roles, Jenkins on EKS, ECR integration, build-agent fleet, ALB, DNS** — extending an internal reference architecture originally on on-prem OpenShift.
- Wrote a separate **Terraform stack for an AWS observability environment** (EKS + Prometheus Operator via Helm + Grafana + persistent storage + ingress).
- Closed out Cisco's long-running SVN-to-Git migration via Python automation against the Bitbucket REST API — with retry logic and batching for SCM rate limits.

**Assignment: Deutsche Telekom — 5G BSS Slicing Pilot on OpenStack**
- Owned the **DevOps platform side** of DT's 5G Network Slicing commercial pilot, delivering Blue Marble's ~30-microservice BSS suite plus the Phenom UI.
- **Terraform against the OpenStack provider** provisioning the Jenkins / Nexus / Tuleap / Rancher / Keycloak / ELK estate.
- **~46 Jenkins jobs** building BMP microservices, tagging build number + short git SHA, pushing to internal Nexus, updating Kubernetes manifests, triggering Rancher rolling updates.
- Owned a **cross-tenant migration weekend** rehoming 54 Tuleap repositories, Jenkins jobs, Nexus artifacts, Keycloak realm, and live Kubernetes workloads via Python/shell automation.

**Assignment: Greenstone Financial Services — Insurance Portal**
- Led DevOps transformation for **.NET / C# microservices**: **Azure DevOps pipelines**, **Terraform for Azure infrastructure**, Docker + Docker Swarm with **Azure Container Registry**, Azure Monitor for observability.

**Assignment: CA ANZ**
- Architected the **GitLab-based CI and source-control model** — branching strategy, repository standards, pipeline conventions; supported team adoption through documentation and knowledge transfer.

---

### Senior AEM Administrator (Cloud) — ICF Next
*Sep 2015 – Jan 2017  |  Bangalore, India*

**Assignment: Channel 7 (Australia) — AEM web platform on AWS**
- Built and operated a production AEM web platform on AWS for a national broadcaster — VPC design, EC2 lifecycle, Apache HTTPD + Dispatcher hardening, SSL termination, **SAML 2.0 federation (Azure AD / ADFS → AWS IAM)** replacing long-lived IAM user keys.
- Authored **Ansible roles** for AEM install, Apache/Dispatcher deployment, SSL, and base OS — turning instance rebuilds into a runbook rather than a discovery exercise.

---

### Unix / Linux Systems Administrator — HP Enterprise Services
*Nov 2011 – Aug 2015  |  Bangalore, India*

Three-and-a-half years on HP's Global Operations Center under Best Shore Services, rotating across enterprise outsourcing customers (HUL, E.ON, Con-way Inc.) — 24×7 incident handling, LVM/SAN, kernel tuning, SOP authorship, HP Service Manager / OpenView / Server Automation.

---

## Education

**B.Tech in Computer Science** — West Bengal University of Technology, Kolkata, India (2005 – 2009)

---

## Certifications

- **Microsoft Certified: Azure Fundamentals (AZ-900)** — Mar 2023 *(Credential ID: 801D970BAA49297)*
- **AWS Certified Solutions Architect – Associate (SAA-C03)** — *in progress*
