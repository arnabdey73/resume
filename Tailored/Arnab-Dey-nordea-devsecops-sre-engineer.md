<div align="center">
	<h1><b>Arnab Dey</b></h1>
	<p>
		Stockholm, Sweden | +46 0764516092 | <a href="mailto:arnabdey009@gmail.com">arnabdey009@gmail.com</a><br>
		<a href="https://www.linkedin.com/in/arnabdey73">LinkedIn</a> | <a href="https://github.com/arnabdey73">GitHub</a>
	</p>
</div>

---

## Professional Summary

DevOps Engineer with deep hands-on experience building and operating infrastructure across on-premise and cloud platforms. I design and automate infrastructure with Terraform, manage Kubernetes clusters at scale, and build observability stacks — Prometheus, Grafana, ELK — that make systems reliable and incident response fast. I bring a security-first mindset shaped by work in regulated and governance-heavy environments: custom RBAC controls, audit-trail automation, credential lifecycle management, and compliance reporting embedded into delivery workflows. Experienced in large enterprise programmes — financial services, telecommunications, automotive — where auditability, separation-of-duties, and cross-country stakeholder collaboration are not optional. Ready to take on SRE ownership including on-call responsibilities.

---

## Core Skills

**Kubernetes & Orchestration** — EKS, K3s, AKS, Rancher RKE; Helm, workload management, GitOps with ArgoCD; Kafka and Zookeeper deployed via Helm charts with queue configuration

**Observability & SRE** — Prometheus, Grafana, ELK Stack (Elasticsearch, Logstash, Kibana), CloudWatch, Azure Monitor / Log Analytics (KQL); alerting design, incident response, 24×7 operations

**Infrastructure as Code** — Terraform (AWS, Azure, OpenStack providers), Terraform Enterprise patterns, reusable module libraries, Ansible

**CI/CD & Automation** — Jenkins, GitHub Actions, GitLab CI, ArgoCD, Azure DevOps Pipelines; pipeline design, build automation, trunk-based and GitFlow workflows

**Cloud & On-Premise** — AWS (EC2, EKS, S3, VPC, IAM, ECR, ALB, CloudWatch, KMS), Azure, OpenStack (PAN-NET), on-premise Linux/HPC

**Security & Compliance** — IAM, custom RBAC role definitions, least-privilege patterns, secret management (Key Vault, sealed-secrets, KMS), credential rotation design, SAML 2.0 federation, compliance auditing (KQL / Azure Resource Graph), separation-of-duties controls

**Scripting & Automation** — Python, Bash, PowerShell

**Source Control** — Git, Gerrit, GitHub, GitLab, Bitbucket; branching strategies, migration at scale

**Languages** — English (fluent), Swedish (SFI C-level)

---

## Professional Experience

### DevOps Engineer — AFRY Digital Solutions AB
*May 2025 – Present  |  Stockholm, Sweden*

**Assignment: Ericsson AB — CI Engineer (Sep 2025 – Present)**
- Maintain and support end-to-end CI for radio-communication smoke and regression testing — Git, Gerrit, Jenkins, Docker, Linux.
- Troubleshoot cross-cutting pipeline and hardware issues across daily delivery and validation workflows.

**GitOps Platform (internal reference project)**
- Designed and deployed a GitOps-based Kubernetes platform (K3s + ArgoCD + Prometheus + Grafana + cert-manager + sealed-secrets) as a cloud-native reference — maintained as a live public demo on GitHub.

---

### Cloud Engineer — Stena Metall AB
*Aug 2024 – Jan 2025  |  Gothenburg, Sweden*

Security and compliance engineering on a production Azure estate — ~100 subscriptions across a multi-management-group hierarchy supporting a multi-billion-SEK industrial group.

- **Authored two custom Azure RBAC role definitions** (a "Backup Remover" role and a modified Contributor with explicit `notActions`) to enforce separation-of-duties between resource management and backup deletion — a ransomware-resilience control, deployed via Terraform + Azure DevOps pipeline.
- Delivered a **tenant-wide Key Vault compliance audit** — KQL against Azure Resource Graph for soft-delete retention, purge protection, and RBAC authorisation — producing CSV inventories and a remediation review for architecture leadership.
- Built **Service Principal lifecycle tooling**: KQL audit for 30-day credential events, PowerShell expiring-credential inventory, and a design for automated client-secret rotation via Logic Apps + Graph API `addPassword`.
- Implemented **Azure Backup policy compliance reporting** with per-resource exempt-rationale tracking.
- KQL-based monitoring contributed to a **~20% reduction in downtime** across supported services.

---

### Senior Software Engineer (DevOps) — Capgemini Sverige AB
*Sep 2021 – Jul 2024  |  Gothenburg, Sweden*

**Assignment: Volvo Cars — Car Safety R&D, MLOps / AI Platform**

- Designed and owned a **GitOps self-service workflow for Azure Databricks**: compute requests go from a GitHub issue → YAML manifest PR → GitHub Actions `terraform plan` for review → merge triggers `terraform apply`. Outcome: provisioning lead time dropped from days to same-day; eliminated idle-cluster spend.
- Contributed to modernising a ~36-node HPC/ML cluster: OS migration, **Rancher-managed Kubernetes (RKE)** with worker fleet, **Kubeflow** via Helm for ML engineers.
- Built a **production ELK Stack** (Elasticsearch, Logstash, Kibana) with X-Pack security, SSL, and snapshot repositories for cluster observability and log aggregation.
- Authored Ansible roles within the shared GitLab-managed codebase.
- Built matched **Terraform stacks on AWS** (EC2 + S3 + KMS + IAM) and Azure as disposable, identically-shaped test rigs for ML object-storage benchmarks.

---

### Senior Business Consultant (DevOps) — Tech Mahindra
*Feb 2017 – Sep 2021 | Bangalore, India | Sydney, Australia*

**Assignment: Cisco Systems — CD 2.0 on AWS**
- Authored **Terraform** for Cisco's continuous-delivery platform on AWS: VPC, subnets, security groups, EKS cluster, IAM roles, Jenkins on EKS, ECR, build-agent fleet, ALB, DNS.
- Deployed **Kafka and Zookeeper via Helm charts** on the EKS cluster and configured message queues for asynchronous inter-service communication across the CD 2.0 platform.
- Built a separate **Terraform stack for an AWS observability environment**: EKS, Prometheus Operator via Helm, Grafana, persistent storage, ingress.
- Automated Cisco's SVN-to-Git migration with **Python**: enumerated repositories, provisioned Bitbucket repos via REST API, migrated history, produced CSV audit reports — with retry logic and rate-limit handling.
- Onboarded application teams to the CI/CD platform via CI engagement templates and Jenkinsfile adaptation.

**Assignment: Deutsche Telekom — 5G BSS Slicing Pilot on OpenStack**
- Owned the **DevOps platform** for DT's 5G Network Slicing commercial pilot on **PAN-NET (OpenStack)** — a large on-premise cloud estate — delivering ~30-microservice BSS suite plus Phenom UI.
- Wrote **Terraform against the OpenStack provider** — networks, subnets, security groups, VMs, floating IPs — provisioning the Jenkins / Nexus / Tuleap / Rancher / Keycloak / ELK estate.
- Deployed **Kafka and Zookeeper via Helm charts** on the Kubernetes cluster and configured message queues to support the 5G BSS event-streaming and billing pipeline.
- Designed and maintained **~46 Jenkins jobs** building microservices, tagging with build number + short git SHA, pushing to Nexus registry, and triggering Rancher rolling updates.
- Built a **Logstash pipeline** ingesting 5G Usage Data Record (UDR) CSV feeds into Elasticsearch for a high-volume billing emulator — structured ingestion, field mapping, index management.
- Automated a **cross-tenant migration** over a weekend: Python/shell scripted the cloning of 54 repositories, re-seeding of Jenkins jobs, and rehoming of Nexus artifacts, Keycloak realm, and running Kubernetes workloads — cutover completed with nothing rebuilt from scratch.
- **Ansible playbooks** for all service configuration; custom Dockerfile for Sonatype Nexus 3 with SSL.

**Assignment: Greenstone Financial Services — Insurance Portal**
- Led DevOps transformation for .NET microservices: Azure DevOps pipelines, Terraform for Azure infrastructure, Docker + Docker Swarm with ACR, Azure Monitor for observability.

---

### Senior AEM Administrator (Cloud) — ICF Next
*Sep 2015 – Jan 2017  |  Bangalore, India*

**Assignment: Channel 7 (Australia) — AEM on AWS**
- Built and operated a production AWS platform: VPC design, EC2 lifecycle, Auto Scaling Group, Apache HTTPD + Dispatcher hardening, SSL termination, and **SAML 2.0 federation** (Azure AD → AWS IAM) replacing long-lived IAM user keys.
- Authored Ansible roles for deployment and system baseline — making instance rebuilds repeatable and auditable.

---

### Unix / Linux Systems Administrator — HP Enterprise Services
*Nov 2011 – Aug 2015  |  Bangalore, India*

L2/L3 systems administration across large outsourcing customers (HUL, E.ON, Con-way Inc.) on Linux/Unix estates — **24×7 shift-based incident handling**, storage management, DNS, console management, and authored a significant portion of the Con-way Linux procedure library (LVM, SAN migration, kernel tuning, ITO/OpsBridge agent management).

---

## Education

**B.Tech in Computer Science** — West Bengal University of Technology, Kolkata, India (2005 – 2009)

---

## Certifications

- **Microsoft Certified: Azure Fundamentals (AZ-900)** — Mar 2023
- **AWS Certified Solutions Architect - Associate (SAA-C03)** — *in progress*
