<div align="center">
	<h1><b>Arnab Dey</b></h1>
	<p>
		Stockholm, Sweden | +46 0764516092 | <a href="mailto:arnabdey009@gmail.com">arnabdey009@gmail.com</a><br>
		<a href="https://www.linkedin.com/in/arnabdey73">LinkedIn</a> | <a href="https://github.com/arnabdey73">GitHub</a>
	</p>
</div>

---

## Professional Summary

DevOps / Cloud Engineer with **15+ years in IT** and **9+ years building and operating Azure platforms with Terraform** at enterprise scale. Hands-on across the full Azure stack — Compute, Networking, Storage, App Services, Key Vault, AKS — delivered through **Terraform modules, archetype-driven CAF Enterprise Scale (Landing Zones)**, and **Azure DevOps / GitHub Actions** pipelines. Most recent enterprise assignment was on a ~100-subscription Azure CAF estate at Stena Metall, where I authored custom RBAC role definitions, ran tenant-wide Key Vault compliance audits, and shipped governance Terraform via the existing Azure DevOps pipeline. Comfortable owning the IaC contract end-to-end: module design, remote state, plan-review workflows, drift, secrets, and cost. Stockholm-based, fluent in English, Swedish at SFI C-level.

---

## Core Skills

**Microsoft Azure** — CAF Enterprise Scale / Landing Zones (~100-subscription estate, multi-management-group hierarchy), Compute (VMs, VMSS, App Services), Networking (VNet, NSG, Private Endpoints), Storage (Blob, ADLS, disk-encryption-sets), Key Vault (soft-delete, purge protection, RBAC authorisation), AKS, Azure Container Registry, Entra ID, Azure Policy, Azure RBAC (including custom role definitions), Azure Monitor, Log Analytics / KQL, Azure Resource Graph.

**Terraform (deep)** — AzureRM, AWS, OpenStack, Databricks providers; reusable module libraries with opinionated, governance-friendly defaults; remote state in Azure Blob with backend config injected from CI environment secrets; archetype-driven CAF deployment; `terraform fmt/validate/plan/apply` separated across PR-time and merge-time workflows; module versioning, state inspection, drift handling.

**HashiCorp ecosystem** — Terraform daily; Vault-style secrets patterns via Azure Key Vault + Kubernetes sealed-secrets in the GitOps reference platform; familiar with Packer image-building patterns from AEM/AMI work; conceptually fluent on Consul / Nomad.

**CI/CD** — Azure DevOps Pipelines (governance Terraform delivery at Stena Metall; .NET microservices for Greenstone), GitHub Actions (Terraform PR-driven workflows for Volvo Cars Databricks), GitLab CI, Jenkins (declarative + scripted, EKS-hosted, on-prem), Gerrit, ArgoCD.

**Containers & Orchestration** — Kubernetes (AKS, EKS, Rancher RKE, K3s), Docker, Helm, Kubeflow, ArgoCD, container registries (ACR, ECR, Nexus).

**Scripting** — Python (automation, REST/SCM tooling, CLI), PowerShell (Azure governance — SP lifecycle, ACR token expiry, App Service .NET runtime audits, Hybrid Benefit, budget automation), Bash.

**Security & Governance** — Custom Azure RBAC role definitions, Key Vault compliance, Service Principal lifecycle / credential rotation design (Logic Apps + Graph `addPassword`), Azure Policy, separation-of-duties / ransomware-resilience controls, SAML federation, least-privilege patterns.

**FinOps / Cost** — Subscription budget automation (PowerShell), Hybrid Benefit enablement, idle-cluster elimination through autoscale + auto-termination defaults, cost-allocation tagging, ACR token / SP credential hygiene, Azure cost-optimisation Terraform templates (public sanitised repo).

**Observability** — Azure Monitor, Log Analytics / KQL, Prometheus, Grafana, ELK Stack, cert-manager.

**Languages** — English (fluent), Swedish (SFI C-level).

---

## Professional Experience

### DevOps Engineer — AFRY Digital Solutions AB
*May 2025 – Present  |  Stockholm, Sweden*

**Assignment: Ericsson AB — CI Engineer, Tiger Test Tools (Sep 2025 – Present)**
- Maintain and support the end-to-end **CI flow for radio-communication smoke and regression testing** — Git, Gerrit, Jenkins, Docker, Linux.
- Troubleshoot pipeline, hardware, and test-server issues across daily delivery and validation workflows.

**Platform engineering (internal reference project)**
- Designed and deployed a **GitOps-based Kubernetes platform** (K3s + ArgoCD + Prometheus + Grafana + cert-manager + sealed-secrets) as a cloud-native delivery reference — illustrates the same **secrets-management and IaC patterns** that map onto Vault + Terraform in an enterprise Azure context. Maintained as a live public demo on GitHub.

---

### Cloud Engineer — Stena Metall AB
*Aug 2024 – Jan 2025  |  Gothenburg, Sweden*

Cloud Infrastructure Engineer on the central Cloud Office (Governance) of a mature **Azure CAF Enterprise Scale** estate — **~100 subscriptions, multi-management-group hierarchy**, production workloads for a multi-billion-SEK industrial group. All infrastructure delivered as **Terraform via Azure DevOps pipelines**.

- **Authored two custom Azure RBAC role definitions** — a "Backup Remover" role and a Contributor variant with explicit `notActions` — to enforce separation-of-duties between resource management and backup deletion (a ransomware-resilience control missing from Azure's built-in Contributor role). **Wired into the CAF archetype framework** and shipped through the existing Terraform + Azure DevOps pipeline. **38 commits across the core-governance repo.**
- Delivered a **tenant-wide Key Vault compliance audit** — KQL against Azure Resource Graph for soft-delete retention, purge protection, and RBAC authorisation — producing CSV inventories and a documented review for architecture leadership.
- Built **Service Principal lifecycle tooling** — KQL audit for 30-day create/update/delete events, PowerShell for expiring-credential inventory, and a design for **client-secret rotation via Logic Apps + Graph API `addPassword`**.
- Implemented **Azure Backup policy compliance reporting** with per-VM exempt-rationale tracking.
- Delivered fixes across multiple **application landing-zone repositories** — IdentityNow VA, Key Vault with disk-encryption-set, cost-allocation tagging, AzureRM provider version alignment.
- **FinOps contributions**: PowerShell subscription budget automation, ACR token expiry inventory, .NET runtime enumeration across App Services, Hybrid Benefit enablement.
- **KQL-based monitoring contributed to a ~20% reduction in downtime** across supported services.
- Published sanitised sister repos on GitHub: <a href="https://github.com/arnabdey73/iac-azure-core-governance">`iac-azure-core-governance`</a> (CAF Enterprise Scale governance), reusable Terraform module library, and Azure cost-optimisation templates.

---

### Senior Software Engineer (DevOps) — Capgemini Sverige AB
*Sep 2021 – Jul 2024  |  Gothenburg, Sweden*

**Assignment: Volvo Cars — Car Safety R&D (MLOps / AI Platform)**

*Self-service Azure platform via GitOps — Terraform + GitHub Actions*
- Designed and owned a **GitOps self-service pattern for Azure Databricks**: data scientists request compute via a GitHub issue → YAML manifest PR → **GitHub Actions runs `terraform fmt/validate/plan` for review** → merge triggers `terraform apply`.
- Authored the **Terraform module** with opinionated, governance-friendly defaults baked in: single-user security mode, **30-minute auto-termination, autoscale 1→3 workers**, cluster-log shipping to DBFS, `CAN_RESTART` permissions — making clusters **cheap and safe by construction (FinOps by design)**.
- **Remote state in Azure Blob Storage** with backend config injected at init from GitHub environment secrets; two-workflow contract (`tf-validate` on PR, `tf-deploy` on merge).
- **Outcome:** provisioning lead time dropped from days to same-day; every cluster traceable to a PR, a manifest, and a named owner; eliminated long-tail idle-cluster spend.

*Kubernetes platform modernisation*
- Contributed to modernising a ~36-node CAE/HPC cluster: OS migration SLES → Ubuntu LTS; stand-up of **Rancher-managed Kubernetes (RKE)**; **Kubeflow** via Helm.
- Built a **production-grade ELK stack** for observability with X-Pack security, SSL, and snapshot repositories.

*Dual-cloud ML benchmarking*
- Built **two matched Terraform stacks** (AWS: EC2 + S3 + KMS + IAM | Azure: VM + Premium BlockBlobStorage) as identically-shaped, disposable test rigs for object-storage benchmarking.

---

### Senior Business Consultant (DevOps) — Tech Mahindra
*Feb 2017 – Sep 2021  |  Bangalore, India  |  Sydney, Australia*

**Assignment: Greenstone Financial Services — Insurance Portal**
- Led DevOps transformation for .NET microservices: **Azure DevOps pipelines**, **Terraform for Azure infrastructure**, Docker + Docker Swarm with **Azure Container Registry**, **Azure Monitor** for observability.

**Assignment: Cisco Systems — CD 2.0 on AWS**
- **Authored the Terraform** for Cisco's CD 2.0 continuous-delivery platform on AWS — VPC, subnets, security groups, **EKS cluster, IAM roles, Jenkins on EKS, ECR integration, build-agent fleet, ALB, DNS** — extending an internal reference architecture originally built on on-prem OpenShift.
- Wrote a separate **Terraform stack for an AWS observability environment** (EKS + Prometheus Operator via Helm + Grafana + persistent storage + ingress).
- Closed out Cisco's long-running SVN-to-Git migration via Python automation against the Bitbucket REST API — with retry logic and batching for SCM rate limits.

**Assignment: Deutsche Telekom — 5G BSS Slicing Pilot on OpenStack**
- Owned the **DevOps platform side** of DT's 5G Network Slicing commercial pilot — **Terraform against the OpenStack provider** provisioning the Jenkins / Nexus / Tuleap / Rancher / Keycloak / ELK estate; **~46 Jenkins jobs** building ~30 microservices, tagging, pushing to Nexus, updating Kubernetes manifests, triggering Rancher rolling updates.
- Owned a **cross-tenant migration weekend** rehoming 54 Tuleap repos, Jenkins jobs, Nexus artifacts, Keycloak realm, and live Kubernetes workloads via Python/shell automation — nothing rebuilt from scratch.

**Assignment: CA ANZ**
- Architected the **GitLab-based CI and source-control model** — branching strategy, repository standards, pipeline conventions; supported team adoption through documentation and knowledge transfer.

---

### Senior AEM Administrator (Cloud) — ICF Next
*Sep 2015 – Jan 2017  |  Bangalore, India*

**Assignment: Channel 7 (Australia) — AEM on AWS**
- Built and operated a production AEM platform on AWS — VPC, EC2 lifecycle, Apache HTTPD + Dispatcher hardening, SSL termination, **SAML 2.0 federation (Azure AD / ADFS → AWS IAM)** replacing long-lived IAM user keys.
- Authored **Ansible roles** for AEM install, Apache/Dispatcher deployment, SSL, and base OS — making instance rebuilds a runbook rather than a discovery exercise.

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
