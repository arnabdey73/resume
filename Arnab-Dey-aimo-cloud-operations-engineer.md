<div align="center">
	<h1><b>Arnab Dey</b></h1>
	<p>
		Stockholm, Sweden | +46 0764516092 | <a href="mailto:arnabdey009@gmail.com">arnabdey009@gmail.com</a><br>
		<a href="https://www.linkedin.com/in/arnabdey73">LinkedIn</a> | <a href="https://github.com/arnabdey73">GitHub</a>
	</p>
</div>

---

## Professional Summary

Cloud Operations Engineer with deep hands-on experience keeping production AWS and Kubernetes environments stable, secure, and improving over time. My background combines modern cloud operations — Terraform, EKS, CI/CD pipelines, structured observability — with a grounding in 24×7 Linux systems administration that shaped how I approach incident management and operational discipline. I care about the unglamorous work that makes platforms sustainable: clear runbooks, meaningful alerting, documented procedures, and the steady improvement of infrastructure that production depends on. Comfortable supporting development teams as a platform partner rather than a gatekeeper.

---

## Core Skills

**Cloud Operations** — AWS (EC2, EKS, S3, VPC, IAM, ECR, ALB, CloudWatch, KMS); production environment maintenance, cost optimisation, security hardening, incident response

**Kubernetes in Production** — EKS, K3s, AKS, Rancher RKE; Helm, workload management, rolling updates, troubleshooting

**CI/CD** — GitLab CI, GitHub Actions, Jenkins, ArgoCD, Azure DevOps Pipelines

**Infrastructure as Code** — Terraform (AWS, Azure, OpenStack providers), reusable modules, Ansible

**Monitoring & Observability** — Prometheus, Grafana, ELK Stack (Elasticsearch, Logstash, Kibana), CloudWatch, Azure Monitor / Log Analytics; alerting design, log aggregation, dashboards

**Incident & Operational Excellence** — 24×7 shift-based incident handling, runbook authoring, procedure library development, structured operational improvement

**Scripting & Automation** — Python, Bash, PowerShell

**Security & Governance** — IAM least-privilege, RBAC, secret management (Key Vault, KMS, sealed-secrets), credential rotation, compliance auditing

**Source Control** — Git, GitLab, GitHub, Gerrit, Bitbucket

**Languages** — English (fluent), Swedish (SFI C-level)

---

## Professional Experience

### DevOps Engineer — AFRY Digital Solutions AB
*May 2025 – Present  |  Stockholm, Sweden*

**Assignment: Ericsson AB — CI Engineer (Sep 2025 – Present)**
- Maintain and support end-to-end CI for radio-communication smoke and regression testing — Git, Gerrit, Jenkins, Docker, Linux.
- Troubleshoot cross-cutting pipeline and hardware issues across daily delivery and validation workflows.
- Operational support for radio-communication hardware and test servers.

**GitOps Platform (internal reference project)**
- Designed and deployed a GitOps-based Kubernetes platform (K3s + ArgoCD + Prometheus + Grafana + cert-manager + sealed-secrets) as a live cloud-native operations reference — publicly maintained on GitHub.

---

### Cloud Engineer — Stena Metall AB
*Aug 2024 – Jan 2025  |  Gothenburg, Sweden*

Operations, security, and governance engineering on a production Azure estate — ~100 subscriptions across a multi-management-group hierarchy supporting a multi-billion-SEK industrial group.

- Delivered a **tenant-wide Key Vault compliance audit** — KQL against Azure Resource Graph for soft-delete retention, purge protection, and RBAC authorisation — producing remediation inventory for architecture leadership.
- **Service Principal lifecycle tooling** — expiring-credential inventory, KQL audit, and automated rotation design via Logic Apps + Graph API.
- Implemented **Azure Backup policy compliance reporting** with per-resource exempt-rationale tracking.
- **Subscription budget automation and cost-allocation tagging** — enforcing financial governance at scale.
- KQL-based monitoring contributed to a **~20% reduction in downtime** across supported services.

---

### Senior Software Engineer (DevOps) — Capgemini Sverige AB
*Sep 2021 – Jul 2024  |  Gothenburg, Sweden*

**Assignment: Volvo Cars — Car Safety R&D, MLOps / AI Platform**

- Designed and owned a **GitOps self-service workflow for Azure Databricks**: GitHub Actions CI/CD runs `terraform plan` on PR → merge triggers `terraform apply`. Every resource traceable to a PR; provisioning dropped from days to same-day.
- Contributed to modernising a ~36-node HPC cluster: OS migration (SLES → Ubuntu LTS), **Rancher-managed Kubernetes (RKE)** with worker fleet, Kubeflow via Helm.
- Built a **production ELK Stack** (Elasticsearch, Logstash, Kibana) with X-Pack security, SSL, and snapshot repositories — full-fleet observability for ML workload monitoring and log aggregation.
- Authored Ansible roles within the shared **GitLab-managed codebase**.
- Built matched **Terraform stacks on AWS** (EC2 + S3 + KMS + IAM) and Azure as disposable, identically-shaped test rigs for ML storage benchmarks.

---

### Senior Business Consultant (DevOps) — Tech Mahindra
*Feb 2017 – Sep 2021 | Bangalore, India | Sydney, Australia*

**Assignment: Cisco Systems — CD 2.0 on AWS** *(Technical Lead from mid-2019)*
- Led the project from mid-2019 — full technical ownership of the AWS delivery platform.
- Authored Terraform for the CD 2.0 continuous-delivery platform on AWS: VPC, subnets, security groups, EKS cluster, IAM roles, Jenkins on EKS, ECR, build-agent fleet, ALB, DNS.
- Built a separate **AWS observability environment**: EKS, Prometheus Operator via Helm, Grafana, persistent storage, ingress.
- Onboarded application teams to the platform — CI engagement templates, Jenkinsfile adaptation, team support.

**Assignment: Deutsche Telekom — 5G BSS Slicing Pilot on OpenStack** *(Technical Lead, mid-2020 – Aug 2021)*
- Took over technical leadership of the DevOps platform for DT's 5G Network Slicing commercial pilot — accountable for operational reliability of a ~30-microservice BSS suite on OpenStack.
- **Built and operated** the Jenkins / Nexus / Tuleap / Rancher / Keycloak / ELK estate — Terraform for provisioning, Ansible for configuration, ~46 Jenkins jobs driving rolling deployments.
- Delivered a cross-tenant migration over a single weekend — 54 repositories, Jenkins jobs, Nexus artifacts, Keycloak realm, and running Kubernetes workloads migrated with zero rebuilds.
- Built a **Logstash pipeline** ingesting 5G Usage Data Record CSV feeds into Elasticsearch for a high-volume billing emulator.

**Assignment: CA ANZ** *(Technical Lead, late 2019)*
- Led the GitLab-based CI and source-control strategy — defined branching model, repository standards, and pipeline conventions.

**Assignment: Greenstone Financial Services — Insurance Portal** *(Technical Lead, late 2019)*
- Led end-to-end DevOps delivery for a regulated financial services platform: Azure DevOps pipelines, Terraform for Azure, Docker + Docker Swarm, Azure Monitor.

---

### Senior AEM Administrator (Cloud) — ICF Next
*Sep 2015 – Jan 2017  |  Bangalore, India*

**Assignment: Channel 7 (Australia) — AEM on AWS**
Operated a **high-availability public-facing platform** on AWS for a national broadcaster.

- VPC design, EC2 lifecycle, Apache HTTPD + Dispatcher hardening, SSL termination, SAML 2.0 federation (Azure AD → AWS IAM).
- Evolved the architecture from separate Dispatcher VMs to Publish tier in an Auto Scaling Group.
- Authored Ansible roles for AEM install, Apache/Dispatcher deployment, and system baseline — making instance rebuilds repeatable and auditable.

---

### Unix / Linux Systems Administrator — HP Enterprise Services
*Nov 2011 – Aug 2015  |  Bangalore, India*

Three and a half years on HP's Global Operations Center (Unix Service Delivery Unit) running **24×7 shift-based operations** across three large enterprise outsourcing customers — directly foundational to how I approach operations today.

- **HUL** (~18 months, L1/L2) — 24×7 incident handling on a SAP-heavy Linux/Unix estate of 140+ servers.
- **E.ON** (~12 months, L2/L3) — multi-site German/UK operations; storage, DNS, console management.
- **Con-way Inc.** (~13 months, L2/L3) — **authored a significant portion of the BSS-ITO Con-way Linux procedure library**: LVM filesystem resizes, Veritas SAN migration, kernel-parameter tuning, ITO/OpsBridge agent management. Procedures adopted as team reference material.

---

## Education

**B.Tech in Computer Science** — West Bengal University of Technology, Kolkata, India (2005 – 2009)

---

## Certifications

- **Microsoft Certified: Azure Fundamentals (AZ-900)** — Mar 2023
- **AWS Certified Solutions Architect - Associate (SAA-C03)** — *in progress*
