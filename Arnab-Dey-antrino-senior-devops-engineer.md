<div align="center">
	<h1><b>Arnab Dey</b></h1>
	<p>
		Stockholm, Sweden | +46 0764516092 | <a href="mailto:arnabdey009@gmail.com">arnabdey009@gmail.com</a><br>
		<a href="https://www.linkedin.com/in/arnabdey73">LinkedIn</a> | <a href="https://github.com/arnabdey73">GitHub</a>
	</p>
</div>

---

## Professional Summary

Senior DevOps / Platform Engineer with **15+ years in IT** and **9+ years owning production cloud platforms** that real teams and real customers depend on. I build infrastructure that other engineers actually use — most recently a **GitOps self-service ML compute platform on Azure Databricks at Volvo Cars** that took provisioning lead time from days to same-day with idle-spend designed out by default, and a **~100-subscription Azure CAF Enterprise Scale governance estate at Stena Metall** where I authored custom RBAC controls and shipped them through the production Terraform pipeline. Strong on Kubernetes (AKS, EKS, RKE, K3s), Terraform at module-library scale, cost-per-workload thinking, and the unglamorous work of keeping platforms reliable as they grow. Most comfortable when the platform is the product the rest of the company is betting on. Stockholm-based, fluent in English.

---

## Core Skills

**Production cloud at scale** — Microsoft Azure (primary; CAF Enterprise Scale, ~100-subscription estate, multi-management-group hierarchy, multi-billion-SEK industrial group), AWS (EC2, S3, VPC, EKS, IAM, ECR, ALB, KMS), OpenStack (5G commercial pilot for Deutsche Telekom).

**Kubernetes & containers** — AKS, EKS, **Rancher RKE**, K3s; Docker, Helm, Kubeflow, ArgoCD; container registries (ACR, ECR, Nexus); ingress, persistent storage, rolling updates against live workloads.

**Multi-tenant compute platforms** — Designed and operated a self-service Azure Databricks platform for Volvo Cars Car Safety R&D where each cluster is provisioned per-team via PR, traceable to a named owner, billed against a manifest, and auto-terminated when idle. Cost-by-construction, not cost-by-dashboard.

**Cost discipline / FinOps** — Autoscale + auto-termination defaults baked into Terraform modules; subscription budget automation; ACR token / SP credential hygiene; .NET runtime audits across App Services; cost-allocation tagging across landing zones; published Azure cost-optimisation Terraform templates.

**Real-time data pipelines** — Built a **Logstash pipeline ingesting 5G UDR (Usage Data Record) feeds into Elasticsearch** for Deutsche Telekom's billing emulator on the BSS Slicing pilot; production ELK stack on LXD with X-Pack security, SSL, and snapshot repositories at Volvo. Comfortable in the territory of streaming ingest, backpressure, and lossy-vs-lossless trade-offs even though my streaming work has been data, not video.

**ML platform adjacency** — Volvo Cars Car Safety R&D: owned the IaC contract for the Abakus MLOps platform — Databricks compute, dual-cloud (AWS + Azure) object-storage benchmark rigs for MLCommons-style tests, Kubeflow on Rancher RKE for ML engineers. Have not personally orchestrated NVIDIA Triton / MIG, but understand the constraints of GPU compute scheduling, lifecycle, and cost.

**Infrastructure as Code** — Terraform (AzureRM, AWS, OpenStack, Databricks providers), reusable module libraries with opinionated defaults, archetype-driven CAF deployment, remote state in Azure Blob with backend config injected from CI environment secrets, two-workflow `validate-on-PR` / `apply-on-merge` contract.

**CI/CD** — GitHub Actions (Volvo Terraform delivery), Azure DevOps Pipelines (Stena governance Terraform; Greenstone .NET microservices), Jenkins (~46-job builds for DT BSS microservices, EKS-hosted Jenkins for Cisco CD 2.0), GitLab CI, Gerrit, ArgoCD.

**Observability** — Azure Monitor, Log Analytics / KQL, Prometheus, Grafana, ELK Stack, CloudWatch, cert-manager.

**Scripting & automation** — Python (REST/SCM automation, batch with retry/rate-limit handling), PowerShell (Azure governance), Bash.

**Languages** — English (fluent).

---

## Professional Experience

### DevOps Engineer — AFRY Digital Solutions AB
*May 2025 – Present  |  Stockholm, Sweden*

**Assignment: Ericsson AB — CI Engineer, Tiger Test Tools (Sep 2025 – Present)**
- Maintain and support the end-to-end **CI flow for radio-communication smoke and regression testing** on real hardware — Git, Gerrit, Jenkins, Docker, Linux. Close the loop between pipeline failures and physical lab state when the test rig misbehaves.

**Platform engineering (internal reference project)**
- Designed and deployed a **GitOps Kubernetes platform** (K3s + ArgoCD + Prometheus + Grafana + cert-manager + sealed-secrets) as a working reference for cloud-native delivery — maintained as a live public demo on GitHub.

---

### Cloud Engineer — Stena Metall AB
*Aug 2024 – Jan 2025  |  Gothenburg, Sweden*

Cloud Infrastructure Engineer on the central Cloud Office (Governance) of a mature **Azure CAF Enterprise Scale** estate — **~100 subscriptions, multi-management-group hierarchy**, production workloads for a multi-billion-SEK industrial group. All infrastructure delivered as **Terraform via Azure DevOps pipelines**.

- **Authored two custom Azure RBAC role definitions** — a "Backup Remover" role and a Contributor variant with explicit `notActions` — to enforce separation-of-duties between resource management and backup deletion (a ransomware-resilience control missing from Azure's built-in Contributor). **Wired into the CAF archetype framework** and shipped through the production Terraform + Azure DevOps pipeline. **38 commits across the core-governance repo.**
- **Tenant-wide Key Vault compliance audit** — KQL against Azure Resource Graph for soft-delete retention, purge protection, and RBAC authorisation; CSV inventories for architecture leadership.
- Built **Service Principal lifecycle tooling** — KQL audit + PowerShell expiring-credential inventory + a Logic Apps / Graph `addPassword` rotation design.
- **FinOps tooling**: subscription budget automation, ACR token expiry inventory, .NET runtime enumeration across App Services, Hybrid Benefit enablement, cost-allocation tagging across landing zones.
- KQL-based monitoring contributed to a **~20% reduction in downtime** across supported services.

---

### Senior Software Engineer (DevOps) — Capgemini Sverige AB
*Sep 2021 – Jul 2024  |  Gothenburg, Sweden*

**Assignment: Volvo Cars — Car Safety R&D (Abakus MLOps / AI Platform)**

*Self-service Databricks compute via GitOps — multi-tenant by design*
- Designed and owned a **GitOps self-service pattern for Azure Databricks** used by Car Safety data scientists: request compute via a GitHub issue → YAML manifest PR → **GitHub Actions runs `terraform fmt/validate/plan` for review** → merge triggers `terraform apply`.
- Authored the **Terraform module** with opinionated, governance-friendly defaults baked in: single-user security mode, **30-minute auto-termination, autoscale 1→3 workers**, cluster-log shipping to DBFS, `CAN_RESTART` permissions — making clusters **cheap and safe by construction, not by dashboard**.
- Remote state in Azure Blob; two-workflow contract (`tf-validate` on PR, `tf-deploy` on merge); backend config injected at init from GitHub environment secrets.
- **Outcome:** provisioning lead time fell from days to same-day; every cluster traceable to a PR, a manifest, and a named owner; long-tail idle-cluster spend eliminated.

*Kubernetes-based ML platform modernisation*
- Contributed to modernising a ~36-node CAE/HPC cluster supporting ML research: OS migration SLES → Ubuntu LTS; stand-up of **Rancher-managed Kubernetes (RKE)**; **Kubeflow** via Helm for ML engineers.
- Built a **production-grade ELK stack** for observability with X-Pack security, SSL, and snapshot repositories.

*Dual-cloud ML benchmarking*
- Built **two matched Terraform stacks** (AWS: EC2 + S3 + KMS + IAM | Azure: VM + Premium BlockBlobStorage) as identically-shaped, disposable test rigs for object-storage benchmarking on equal footing — the infrastructure was the control variable.

---

### Senior Business Consultant (DevOps) — Tech Mahindra
*Feb 2017 – Sep 2021  |  Bangalore, India  |  Sydney, Australia*

**Assignment: Deutsche Telekom — 5G BSS Slicing Pilot on OpenStack**
- Owned the **DevOps platform side** of DT's 5G Network Slicing commercial pilot on PAN-NET (OpenStack), delivering Blue Marble's ~30-microservice BSS suite.
- **Terraform against the OpenStack provider** — networks, subnets, security groups, VMs, floating IPs — provisioning the Jenkins / Nexus / Tuleap / Rancher / Keycloak / ELK estate.
- Designed and ran **~46 Jenkins jobs** building BMP microservices, tagging with build number + short git SHA, pushing to internal Nexus, updating Kubernetes manifests, and triggering Rancher rolling updates.
- Built a **Logstash pipeline ingesting 5G UDR (Usage Data Record) CSV feeds into Elasticsearch** for the billing emulator — real-time data ingest under production constraints.
- Owned a **cross-tenant migration weekend** rehoming 54 Tuleap repositories, Jenkins jobs, Nexus artifacts, Keycloak realm, and live Kubernetes workloads via Python/shell automation — nothing rebuilt from scratch.

**Assignment: Cisco Systems — CD 2.0 Continuous-Delivery Platform on AWS**
- **Authored the Terraform** for Cisco's CD 2.0 platform on AWS — VPC, subnets, security groups, **EKS cluster, IAM roles, Jenkins on EKS, ECR integration, build-agent fleet, ALB, DNS** — extending an internal reference architecture.
- Wrote a separate **Terraform stack for an AWS observability environment** (EKS + Prometheus Operator via Helm + Grafana + persistent storage + ingress).
- Closed out Cisco's long-running SVN-to-Git migration via Python automation against the Bitbucket REST API — with retry logic and batching for SCM rate limits.

**Assignment: Greenstone Financial Services — Insurance Portal**
- DevOps transformation for .NET microservices: Azure DevOps pipelines, **Terraform for Azure infrastructure**, Docker + Docker Swarm with Azure Container Registry, Azure Monitor.

---

### Senior AEM Administrator (Cloud) — ICF Next
*Sep 2015 – Jan 2017  |  Bangalore, India*

**Assignment: Channel 7 (Australia) — AEM on AWS**
- Built and operated a production AEM platform on AWS for a national broadcaster — VPC, EC2 lifecycle, Apache HTTPD + Dispatcher hardening, SSL termination, **SAML 2.0 federation (Azure AD / ADFS → AWS IAM)** replacing long-lived IAM keys.
- Authored **Ansible roles** for AEM install, Apache/Dispatcher deployment, SSL, and base OS — turning instance rebuilds into a runbook rather than a discovery exercise.

---

### Unix / Linux Systems Administrator — HP Enterprise Services
*Nov 2011 – Aug 2015  |  Bangalore, India*

Three-and-a-half years on HP's Global Operations Center under Best Shore Services, rotating across enterprise outsourcing customers (HUL, E.ON, Con-way Inc.) — **24×7 incident handling on customer-critical Linux/Unix estates**, LVM/SAN, kernel tuning, SOP authorship, HP Service Manager / OpenView / Server Automation.

---

## Education

**B.Tech in Computer Science** — West Bengal University of Technology, Kolkata, India (2005 – 2009)

---

## Certifications

- **Microsoft Certified: Azure Fundamentals (AZ-900)** — Mar 2023 *(Credential ID: 801D970BAA49297)*
- **AWS Certified Solutions Architect – Associate (SAA-C03)** — *in progress*
