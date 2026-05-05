<div align="center">
	<h1><b>Arnab Dey</b></h1>
	<p>
		Senior Platform Engineer — AWS · Terraform · Kubernetes · GitOps · Observability<br>
		Stockholm, Sweden — open to relocation to Berlin under EU Blue Card sponsorship<br>
		+46 76 451 60 92 | <a href="mailto:arnabdey009@gmail.com">arnabdey009@gmail.com</a><br>
		<a href="https://www.linkedin.com/in/arnabdey73">LinkedIn</a> | <a href="https://github.com/arnabdey73">GitHub</a> | <a href="https://arnabdey.dev">arnabdey.dev</a>
	</p>
</div>

---

## Professional Summary

Cloud and Platform Engineer with **15+ years in IT** and **9+ years building platforms that engineering teams depend on** across AWS, Azure, and OpenStack. Most recently designed and owned a **GitOps self-service Azure Databricks platform at Volvo Cars** — engineers request compute via a GitHub issue, a YAML manifest PR is validated in GitHub Actions, merge applies the change; lead time fell from days to same-day, idle-cluster spend eliminated, every cluster traceable to a PR and a named owner. Earlier, **authored the Terraform for Cisco's CD 2.0 continuous-delivery platform on AWS** — VPC, EKS, IAM, ALB, ECR, Jenkins on EKS — alongside a separate **Prometheus + Grafana observability environment**. Claude Code and Copilot are part of my daily workflow. Stockholm-based, fluent in English, open to relocation to Berlin.

---

## Core Skills

**AWS (production)** — EC2 (Auto Scaling Groups), S3, VPC + subnets + security groups, IAM (roles, SAML federation), **EKS, ECR, ALB**, KMS, CloudWatch; Terraform-driven AWS estate at Cisco; high-availability AEM platform on AWS at Channel 7.

**Terraform** — Multi-provider (AWS, AzureRM, OpenStack, Databricks); reusable module libraries with opinionated, governance-friendly defaults; archetype-driven CAF deployment; remote state in object storage with backend config injected from CI; module versioning, drift handling. Pragmatic about when a module earns its keep and when raw resources are clearer.

**Kubernetes (operator, not tourist)** — **Rancher-managed Kubernetes (RKE)** on bare-metal CAE/HPC fleet at Volvo (~36 nodes), EKS at Cisco, AKS, **K3s** (live single-node GitOps reference platform), Helm, Kubeflow, ArgoCD; cluster bootstrap, control-plane troubleshooting, ingress, networking, rolling-update orchestration.

**CI/CD** — **GitHub Actions** (Volvo Databricks self-service, K3s reference platform), Azure DevOps Pipelines, GitLab CI, Jenkins; reusable workflows, two-workflow contracts (validate on PR, deploy on merge), automated quality gates separating validation and review from production apply.

**Observability** — **Prometheus + Grafana** (AWS observability stack at Cisco, K3s reference platform), production **ELK Stack** (Elasticsearch, Logstash, Kibana on LXD with X-Pack security, SSL, snapshot repositories at Volvo), Azure Monitor / Log Analytics / KQL; Loki / Datadog / Incident.io are adjacent — comfortable picking them up against the Prometheus/Grafana baseline.

**Scripting & systems languages** — **Python** (REST/SCM automation, CLI tooling, batched migrations with retry logic), **Bash**, PowerShell. **Go** — exposure via a reference project (`go-url-shortener` on GitHub); willing to ramp on Zenjob's in-house CLI and contribute production code.

**Security & DevSecOps** — Custom Azure RBAC (separation-of-duties for ransomware resilience), tenant-wide Key Vault compliance audit, Service Principal lifecycle and credential-rotation design, SAML 2.0 federation replacing long-lived IAM keys, Azure Backup policy compliance reporting.

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
- **FinOps that landed on the invoice**: subscription budget automation, ACR token expiry inventory, cost-allocation tagging across landing zones, **Hybrid Benefit enablement**.
- **KQL-based monitoring contributed to a ~20% reduction in downtime** across supported services.
- Sanitised public reference repo: <a href="https://github.com/arnabdey73/iac-azure-core-governance">`iac-azure-core-governance`</a> (CAF Enterprise Scale governance platform), reusable Terraform module library, Azure cost-optimisation templates.

---

### Senior Software Engineer (DevOps) — Capgemini Sverige AB
*Sep 2021 – Jul 2024  |  Gothenburg, Sweden*

**Assignment: Volvo Cars — Car Safety R&D (Abakus MLOps / AI Platform) — platform-as-a-product**

- Designed and owned a **GitOps self-service pattern for Azure Databricks**: data scientists request compute via a GitHub issue → YAML manifest PR → **GitHub Actions** validates the change for review → merge applies it. **Lead time fell from days to same-day**; every cluster traceable to a PR, a manifest, and a named owner; long-tail idle-cluster spend eliminated.
- Authored the **Terraform module** with reliability and cost defaults baked in: single-user security mode, **30-minute auto-termination, autoscale 1→3 workers**, cluster-log shipping to DBFS, `CAN_RESTART` permissions — clusters cheap and safe by construction. Remote state in Azure Blob Storage with backend config injected at init from GitHub environment secrets.
- Contributed to modernising a **~36-node bare-metal CAE/HPC cluster** for ML research: OS migration SLES → Ubuntu LTS; stand-up of **Rancher-managed Kubernetes (RKE)**; **Kubeflow** via Helm; production-grade **ELK stack** on LXD with X-Pack security, SSL, and snapshot repositories.
- Built **two matched Terraform stacks** (AWS: EC2 + S3 + KMS + IAM | Azure: VM + Premium BlockBlobStorage) as disposable test rigs for MLCommons-style object-storage benchmarking.

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
- Designed and ran **~46 Jenkins jobs** building BMP microservices, tagging build number + short git SHA, pushing to internal Nexus, updating Kubernetes manifests, triggering Rancher rolling updates.
- Owned a **cross-tenant migration weekend** rehoming 54 Tuleap repositories, Jenkins jobs, Nexus artifacts, Keycloak realm, and live Kubernetes workloads via Python/shell automation — incident-grade coordination, single weekend cutover, nothing rebuilt from scratch.

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

Three-and-a-half years on HP's Global Operations Center under Best Shore Services, rotating across enterprise customers including **E.ON (multi-site German / UK operations)** — **24×7 incident handling on customer-critical Linux/Unix estates**, storage, DNS, console management, kernel tuning, SOP authorship; HP Service Manager / OpenView / Server Automation.

---

## Education

**B.Tech in Computer Science** — West Bengal University of Technology, Kolkata, India (2005 – 2009)

---

## Certifications

- **Microsoft Certified: Azure Fundamentals (AZ-900)** — Mar 2023 *(Credential ID: 801D970BAA49297)*
- **AWS Certified Solutions Architect – Associate (SAA-C03)** — *in progress*
