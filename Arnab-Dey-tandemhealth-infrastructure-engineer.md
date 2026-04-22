<div align="center">
	<h1><b>Arnab Dey</b></h1>
	<p>
		Stockholm, Sweden | +46 0764516092 | <a href="mailto:arnabdey009@gmail.com">arnabdey009@gmail.com</a><br>
		<a href="https://www.linkedin.com/in/arnabdey73">LinkedIn</a> | <a href="https://github.com/arnabdey73">GitHub</a>
	</p>
</div>

---

## Professional Summary

Infrastructure Engineer with Azure as my primary cloud and deep hands-on experience in Kubernetes, CI/CD, security, and encryption. I don't just configure systems — I build them: Terraform modules, Python automation tooling, Ansible playbooks, and GitOps self-service workflows designed to make development teams faster without sacrificing correctness. I've operated in regulated, governance-heavy environments where encryption, key management, audit trails, and access controls are load-bearing — not afterthoughts. I bring a craftsmanship mindset: observable systems, documented decisions, and infrastructure that stays up. Comfortable in small, high-ownership platform teams where the work is highly visible and the standards are high.

---

## Core Skills

**Cloud** — Azure (primary: AKS, Key Vault, Azure Policy, RBAC, Azure Monitor, Blob Storage, Entra ID); AWS (EC2, EKS, S3, VPC, IAM, ECR, KMS, CloudWatch); OpenStack

**Kubernetes** — AKS, EKS, K3s, Rancher RKE; Helm, ArgoCD (GitOps), workload management, cert-manager, sealed-secrets

**Security & Encryption** — Key Vault (soft-delete, purge protection, RBAC authorisation), KMS, custom RBAC role definitions, least-privilege IAM, secret management, credential rotation, SAML 2.0 federation, separation-of-duties controls, SSL/TLS termination, X-Pack security

**CI/CD & Automation** — GitHub Actions, Azure DevOps Pipelines, GitLab CI, Jenkins, ArgoCD; pipeline design, automated testing, secure deployment workflows

**Infrastructure as Code** — Terraform (Azure, AWS, OpenStack providers), reusable modules, Ansible

**Observability** — Prometheus, Grafana, ELK Stack (Elasticsearch, Logstash, Kibana), Azure Monitor / Log Analytics (KQL), CloudWatch; alerting design and incident response

**Programming & Scripting** — Python (automation, CLI tooling, REST API integration, migration tooling), Bash, PowerShell

**Regulated Environments** — governance frameworks, compliance auditing, audit-trail automation, data protection controls, financial services (Greenstone Financial Services)

**Languages** — English (fluent), Swedish (SFI C-level)

---

## Professional Experience

### DevOps Engineer — AFRY Digital Solutions AB
*May 2025 – Present  |  Stockholm, Sweden*

**Assignment: Ericsson AB — CI Engineer (Sep 2025 – Present)**
- Maintain and support end-to-end CI for radio-communication smoke and regression testing — Git, Gerrit, Jenkins, Docker, Linux.
- Troubleshoot cross-cutting pipeline and hardware issues across daily delivery and validation workflows.

**GitOps Platform (internal reference project)**
- Designed and deployed a GitOps-based Kubernetes platform (K3s + ArgoCD + Prometheus + Grafana + cert-manager + sealed-secrets) with TLS automation and encrypted secret management built in from the start — maintained as a live public demo on GitHub.

---

### Cloud Engineer — Stena Metall AB
*Aug 2024 – Jan 2025  |  Gothenburg, Sweden*

Security, encryption, and governance engineering on a production Azure estate — ~100 subscriptions supporting a large industrial group. The work here was directly about making sensitive data and critical systems auditable, access-controlled, and resilient.

- **Key Vault compliance audit** — KQL against Azure Resource Graph for soft-delete retention, purge protection, and RBAC authorisation across all Key Vaults in the tenant. Produced CSV inventories and a remediation plan for architecture leadership. This is the same class of control required for PHI and sensitive data management.
- **Custom Azure RBAC role definitions** — authored a "Backup Remover" role and a modified Contributor with explicit `notActions` to enforce separation-of-duties between resource management and backup deletion, a ransomware-resilience control missing from Azure built-ins. Deployed via Terraform + Azure DevOps pipeline into the CAF archetype framework.
- **Service Principal lifecycle tooling** — KQL audit for 30-day credential events, PowerShell expiring-credential inventory, and a design for automated client-secret rotation via Logic Apps + Graph API `addPassword` — systematic credential hygiene at scale.
- Implemented **Azure Backup policy compliance reporting** with per-resource exempt-rationale tracking.
- KQL-based monitoring contributed to a **~20% reduction in downtime** across supported services.

---

### Senior Software Engineer (DevOps) — Capgemini Sverige AB
*Sep 2021 – Jul 2024  |  Gothenburg, Sweden*

**Assignment: Volvo Cars — Car Safety R&D, MLOps / AI Platform**

- Designed and owned a **GitOps self-service workflow for Azure Databricks**: engineers request compute via a GitHub issue → YAML manifest PR → GitHub Actions `terraform plan` for review → merge triggers `terraform apply`. Secrets injected at init from GitHub environment secrets; remote state in Azure Blob Storage. Outcome: provisioning dropped from days to same-day; every resource traceable to a PR and named owner.
- Contributed to modernising a ~36-node HPC/ML cluster: OS migration (SLES → Ubuntu LTS), **Rancher-managed Kubernetes (RKE)** with worker fleet, **Kubeflow** via Helm for ML engineers.
- Built a **production ELK Stack** with X-Pack security, SSL, and snapshot repositories — full observability for ML workload monitoring and log aggregation.
- Authored Ansible roles within the shared GitLab-managed codebase.
- Built matched **Terraform stacks on AWS** (EC2 + S3 + KMS + IAM) and Azure as disposable, identically-shaped test rigs for ML object-storage benchmarks.

---

### Senior Business Consultant (DevOps) — Tech Mahindra
*Feb 2017 – Sep 2021 | Bangalore, India | Sydney, Australia*

**Assignment: Cisco Systems — CD 2.0 on AWS**
- Authored **Terraform** for Cisco's continuous-delivery platform on AWS: VPC, subnets, security groups, EKS cluster, IAM roles, Jenkins on EKS, ECR, build-agent fleet, ALB, DNS.
- Built a separate **Terraform stack for an AWS observability environment**: EKS, Prometheus Operator via Helm, Grafana, persistent storage, ingress.
- Wrote **Python automation** for Cisco's SVN-to-Git migration: repository enumeration, Bitbucket provisioning via REST API, history migration, CSV audit reports — with retry logic and rate-limit handling. Automated what would otherwise have been months of manual work.

**Assignment: Deutsche Telekom — 5G BSS Slicing Pilot on OpenStack**
- Owned the DevOps platform for DT's 5G Network Slicing commercial pilot: Terraform for on-premise OpenStack networks and VMs; Ansible for all service configuration; ~46 Jenkins jobs building and deploying ~30 microservices to Kubernetes.
- Deployed Kafka and Zookeeper via Helm charts; configured message queues for event-streaming and billing pipelines.
- Automated a cross-tenant migration over a weekend: Python/shell scripted 54 repositories, Jenkins jobs, Nexus artifacts, Keycloak realm, and running Kubernetes workloads — zero rebuilds.

**Assignment: Greenstone Financial Services — Insurance Portal**
- Led DevOps for a regulated financial services platform: Azure DevOps pipelines, Terraform for Azure infrastructure, Docker + Docker Swarm with ACR, Azure Monitor for observability.

---

### Senior AEM Administrator (Cloud) — ICF Next
*Sep 2015 – Jan 2017  |  Bangalore, India*

**Assignment: Channel 7 (Australia) — AEM on AWS**
- Built and operated a production AWS platform: VPC, EC2, Auto Scaling Group, Apache HTTPD hardening, SSL termination, **SAML 2.0 federation** (Azure AD → AWS IAM) replacing long-lived IAM user keys.
- Authored Ansible roles for deployment and system baseline — repeatable, auditable instance rebuilds.

---

### Unix / Linux Systems Administrator — HP Enterprise Services
*Nov 2011 – Aug 2015  |  Bangalore, India*

L2/L3 systems administration across large outsourcing customers on Linux/Unix estates — 24×7 incident handling, storage management, DNS, and authored a significant portion of the Con-way Linux procedure library (LVM, SAN migration, kernel tuning).

---

## Education

**B.Tech in Computer Science** — West Bengal University of Technology, Kolkata, India (2005 – 2009)

---

## Certifications

- **Microsoft Certified: Azure Fundamentals (AZ-900)** — Mar 2023
- **AWS Certified Solutions Architect - Associate (SAA-C03)** — *in progress*
