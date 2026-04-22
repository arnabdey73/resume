<div align="center">
	<h1><b>Arnab Dey</b></h1>
	<p>
		Stockholm, Sweden | +46 0764516092 | <a href="mailto:arnabdey009@gmail.com">arnabdey009@gmail.com</a><br>
		<a href="https://www.linkedin.com/in/arnabdey73">LinkedIn</a> | <a href="https://github.com/arnabdey73">GitHub</a>
	</p>
</div>

---

## Professional Summary

Infrastructure Engineer with strong hands-on expertise in AWS, Kubernetes, Elasticsearch, and Terraform. I've deployed and operated production ELK stacks, built and maintained Kubernetes clusters across EKS, RKE, and K3s, and designed self-service CI/CD workflows that improve developer velocity without sacrificing reliability. Equally comfortable being hands-on and providing technical direction — I've shaped DevOps practices, mentored engineers, and driven platform improvements in cross-functional teams. In fast-paced product environments I focus on building observable, scalable, and reproducible systems that engineering teams can trust and iterate on confidently.

---

## Core Skills

**Kubernetes** — EKS, K3s, AKS, Rancher RKE; cluster management, Helm, workload scaling, GitOps with ArgoCD

**Elasticsearch & Observability** — Production ELK Stack (Elasticsearch, Logstash, Kibana) with SSL; Logstash pipeline design for data ingestion; Prometheus, Grafana, CloudWatch, Azure Monitor

**AWS** — EC2, EKS, S3, VPC, IAM, ECR, ALB, CloudWatch, KMS; infrastructure design and operations

**Infrastructure as Code** — Terraform (AWS, Azure, OpenStack providers), reusable modules, Ansible

**CI/CD** — GitHub Actions, GitLab CI, Jenkins, ArgoCD, Azure DevOps Pipelines

**Containers** — Docker, Helm, Kubeflow

**Scripting & Automation** — Python, Bash, PowerShell

**Security** — IAM, RBAC, least-privilege patterns, secret management (Key Vault, sealed-secrets, KMS), credential rotation, SAML federation

**Ways of Working** — Technical leadership, mentoring, agile cross-functional teams, documentation, DevOps best practices

**Languages** — English (fluent), Swedish (SFI C-level)

---

## Professional Experience

### DevOps Engineer — AFRY Digital Solutions AB
*May 2025 – Present  |  Stockholm, Sweden*

**Assignment: Ericsson AB — CI Engineer (Sep 2025 – Present)**
- Maintain and support end-to-end CI for radio-communication smoke and regression testing — Git, Gerrit, Jenkins, Docker, Linux.
- Troubleshoot cross-cutting pipeline and hardware issues across daily delivery and validation workflows.

**GitOps Platform (internal reference project)**
- Designed and deployed a GitOps-based Kubernetes platform (K3s + ArgoCD + Prometheus + Grafana + cert-manager + sealed-secrets) as a cloud-native reference, maintained as a live public demo on GitHub.

---

### Senior Software Engineer (DevOps) — Capgemini Sverige AB
*Sep 2021 – Jul 2024  |  Gothenburg, Sweden*

**Assignment: Volvo Cars — Car Safety R&D, MLOps / AI Platform**

*Production ELK Stack*
- Built a **production-grade ELK Stack** (Elasticsearch, Logstash, Kibana) on LXD with **SSL termination, and snapshot repositories** for a ~36-node HPC/ML cluster — providing full observability for ML workload monitoring and log aggregation across the fleet.

*HPC / Kubernetes platform*
- Contributed to modernising the HPC cluster: OS migration (SLES → Ubuntu LTS), **Rancher-managed Kubernetes (RKE)** with worker fleet, **Kubeflow** via Helm for ML engineers.
- Authored Ansible roles within the shared GitLab-managed codebase.

*Self-service infrastructure via GitOps*
- Designed and owned a **GitOps self-service workflow for Azure Databricks**: engineers request compute via a GitHub issue → YAML manifest PR → GitHub Actions `terraform plan` for review → merge triggers `terraform apply`.
- **Outcome:** provisioning lead time dropped from days to same-day; every environment traceable to a PR and a named owner; eliminated idle-cluster spend.

*Cloud storage benchmarking*
- Built matched Terraform stacks on AWS (EC2 + S3 + KMS + IAM) and Azure as disposable, identically-shaped test rigs for ML object-storage benchmarks.

---

### Cloud Engineer — Stena Metall AB
*Aug 2024 – Jan 2025  |  Gothenburg, Sweden*

Infrastructure, monitoring, and security engineering on a production Azure estate supporting a large industrial group.

- Delivered a **tenant-wide Key Vault compliance audit** — KQL against Azure Resource Graph for soft-delete retention, purge protection, and RBAC authorisation.
- Designed and delivered **custom RBAC role definitions** via Terraform + CI pipeline to enforce separation-of-duties and ransomware resilience.
- Built **Service Principal lifecycle tooling**: expiring-credential inventory, KQL audit, and automated rotation design via Logic Apps + Graph API.
- KQL-based monitoring contributed to a **~20% reduction in downtime** across supported services.

---

### Senior Business Consultant (DevOps) — Tech Mahindra
*Feb 2017 – Sep 2021 | Bangalore, India | Sydney, Australia*

**Assignment: Cisco Systems — CD 2.0 on AWS**
- Authored **Terraform** for Cisco's continuous-delivery platform on AWS: VPC, subnets, security groups, EKS cluster, IAM roles, Jenkins on EKS, ECR, build-agent fleet, ALB, DNS.
- Built a separate **Terraform stack for an AWS observability environment**: EKS, Prometheus Operator via Helm, Grafana, persistent storage, ingress.
- Automated Cisco's SVN-to-Git migration with **Python**: repository enumeration, Bitbucket provisioning via REST API, history migration, CSV audit reports — with retry logic and rate-limit handling.
- Onboarded application teams to the CI/CD platform via engagement templates and Jenkinsfile adaptation.

**Assignment: Deutsche Telekom — 5G BSS Slicing Pilot on OpenStack**
- Owned the DevOps platform for DT's 5G Network Slicing commercial pilot: Terraform for networks, VMs, and floating IPs; Ansible for all service configuration.
- Designed and maintained **~46 Jenkins jobs** building and deploying ~30 microservices to Kubernetes via Rancher rolling updates.
- Built a **Logstash pipeline** ingesting 5G Usage Data Record (UDR) CSV feeds into **Elasticsearch** for a high-volume billing emulator — production data pipeline with structured ingestion, field mapping, and index management.
- Automated a cross-tenant migration over a weekend: 54 repositories, Jenkins jobs, Nexus artifacts, Keycloak realm, and running Kubernetes workloads — zero rebuilds from scratch.

**Assignment: Greenstone Financial Services — Insurance Portal**
- Set up Azure DevOps pipelines, Terraform for Azure infrastructure, Docker + Docker Swarm with ACR, and Azure Monitor for a .NET microservices platform.

---

### Senior AEM Administrator (Cloud) — ICF Next
*Sep 2015 – Jan 2017  |  Bangalore, India*

**Assignment: Channel 7 (Australia) — AEM on AWS**
- Built and operated a production AWS platform: VPC design, EC2 lifecycle, Auto Scaling Group, Apache HTTPD hardening, SSL termination, SAML 2.0 federation (Azure AD → AWS IAM).
- Authored Ansible roles for deployment and system baseline — making instance rebuilds repeatable and auditable.

---

### Unix / Linux Systems Administrator — HP Enterprise Services
*Nov 2011 – Aug 2015  |  Bangalore, India*

L2/L3 systems administration across large outsourcing customers (HUL, E.ON, Con-way Inc.) on Linux/Unix estates — 24×7 incident handling, storage, DNS, and authored a significant portion of the Con-way Linux procedure library (LVM, SAN migration, kernel tuning).

---

## Education

**B.Tech in Computer Science** — West Bengal University of Technology, Kolkata, India (2005 – 2009)

---

## Certifications

- **Microsoft Certified: Azure Fundamentals (AZ-900)** — Mar 2023
- **AWS Certified Solutions Architect - Associate (SAA-C03)** — *in progress*
