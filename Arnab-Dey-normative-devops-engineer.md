<div align="center">
	<h1><b>Arnab Dey</b></h1>
	<p>
		Stockholm, Sweden | +46 0764516092 | <a href="mailto:arnabdey009@gmail.com">arnabdey009@gmail.com</a><br>
		<a href="https://www.linkedin.com/in/arnabdey73">LinkedIn</a> | <a href="https://github.com/arnabdey73">GitHub</a>
	</p>
</div>

---

## Professional Summary

DevOps and Cloud Engineer with a strong AWS background and a hands-on approach to infrastructure, reliability, and automation. I work in code — Terraform for infrastructure, GitHub Actions and ArgoCD for delivery, Prometheus and Grafana for observability — and favour systems that are reproducible, auditable, and easy for development teams to reason about. Comfortable operating independently in small platform teams and owning the full lifecycle: building environments, wiring CI/CD, leading incident response, and iterating with developers. Track record of reducing manual toil through automation and improving reliability through structured monitoring.

---

## Core Skills

**Cloud** — AWS (EC2, S3, VPC, EKS, IAM, CloudWatch, KMS, ECR, ALB); Azure; OpenStack; comfortable adapting to new cloud providers

**Infrastructure as Code** — Terraform (AWS, Azure, OpenStack providers), reusable modules, Ansible

**CI/CD** — GitHub Actions, GitLab CI, Jenkins, ArgoCD, Azure DevOps Pipelines

**Containers & Orchestration** — Kubernetes (EKS, K3s, AKS, Rancher RKE), Docker, ECS, Helm

**Observability & Reliability** — Prometheus, Grafana, ELK Stack (Elasticsearch, Logstash, Kibana), CloudWatch, Azure Monitor; incident management and alerting design

**Scripting & Automation** — Python, Bash, PowerShell

**Cloud Storage** — S3, Azure Blob Storage, DBFS; object-storage benchmarking and performance tuning

**Security** — IAM, RBAC, least-privilege patterns, secret management, SAML federation, credential rotation

**Ways of Working** — Agile, cross-team collaboration, technical documentation, independent ownership in small teams

**Languages** — English (fluent), Swedish (SFI C-level)

---

## Professional Experience

### DevOps Engineer — AFRY Digital Solutions AB
*May 2025 – Present  |  Stockholm, Sweden*

**Assignment: Ericsson AB — CI Engineer (Sep 2025 – Present)**
- Maintain and support the end-to-end CI flow for radio-communication smoke and regression testing — Git, Gerrit, Jenkins, Docker, Linux.
- Troubleshoot cross-cutting pipeline and hardware issues across daily delivery and validation workflows.

**GitOps Platform (internal reference project)**
- Designed and deployed a **GitOps-based Kubernetes platform** (K3s + ArgoCD + Prometheus + Grafana + cert-manager + sealed-secrets) as a cloud-native delivery reference — maintained as a live public demo.

---

### Cloud Engineer — Stena Metall AB
*Aug 2024 – Jan 2025  |  Gothenburg, Sweden*

Infrastructure and reliability work on a production Azure cloud estate supporting a large industrial group.

- Designed and delivered **RBAC controls** (Terraform + CI pipeline) to enforce separation-of-duties and ransomware-resilience — a governance gap in the platform's existing Contributor roles.
- Built a **Key Vault compliance audit** using KQL against Azure Resource Graph, producing inventory and remediation reports.
- Built **Service Principal lifecycle tooling** — expiring-credential inventory, audit queries, and a design for automated client-secret rotation via Logic Apps and the Graph API.
- Implemented **Azure Backup policy compliance reporting** with per-resource exemption tracking.
- KQL-based monitoring work contributed to a **~20% reduction in downtime** across supported services.

---

### Senior Software Engineer (DevOps) — Capgemini Sverige AB
*Sep 2021 – Jul 2024  |  Gothenburg, Sweden*

**Assignment: Volvo Cars — Car Safety R&D (MLOps / AI platform)**

*Self-service cloud infrastructure via GitOps*
- Designed and owned a **GitOps self-service workflow for Azure Databricks**: compute requests go from a GitHub issue → YAML manifest PR → `terraform plan` for review → merge triggers `terraform apply`.
- Terraform module with governance-friendly defaults: auto-termination, autoscale, DBFS log shipping, least-privilege permissions.
- **Outcome:** provisioning lead time dropped from days to same-day; every environment traceable to a PR and a named owner; eliminated idle-cluster spend.

*HPC platform modernisation (on-prem)*
- Contributed to upgrading a ~36-node HPC/ML cluster: OS migration, **Rancher-managed Kubernetes (RKE)**, **Kubeflow** via Helm for ML engineers.
- Built a production **ELK Stack** (Elasticsearch, Logstash, Kibana) with X-Pack security and SSL for cluster observability.
- Authored Ansible roles within the shared GitLab-managed codebase.

*Cloud storage benchmarking*
- Built **matched Terraform stacks** on AWS (EC2 + S3 + KMS + IAM) and Azure (VM + Premium BlockBlobStorage) as disposable, identically-shaped test rigs for object-storage performance benchmarks.

---

### Senior Business Consultant (DevOps) — Tech Mahindra
*Feb 2017 – Sep 2021 | Bangalore, India | Sydney, Australia*

**Assignment: Cisco Systems — CD 2.0 on AWS**
- **Authored Terraform** for Cisco's continuous-delivery platform on AWS: VPC, subnets, security groups, EKS cluster, IAM roles, Jenkins on EKS, ECR, build-agent fleet, ALB, DNS.
- Built a separate **Terraform stack for an AWS observability environment**: EKS, Prometheus Operator via Helm, Grafana, persistent storage, ingress.
- Automated Cisco's SVN-to-Git migration with Python: enumerated repositories, provisioned Bitbucket repos via REST API, migrated history, generated CSV reports — with retry logic and rate-limit handling.
- Onboarded application teams to the CD 2.0 platform via CI engagement templates and Jenkinsfile adaptation.

**Assignment: Deutsche Telekom — 5G BSS Slicing Pilot on OpenStack**
- Owned the DevOps platform for DT's 5G Network Slicing commercial pilot: Terraform for networks, VMs, floating IPs; Ansible for service configuration; ~46 Jenkins jobs building and deploying ~30 microservices to Kubernetes.
- Automated a cross-tenant migration over a weekend using Python/shell — 54 repositories, Jenkins jobs, Nexus artifacts, Keycloak realm, and running Kubernetes workloads — zero rebuilds from scratch.
- Built a **Logstash pipeline** ingesting 5G Usage Data Record CSV feeds into Elasticsearch for a billing emulator.

**Assignment: Greenstone Financial Services — Insurance Portal**
- Set up Azure DevOps pipelines, Terraform for Azure infrastructure, Docker + Docker Swarm with ACR, and Azure Monitor for a .NET microservices platform.

---

### Senior AEM Administrator (Cloud) — ICF Next
*Sep 2015 – Jan 2017  |  Bangalore, India*

**Assignment: Channel 7 (Australia) — AEM on AWS**
- Built and operated a production platform on AWS: VPC design, EC2 lifecycle, Apache HTTPD + Dispatcher hardening, SSL termination, SAML 2.0 federation (Azure AD → AWS IAM), and Auto Scaling Group configuration.
- Authored Ansible roles for deployment and system baseline — making instance rebuilds a runbook rather than a discovery exercise.

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
