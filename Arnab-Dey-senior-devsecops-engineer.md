<div align="center">
	<h1><b>Arnab Dey</b></h1>
	<p>
		Stockholm, Sweden | +46 0764516092 | <a href="mailto:arnabdey009@gmail.com">arnabdey009@gmail.com</a><br>
		<a href="https://www.linkedin.com/in/arnabdey73">LinkedIn</a> | <a href="https://github.com/arnabdey73">GitHub</a>
	</p>
</div>

---

## Professional Summary

Senior DevOps Engineer who treats security as an engineering discipline, not a compliance checkbox. I embed security controls directly into delivery pipelines and infrastructure: custom RBAC role definitions to enforce separation-of-duties, least-privilege IAM patterns, automated credential rotation, secret management via Key Vault and sealed-secrets, SAML federation replacing long-lived keys, and compliance reporting built into CI workflows. Security is the first conversation I have when designing a pipeline or an environment — not the last. Beyond security, I bring 9+ years of hands-on platform engineering across AWS and Azure: Terraform and Ansible for infrastructure, Jenkins and GitHub Actions for pipelines, Kubernetes and Docker for workloads. Experienced in large cross-functional transformation programmes where security, reliability, and developer velocity all need to improve together.

---

## Core Skills

**Security & DevSecOps** — IAM / RBAC (custom role definitions, least-privilege), secret management (Key Vault, sealed-secrets, KMS), credential rotation design, SAML 2.0 federation, compliance auditing (KQL / Azure Resource Graph), separation-of-duties controls, ransomware resilience patterns

**CI/CD & Automation** — Jenkins, GitHub Actions, GitLab CI, Azure DevOps Pipelines, ArgoCD; pipeline design, build environment automation, trunk-based and GitFlow workflows

**Infrastructure as Code** — Terraform (AWS, Azure, OpenStack providers), reusable module libraries, Ansible

**Cloud Platforms** — AWS (EC2, EKS, S3, VPC, IAM, ECR, ALB, CloudWatch, KMS), Azure (AKS, Key Vault, Azure Policy, Azure Monitor), OpenStack

**Containers & Orchestration** — Kubernetes (EKS, AKS, K3s, Rancher RKE), Docker, Helm

**Observability** — Prometheus, Grafana, ELK Stack (Elasticsearch, Logstash, Kibana), CloudWatch, Azure Monitor / Log Analytics (KQL)

**Scripting & Automation** — Python, Bash, PowerShell

**Ways of Working** — Agile / SAFe, cross-functional team collaboration, technical documentation, stakeholder engagement, mentoring

**Languages** — English (fluent), Swedish (SFI C-level)

---

## Professional Experience

### DevOps Engineer — AFRY Digital Solutions AB
*May 2025 – Present  |  Stockholm, Sweden*

**Assignment: Ericsson AB — CI Engineer, Tiger Test Tools (Sep 2025 – Present)**
- Maintain and support the end-to-end CI flow for radio-communication smoke and regression testing — Git, Gerrit, Jenkins, Docker, Linux.
- Troubleshoot cross-cutting pipeline and hardware issues across daily delivery and validation workflows.

**GitOps Platform (internal reference project)**
- Designed and deployed a **GitOps-based Kubernetes platform** (K3s + ArgoCD + Prometheus + Grafana + cert-manager + sealed-secrets) as a cloud-native delivery reference, with secrets management and TLS automation built in from the start.

---

### Cloud Engineer — Stena Metall AB
*Aug 2024 – Jan 2025  |  Gothenburg, Sweden*

Security and governance engineering on a production Azure estate — ~100 subscriptions across a multi-management-group hierarchy supporting a multi-billion-SEK industrial group.

- **Authored two custom Azure RBAC role definitions** — a "Backup Remover" role and a modified Contributor with explicit `notActions` — to enforce separation-of-duties between resource management and backup deletion, a ransomware-resilience control missing from Azure built-ins. Deployed via Terraform + Azure DevOps pipeline into the CAF archetype framework.
- Delivered a **tenant-wide Key Vault compliance audit** — KQL against Azure Resource Graph for soft-delete retention, purge protection, and RBAC authorisation — producing CSV inventories and a documented remediation review.
- Built **Service Principal lifecycle tooling**: KQL audit for 30-day credential events, PowerShell expiring-credential inventory, and a design for automated client-secret rotation via Logic Apps + Graph API `addPassword`.
- Implemented **Azure Backup policy compliance reporting** with per-resource exempt-rationale tracking.
- KQL-based monitoring contributed to a **~20% reduction in downtime** across supported services.
- Delivered fixes across multiple application landing-zone repositories: cost-allocation tagging, Key Vault configuration, AzureRM version alignment.

---

### Senior Software Engineer (DevOps) — Capgemini Sverige AB
*Sep 2021 – Jul 2024  |  Gothenburg, Sweden*

**Assignment: Volvo Cars — Car Safety R&D (Abakus MLOps / AI ART)**

*GitOps self-service pipeline*
- Designed and owned a **GitOps self-service pattern for Azure Databricks**: compute requests go from a GitHub issue template → YAML manifest PR → GitHub Actions runs `terraform fmt/validate/plan` for review → merge triggers `terraform apply`.
- Terraform module with security baked in: single-user security mode, 30-minute auto-termination, autoscale, cluster-log shipping to DBFS, `CAN_RESTART` permissions, remote state in Azure Blob Storage with secrets injected at init from GitHub environment secrets.
- **Outcome:** provisioning lead time dropped from days to same-day; every cluster traceable to a PR, a manifest, and a named owner; eliminated idle-cluster spend.

*HPC platform modernisation (on-prem)*
- Contributed to upgrading a ~36-node CAE/HPC cluster: OS migration from SLES to Ubuntu LTS, **Rancher-managed Kubernetes (RKE)**, **Kubeflow** via Helm for ML engineers.
- Built a production **ELK Stack** with X-Pack security, SSL, and snapshot repositories for cluster observability.
- Authored Ansible roles within the shared GitLab-managed codebase.

*Dual-cloud benchmarking infrastructure*
- Built matched Terraform stacks on AWS (EC2 + S3 + KMS + IAM) and Azure (VM + Premium BlockBlobStorage) as identically-shaped, disposable test rigs — demonstrating secure, reproducible infrastructure patterns across cloud providers.

---

### Senior Business Consultant (DevOps) — Tech Mahindra
*Feb 2017 – Sep 2021 | Bangalore, India | Sydney, Australia*

**Assignment: Cisco Systems — CD 2.0 on AWS**
- **Authored Terraform** for Cisco's CD 2.0 continuous-delivery platform on AWS — VPC, subnets, security groups, EKS cluster, IAM roles, Jenkins on EKS, ECR integration, build-agent fleet, ALB, DNS — extending an internal reference architecture.
- Wrote a separate **Terraform stack for an AWS observability environment** — EKS, Prometheus Operator via Helm, Grafana, persistent storage, ingress.
- Automated Cisco's SVN-to-Git migration with **Python**: enumerated repositories, provisioned Bitbucket repos via REST API, migrated history, produced CSV audit reports — with retry logic and rate-limit handling.
- Onboarded application teams to CD 2.0 via CI engagement templates, Bitbucket/Crucible provisioning, and Jenkinsfile adaptation.

**Assignment: Deutsche Telekom — 5G BSS Slicing Pilot on OpenStack**
- Owned the **DevOps platform** for DT's 5G Network Slicing commercial pilot: Terraform for networks, subnets, security groups, VMs, and floating IPs; Ansible playbooks for all service configuration.
- Designed and maintained **~46 Jenkins jobs** building ~30 microservices, tagging with build number + short git SHA, pushing to internal Nexus registry, and triggering Kubernetes rolling updates via Rancher.
- Automated a **cross-tenant migration** over a weekend: Python/shell scripted the cloning of 54 Tuleap repositories, re-seeding of Jenkins jobs, and rehoming of Nexus artifacts, Keycloak realm, and running Kubernetes workloads — cutover completed without rebuilding anything from scratch.
- Built a **Logstash pipeline** ingesting 5G Usage Data Record CSV feeds into Elasticsearch for a billing emulator.

**Assignment: Greenstone Financial Services — Insurance Portal**
- Led DevOps transformation for .NET microservices: Azure DevOps pipelines, Terraform for Azure infrastructure, Docker + Docker Swarm with ACR, Azure Monitor for observability.

---

### Senior AEM Administrator (Cloud) — ICF Next
*Sep 2015 – Jan 2017  |  Gothenburg / Remote*

**Assignment: Channel 7 (Australia) — AEM on AWS**
- Built and operated a production platform on AWS with a security-first baseline: VPC design, EC2 lifecycle, Apache HTTPD + Dispatcher hardening, SSL termination, and **SAML 2.0 federation** (Azure AD / ADFS → AWS IAM) replacing long-lived IAM user keys.
- Authored Ansible roles for AEM install, Apache/Dispatcher deployment, SSL, and system baseline — making instance rebuilds repeatable and auditable.

---

### Unix / Linux Systems Administrator — HP Enterprise Services
*Nov 2011 – Aug 2015  |  India*

L2/L3 systems administration across large outsourcing customers (HUL, E.ON, Con-way Inc.) on Linux/Unix estates — 24×7 incident handling, storage, DNS, and authored a significant portion of the Con-way Linux procedure library (LVM, SAN migration, kernel tuning, ITO/OpsBridge agent management).

---

## Education

**B.Tech in Computer Science** — West Bengal University of Technology, Kolkata, India (2005 – 2009)

---

## Certifications

- **Microsoft Certified: Azure Fundamentals (AZ-900)** — Mar 2023
- **AWS Certified Solutions Architect - Associate (SAA-C03)** — *in progress*
