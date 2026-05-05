<div align="center">
	<h1><b>Arnab Dey</b></h1>
	<p>
		Stockholm, Sweden | +46 0764516092 | <a href="mailto:arnabdey009@gmail.com">arnabdey009@gmail.com</a><br>
		<a href="https://www.linkedin.com/in/arnabdey73">LinkedIn</a> | <a href="https://github.com/arnabdey73">GitHub</a>
	</p>
</div>

---

## Professional Summary

Linux-rooted Infrastructure Engineer with **15+ years in IT** spanning **classical Unix/Linux systems administration, AWS environment management, and on-premise platform engineering**. Started on HP Enterprise Services' Global Operations Center handling 24×7 incidents on customer-critical Unix/Linux estates (140+ servers, SAP-heavy), authored a substantial portion of a customer's Linux procedure library, and built fluency in **HP Server Automation (Opsware)**, NIM, and patch management at scale. Since then, owned **on-prem CAE/HPC cluster modernisation at Volvo Cars** (SLES → Ubuntu migration, Rancher-managed Kubernetes, production ELK stack), **AWS infrastructure for Cisco's CD 2.0 platform** (VPC, EKS, IAM, ALB, ECR), and **Azure governance work at Stena Metall** focused on security-first defaults and ransomware-resilient RBAC. Comfortable across the full stack the role calls for — Linux administration, AWS, Docker, Terraform/Ansible, Prometheus/Grafana, ELK, S3/NAS-class storage, and disaster-recovery / backup design. Stockholm-based, fluent in English.

---

## Core Skills

**Linux / Unix Administration** — Production estate ownership across RHEL, SLES, Ubuntu, CentOS; LVM filesystem operations, Veritas SAN migration, kernel-parameter tuning, sysctl, performance triage; out-of-band console management via HP iLO / Dell iDRAC; runbook / SOP authorship for production procedures.

**Shell Scripting & Automation** — Bash, **Python** (REST/SCM automation, CLI tooling, batched migrations with retry logic), PowerShell.

**AWS** — EC2 (m3 family AEM workloads, Auto Scaling Groups), S3, VPC, subnets, security groups, IAM (roles, SAML federation), EKS, ECR, ALB, KMS, CloudWatch; Terraform-driven AWS estate at Cisco.

**Networking Architecture** — VPC / VNet design, subnetting, NSGs / security groups, private endpoints, DNS (BIND zone management, Apache HTTPD reverse-proxy / Dispatcher), SSL termination, SAML 2.0 federation, load-balancer fronting (ALB).

**Docker & Containers** — Docker daily-driver across CI build agents, on-prem ELK, AEM publishing, .NET microservices on Docker Swarm; Kubernetes (Rancher RKE on bare-metal CAE/HPC, K3s, EKS, AKS), Helm.

**Infrastructure as Code** — **Terraform** (AWS, Azure, OpenStack, Databricks providers): reusable module libraries, archetype-driven CAF deployment, remote state in object storage, module versioning, drift handling. **Ansible** roles for AEM / Apache / Dispatcher / SSL / OS baseline at ICF Next and Volvo. CloudFormation-equivalent reasoning via heavy ARM-template and Terraform exposure.

**Patch Management & Software Distribution** — HP Server Automation (Opsware), NIM, HP OpenView / OpsBridge agent management at HP Enterprise Services across customer Linux/Unix estates; package-parity procedures between staging and production at ICF Next.

**Monitoring & Observability** — **Prometheus + Grafana** (AWS observability stack at Cisco — Prometheus Operator via Helm, persistent storage, ingress), production **ELK Stack** (Elasticsearch, Logstash, Kibana on LXD with X-Pack security, SSL, snapshot repositories at Volvo Cars), Azure Monitor / Log Analytics / KQL.

**Storage** — **S3** (Cisco AWS, Volvo dual-cloud benchmark rigs), on-prem block / NAS-class storage on the CAE/HPC fleet at Volvo, **Sonatype Nexus** registry (Artifactory-class artifact store at Deutsche Telekom — custom Dockerfile with SSL, ~46 Jenkins jobs publishing build artifacts), ECR / ACR; backup-integrity by RBAC at Stena Metall.

**Security & Disaster Recovery** — Custom Azure RBAC (separation-of-duties for ransomware resilience), tenant-wide Key Vault compliance audit, Service Principal lifecycle / credential-rotation design, SAML 2.0 federation replacing long-lived IAM keys, **Azure Backup policy compliance reporting with per-VM exempt-rationale tracking**, snapshot repositories on production ELK.

**Languages** — English (fluent), Swedish (SFI C-level).

---

## Professional Experience

### DevOps Engineer — AFRY Digital Solutions AB
*May 2025 – Present  |  Stockholm, Sweden*

**Assignment: Ericsson AB — CI Engineer, Tiger Test Tools (Sep 2025 – Present)**
- Maintain and support the end-to-end **CI flow for radio-communication smoke and regression testing** — Git, Gerrit, Jenkins, **Docker, Linux**. Triage failures across pipeline state and physical lab hardware (test rigs, radio equipment).

**Platform engineering (internal reference project — public on GitHub)**
- Designed and operate a **GitOps Kubernetes platform**: K3s + ArgoCD + Prometheus + Grafana + cert-manager + sealed-secrets. Live demonstration of declarative infrastructure foundations.

---

### Cloud Engineer — Stena Metall AB
*Aug 2024 – Jan 2025  |  Gothenburg, Sweden*

Cloud Infrastructure Engineer on the central Cloud Office of a mature **Azure CAF Enterprise Scale** estate — ~100 subscriptions, multi-management-group hierarchy, production workloads for a multi-billion-SEK industrial group. All infrastructure delivered as **Terraform via Azure DevOps pipelines**.

- **Authored two custom Azure RBAC role definitions** — a "Backup Remover" role and a Contributor variant with explicit `notActions` — to enforce **separation-of-duties** between resource management and backup deletion (a ransomware-resilience control missing from Azure's built-in Contributor). Wired into the CAF archetype framework and shipped through the production pipeline.
- Delivered a **tenant-wide Key Vault compliance audit** — KQL against Azure Resource Graph for soft-delete retention, purge protection, and RBAC authorisation; CSV inventories and a documented review for architecture leadership.
- **Azure Backup policy compliance reporting** with per-VM exempt-rationale tracking; PowerShell tooling for Service Principal credential lifecycle and ACR token expiry.
- **KQL-based monitoring contributed to a ~20% reduction in downtime** across supported services.

---

### Senior Software Engineer (DevOps) — Capgemini Sverige AB
*Sep 2021 – Jul 2024  |  Gothenburg, Sweden*

**Assignment: Volvo Cars — Car Safety R&D (Abakus MLOps / AI Platform)**

*On-prem CAE / HPC platform modernisation*
- Contributed to modernising a **~36-node on-premise CAE/HPC cluster** supporting ML research: **OS migration from SLES to Ubuntu LTS** across the worker fleet; stand-up of **Rancher-managed Kubernetes (RKE)**; **Kubeflow** installation via Helm.
- Built a **production-grade ELK stack** (Elasticsearch, Logstash, Kibana) on **LXD** with **X-Pack security, SSL, and snapshot repositories** for centralised observability.
- Authored **Ansible roles** within the shared GitLab-managed codebase for repeatable cluster configuration.

*Self-service compute platform via GitOps*
- Designed and owned a **GitOps self-service pattern for Azure Databricks**: data scientists request compute via a GitHub issue → YAML manifest PR → GitHub Actions runs `terraform fmt/validate/plan` → merge triggers `terraform apply`. Lead time fell from days to same-day; idle-cluster spend eliminated.

*Dual-cloud storage benchmarking*
- Built **two matched Terraform stacks** (AWS: EC2 + **S3** + KMS + IAM | Azure: VM + Premium BlockBlobStorage) as identically-shaped, disposable test rigs for **MLCommons-style object-storage benchmarking** — the infrastructure was the control variable.

---

### Senior Business Consultant (DevOps) — Tech Mahindra
*Feb 2017 – Sep 2021  |  Bangalore, India  |  Sydney, Australia*

**Assignment: Cisco Systems — CD 2.0 Continuous-Delivery Platform on AWS**
- **Authored the Terraform** for Cisco's CD 2.0 platform on **AWS** — VPC, subnets, security groups, **EKS cluster, IAM roles, Jenkins on EKS, ECR integration, build-agent fleet, ALB, DNS** — extending an internal reference architecture originally built on on-prem OpenShift.
- Wrote a separate **Terraform stack for an AWS observability environment** — EKS + **Prometheus Operator via Helm + Grafana** + persistent storage + ingress.
- Closed out Cisco's long-running SVN-to-Git migration via **Python automation** against the Bitbucket REST API — enumeration, history extraction, repo provisioning, push, CSV reporting — with **retry logic and batching** to work around SCM rate limits.

**Assignment: Deutsche Telekom — 5G BSS Slicing Pilot on OpenStack**
- Owned the **DevOps platform side** of DT's 5G Network Slicing commercial pilot on **PAN-NET (OpenStack)**, delivering a ~30-microservice BSS suite plus the Phenom UI.
- **Terraform against the OpenStack provider** provisioned the Jenkins / **Sonatype Nexus** / Tuleap / Rancher / Keycloak / **ELK** estate; **Ansible playbooks** for all service configuration; custom Dockerfile for **Sonatype Nexus 3 with SSL** (Artifactory-class registry).
- Designed and ran **~46 Jenkins jobs** building BMP microservices, tagging with build number + short git SHA, pushing to internal Nexus registry, updating Kubernetes manifests, triggering Rancher rolling updates.
- Owned the **cross-tenant migration weekend** when the pilot moved PAN-NET tenants — Python/shell automation rehoming 54 Tuleap repositories, Jenkins jobs, Nexus artifacts, Keycloak realm, and live Kubernetes workloads. Cutover completed without rebuilding from scratch.
- Built a **Logstash pipeline** ingesting 5G UDR (Usage Data Record) CSV feeds into Elasticsearch for the billing emulator.

---

### Senior AEM Administrator (Cloud) — ICF Next
*Sep 2015 – Jan 2017  |  Bangalore, India*

**Assignment: Channel 7 (Australia) — AEM web platform on AWS**
- Built and operated a production AEM web platform on **AWS** for a national broadcaster — VPC, **EC2 lifecycle (m3 family)**, Apache HTTPD + AEM Dispatcher hardening, **SSL termination**, and **SAML 2.0 federation (Azure AD / ADFS → AWS IAM)** replacing long-lived IAM user keys.
- Evolved the architecture from Phase-1 (separate Dispatcher VM) to Phase-2 (Dispatcher co-located on Gold Publisher; Publish tier in an **Auto Scaling Group**).
- Authored **Ansible roles** for AEM install, Apache/Dispatcher deployment, SSL, and base OS — turning instance rebuilds into a runbook rather than a discovery exercise.
- Maintained the **package-parity procedure** between staging and production, catching release drift before deployments.

---

### Unix / Linux Systems Administrator — HP Enterprise Services
*Nov 2011 – Aug 2015  |  Bangalore, India*

Three-and-a-half years on HP Enterprise Services' Global Operations Center (Unix Service Delivery Unit) under the Best Shore Services model, rotating across three large outsourcing customers — **24×7 incident handling on customer-critical Linux/Unix estates**.

- **HUL** (~18 months, L1/L2) — Shift-based incident handling on a SAP-heavy Linux/Unix estate **(140+ servers)**.
- **E.ON** (~12 months, L2/L3) — Multi-site German/UK operations: **storage, DNS, console management**; started authoring SOPs.
- **Con-way Inc.** (~13 months, L2/L3 SOP author) — **Authored a substantial portion of the BSS-ITO Con-way Linux procedure library** covering **LVM filesystem resizes, Veritas SAN migration, kernel-parameter tuning**, and ITO/OpsBridge agent management. Procedures used as team reference material.
- **Tooling fluency:** **HP Server Automation (Opsware)** for patch management and software distribution at fleet scale, **NIM** for AIX provisioning, HP Service Manager, HP OpenView / OpsBridge, HPSA.

---

### Earlier roles

**Linux Systems Administrator — Trainz** *(May 2011 – Oct 2011, Bangalore)*. Production Linux fleet administration for a leading Indian online retailer — installs, configuration, version upgrades and rollbacks, performance tuning; incident response on server-down and service-failure events; out-of-band console management via **HP iLO and Dell iDRAC**; **VMware** virtual-server lifecycle (build, configure, decommission).

**Linux Systems Administrator — Bobcares** *(Nov 2009 – May 2010, India)*. Managed-hosting support — Linux VPS build / configuration / lifecycle on cPanel/WHM and Plesk; **BIND (DNS)** and **Exim / Postfix (SMTP)** administration across customer estates; **DHCP** for NOC-side server provisioning; **RAID and LVM troubleshooting** (array degradation, volume-group recovery, filesystem repair); customer-facing incident communications and **RCA / log-analysis write-ups**; first-line response to server-down, service-failure, and resource-exhaustion tickets.

---

## Education

**B.Tech in Computer Science** — West Bengal University of Technology, Kolkata, India (2005 – 2009)

---

## Certifications

- **Microsoft Certified: Azure Fundamentals (AZ-900)** — Mar 2023 *(Credential ID: 801D970BAA49297)*
- **AWS Certified Solutions Architect – Associate (SAA-C03)** — *in progress*
