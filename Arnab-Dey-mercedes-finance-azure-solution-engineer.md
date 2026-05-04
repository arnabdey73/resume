<div align="center">
	<h1><b>Arnab Dey</b></h1>
	<p>
		Stockholm, Sweden (open to relocation to Malmö) | +46 0764516092 | <a href="mailto:arnabdey009@gmail.com">arnabdey009@gmail.com</a><br>
		<a href="https://www.linkedin.com/in/arnabdey73">LinkedIn</a> | <a href="https://github.com/arnabdey73">GitHub</a>
	</p>
</div>

---

## Professional Summary

Senior Cloud / Solution Engineer with **15+ years in IT** and **9+ years owning Azure platforms end-to-end** for enterprise clients — delivered through three managed-service-provider consultancies (AFRY, Capgemini, Tech Mahindra) onto assignments at Volvo Cars, Ericsson, Stena Metall, Cisco, Deutsche Telekom, and others. Comfortable wearing both engineer and solution-owner hats: at Stena Metall I designed and shipped governance controls into a ~100-subscription Azure CAF estate while collaborating with architecture leadership and stakeholders on roadmap; at Volvo Cars I owned a **GitOps self-service Azure Databricks platform** that reduced data-science cluster provisioning from days to same-day. Strong on **Azure containers (AKS, VMs)**, **CI/CD across Azure DevOps and GitHub Actions**, **Python**, **Azure Monitor / Log Analytics / KQL**, **FinOps**, and the API-integration / vendor-collaboration patterns that come with running production Azure workloads in regulated, multi-vendor environments. Stockholm-based today, open to relocation to Malmö. Fluent in English.

---

## Core Skills

**Azure end-to-end** — CAF Enterprise Scale / Landing Zones (~100-subscription estate), **Compute** (VM/VMSS, App Services), **Containers** (**AKS**, ACR, Docker; familiar with Container Apps / ACI patterns and able to pick up quickly), **Networking** (VNet, NSG, Private Endpoints), **Identity** (Entra ID, RBAC including custom role definitions, Service Principals), **Storage** (Blob, ADLS, disk-encryption-sets), **Key Vault**, Azure Policy, Azure Resource Graph.

**Solution ownership & stakeholder collaboration** — Architecture-leadership reviews of Key Vault compliance audits at Stena Metall; design and roll-out of GitOps self-service for data scientists at Volvo Cars (issue-template → manifest PR → review → apply); CI engagement templates and onboarding for application teams at Cisco; cross-tenant migration planning weekend at Deutsche Telekom — comfortable owning the lifecycle from concept through delivery and stakeholder sign-off.

**API integration & vendor collaboration** — Microsoft Graph API (Service Principal credential rotation design via Logic Apps + `addPassword`), Azure Resource Graph (KQL audits across tenants), Bitbucket REST (Cisco SVN→Git migration via Python with retry/rate-limit handling), OpenStack provider against PAN-NET; managed-service-provider career means continuous collaboration with internal stakeholders and external vendors.

**CI/CD** — **Azure DevOps Pipelines** (Stena governance Terraform; Greenstone .NET microservices), **GitHub Actions** (Volvo Cars Terraform delivery on PR/merge); reusable workflow templates, automated quality gates (`fmt/validate/plan` separated from `apply`), GitLab CI, Jenkins (declarative + scripted, EKS-hosted, on-prem), Gerrit, ArgoCD.

**Application stacks I deliver for (CI/CD + Azure infrastructure, not application code)** — **C# / .NET microservices** (Greenstone Financial Services — Azure DevOps pipelines + Docker Swarm + ACR; Stena .NET runtime audits across the App Service estate via PowerShell); Java/JVM and Node.js workloads incidentally as part of broader platform delivery.

**Languages I write** — **Python** (REST/SCM automation, CLI tooling, public automation toolkit), **PowerShell** (Azure governance — SP lifecycle, ACR token expiry, .NET runtime enumeration, budget automation), **Bash**.

**Observability & monitoring** — **Azure Monitor**, **Application Insights**, **Log Analytics / KQL**, **Alerts** (KQL-based monitoring at Stena contributed to a ~20% reduction in downtime); Prometheus, Grafana, ELK Stack, CloudWatch, cert-manager.

**FinOps & cost** — Subscription budget automation (PowerShell), Hybrid Benefit enablement, ACR token / SP credential hygiene, cost-allocation tagging across landing zones, .NET runtime enumeration for App Service rationalisation, idle-cluster elimination via autoscale + auto-termination defaults baked into Terraform modules; published Azure cost-optimisation Terraform templates (public repo).

**Infrastructure as Code** — Terraform (AzureRM, AWS, OpenStack, Databricks providers); reusable module libraries; archetype-driven CAF deployment; remote state in Azure Blob.

**AI / data adjacency** — Volvo Cars Car Safety R&D MLOps platform (Databricks + dual-cloud benchmarking + Kubeflow on Rancher RKE) — comfortable supporting AI-driven workloads from the platform side. Internal AI-powered Resume Builder Agent as a side project (sanitised public repo).

**Managed Service Provider background** — Career-long: AFRY (current), Capgemini, Tech Mahindra, ICF Next, HP Enterprise Services — five MSP-style consultancies, customer-embedded engagements across Sweden, Australia, India, the UK, and Germany.

**Languages** — English (fluent), Swedish (SFI C-level).

---

## Professional Experience

### DevOps Engineer — AFRY Digital Solutions AB
*May 2025 – Present  |  Stockholm, Sweden*

**Assignment: Ericsson AB — CI Engineer, Tiger Test Tools (Sep 2025 – Present)**
- Maintain and support the end-to-end **CI flow for radio-communication smoke and regression testing** — Git, Gerrit, Jenkins, Docker, Linux.

**Platform engineering (internal reference project — public on GitHub)**
- Designed and operate a **GitOps Kubernetes platform**: K3s + ArgoCD + Prometheus + Grafana + cert-manager + sealed-secrets — a working reference for cloud-native delivery patterns.

---

### Cloud Engineer — Stena Metall AB
*Aug 2024 – Jan 2025  |  Gothenburg, Sweden*

Cloud Infrastructure Engineer on the central Cloud Office (Governance) of a mature **Azure CAF Enterprise Scale** estate — **~100 subscriptions, multi-management-group hierarchy**, production workloads for a multi-billion-SEK industrial group. All infrastructure delivered as **Terraform via Azure DevOps pipelines**.

- **Solution ownership**: collaborated with architecture leadership on a tenant-wide **Key Vault compliance audit** (KQL across Azure Resource Graph for soft-delete retention, purge protection, and RBAC authorisation), producing CSV inventories and a documented review for sign-off.
- **Authored two custom Azure RBAC role definitions** — a "Backup Remover" role and a Contributor variant with explicit `notActions` — to enforce separation-of-duties between resource management and backup deletion. Wired into the CAF archetype framework and shipped through the production Terraform + Azure DevOps pipeline. **38 commits across the core-governance repo.**
- Built **Service Principal lifecycle tooling** integrating Azure Resource Graph (KQL audit), PowerShell (expiring-credential inventory), and a Logic Apps + Microsoft Graph `addPassword` rotation design — a multi-API integration pattern.
- Implemented **Azure Backup policy compliance reporting** with per-VM exempt-rationale tracking.
- **PowerShell tooling**: subscription budget automation, ACR token expiry inventory, **.NET runtime enumeration across App Services**, Hybrid Benefit enablement, cost-allocation tagging.
- **KQL-based monitoring contributed to a ~20% reduction in downtime** across supported services.
- Published sanitised sister repos on GitHub: <a href="https://github.com/arnabdey73/iac-azure-core-governance">`iac-azure-core-governance`</a> (CAF Enterprise Scale governance), reusable Terraform module library, and Azure cost-optimisation templates.

---

### Senior Software Engineer (DevOps) — Capgemini Sverige AB
*Sep 2021 – Jul 2024  |  Gothenburg, Sweden*

**Assignment: Volvo Cars — Car Safety R&D (Abakus MLOps / AI Platform)**

*Self-service compute platform via GitOps — solution ownership end-to-end*
- Designed and owned a **GitOps self-service pattern for Azure Databricks** used by Car Safety data scientists: request compute via a GitHub issue → YAML manifest PR → **GitHub Actions runs `terraform fmt/validate/plan`** for review → merge triggers `terraform apply`.
- Authored the **Terraform module** with opinionated, governance-friendly defaults: single-user security mode, **30-minute auto-termination, autoscale 1→3 workers**, cluster-log shipping to DBFS, `CAN_RESTART` permissions — making clusters cheap and safe by construction (FinOps by design).
- Two-workflow contract (`tf-validate` on PR, `tf-deploy` on merge); remote state in Azure Blob with backend config injected from GitHub environment secrets.
- **Outcome:** provisioning lead time fell from days to same-day; every cluster traceable to a PR, manifest, and named owner; idle-cluster spend eliminated.

*Kubernetes platform modernisation*
- Contributed to modernising a ~36-node CAE/HPC cluster: OS migration SLES → Ubuntu LTS; stand-up of **Rancher-managed Kubernetes (RKE)**; **Kubeflow** via Helm.
- Built a **production-grade ELK stack** for observability with X-Pack security, SSL, and snapshot repositories.

*Dual-cloud benchmarking*
- Built **two matched Terraform stacks** (AWS + Azure) as identically-shaped, disposable test rigs for object-storage benchmarking on equal footing.

---

### Senior Business Consultant (DevOps) — Tech Mahindra
*Feb 2017 – Sep 2021  |  Bangalore, India  |  Sydney, Australia*

**Assignment: Greenstone Financial Services — Insurance Portal**
- Led DevOps transformation for **.NET / C# microservices**: **Azure DevOps pipelines**, **Terraform for Azure infrastructure**, Docker + Docker Swarm with **Azure Container Registry**, Azure Monitor for observability.

**Assignment: Cisco Systems — CD 2.0 on AWS**
- **Authored the Terraform** for Cisco's CD 2.0 platform on AWS (VPC, EKS, IAM, Jenkins, ECR, ALB) extending an internal reference architecture; **API integration via Bitbucket REST** in Python to close out a long-running SVN-to-Git migration with retry / rate-limit handling.
- Onboarded application teams via **CI engagement templates**, Bitbucket/Crucible provisioning, and Jenkinsfile adaptation — a stakeholder-facing solution-ownership role.

**Assignment: Deutsche Telekom — 5G BSS Slicing Pilot on OpenStack**
- Owned the **DevOps platform side** of DT's 5G Network Slicing commercial pilot, delivering Blue Marble's ~30-microservice BSS suite — Terraform against the OpenStack provider, ~46 Jenkins jobs, Rancher rolling updates.
- Owned a **cross-tenant migration weekend** rehoming 54 Tuleap repositories, Jenkins jobs, Nexus artifacts, Keycloak realm, and live Kubernetes workloads via Python/shell automation.

**Assignment: CA ANZ**
- Architected the **GitLab-based CI and source-control model** — branching strategy, repository standards; supported team adoption through documentation and knowledge transfer.

---

### Senior AEM Administrator (Cloud) — ICF Next
*Sep 2015 – Jan 2017  |  Bangalore, India*

**Assignment: Channel 7 (Australia) — AEM web platform on AWS**
- Built and operated a production AEM platform on AWS — VPC, EC2 lifecycle, Apache HTTPD + Dispatcher hardening, SSL termination, **SAML 2.0 federation (Azure AD / ADFS → AWS IAM)** replacing long-lived IAM keys.
- Authored **Ansible roles** for AEM install, Apache/Dispatcher deployment, SSL, and base OS.

---

### Unix / Linux Systems Administrator — HP Enterprise Services
*Nov 2011 – Aug 2015  |  Bangalore, India*

Three-and-a-half years on HP's Global Operations Center under Best Shore Services, rotating across enterprise outsourcing customers (HUL, E.ON, Con-way Inc.) — 24×7 incident handling, LVM/SAN, kernel tuning, SOP authorship for production runbooks, HP Service Manager / OpenView / Server Automation.

---

## Education

**B.Tech in Computer Science** — West Bengal University of Technology, Kolkata, India (2005 – 2009)

---

## Certifications

- **Microsoft Certified: Azure Fundamentals (AZ-900)** — Mar 2023 *(Credential ID: 801D970BAA49297)*
- **AWS Certified Solutions Architect – Associate (SAA-C03)** — *in progress*
