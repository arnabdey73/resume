<div align="center">
	<h1><b>Arnab Dey</b></h1>
	<p>
		Cloud Infrastructure Engineer — AWS · Kubernetes · Terraform · Observability · Open Source<br>
		Stockholm, Sweden (EU timezone, CET+1) | +46 76 451 60 92 | <a href="mailto:arnabdey009@gmail.com">arnabdey009@gmail.com</a><br>
		<a href="https://www.linkedin.com/in/arnabdey73">LinkedIn</a> | <a href="https://github.com/arnabdey73">GitHub</a> | <a href="https://arnabdey.dev">arnabdey.dev</a><br>
		<i>Available for remote-first work across EU timezones; comfortable with monthly Berlin onsite.</i>
	</p>
</div>

---

## Professional Summary

Cloud Infrastructure Engineer with **15+ years in IT** and **9+ years building and operating production systems** across AWS, Azure, OpenStack, and on-prem Kubernetes. I treat infrastructure as a product: opinionated modules with sensible defaults, GitOps where it makes sense, observability that catches problems before users do, and self-hostable patterns that work on more than just the author's machine. Maintain a live public **K3s + ArgoCD + Prometheus + Grafana + cert-manager + sealed-secrets** GitOps reference platform on GitHub — a single-node, self-hostable demonstration of the same patterns I bring to enterprise work. Recent production work spans a **GitOps self-service compute platform at Volvo Cars** (~30-min mean time to provision down from days), a **Terraform-managed AWS continuous-delivery platform at Cisco** (EKS + Jenkins + IAM + ECR + ALB), and a **5G BSS billing pipeline at Deutsche Telekom** ingesting UDR event feeds into Elasticsearch through Logstash.

---

## Core Skills

**AWS** — VPC, EC2, S3, **EKS** (Kubernetes), IAM, ECR, ALB, KMS, CloudWatch, Route53, Auto Scaling Groups; Terraform AWS provider for full-stack provisioning of CD platforms, observability stacks (Prometheus Operator + Grafana on EKS), and benchmarking rigs. **ECS/Fargate is adjacent** — same EKS-style operational mental model; comfortable picking up.

**Kubernetes & containers** — **EKS, AKS, Rancher RKE, K3s** (production); Helm charts (authored and operated), Docker, containerd, Kubeflow, **ArgoCD**, ingress controllers, persistent storage, rolling updates against live workloads, sealed-secrets, cert-manager.

**Infrastructure as Code** — Terraform (AWS, AzureRM, OpenStack, Databricks providers); reusable module libraries with opinionated, sensible defaults; remote state in Azure Blob / S3 with backend config injected from CI environment secrets; two-workflow `validate-on-PR` / `apply-on-merge` contract; module versioning, drift handling, state inspection. Ansible roles for legacy + on-prem.

**Observability with strong instincts for what's useful** — Prometheus + Grafana (operator-deployed on EKS at Cisco; on K3s in the public reference platform); ELK Stack (production-grade with X-Pack security, SSL, snapshot repositories at Volvo); Azure Monitor + Log Analytics + KQL (KQL-based monitoring at Stena contributed to a **~20% reduction in downtime** across supported services); CloudWatch. **Comfortable distinguishing alerts that catch problems from dashboards that decorate.** Datadog is the one major observability platform I haven't operated — comparable mental model, would ramp quickly.

**Self-hostable infrastructure** — Public **`single-node-gitops`** reference platform (K3s + ArgoCD + Prometheus + Grafana + cert-manager + sealed-secrets) demonstrates the "works on every machine" pattern from a single-node setup to a multi-node deployment. Helm chart authorship and operation across Kubeflow, Prometheus Operator, and the BSS microservice estate at Deutsche Telekom.

**High-throughput event processing** — Built a **Logstash pipeline ingesting 5G UDR (Usage Data Record) feeds into Elasticsearch** at Deutsche Telekom for the billing emulator; production ELK stack on LXD with snapshot repositories at Volvo Cars; Cisco AWS observability environment with Prometheus + persistent storage for metrics ingestion. Comfortable with the territory of streaming ingest, backpressure, and lossy-vs-lossless trade-offs.

**Reliability & automation** — Reduced cluster provisioning lead time **from days to same-day** at Volvo via GitOps self-service with cost/governance defaults baked in (auto-termination, autoscale, cluster-log shipping). KQL-driven monitoring at Stena → ~20% downtime reduction. SOP authorship at HP Enterprise Services across customer-critical 24×7 estates.

**CI/CD** — GitHub Actions, Azure DevOps Pipelines, Jenkins (declarative + scripted, EKS-hosted, on-prem), GitLab CI, ArgoCD, Gerrit; reusable workflow templates, Terraform automation patterns (`fmt/validate/plan` separated from `apply`, state locking, credential flow).

**Scripting** — **Python** (REST/SCM automation, CLI tooling — including a Python migration tool against the Bitbucket REST API at Cisco with retry/rate-limit handling), **Bash**, **PowerShell** (Azure governance — SP lifecycle, runtime audits, budget automation). Familiar with Go from open-source side projects (`go-url-shortener`); comfortable picking up for tooling work.

**Security** — IAM, custom RBAC role definitions, secrets management (Key Vault, sealed-secrets, AWS Secrets Manager via Terraform), SAML 2.0 federation (Azure AD / ADFS → AWS IAM) replacing long-lived keys, Service Principal credential rotation design (Logic Apps + Microsoft Graph `addPassword`).

**Open source contributions** — Sanitised production patterns published as public repos: <a href="https://github.com/arnabdey73/iac-azure-core-governance">`iac-azure-core-governance`</a>, reusable Terraform module library, Azure cost-optimisation templates, GitOps Kubernetes reference platform. Comfortable supporting community users debugging self-hosted deployments.

---

## Professional Experience

### DevOps Engineer — AFRY Digital Solutions AB
*May 2025 – Present  |  Stockholm, Sweden*

**Assignment: Ericsson AB — CI Engineer, Tiger Test Tools (Sep 2025 – Present)**
- Maintain end-to-end **CI flow for radio-communication smoke and regression testing** — Git, Gerrit, Jenkins, Docker, Linux. Debug across CI pipelines, hardware, and test-server interactions when deliveries fail.

**Open-source platform engineering (public on GitHub)**
- Designed, deployed, and operate a **GitOps Kubernetes reference platform**: K3s + ArgoCD + Prometheus + Grafana + cert-manager + sealed-secrets. Self-hostable from a single-node setup, declarative cluster state in Git, ArgoCD reconciling, secrets sealed at rest, ingress and certificates automated, observability built in.

---

### Cloud Engineer — Stena Metall AB
*Aug 2024 – Jan 2025  |  Gothenburg, Sweden*

Cloud Infrastructure Engineer on the central Cloud Office (Governance) of an **Azure CAF Enterprise Scale** estate — ~100 subscriptions across a multi-management-group hierarchy, production workloads for a multi-billion-SEK industrial group. Infrastructure delivered as Terraform via Azure DevOps pipelines.

- **Authored two custom Azure RBAC role definitions** enforcing separation-of-duties between resource management and backup deletion (a ransomware-resilience control missing from Azure's built-in Contributor). Wired into the CAF archetype framework and shipped through the production pipeline.
- **Tenant-wide Key Vault compliance audit** — KQL across Azure Resource Graph for soft-delete retention, purge protection, and RBAC authorisation; CSV inventories and a documented review for architecture leadership.
- Built **Service Principal lifecycle tooling** integrating Resource Graph (KQL audit), PowerShell (expiring-credential inventory), and a Logic Apps + Microsoft Graph `addPassword` rotation design.
- **KQL-based monitoring contributed to a ~20% reduction in downtime** across supported services — dashboards and alerts that caught problems, not decorative ones.
- Public sister repos: <a href="https://github.com/arnabdey73/iac-azure-core-governance">`iac-azure-core-governance`</a>, reusable Terraform module library, Azure cost-optimisation templates.

---

### Senior Software Engineer (DevOps) — Capgemini Sverige AB
*Sep 2021 – Jul 2024  |  Gothenburg, Sweden*

**Assignment: Volvo Cars — Car Safety R&D (Abakus MLOps / AI Platform)**

- Designed and owned a **GitOps self-service pattern for Azure Databricks** for Car Safety data scientists (GitHub issue → manifest PR → GitHub Actions → `terraform apply`) with reliability and cost defaults — auto-termination, autoscale, single-user mode — baked into the Terraform module. **Outcome:** provisioning lead time fell from days to same-day; every cluster traceable to a PR and named owner; idle-cluster spend eliminated.
- Modernised a ~36-node CAE/HPC cluster: SLES → Ubuntu LTS migration, **Rancher-managed Kubernetes (RKE)** stand-up, **Kubeflow** via Helm; production ELK stack (Elasticsearch, Logstash, Kibana) with X-Pack security, SSL, snapshot repositories.
- Built **two matched Terraform stacks (AWS + Azure)** as identically-shaped, disposable test rigs for MLCommons-style ML object-storage benchmarking — infrastructure as the control variable.

---

### Senior Business Consultant (DevOps) — Tech Mahindra
*Feb 2017 – Sep 2021  |  Bangalore, India · Sydney, Australia*

**Assignment: Cisco Systems — CD 2.0 Continuous-Delivery Platform on AWS**
- **Authored the Terraform** for Cisco's CD 2.0 platform on AWS — VPC, subnets, security groups, **EKS cluster, IAM roles, Jenkins on EKS, ECR integration, build-agent fleet, ALB, DNS** — extending an internal reference architecture.
- Wrote a separate **Terraform stack for an AWS observability environment** (EKS + Prometheus Operator via Helm + Grafana + persistent storage + ingress).
- Closed out Cisco's long-running SVN-to-Git migration via **Python automation against the Bitbucket REST API** — enumeration, history extraction, repo provisioning, push, CSV reports — with retry logic and batching for SCM rate limits.

**Assignment: Deutsche Telekom — 5G BSS Slicing Pilot on OpenStack (15 months)**
- Owned the **DevOps platform side** of DT's 5G Network Slicing commercial pilot on PAN-NET (OpenStack), delivering ~30-microservice BSS suite plus the Phenom UI.
- **Terraform against the OpenStack provider** provisioning the Jenkins / Nexus / Tuleap / Rancher / Keycloak / ELK estate; Ansible playbooks for service configuration.
- **~46 Jenkins jobs** building BMP microservices, tagging build number + short git SHA, pushing to Nexus, updating Kubernetes manifests, triggering Rancher rolling updates.
- Built a **Logstash pipeline ingesting 5G UDR (Usage Data Record) CSV feeds into Elasticsearch** for the billing emulator — real-time event processing under production constraints.

**Other Tech Mahindra assignments**
- **Greenstone Financial Services & CA ANZ:** DevOps transformation for .NET microservices on Azure DevOps + Terraform + ACR; architected GitLab-based CI and source-control model.

---

### Senior AEM Administrator (Cloud) — ICF Next
*Sep 2015 – Jan 2017  |  Bangalore, India*

Built and operated a production AEM web platform on AWS for Channel 7 (national Australian broadcaster) — VPC, EC2 lifecycle, Apache HTTPD + Dispatcher hardening, **SAML 2.0 federation (Azure AD / ADFS → AWS IAM)** replacing long-lived IAM keys; Ansible roles for AEM, Apache, SSL, base OS.

---

### Unix / Linux Systems Administrator — HP Enterprise Services
*Nov 2011 – Aug 2015  |  Bangalore, India*

Three-and-a-half years on HP's Global Operations Center (Unix Service Delivery Unit) — 24×7 incident handling on customer-critical Linux/Unix estates (140+ servers across HUL, E.ON, Con-way Inc.), LVM/SAN, kernel tuning, SOP authoring for production runbooks.

---

## Public Projects (GitHub)

- **single-node-gitops** — Single-node GitOps Kubernetes platform (K3s + ArgoCD + Prometheus + Grafana + cert-manager + sealed-secrets), provisioned via Terraform. Self-hostable reference for the platform pattern.
- **iac-azure-core-governance** — Sanitised CAF Enterprise Scale governance platform (Terraform + Azure DevOps).
- **resume-builder-agent**, **weather-app**, **go-url-shortener** — Reference applications and tooling.

---

## Education

**B.Tech in Computer Science** — West Bengal University of Technology, Kolkata, India (2005 – 2009)

---

## Certifications

- **Microsoft Certified: Azure Fundamentals (AZ-900)** — Mar 2023 *(801D970BAA49297)*
- **AWS Certified Solutions Architect – Associate (SAA-C03)** — *in progress*

---

## Languages

- **English** — Fluent (working language for 15+ years)
- **Swedish** — SFI C-level
- **Hindi**, **Bengali** — Native
