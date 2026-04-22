<div align="center">
	<h1><b>Arnab Dey</b></h1>
	<p>
		Stockholm, Sweden | +46 0764516092 | <a href="mailto:arnabdey009@gmail.com">arnabdey009@gmail.com</a><br>
		<a href="https://www.linkedin.com/in/arnabdey73">LinkedIn</a> | <a href="https://github.com/arnabdey73">GitHub</a>
	</p>
</div>

---

## Professional Summary

Infrastructure and Platform Engineer with deep AWS expertise and a consistent track record of end-to-end platform ownership in complex, high-impact environments. I've led platform initiatives across large enterprise and scale-up contexts — accountable for availability, security, cost, and developer enablement — while staying hands-on in critical infrastructure decisions and code. I design and automate with Terraform, operate Kubernetes at scale, build CI/CD pipelines that development teams actually trust, and set up observability stacks that make incidents short and post-mortems useful. I communicate clearly with engineering, product, and security stakeholders, and bring both technical depth and the cross-functional perspective needed to contribute to tech strategy at a senior level.

---

## Core Skills

**AWS** — EC2, EKS, S3, VPC, IAM, ECR, ALB, CloudWatch, KMS, RDS; production operations, cost optimisation, security hardening

**Infrastructure as Code** — Terraform (AWS, Azure, OpenStack providers), reusable module libraries, Ansible

**Containers & Orchestration** — Kubernetes (EKS, K3s, AKS, Rancher RKE), Docker, Helm

**CI/CD & DevOps Enablement** — GitHub Actions, Jenkins, GitLab CI, ArgoCD, Azure DevOps Pipelines; platform tooling for development teams

**Observability & Incident Management** — Prometheus, Grafana, ELK Stack, CloudWatch, Azure Monitor; alerting design, on-call, 24×7 operations

**Security & Cost Governance** — IAM least-privilege, RBAC, secret management (Key Vault, KMS, sealed-secrets), credential rotation, compliance auditing, budget automation, cost-allocation tagging

**Scripting & Automation** — Python, Bash, PowerShell

**Leadership & Collaboration** — Platform strategy, cross-functional stakeholder alignment, technical mentoring, documentation, agile delivery

**Languages** — English (fluent), Swedish (SFI C-level)

---

## Professional Experience

### DevOps Engineer — AFRY Digital Solutions AB
*May 2025 – Present  |  Stockholm, Sweden*

**Assignment: Ericsson AB — CI Engineer (Sep 2025 – Present)**
- Maintain and support end-to-end CI for radio-communication smoke and regression testing — Git, Gerrit, Jenkins, Docker, Linux.
- Troubleshoot cross-cutting pipeline and hardware issues across daily delivery and validation workflows.

**GitOps Platform (internal reference project)**
- Designed and deployed a GitOps-based Kubernetes platform (K3s + ArgoCD + Prometheus + Grafana + cert-manager + sealed-secrets) as a live cloud-native reference — publicly maintained on GitHub.

**AI-powered Resume Builder Agent** *(Led since inception)*
- Conceived and led development of an LLM-backed agent that automates resume tailoring — prompt engineering, document parsing, and structured output generation. Drove the project from idea to working public release. <a href="https://github.com/arnabdey73/resume-builder-agent">Public repo</a>.

---

### Cloud Engineer — Stena Metall AB
*Aug 2024 – Jan 2025  |  Gothenburg, Sweden*

End-to-end infrastructure and governance ownership on a production Azure estate — ~100 subscriptions across a multi-management-group hierarchy supporting a multi-billion-SEK industrial group.

- **Custom RBAC role definitions** deployed via Terraform + Azure DevOps to enforce separation-of-duties and ransomware resilience — a security gap in the platform's existing design.
- **Key Vault compliance audit** across the full tenant — soft-delete retention, purge protection, RBAC authorisation — producing remediation plans for architecture leadership.
- **Service Principal credential lifecycle tooling** — automated expiry inventory and client-secret rotation design via Logic Apps + Graph API.
- **Subscription budget automation and cost-allocation tagging** — PowerShell tooling to enforce financial governance at scale.
- KQL-based monitoring contributed to a **~20% reduction in downtime** across supported services.

---

### Senior Software Engineer (DevOps) — Capgemini Sverige AB
*Sep 2021 – Jul 2024  |  Gothenburg, Sweden*

**Assignment: Volvo Cars — Car Safety R&D, MLOps / AI Platform**

Platform ownership for a cross-functional AI/ML engineering programme — accountable for infrastructure design, developer enablement, and delivery reliability.

- Designed and owned a **GitOps self-service platform for Azure Databricks** — GitHub Actions CI/CD, Terraform modules with governance defaults, remote state management, secret injection from environment secrets. Outcome: provisioning dropped from days to same-day; every resource traceable to a PR and a named owner; idle-cluster spend eliminated.
- Led modernisation of a ~36-node HPC/ML cluster: OS migration (SLES → Ubuntu LTS), **Rancher-managed Kubernetes (RKE)** with worker fleet, Kubeflow via Helm for ML engineers.
- Built a **production ELK Stack** with X-Pack security, SSL, and snapshot repositories for full-fleet observability.
- Built matched **Terraform stacks on AWS** (EC2 + S3 + KMS + IAM) and Azure as disposable, identically-shaped test rigs for ML storage benchmarks.
- Authored Ansible roles and contributed to the shared GitLab-managed codebase.

---

### Senior Business Consultant (DevOps) — Tech Mahindra
*Feb 2017 – Sep 2021 | Bangalore, India | Sydney, Australia*

**Assignment: Cisco Systems — CD 2.0 on AWS** *(Technical Lead from mid-2019)*
- **Led the project from mid-2019**, taking full technical ownership of the AWS delivery platform — accountable for architecture decisions, delivery timeline, and team onboarding.
- **Sole author of the Terraform** for Cisco's continuous-delivery platform on AWS — VPC, subnets, security groups, EKS cluster, IAM roles, Jenkins on EKS, ECR, build-agent fleet, ALB, DNS.
- Built a separate **AWS observability environment**: EKS, Prometheus Operator via Helm, Grafana, persistent storage, ingress.
- Onboarded multiple application teams to the platform via CI templates and Jenkinsfile adaptation.
- Automated Cisco's SVN-to-Git migration with Python: REST API-driven provisioning, history migration, CSV audit reports — eliminating months of manual effort.

**Assignment: Deutsche Telekom — 5G BSS Slicing Pilot on OpenStack** *(Technical Lead, mid-2020 – August 2021)*
- **Took over technical leadership from mid-2020** of the DevOps platform for DT's 5G Network Slicing commercial pilot — accountable for infrastructure, CI/CD, and delivery reliability across the full programme for a ~30-microservice BSS suite on OpenStack (on-premise).
- Terraform for all networking and compute; Ansible for service configuration; ~46 Jenkins jobs; Rancher-managed Kubernetes rolling deployments.
- Delivered a cross-tenant platform migration over a single weekend — 54 repositories, Jenkins jobs, Nexus artifacts, Keycloak realm, and running Kubernetes workloads migrated with zero rebuilds.

**Assignment: Greenstone Financial Services — Insurance Portal** *(Technical Lead, late 2019)*
- **Led end-to-end DevOps delivery** for a regulated financial services platform: Azure DevOps pipelines, Terraform for Azure, Docker + Docker Swarm, Azure Monitor.

**Assignment: CA ANZ** *(Technical Lead, late 2019)*
- **Led the GitLab-based CI and source-control strategy** — defined branching model, repository standards, and pipeline conventions; drove team adoption through documentation and knowledge transfer.

---

### Senior AEM Administrator (Cloud) — ICF Next
*Sep 2015 – Jan 2017  |  Gothenburg / Remote*

**Assignment: Channel 7 (Australia) — AEM on AWS**
- Built and operated a production AWS platform: VPC, EC2, Auto Scaling Group, Apache HTTPD hardening, SSL termination, SAML 2.0 federation (Azure AD → AWS IAM) replacing long-lived IAM keys.
- Authored Ansible roles for repeatable, auditable deployments.

---

### Unix / Linux Systems Administrator — HP Enterprise Services
*Nov 2011 – Aug 2015  |  India*

L2/L3 operations across three large enterprise outsourcing customers — 24×7 incident handling, storage management, DNS, physical and virtual server management across HUL (140+ servers), E.ON (multi-site UK/Germany), and Con-way Inc. Authored a substantial portion of the Con-way Linux procedure library: LVM, SAN migration, kernel tuning, OpsBridge agent management.

---

## Education

**B.Tech in Computer Science** — West Bengal University of Technology, Kolkata, India (2005 – 2009)

---

## Certifications

- **Microsoft Certified: Azure Fundamentals (AZ-900)** — Mar 2023
- **AWS Certified Solutions Architect - Associate (SAA-C03)** — *in progress*
