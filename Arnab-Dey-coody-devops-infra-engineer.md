<div align="center">
	<h1><b>Arnab Dey</b></h1>
	<p>
		Stockholm, Sweden | +46 0764516092 | <a href="mailto:arnabdey009@gmail.com">arnabdey009@gmail.com</a><br>
		<a href="https://www.linkedin.com/in/arnabdey73">LinkedIn</a> | <a href="https://github.com/arnabdey73">GitHub</a>
	</p>
</div>

---

## Professional Summary

Senior DevOps / Infrastructure Engineer with **15+ years in IT** and **9+ years building and modernising CI/CD and cloud platforms** for enterprise clients across Sweden, Australia, India, and the UK. Long-running consulting background — Capgemini, Tech Mahindra, AFRY, ICF Next — placed on assignments at Volvo Cars, Ericsson, Cisco, Deutsche Telekom, Stena Metall, and Channel 7, owning the platform end of each engagement from day one. Specialise in CI/CD pipeline design and migration (Jenkins, GitHub Actions, Azure DevOps, GitLab CI, Gerrit), Terraform across AzureRM / AWS / OpenStack, and Ansible for everything-as-code. Comfortable as the senior platform voice in cross-functional teams. Stockholm-based, fluent in English, Swedish at SFI C-level.

---

## Core Skills

**CI/CD Pipeline Design & Modernisation** — Jenkins (declarative + scripted, EKS-hosted, on-prem), GitHub Actions, Azure DevOps Pipelines, GitLab CI, Gerrit. Migrated and modernised pipelines for Cisco (on-prem OpenShift → AWS EKS), Deutsche Telekom (~46 Jenkins jobs for ~30 microservices on OpenStack), Volvo Cars (PR-driven Terraform via GitHub Actions), Ericsson (Git/Gerrit/Jenkins for radio-comm CI).

**Infrastructure as Code** — Terraform (AzureRM, AWS, OpenStack, Databricks providers), reusable module libraries, ARM, **Ansible roles** (AEM, ELK, BSS microservice config, base OS), archetype-driven Azure CAF Enterprise Scale.

**.NET / C# Pipeline Experience** — Azure DevOps pipelines for .NET microservices (Greenstone Insurance Portal); PowerShell tooling for App Service .NET runtime audits across an Azure CAF estate (Stena Metall); Docker Swarm + ACR for C# workloads.

**Cloud Platforms** — Microsoft Azure (primary, CAF Enterprise Scale, ~100-subscription estate), AWS (EC2, S3, VPC, EKS, IAM, ECR, ALB, CloudWatch, KMS), OpenStack, hybrid / on-prem.

**Containers & Orchestration** — Kubernetes (Rancher RKE, K3s, EKS, AKS), Docker, Helm, Kubeflow, ArgoCD.

**Scripting** — Python (REST/SCM automation, CLI tooling), Bash, PowerShell.

**Source Control & Code Review** — Git, Gerrit, GitHub, GitLab, Bitbucket, Crucible; branching strategy design, large-scale repo migrations.

**Observability** — Prometheus, Grafana, Azure Monitor, Log Analytics / KQL, ELK Stack, CloudWatch.

**Ways of Working** — Consulting / assignment-based delivery, Agile / SAFe, cross-team platform enablement, technical documentation, mentoring.

**Languages** — English (fluent), Swedish (SFI C-level).

---

## Professional Experience

### DevOps Engineer — AFRY Digital Solutions AB
*May 2025 – Present  |  Stockholm, Sweden*

**Assignment: Ericsson AB — CI Engineer, Tiger Test Tools (Sep 2025 – Present)**
- Maintain and support the end-to-end **CI flow for radio-communication smoke and regression testing** — Git, Gerrit, Jenkins, Docker, Linux.
- Troubleshoot pipeline, hardware, and test-server issues across daily delivery and validation workflows; close the loop between pipeline failures and physical lab state.

**Platform engineering (internal reference project)**
- Designed and deployed a **GitOps-based Kubernetes platform** (K3s + ArgoCD + Prometheus + Grafana + cert-manager + sealed-secrets) as a cloud-native delivery reference — maintained as a live public demo on GitHub.

---

### Cloud Engineer — Stena Metall AB
*Aug 2024 – Jan 2025  |  Gothenburg, Sweden*

Cloud Infrastructure Engineer on the central Cloud Office (Governance) of a mature **Azure CAF Enterprise Scale** estate — ~100 subscriptions, multi-management-group hierarchy, production workloads for a multi-billion-SEK industrial group.

- **Authored two custom Azure RBAC role definitions** (a "Backup Remover" role and a Contributor variant with explicit `notActions`) to enforce separation-of-duties between resource management and backup deletion. Wired into the CAF archetype framework and deployed via the existing **Terraform + Azure DevOps pipeline**.
- Delivered a **tenant-wide Key Vault compliance audit** — KQL against Azure Resource Graph for soft-delete, purge protection, and RBAC.
- Built **Service Principal lifecycle tooling** (KQL audit + PowerShell expiring-credential inventory + Logic Apps/Graph rotation design).
- Contributed PowerShell tooling: subscription budget automation, ACR token expiry inventory, **.NET runtime enumeration across App Services**, Hybrid Benefit enablement.
- KQL-based monitoring contributed to a **~20% reduction in downtime** across supported services.

---

### Senior Software Engineer (DevOps) — Capgemini Sverige AB
*Sep 2021 – Jul 2024  |  Gothenburg, Sweden*

**Assignment: Volvo Cars — Car Safety R&D (MLOps / AI Platform)**

*Self-service Databricks platform via GitOps — CI/CD-driven infrastructure*
- Designed and owned a **GitOps self-service pattern for Azure Databricks**: data scientists request compute via a GitHub issue → YAML manifest PR → **GitHub Actions runs `terraform fmt/validate/plan`** → merge triggers `terraform apply`.
- Authored the **Terraform module** with governance-friendly defaults (single-user mode, 30-min auto-termination, autoscale 1→3, cluster-log shipping, `CAN_RESTART` permissions).
- Two-workflow contract (`tf-validate` on PR, `tf-deploy` on merge) with remote state in Azure Blob and backend config injected from GitHub environment secrets.
- **Outcome:** provisioning lead time fell from days to same-day; every cluster traceable to a PR, manifest, and named owner; idle-cluster spend eliminated.

*HPC platform modernisation (on-prem → Kubernetes)*
- Contributed to modernising a ~36-node CAE/HPC cluster: OS migration SLES → Ubuntu LTS; stand-up of **Rancher-managed Kubernetes (RKE)**; **Kubeflow** via Helm.
- Built a **production-grade ELK stack** (Elasticsearch, Logstash, Kibana) on LXD with X-Pack, SSL, and snapshot repositories.
- Authored **Ansible roles** within the shared GitLab-managed codebase.

*Dual-cloud ML benchmarking*
- Built **two matched Terraform stacks** (AWS: EC2 + S3 + KMS + IAM | Azure: VM + Premium Blob) as identically-shaped, disposable test rigs for object-storage benchmarking.

---

### Senior Business Consultant (DevOps) — Tech Mahindra
*Feb 2017 – Sep 2021  |  Bangalore, India  |  Sydney, Australia*

**Assignment: Cisco Systems — CD 2.0 on AWS (Continuous-Delivery Platform Migration)**
- **Authored the Terraform** for Cisco's CD 2.0 continuous-delivery platform on AWS — VPC, subnets, security groups, **EKS cluster, IAM roles, Jenkins on EKS, ECR integration, build-agent fleet, ALB, DNS** — extending an internal reference architecture originally built on on-prem OpenShift.
- Wrote a separate **Terraform stack for an AWS observability environment** (EKS + Prometheus Operator via Helm + Grafana + persistent storage + ingress).
- **Closed out Cisco's long-running SVN-to-Git migration**: Python automation enumerated SVN repos, extracted history, provisioned Bitbucket repos via REST, pushed converted Git history, and produced CSV reports — with retry logic and batching for SCM rate limits.
- Onboarded application teams to CD 2.0 via **CI engagement templates**, Bitbucket/Crucible provisioning, and Jenkinsfile adaptation.

**Assignment: Deutsche Telekom — 5G BSS Slicing Pilot on OpenStack**
- Owned the **DevOps platform side** of DT's 5G Network Slicing commercial pilot on **PAN-NET (OpenStack)**, delivering Blue Marble's ~30-microservice BSS suite plus the Phenom UI.
- **Terraform against the OpenStack provider** — networks, subnets, security groups, VMs, floating IPs — provisioning the **Jenkins / Nexus / Tuleap / Rancher / Keycloak / ELK** estate.
- **Ansible playbooks** for all service configuration; custom Dockerfile for Sonatype Nexus 3 with SSL.
- Designed and ran **~46 Jenkins jobs** building BMP microservices, tagging build number + short git SHA, pushing to Nexus, updating Kubernetes manifests, and triggering Rancher rolling updates.
- Owned a **cross-tenant migration** when the pilot moved PAN-NET tenants: Python/shell automation cloned 54 Tuleap repositories, re-seeded Jenkins jobs, and rehomed Nexus, Keycloak, and live Kubernetes workloads — completed over a weekend, nothing rebuilt from scratch.

**Assignment: Greenstone Financial Services — Insurance Portal**
- Led DevOps transformation for **.NET / C# microservices**: Azure DevOps pipelines, **Terraform for Azure infrastructure**, **Docker + Docker Swarm with Azure Container Registry**, Azure Monitor for observability.

**Assignment: CA ANZ**
- Architected the **GitLab-based CI and source-control model** — branching strategy, repository standards, pipeline conventions; supported team adoption through documentation and knowledge transfer.

---

### Senior AEM Administrator (Cloud) — ICF Next
*Sep 2015 – Jan 2017  |  Bangalore, India*

**Assignment: Channel 7 (Australia) — AEM on AWS**
- Built and operated a production AEM platform on AWS for a national Australian broadcaster — VPC, EC2 lifecycle, Apache HTTPD + Dispatcher hardening, SSL termination, **SAML 2.0 federation** (Azure AD / ADFS → AWS IAM) replacing long-lived IAM keys.
- Evolved architecture from Phase-1 to Phase-2 (Dispatcher co-located on Gold Publisher; Publish tier in Auto Scaling Group).
- Authored **Ansible roles** for AEM install, Apache/Dispatcher deployment, SSL, and base OS — turning instance rebuilds into a runbook rather than a discovery exercise.

---

### Unix / Linux Systems Administrator — HP Enterprise Services
*Nov 2011 – Aug 2015  |  Bangalore, India*

Three-and-a-half years on HP's Global Operations Center under Best Shore Services, rotating across enterprise outsourcing customers (HUL, E.ON, Con-way Inc.) — 24×7 incident handling, LVM/SAN, kernel tuning, SOP authorship, HP Service Manager / OpenView / Server Automation.

---

## Education

**B.Tech in Computer Science** — West Bengal University of Technology, Kolkata, India (2005 – 2009)

---

## Certifications

- **Microsoft Certified: Azure Fundamentals (AZ-900)** — Mar 2023 *(Credential ID: 801D970BAA49297)*
- **AWS Certified Solutions Architect – Associate (SAA-C03)** — *in progress*
