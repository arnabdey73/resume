<div align="center">
	<h1><b>Arnab Dey</b></h1>
	<p>
		Stockholm, Sweden | +46 0764516092 | <a href="mailto:arnabdey009@gmail.com">arnabdey009@gmail.com</a><br>
		<a href="https://www.linkedin.com/in/arnabdey73">LinkedIn</a> | <a href="https://github.com/arnabdey73">GitHub</a>
	</p>
</div>

---

## Professional Summary

DevOps Engineer with hands-on experience building and operating cloud infrastructure for ML and data science teams. My most relevant work is at Volvo Cars, where I owned the platform side of an MLOps initiative — self-service Databricks provisioning via GitOps, HPC cluster modernisation with Kubernetes and Kubeflow, ELK-based observability, and dual-cloud storage benchmarking for ML workloads. I work primarily in AWS, Terraform, and Kubernetes, automate in Python and Bash, and build CI/CD pipelines in GitHub Actions and Jenkins. I thrive in small, fast-moving teams where I can take ownership end-to-end and drive delivery improvements without layers of process in the way.

---

## Core Skills

**Cloud & Infrastructure** — AWS (EC2, S3, VPC, EKS, IAM, CloudWatch, KMS, ECR, ALB), Terraform, Ansible

**Containers & Orchestration** — Kubernetes (EKS, K3s, AKS, Rancher RKE), Docker, Helm, Kubeflow

**CI/CD & Automation** — GitHub Actions, Jenkins, GitLab CI, ArgoCD, Azure DevOps Pipelines

**ML Platform** — Databricks (GitOps self-service provisioning), Kubeflow, HPC cluster operations, object-storage benchmarking for ML workloads

**Observability** — Prometheus, Grafana, ELK Stack (Elasticsearch, Logstash, Kibana), CloudWatch

**Scripting** — Python (automation, CLI tooling, migration scripts), Bash, PowerShell

**Security** — IAM, RBAC, least-privilege patterns, secret management (Key Vault, sealed-secrets, KMS), SAML federation

**Ways of Working** — Agile, small-team ownership, technical documentation, cross-functional collaboration

**Languages** — English (fluent), Swedish (SFI C-level)

---

## Professional Experience

### DevOps Engineer — AFRY Digital Solutions AB
*May 2025 – Present  |  Stockholm, Sweden*

**Assignment: Ericsson AB — CI Engineer (Sep 2025 – Present)**
- Maintain and support end-to-end CI for radio-communication smoke and regression testing — Git, Gerrit, Jenkins, Docker, Linux.
- Troubleshoot pipeline and hardware issues across daily delivery and validation workflows.

**GitOps Platform (internal reference project)**
- Designed and deployed a GitOps-based Kubernetes platform (K3s + ArgoCD + Prometheus + Grafana + cert-manager + sealed-secrets) as a live cloud-native reference — publicly maintained on GitHub.

---

### Senior Software Engineer (DevOps) — Capgemini Sverige AB
*Sep 2021 – Jul 2024  |  Gothenburg, Sweden*

**Assignment: Volvo Cars — Car Safety R&D, MLOps / AI Platform**

*Self-service ML infrastructure via GitOps*
- Designed and owned a **GitOps self-service workflow for Azure Databricks**: ML engineers request compute via a GitHub issue template → YAML manifest PR → GitHub Actions runs `terraform fmt/validate/plan` for review → merge triggers `terraform apply`.
- Terraform module with ML-friendly defaults baked in: single-user security mode, 30-minute auto-termination, autoscale 1→3 workers, cluster-log shipping to DBFS, `CAN_RESTART` permissions, remote state in Azure Blob Storage.
- **Outcome:** provisioning lead time dropped from days to same-day; every cluster traceable to a PR and a named owner; eliminated idle-cluster spend.

*HPC / ML cluster modernisation (on-prem)*
- Contributed to modernising a ~36-node HPC cluster supporting ML research: OS migration (SLES → Ubuntu LTS), **Rancher-managed Kubernetes (RKE)** with worker fleet, **Kubeflow** installation via Helm for ML engineers.
- Built a production **ELK Stack** (Elasticsearch, Logstash, Kibana) with X-Pack security and SSL — cluster observability for ML workload monitoring.
- Authored Ansible roles within the shared GitLab-managed codebase.

*Cloud storage benchmarking for ML workloads*
- Built **matched Terraform stacks** on AWS (EC2 + S3 + KMS + IAM) and Azure (VM + Premium BlockBlobStorage) as identically-shaped, disposable test rigs for MLCommons-style object-storage benchmarks — infrastructure as a controlled variable so data scientists could compare cloud storage performance on equal footing.

---

### Cloud Engineer — Stena Metall AB
*Aug 2024 – Jan 2025  |  Gothenburg, Sweden*

Security and governance engineering on a production Azure estate.

- Designed and delivered **custom RBAC role definitions** via Terraform + CI pipeline to enforce separation-of-duties and ransomware resilience.
- Built a **Key Vault compliance audit** using KQL against Azure Resource Graph, producing remediation inventory for architecture leadership.
- Built **Service Principal lifecycle tooling** — expiring-credential inventory and automated rotation design via Logic Apps + Graph API.
- KQL-based monitoring contributed to a **~20% reduction in downtime** across supported services.

---

### Senior Business Consultant (DevOps) — Tech Mahindra
*Feb 2017 – Sep 2021 | Bangalore, India | Sydney, Australia*

**Assignment: Cisco Systems — CD 2.0 on AWS**
- Authored **Terraform** for Cisco's continuous-delivery platform on AWS: VPC, subnets, security groups, EKS cluster, IAM roles, Jenkins on EKS, ECR, build-agent fleet, ALB, DNS.
- Built a separate **Terraform stack for an AWS observability environment**: EKS, Prometheus Operator via Helm, Grafana, persistent storage, ingress.
- Automated Cisco's SVN-to-Git migration with **Python**: enumerated repositories, provisioned Bitbucket repos via REST API, migrated history with retry logic and rate-limit handling, produced CSV audit reports.

**Assignment: Deutsche Telekom — 5G BSS Slicing Pilot on OpenStack**
- Owned the DevOps platform for DT's 5G Network Slicing pilot: Terraform for networks and VMs; Ansible for service configuration; ~46 Jenkins jobs building and deploying ~30 microservices to Kubernetes via Rancher.
- Automated a cross-tenant migration over a weekend — 54 repositories, Jenkins jobs, Nexus artifacts, Keycloak realm, and running Kubernetes workloads — zero rebuilds from scratch.
- Built a **Logstash pipeline** ingesting Usage Data Record CSV feeds into Elasticsearch for a billing emulator.

---

### Senior AEM Administrator (Cloud) — ICF Next
*Sep 2015 – Jan 2017  |  Gothenburg / Remote*

**Assignment: Channel 7 (Australia) — AEM on AWS**
- Built and operated a production AWS platform: VPC, EC2, Auto Scaling Group, Apache HTTPD + Dispatcher hardening, SSL, SAML 2.0 federation (Azure AD → AWS IAM).
- Authored Ansible roles for deployment and system baseline.

---

### Unix / Linux Systems Administrator — HP Enterprise Services
*Nov 2011 – Aug 2015  |  India*

L2/L3 systems administration on Linux/Unix estates across HUL, E.ON, and Con-way Inc. — 24×7 incident handling, storage, DNS, and authored the Con-way Linux procedure library (LVM, SAN migration, kernel tuning).

---

## Education

**B.Tech in Computer Science** — West Bengal University of Technology, Kolkata, India (2005 – 2009)

---

## Certifications

- **Microsoft Certified: Azure Fundamentals (AZ-900)** — Mar 2023
- **AWS Certified Solutions Architect - Associate (SAA-C03)** — *in progress*
