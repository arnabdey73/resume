<div align="center">
	<h1><b>Arnab Dey</b></h1>
	<p>
		Stockholm, Sweden | +46 0764516092 | <a href="mailto:arnabdey009@gmail.com">arnabdey009@gmail.com</a><br>
		<a href="https://www.linkedin.com/in/arnabdey73">LinkedIn</a> | <a href="https://github.com/arnabdey73">GitHub</a>
	</p>
</div>

---

## Professional Summary

Senior CI/CD Engineer with **15+ years in IT** and **9+ years designing, leading, and operating CI/CD pipelines** across Jenkins, GitHub Actions, Azure DevOps, and GitLab CI. I've already lived the Jenkins-to-GitHub-Actions migration arc this role targets — Jenkins on EKS for Cisco's CD 2.0, ~46 Jenkins-driven rolling deployments of ~30 microservices at Deutsche Telekom, and a GitHub Actions + Terraform GitOps workflow at Volvo Cars. Deep Azure experience (AKS, Azure DevOps, Azure Monitor / Log Analytics / KQL) and cross-cloud Kubernetes fluency (AKS, EKS, OpenShift-derived platforms, Rancher RKE, K3s). Track record of leading CI/CD streams as Technical Lead on the Cisco CD 2.0 platform and the Deutsche Telekom 5G BSS DevOps platform, including onboarding and mentoring application teams into the pipelines they depend on. Based in Stockholm.

---

## Core Skills

**CI/CD Pipeline Engineering** — Jenkins (Jenkinsfile / Groovy), GitHub Actions, Azure DevOps Pipelines, GitLab CI, ArgoCD; pipeline design, Jenkins → GitHub Actions migration, large-scale build/test/deploy automation

**Azure** — AKS, Azure DevOps, Azure Monitor / Log Analytics / KQL, Entra ID, Key Vault, Azure Resource Graph; production estate operations

**Kubernetes & Containers** — AKS, EKS, OpenShift-derived reference architectures, Rancher RKE, K3s; Docker, Helm; microservices-based workloads

**Scripting** — Groovy (Jenkinsfile), Python (automation, CLI tooling, REST API integration), Bash, Shell, PowerShell

**Infrastructure as Code** — Terraform (AzureRM, AWS, OpenStack providers), Ansible; reusable module libraries

**Observability & Monitoring** — Prometheus, Grafana, ELK Stack (Elasticsearch, Logstash, Kibana), Azure Monitor, CloudWatch; dashboards, alerting design

**Leadership & Mentoring** — technical lead on CI/CD platforms (Cisco CD 2.0, Deutsche Telekom 5G BSS); CI onboarding, team enablement, and engineer mentoring

**Languages** — English (fluent), Swedish (SFI C-level)

---

## Professional Experience

### DevOps Engineer — AFRY Digital Solutions AB
*May 2025 – Present  |  Stockholm, Sweden*

**Assignment: Ericsson AB — CI Engineer, Tiger Test Tools (Sep 2025 – Present)**
- Maintain and support the end-to-end CI flow for radio-communication smoke and regression testing — **Git, Gerrit, Jenkins, Docker, Linux**.
- Troubleshoot cross-cutting pipeline and hardware issues across daily delivery and validation workflows.

**GitOps Platform (internal reference project)**
- Designed and deployed a GitOps-based Kubernetes platform (K3s + ArgoCD + Prometheus + Grafana + cert-manager + sealed-secrets) as a live cloud-native CI/CD reference — publicly maintained on GitHub.

---

### Cloud Engineer — Stena Metall AB
*Aug 2024 – Jan 2025  |  Gothenburg, Sweden*

Cloud Infrastructure Engineer on a production Azure estate — ~100 subscriptions, multi-management-group hierarchy — delivering governance, RBAC, and infrastructure changes via **Azure DevOps + Terraform** pipelines.

- Authored and shipped changes through the existing **Azure DevOps + Terraform delivery pipeline** across the full CAF archetype framework — custom RBAC role definitions, application landing-zone fixes, and reusable Terraform modules.
- KQL-based monitoring against Azure Resource Graph contributed to a **~20% reduction in downtime** across supported services.
- Published sanitized sister repos on GitHub including [`iac-azure-core-governance`](https://github.com/arnabdey73/iac-azure-core-governance) (CAF Enterprise Scale governance platform).

---

### Senior Software Engineer (DevOps) — Capgemini Sverige AB
*Sep 2021 – Jul 2024  |  Gothenburg, Sweden*

**Assignment: Volvo Cars — Car Safety R&D (MLOps / AI Platform)**

*GitHub Actions CI/CD for Azure Databricks self-service*
- Designed and owned a **GitHub Actions CI/CD workflow** for Azure Databricks self-service provisioning: data scientists request compute via an issue template → YAML manifest PR → GitHub Actions validates and plans changes for review → merge triggers deployment.
- Authored the Terraform module with governance-friendly defaults baked in — single-user security mode, 30-minute auto-termination, autoscale, cluster-log shipping — making provisioning cheap and safe by construction.
- **Outcome:** provisioning lead time dropped from days to same-day; every cluster traceable to a PR and named owner.

*CAE HPC platform modernisation (on-prem)*
- Contributed to modernising a ~36-node CAE/HPC cluster supporting ML research: stand-up of **Rancher-managed Kubernetes (RKE)** with worker fleet, **Kubeflow** via Helm, OS migration from SLES to Ubuntu LTS.
- Built a **production-grade ELK stack** (Elasticsearch, Logstash, Kibana) on LXD with X-Pack security, SSL, and snapshot repositories — full-fleet observability for ML workload monitoring and log aggregation.
- Authored **Ansible roles** within the shared GitLab-managed codebase.

---

### Senior Business Consultant (DevOps) — Tech Mahindra
*Feb 2017 – Sep 2021 | Bangalore, India | Sydney, Australia*

**Assignment: Cisco Systems — CD 2.0 on AWS** *(Technical Lead from mid-2019)*
- **Led the CD 2.0 platform from mid-2019** — full technical ownership of Cisco's continuous-delivery platform, including CI/CD roadmap and team onboarding.
- **Authored the Terraform** for CD 2.0 on AWS — VPC, EKS cluster, **Jenkins on EKS**, ECR integration, **build-agent fleet**, IAM roles, ALB, DNS — **extending an internal Cisco reference architecture originally built on on-prem OpenShift**.
- Built a separate **AWS observability environment** — EKS, Prometheus Operator via Helm, Grafana, persistent storage, ingress — as a repeatable IaC pattern.
- **Closed out Cisco's long-running SVN-to-Git migration** with Python automation: enumerated SVN repos, extracted history, provisioned Bitbucket repos via REST API, pushed converted Git history, with retry logic and batching around SCM rate limits.
- Onboarded application teams to CD 2.0 via **CI engagement templates**, Bitbucket/Crucible provisioning, and **Jenkinsfile (Groovy) adaptation** — the mentoring/enablement motion this role calls for.

**Assignment: Deutsche Telekom — 5G BSS Slicing Pilot on OpenStack** *(Technical Lead, mid-2020 – Aug 2021)*
- Owned the **DevOps platform side** of DT's 5G Network Slicing commercial pilot — accountable for operational reliability of a **~30-microservice BSS suite** plus the Phenom UI.
- Designed and ran **~46 Jenkins jobs** building microservices, tagging with build number + short git SHA, pushing to internal Nexus registry, updating Kubernetes manifests, and **triggering Rancher rolling updates**.
- Owned the **cross-tenant migration** when the pilot moved PAN-NET tenants — Python/shell automation to clone 54 Tuleap repos at correct branches, **re-seed Jenkins jobs**, and rehome Nexus artifacts, Keycloak realm, and running Kubernetes workloads. Cutover completed over a single weekend.
- Wrote **Terraform against the OpenStack provider** and **Ansible playbooks** for configuration across the Jenkins / Nexus / Tuleap / Rancher / Keycloak / ELK estate.
- Built a **Logstash pipeline** ingesting 5G Usage Data Record CSV feeds into Elasticsearch for the billing emulator.

**Assignment: Greenstone Financial Services — Insurance Portal** *(Technical Lead, late 2019)*
- DevOps delivery for .NET microservices — **Azure DevOps pipelines**, Terraform for Azure, Docker + Docker Swarm with Azure Container Registry, Azure Monitor.

**Assignment: CA ANZ** *(Technical Lead, late 2019)*
- Architected the **GitLab-based CI and source-control strategy** — branching model, repository standards, pipeline conventions; supported team adoption through documentation and knowledge transfer.

---

### Senior AEM Administrator (Cloud) — ICF Next
*Sep 2015 – Jan 2017  |  Bangalore, India*

**Assignment: Channel 7 (Australia) — AEM on AWS**
- Operated a high-availability AWS platform for a national Australian broadcaster — VPC design, EC2 lifecycle, Apache/Dispatcher hardening, SSL, SAML 2.0 federation.
- Authored **Ansible roles** for AEM install, Apache/Dispatcher deployment, SSL, and system baseline — making instance rebuilds a runbook rather than a discovery exercise.
- Established a **package-parity procedure** between staging and production, catching release drift before deployments.

---

### Unix / Linux Systems Administrator — HP Enterprise Services
*Nov 2011 – Aug 2015  |  Bangalore, India*

Three and a half years on HP's Global Operations Center running **24×7 shift-based Linux/Unix operations** across HUL, E.ON, and Con-way Inc. — SOP authoring, procedure library contributions, and L1–L3 incident handling on enterprise estates.

---

## Education

**B.Tech in Computer Science** — West Bengal University of Technology, Kolkata, India (2005 – 2009)

---

## Certifications

- **Microsoft Certified: Azure Fundamentals (AZ-900)** — Mar 2023
- **AWS Certified Solutions Architect – Associate (SAA-C03)** — *in progress*
