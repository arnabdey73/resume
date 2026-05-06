<div align="center">
	<h1><b>Arnab Dey</b></h1>
	<p>
		Platform Engineer — AWS · EKS · Terraform · Linux · GitOps · Cert &amp; Secret Lifecycle<br>
		Stockholm, Sweden — open to relocation to Gothenburg (extensive Gothenburg work history)<br>
		+46 76 451 60 92 | <a href="mailto:arnabdey009@gmail.com">arnabdey009@gmail.com</a><br>
		<a href="https://www.linkedin.com/in/arnabdey73">LinkedIn</a> | <a href="https://github.com/arnabdey73">GitHub</a> | <a href="https://arnabdey.dev">arnabdey.dev</a>
	</p>
</div>

---

## Professional Summary

Platform Engineer with **15+ years in IT** and **9+ years building and operating AWS / Azure / OpenStack platforms** that engineering teams depend on. **Authored the Terraform for Cisco's CD 2.0 platform on AWS** — VPC, EKS, IAM, ALB, ECR, Jenkins on EKS — alongside a separate **Prometheus Operator + Grafana observability stack**. Operational TLS / certificate / key-lifecycle work runs through the career: **Apache HTTPD + Dispatcher SSL hardening** at Channel 7 (with **SAML 2.0 federation replacing long-lived IAM keys**), **X-Pack security with SSL and snapshot repositories** on a production Elasticsearch cluster at Volvo, **custom Sonatype Nexus 3 Dockerfile with SSL** at Deutsche Telekom, **cert-manager + sealed-secrets** on a live K3s reference platform, **AWS KMS** integrated with S3 / IAM at Volvo, and a **tenant-wide Azure Key Vault compliance audit** plus **Service Principal credential-rotation design** at Stena Metall. Three and a half years of **24×7 shift-based Linux operations** at HP Enterprise Services — storage, SAN, LVM, kernel tuning, on-call — is where the systems instincts come from. Gothenburg-experienced (Volvo Cars, Stena Metall) and happy to return.

---

## Core Skills

**AWS (production)** — **EC2** (Auto Scaling Groups, m3 lifecycle), **S3** (with KMS encryption, lifecycle, IAM), **VPC** + subnets + security groups, **IAM** (roles, SAML federation, least-privilege), **EKS, ECR, ALB**, KMS, CloudWatch; Terraform-driven AWS estate at Cisco CD 2.0; high-availability AEM platform on AWS at Channel 7. CloudFormation reading-knowledge.

**TLS, PKI, SSL & certificate operations** — Apache HTTPD + AEM Dispatcher SSL hardening and termination at Channel 7; **X-Pack security with SSL** on production Elasticsearch at Volvo; custom Sonatype Nexus 3 Docker image with SSL at Deutsche Telekom; **cert-manager** for automated certificate issuance and rotation on a live K3s reference platform; SSL-terminating ALB at Cisco. Operational comfort with certificate chains, expiry/rotation, and key handling — open to deepening into internal-CA and PKI-design work.

**Secret management & key lifecycle** — **AWS KMS** integrated with S3 + IAM at Volvo; **Azure Key Vault tenant-wide compliance audit** (KQL against Resource Graph: soft-delete, purge protection, RBAC) at Stena Metall; **Service Principal credential-rotation design** (Logic Apps + Microsoft Graph `addPassword`); **sealed-secrets** controller on K3s; SAML 2.0 federation eliminating long-lived IAM user keys.

**Linux engineering (networking, storage, OS)** — Three-and-a-half years **24×7 shift-based Linux operations** at HP Enterprise Services on enterprise customer estates (E.ON Germany/UK, HUL ~140 servers): **LVM filesystem operations, Veritas SAN migration, kernel-parameter tuning**, NIM provisioning, DNS, console, ITO/OpsBridge agent management. **Authored a substantial portion** of the BSS-ITO Con-way Linux procedure library used as team reference material.

**Terraform** — Multi-provider (AWS, AzureRM, OpenStack, Databricks); reusable module libraries with opinionated, governance-friendly defaults; archetype-driven CAF deployment; remote state in object storage with backend config injected from CI; module versioning, drift handling.

**Kubernetes (operator, not tourist)** — **EKS** at Cisco (CD 2.0 platform), **Rancher-managed Kubernetes (RKE)** on bare-metal CAE/HPC fleet at Volvo (~36 nodes), AKS, **K3s** (live single-node GitOps reference platform), Helm, Kubeflow, ArgoCD; cluster bootstrap, ingress, networking, rolling-update orchestration, on-call.

**GitOps & CI/CD** — **GitHub Actions** (Volvo Databricks self-service, K3s reference platform), **ArgoCD** (K3s reference platform), **Jenkins** (CD 2.0 platform on EKS at Cisco; ~46 Jenkins jobs at Deutsche Telekom), Azure DevOps Pipelines, GitLab CI; reusable workflows, two-workflow contracts (validate on PR, deploy on merge), automated quality gates.

**Observability** — **Prometheus + Grafana** (AWS observability stack at Cisco, K3s reference platform), production **ELK Stack** (Elasticsearch, Logstash, Kibana on LXD with X-Pack security, SSL, snapshot repositories at Volvo), Azure Monitor / Log Analytics / KQL.

**Reliability & on-call** — 24×7 shift-based incident handling at HP Enterprise Services; cross-tenant migration weekend at Deutsche Telekom rehoming live Kubernetes workloads, repos, artifacts, and identity systems; KQL-based monitoring contributing to **~20% downtime reduction** at Stena Metall.

**Scripting & systems languages** — **Python** (REST/SCM automation, CLI tooling, batched migrations with retry logic), **Bash**, PowerShell. Go exposure via a reference project (`go-url-shortener` on GitHub).

**Languages** — English (fluent, working language), Hindi and Bengali (native), Swedish (SFI C-level basic).

---

## Professional Experience

### DevOps Engineer — AFRY Digital Solutions AB
*May 2025 – Present  |  Stockholm, Sweden*

**Assignment: Ericsson AB — CI Engineer, Tiger Test Tools (Sep 2025 – Present)**
- Maintain and support the end-to-end **CI flow for radio-communication smoke and regression testing** — Git, Gerrit, Jenkins, Docker, Linux. Triage failures across pipeline state and physical lab hardware.

**Platform engineering** — designed and operate a **GitOps Kubernetes platform** (K3s + ArgoCD + Prometheus + Grafana + **cert-manager + sealed-secrets**), provisioned via Terraform. **cert-manager** issues and rotates TLS certificates automatically; **sealed-secrets** keeps encrypted secret material in Git. Live demonstration of declarative platform foundations — public reference repo `single-node-gitops` on GitHub.

---

### Cloud Engineer — Stena Metall AB
*Aug 2024 – Jan 2025  |  Gothenburg, Sweden*

Cloud Infrastructure Engineer on the central Cloud Office of a mature **Azure CAF Enterprise Scale** estate — ~100 subscriptions, multi-management-group hierarchy, production workloads for a multi-billion-SEK industrial group. All infrastructure delivered as **Terraform via Azure DevOps pipelines**.

- **Tenant-wide Key Vault compliance audit** — KQL against Azure Resource Graph for soft-delete retention, purge protection, and RBAC authorisation — producing CSV inventories and a documented review for architecture leadership.
- **Service Principal lifecycle and credential-rotation tooling** — KQL audit for 30-day create/update/delete events, PowerShell expiring-credential inventory, and a design for client-secret rotation via Logic Apps + Microsoft Graph `addPassword`. **Eliminated long-lived secret risk by design**, not policy.
- **Authored two custom Azure RBAC role definitions** — a "Backup Remover" role and a Contributor variant with explicit `notActions` — to enforce **separation-of-duties** between resource management and backup deletion (ransomware-resilience control). Wired into the CAF archetype framework and shipped through the production pipeline.
- **KQL-based monitoring contributed to a ~20% reduction in downtime** across supported services.
- Sanitised public reference repo: <a href="https://github.com/arnabdey73/iac-azure-core-governance">`iac-azure-core-governance`</a> (CAF Enterprise Scale governance platform), reusable Terraform module library.

---

### Senior Software Engineer (DevOps) — Capgemini Sverige AB
*Sep 2021 – Jul 2024  |  Gothenburg, Sweden*

**Assignment: Volvo Cars — Car Safety R&D (Abakus MLOps / AI Platform)**

- Built a **production Elasticsearch cluster on LXD** with **X-Pack security, SSL, and snapshot repositories** as the observability and search backbone for a ~36-node bare-metal CAE/HPC fleet. End-to-end TLS, role-based access, and tested backup/restore via snapshot repositories.
- Built **two matched Terraform stacks** (AWS: **EC2 + S3 + KMS + IAM** | Azure: VM + Premium BlockBlobStorage) as disposable test rigs for MLCommons-style object-storage benchmarking — KMS-encrypted S3 buckets with explicit IAM bindings as the reference encrypted-at-rest pattern.
- Modernised a **~36-node bare-metal CAE/HPC cluster** for ML research: OS migration SLES → Ubuntu LTS; stand-up of **Rancher-managed Kubernetes (RKE)**; **Kubeflow** via Helm.
- Designed and owned a **GitOps self-service pattern for Azure Databricks**: data scientists request compute via a GitHub issue → YAML manifest PR → **GitHub Actions** validates the change → merge applies it. Lead time fell from days to same-day; idle-cluster spend eliminated; every cluster traceable to a PR and a named owner.

---

### Senior Business Consultant (DevOps) — Tech Mahindra
*Feb 2017 – Sep 2021  |  Bangalore, India · Sydney, Australia*

**Assignment: Cisco Systems — CD 2.0 Continuous-Delivery Platform on AWS**
- **Authored the Terraform** for Cisco's CD 2.0 platform on **AWS** — VPC, subnets, security groups, **EKS cluster, IAM roles, Jenkins on EKS, ECR integration, build-agent fleet, ALB with SSL termination, DNS** — extending an internal reference architecture originally built on on-prem OpenShift.
- Wrote a separate **Terraform stack for an AWS observability environment** — EKS + **Prometheus Operator via Helm + Grafana** + persistent storage + ingress.
- Closed out Cisco's long-running SVN-to-Git migration via **Python automation** against the Bitbucket REST API — enumeration, history extraction, batched push with retry logic.

**Assignment: Deutsche Telekom — 5G BSS Slicing Pilot on OpenStack (Apr 2020 – Jul 2021)**
- Owned the **DevOps platform side** of DT's 5G Network Slicing commercial pilot on **PAN-NET (OpenStack)**, delivering Blue Marble's ~30-microservice BSS suite plus the Phenom UI.
- **Terraform against the OpenStack provider** provisioned the Jenkins / Nexus / Tuleap / Rancher / Keycloak / **ELK** estate; **Ansible playbooks** for all service configuration.
- **Authored a custom Sonatype Nexus 3 Docker image with SSL** for internal artifact distribution.
- Owned a **cross-tenant migration weekend** rehoming 54 Tuleap repositories, Jenkins jobs, Nexus artifacts, **Keycloak realm**, and live Kubernetes workloads via Python/shell automation — incident-grade coordination, single weekend cutover, **nothing rebuilt from scratch**.

**Assignment: Greenstone Financial Services — Insurance Portal**
- Led DevOps transformation for **.NET microservices**: Azure DevOps pipelines, Terraform for Azure infrastructure, Docker + Docker Swarm with Azure Container Registry, Azure Monitor.

---

### Senior AEM Administrator (Cloud) — ICF Next
*Sep 2015 – Jan 2017  |  Bangalore, India*

**Assignment: Channel 7 (Australia) — AEM web platform on AWS**
- Built and operated a production AEM web platform on AWS for a national broadcaster — VPC, **EC2 lifecycle (m3 family, Auto Scaling Groups)**, **Apache HTTPD + AEM Dispatcher hardening with SSL termination**, **SAML 2.0 federation (Azure AD / ADFS → AWS IAM) replacing long-lived IAM user keys** — eliminating the standing credential footprint.
- Authored **Ansible roles** for AEM install, Apache/Dispatcher deployment, SSL, and base OS — turning instance rebuilds into a runbook rather than a discovery exercise.

---

### Unix / Linux Systems Administrator — HP Enterprise Services
*Nov 2011 – Aug 2015  |  Bangalore, India*

Three-and-a-half years on HP's Global Operations Center under Best Shore Services, rotating across enterprise customers — **24×7 incident handling on customer-critical Linux/Unix estates**.
- **HUL** (~18 months, L1/L2) — SAP-heavy Linux/Unix estate (140+ servers).
- **E.ON** (~12 months, L2/L3) — multi-site German / UK operations; storage, DNS, console management; SOP authorship.
- **Con-way Inc.** (~13 months, L2/L3 SOP author) — **authored a substantial portion of the BSS-ITO Con-way Linux procedure library** covering **LVM filesystem resizes, Veritas SAN migration, kernel-parameter tuning**, and ITO/OpsBridge agent management. Procedures used as team reference material.
- Tooling fluency: HP Service Manager, HP OpenView / OpsBridge, HP Server Automation (Opsware), NIM.

---

## Education

**B.Tech in Computer Science** — West Bengal University of Technology, Kolkata, India (2005 – 2009)

---

## Certifications

- **Microsoft Certified: Azure Fundamentals (AZ-900)** — Mar 2023 *(Credential ID: 801D970BAA49297)*
- **AWS Certified Solutions Architect – Associate (SAA-C03)** — *in progress*
