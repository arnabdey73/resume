<div align="center">
	<h1><b>Arnab Dey</b></h1>
	<p>
		Stockholm, Sweden | +46 0764516092 | <a href="mailto:arnabdey009@gmail.com">arnabdey009@gmail.com</a><br>
		<a href="https://www.linkedin.com/in/arnabdey73">LinkedIn</a> | <a href="https://github.com/arnabdey73">GitHub</a>
	</p>
</div>

---

## Professional Summary

Cloud and Platform Engineer with hands-on experience building and operating infrastructure on AWS, Azure, and on-prem environments. I work primarily in code — Terraform for infrastructure, Python and Bash for automation, GitHub Actions and ArgoCD for delivery — and value reproducible, reviewable systems over manual operations. Comfortable across the full platform lifecycle: spinning up environments, wiring CI/CD pipelines, setting up monitoring and alerting, and iterating with development teams in agile workflows. Actively integrating GenAI and LLM tooling into DevOps processes to automate repetitive work and accelerate delivery.

---

## Core Skills

**Infrastructure as Code** — Terraform (AWS, Azure, OpenStack providers), reusable modules, Ansible

**Cloud Platforms** — AWS (EC2, S3, VPC, EKS, IAM, CloudWatch, RDS), Azure, OpenStack; comfortable adapting to new cloud providers

**CI/CD & GitOps** — GitHub Actions, GitLab CI, Jenkins, ArgoCD, Azure DevOps Pipelines; trunk-based and GitFlow workflows

**Containers & Orchestration** — Kubernetes (K3s, EKS, AKS, Rancher RKE), Docker, Helm

**Observability** — Prometheus, Grafana, ELK Stack, CloudWatch, Azure Monitor, Log Analytics

**Cloud Storage & Databases** — S3, Azure Blob Storage, DBFS (Databricks), object-storage benchmarking; experience with Key Vault and secret management

**Scripting & Automation** — Python, Bash, PowerShell

**GenAI / LLM tooling** — Built an AI-powered Resume Builder Agent (LLM-backed); integrating LLM and automation tooling into DevOps workflows

**Security & Governance** — IAM, RBAC, least-privilege patterns, secret rotation, SAML federation, Azure Policy

**Ways of Working** — Agile / SAFe, cross-team collaboration, technical documentation, knowledge sharing

**Languages** — English (fluent), Swedish (SFI C-level)

---

## Professional Experience

### DevOps Engineer — AFRY Digital Solutions AB
*May 2025 – Present  |  Stockholm, Sweden*

**Assignment: Ericsson AB — CI Engineer, Tiger Test Tools (Sep 2025 – Present)**
- Maintain and support the end-to-end CI flow for radio-communication smoke and regression testing across Git, Gerrit, Jenkins, Docker, and Linux environments.
- Troubleshoot delivery and validation pipeline issues and support hardware test infrastructure.

**AI-powered Resume Builder Agent (side project)**
- Built an LLM-backed agent that automates resume tailoring — prompt engineering, document parsing, and structured output generation. Demonstrates practical GenAI integration in automation workflows. <a href="https://github.com/arnabdey73/resume-builder-agent">Public repo</a>.

**GitOps Platform (internal reference project)**
- Designed and deployed a **GitOps-based Kubernetes platform** (K3s + ArgoCD + Prometheus + Grafana + cert-manager + sealed-secrets) as a cloud-native delivery reference — maintained as a live public demo to demonstrate end-to-end platform patterns.

**RPA Automation (Jul – Sep 2025)**
- Built a hybrid Power Automate solution that processes procurement emails, extracts document links, and automates secure browser-based downloads end-to-end.

---

### Cloud Engineer — Stena Metall AB
*Aug 2024 – Jan 2025  |  Gothenburg, Sweden*

Worked within the central Cloud Office on a mature Azure cloud estate, contributing to governance, security, and operational tooling.

- Designed and delivered **custom RBAC role definitions** (Terraform + Azure DevOps pipeline) to enforce separation-of-duties and ransomware resilience controls.
- Built a **Key Vault compliance audit** using KQL against Azure Resource Graph — producing inventory reports for architecture leadership.
- Built **Service Principal lifecycle tooling**: KQL audit for expiring credentials, PowerShell inventory, and a design for automated client-secret rotation via Logic Apps and the Graph API.
- Implemented **Azure Backup policy compliance reporting** with per-resource exemption tracking.
- KQL-based monitoring work contributed to a **~20% reduction in downtime** across supported services.
- Published sanitized GitHub repos: reusable Terraform module library, CAF governance templates, and cost-optimisation patterns.

---

### Senior Software Engineer (DevOps) — Capgemini Sverige AB
*Sep 2021 – Jul 2024  |  Gothenburg, Sweden*

**Assignment: Volvo Cars — Car Safety R&D (MLOps / AI platform)**

*Self-service cloud infrastructure via GitOps*
- Built a **GitOps self-service workflow for Azure Databricks**: data scientists request compute via a GitHub issue → YAML manifest PR → GitHub Actions runs `terraform plan` for review → merge triggers `terraform apply`.
- Terraform module with opinionated defaults: auto-termination, autoscale, DBFS log shipping, least-privilege permissions.
- **Outcome:** provisioning lead time dropped from days to same-day; every environment traceable to a PR and a named owner; eliminated idle-cluster spend.

*HPC platform modernisation (on-prem)*
- Contributed to upgrading a ~36-node HPC/ML cluster: OS migration, **Rancher-managed Kubernetes (RKE)**, **Kubeflow** via Helm for ML engineers.
- Built a production **ELK Stack** (Elasticsearch, Logstash, Kibana) with X-Pack security and SSL for cluster observability.
- Authored Ansible roles within the shared GitLab-managed codebase.

*Cloud storage benchmarking*
- Built **matched Terraform stacks** on AWS (EC2 + S3 + KMS + IAM) and Azure (VM + Premium BlockBlobStorage) as disposable, identically-shaped test rigs for object-storage benchmarks — infrastructure as a controlled variable.

---

### Senior Business Consultant (DevOps) — Tech Mahindra
*Feb 2017 – Sep 2021 | Bangalore, India | Sydney, Australia*

**Assignment: Cisco Systems — CD 2.0 on AWS**
- Authored Terraform for Cisco's continuous-delivery platform on AWS: VPC, subnets, EKS cluster, IAM roles, Jenkins on EKS, ECR, build-agent fleet, ALB, DNS.
- Built a separate **Terraform stack for an AWS observability environment**: EKS, Prometheus Operator via Helm, Grafana, persistent storage, ingress.
- Automated Cisco's SVN-to-Git migration with a Python script that enumerated repositories, provisioned Bitbucket repos via REST API, migrated history, and generated CSV reports — with retry logic and rate-limit handling.

**Assignment: Deutsche Telekom — 5G BSS Slicing Pilot on OpenStack**
- Owned the DevOps platform for DT's 5G Network Slicing commercial pilot on OpenStack: Terraform for networks, VMs, floating IPs; Ansible for all service configuration.
- Designed and maintained **~46 Jenkins jobs** building, tagging, and deploying ~30 microservices to Kubernetes via Rancher rolling updates.
- Automated a cross-tenant migration over a weekend using Python/shell: cloned 54 repositories, re-seeded Jenkins jobs, rehomed Nexus artifacts, Keycloak realm, and running Kubernetes workloads — zero rebuilds from scratch.
- Built a **Logstash pipeline** ingesting 5G Usage Data Record CSV feeds into Elasticsearch for a billing emulator.

**Assignment: Greenstone Financial Services — Insurance Portal**
- Set up Azure DevOps pipelines, Terraform for Azure infrastructure, Docker + Docker Swarm with ACR, and Azure Monitor for a .NET microservices platform.

---

### Senior AEM Administrator (Cloud) — ICF Next
*Sep 2015 – Jan 2017  |  Gothenburg / Remote*

**Assignment: Channel 7 (Australia) — AEM on AWS**
- Built and operated a production platform on AWS: VPC design, EC2 lifecycle, Apache HTTPD + Dispatcher hardening, SSL termination, and **SAML 2.0 federation** (Azure AD → AWS IAM).
- Authored Ansible roles for deployment and system baseline — making instance rebuilds a runbook rather than a discovery exercise.

---

### Unix / Linux Systems Administrator — HP Enterprise Services
*Nov 2011 – Aug 2015  |  India*

L2/L3 systems administration across large outsourcing customers (HUL, E.ON, Con-way Inc.) on Linux/Unix estates — incident handling, storage, DNS, and authored a significant portion of the Con-way Linux procedure library (LVM, SAN migration, kernel tuning).

---

## Education

**B.Tech in Computer Science** — West Bengal University of Technology, Kolkata, India (2005 – 2009)

---

## Certifications

- **Microsoft Certified: Azure Fundamentals (AZ-900)** — Mar 2023
- **AWS Certified Solutions Architect - Associate (SAA-C03)** — *in progress*
