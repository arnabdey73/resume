<div align="center">
	<h1><b>Arnab Dey</b></h1>
	<p>
		Stockholm, Sweden | +46 0764516092 | <a href="mailto:arnabdey009@gmail.com">arnabdey009@gmail.com</a><br>
		<a href="https://www.linkedin.com/in/arnabdey73">LinkedIn</a> | <a href="https://github.com/arnabdey73">GitHub</a>
	</p>
</div>

---

## Professional Summary

Senior Platform Engineer with **15+ years in IT** and **9+ years building Azure / Kubernetes / Terraform platforms** that take friction out of the way for product teams. I build with code — Terraform for infrastructure, GitHub Actions and ArgoCD for delivery, Helm for the K8s layer — and favour reviewable, repeatable patterns over manual operations. Hands-on across Azure CAF Enterprise Scale, Kubernetes (Rancher RKE, K3s, AKS, EKS), GitHub Actions, ArgoCD, Helm, Prometheus/Grafana, and Azure Policy / RBAC. Active user of AI tooling — Claude Code in the daily workflow, an AI-powered side project on GitHub — and a believer that the platform team's job is to remove bottlenecks, not become one. Stockholm-based, fluent in English, Swedish at SFI C-level.

---

## Core Skills

**Kubernetes** — Rancher RKE (Volvo HPC), K3s (public reference platform), AKS, EKS (Cisco CD 2.0); Helm chart authoring and operator deployment (Kubeflow, Prometheus Operator).

**Azure (primary)** — CAF Enterprise Scale at ~100-subscription scale, multi-management-group hierarchy, Azure Policy, Azure RBAC (including custom role definitions), Entra ID, Key Vault, Log Analytics / KQL, App Services, ACR, AKS, Logic Apps, Resource Graph.

**Infrastructure as Code** — Terraform (AzureRM, AWS, OpenStack, Databricks providers), reusable module libraries, archetype-driven CAF, ARM templates (Bicep-adjacent), Ansible roles.

**CI/CD & GitOps** — **GitHub Actions** (PR-driven `terraform plan/apply`), **ArgoCD**, Helm, Azure DevOps Pipelines, Jenkins, GitLab CI, Gerrit. Two-workflow GitOps pattern with environment-scoped secrets and remote state.

**Linux & Networking** — RHEL, SLES, Ubuntu, Solaris; LVM/SAN, kernel tuning, 24×7 SLA experience; VPC / subnet / security-group design across AWS, Azure, OpenStack.

**Observability & Reliability** — Prometheus, Grafana, Azure Monitor, Log Analytics / KQL, ELK Stack with snapshot repositories, cert-manager, sealed-secrets. Backup-integrity controls via custom RBAC.

**Languages & Scripting** — Python (REST/SCM automation, CLI tooling), Bash, PowerShell.

**Product-stack adjacency** — Azure DevOps pipelines for **.NET / C# microservices** (Greenstone); App Service .NET runtime audits (Stena Metall); MongoDB platform support (Cisco CD 2.0, DT 5G BSS).

**AI in the workflow** — Claude Code for scripting, debugging, and review; AI-powered Resume Builder Agent side project; comfortable building with LLMs as a daily tool, not a novelty.

**Languages** — English (fluent), Swedish (SFI C-level).

---

## Professional Experience

### DevOps Engineer — AFRY Digital Solutions AB
*May 2025 – Present  |  Stockholm, Sweden*

**Assignment: Ericsson AB — CI Engineer, Tiger Test Tools (Sep 2025 – Present)**
- Maintain the end-to-end CI flow for radio-communication smoke and regression testing — Git, Gerrit, Jenkins, Docker, Linux. Close the loop between pipeline failures and physical lab state.

**Platform engineering (live public reference)**
- Designed and deployed a **GitOps-based single-node Kubernetes platform** — **K3s + ArgoCD + Prometheus + Grafana + cert-manager + sealed-secrets** — as a cloud-native delivery reference. Maintained as a public demo on GitHub.

---

### Cloud Engineer — Stena Metall AB
*Aug 2024 – Jan 2025  |  Gothenburg, Sweden*

Platform engineer on the central Cloud Office (Governance) of a mature **Azure CAF Enterprise Scale** estate — ~100 subscriptions, multi-management-group hierarchy, production workloads for a multi-billion-SEK industrial group.

- **Authored two custom Azure RBAC role definitions** — a "Backup Remover" role and a Contributor variant with explicit `notActions` — to enforce **separation-of-duties between resource management and backup deletion**. A ransomware-resilience / DR-integrity control missing from Azure's built-in Contributor role. Wired into the CAF archetype framework and deployed via the **Terraform + Azure DevOps pipeline**.
- Delivered a **tenant-wide Key Vault compliance audit** — KQL against Azure Resource Graph for soft-delete retention, purge protection, and RBAC.
- Built **Service Principal lifecycle tooling** — KQL audit for 30-day events, PowerShell expiring-credential inventory, and a design for Logic Apps + Graph API client-secret rotation.
- PowerShell tooling: subscription budget automation, ACR token expiry inventory, **.NET runtime enumeration across App Services**, Hybrid Benefit enablement.
- KQL-based monitoring contributed to a **~20% reduction in downtime** across supported services.
- Published sanitized sister repo on GitHub: <a href="https://github.com/arnabdey73/iac-azure-core-governance">`iac-azure-core-governance`</a>.

---

### Senior Software Engineer (DevOps) — Capgemini Sverige AB
*Sep 2021 – Jul 2024  |  Gothenburg, Sweden*

**Assignment: Volvo Cars — Car Safety R&D (MLOps / AI Platform)**

*Self-service Databricks platform via GitOps — friction removal for data scientists*
- Designed and owned a **GitOps self-service pattern for Azure Databricks**: data scientists request compute via a GitHub issue → YAML manifest PR → **GitHub Actions** runs `terraform fmt/validate/plan` for review → merge triggers `terraform apply`.
- Authored the **Terraform module** with governance-friendly defaults baked in — single-user mode, 30-min auto-termination, autoscale 1→3, cluster-log shipping, `CAN_RESTART` permissions.
- Two-workflow contract (`tf-validate` on PR, `tf-deploy` on merge); remote state in Azure Blob with backend config injected from GitHub environment secrets.
- **Outcome:** provisioning lead time dropped from days to same-day; every cluster traceable to a PR, manifest, and named owner — exactly the bottleneck-removal a platform team is hired to deliver.

*Kubernetes platform modernisation*
- Stood up **Rancher-managed Kubernetes (RKE)** with worker fleet on a ~36-node CAE/HPC cluster; **Kubeflow installed via Helm** for ML engineers.
- Built a **production-grade ELK stack** on LXD with X-Pack security, SSL, and snapshot repositories for log integrity and observability.
- Authored **Ansible roles** within the shared GitLab-managed codebase.

*Dual-cloud ML benchmarking*
- Built **two matched Terraform stacks** (AWS + Azure) as identically-shaped, disposable test rigs for MLCommons-style storage benchmarking.

*AI side project*
- Led an internal **AI-powered Resume Builder Agent** as a side project — <a href="https://github.com/arnabdey73/resume-builder-agent">sanitized public repo</a>.

---

### Senior Business Consultant (DevOps) — Tech Mahindra
*Feb 2017 – Sep 2021  |  Bangalore, India  |  Sydney, Australia*

**Assignment: Cisco Systems — CD 2.0 on AWS**
- **Authored the Terraform** for Cisco's CD 2.0 continuous-delivery platform on AWS — VPC, subnets, security groups, **EKS cluster, IAM roles, Jenkins on EKS, ECR, build-agent fleet, ALB, DNS** — extending a reference architecture originally on on-prem OpenShift.
- Built a separate **Terraform observability stack** (EKS + **Prometheus Operator via Helm** + Grafana + persistent storage + ingress).
- Wrote **Python automation** for Cisco's SVN-to-Git migration (REST API integration, retries, batching, CSV audit reports).

**Assignment: Deutsche Telekom — 5G BSS Slicing Pilot on OpenStack**
- Owned the platform side of DT's 5G Network Slicing pilot: **Terraform on OpenStack**, Ansible for service config, ~46 Jenkins jobs building ~30 microservices, **MongoDB platform support** for the BSS suite.
- Led a **cross-tenant migration over a single weekend** — 54 Tuleap repos, Jenkins jobs, Nexus artifacts, Keycloak realm, and live K8s workloads — nothing rebuilt from scratch.
- Built a **Logstash pipeline** ingesting 5G UDR (Usage Data Record) CSV feeds into Elasticsearch.

**Assignment: Greenstone Financial Services — Insurance Portal**
- Led DevOps transformation for **.NET / C# microservices**: Azure DevOps pipelines, **Terraform for Azure**, **Docker + Docker Swarm with ACR**, Azure Monitor for observability.

---

### Senior AEM Administrator (Cloud) — ICF Next
*Sep 2015 – Jan 2017  |  Bangalore, India*

**Assignment: Channel 7 (Australia) — AEM on AWS**
- Built and operated a production AWS platform for a national Australian broadcaster — VPC, EC2 lifecycle, Auto Scaling, Apache HTTPD + Dispatcher hardening, SSL termination, **SAML 2.0 federation** (Azure AD / ADFS → AWS IAM) replacing long-lived IAM keys.
- Authored **Ansible roles** for AEM install, Apache/Dispatcher deployment, SSL, and base OS — instance rebuilds became a runbook rather than a discovery exercise.

---

### Unix / Linux Systems Administrator — HP Enterprise Services
*Nov 2011 – Aug 2015  |  Bangalore, India*

Three-and-a-half years on HP's Global Operations Center under Best Shore Services — 24×7 incident handling on SAP-heavy Linux/Unix estates (HUL, E.ON, Con-way Inc.), LVM/SAN, kernel tuning, SOP authorship. The reflexes for owning production platforms come from here.

---

## Education

**B.Tech in Computer Science** — West Bengal University of Technology, Kolkata, India (2005 – 2009)

---

## Certifications

- **Microsoft Certified: Azure Fundamentals (AZ-900)** — Mar 2023 *(Credential ID: 801D970BAA49297)*
- **AWS Certified Solutions Architect – Associate (SAA-C03)** — *in progress*
