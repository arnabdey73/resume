# Aimo — Cloud Operations Engineer (Stockholm)

## Describe your hands-on experience with AWS and Kubernetes in production

I've been running AWS and Kubernetes in production for several years. At Cisco I led the CD 2.0 delivery platform on AWS — authored the Terraform for VPC, EKS cluster, Jenkins on EKS, ECR, IAM, ALB, DNS, plus a separate EKS-based observability environment running Prometheus and Grafana. At Volvo Cars I operated a Rancher-managed Kubernetes cluster (RKE) across a ~36-node HPC estate, installed Kubeflow via Helm for ML engineers, and built an ELK stack for cluster observability. At Deutsche Telekom I was the operational owner of a Rancher-managed Kubernetes cluster running ~30 microservices in production, with ~46 Jenkins jobs driving rolling deployments. I currently maintain a K3s + ArgoCD + Prometheus + Grafana + cert-manager + sealed-secrets platform as a live public demo. Across all of these I've handled the real production concerns — upgrades, incident response, workload troubleshooting, cost, and security hardening.

---

## Walk us through a production incident you handled and your approach

During the CD 2.0 build-out on AWS at Cisco, one of our Jenkins agent pods running on EKS started failing to push built artifacts to ECR — which blocked the downstream deploy stages across multiple application teams onboarded to the platform. My approach: stabilise first, investigate second. Step one was pinning affected teams back to the last known-good image tag already in ECR and redeploying via the existing Helm charts, so development kept moving while I diagnosed. Step two was looking at the actual evidence — kubectl events on the failing pods, Prometheus metrics from the observability environment, and CloudWatch logs for the EKS control plane. The root cause turned out to be an IAM issue on the service account the Jenkins pods were using — a recent policy update had tightened permissions in a way that blocked the specific ECR `PutImage` action from a subset of agents. Step three was the fix: corrected the IAM policy via Terraform (so the fix was version-controlled and reproducible), documented the exact failure signature and remediation in the runbook, and added a CloudWatch alarm on ECR push failures so the next occurrence surfaces in minutes rather than at the point the deploy stage breaks. My general approach to incidents: restore service first, even with a short-term workaround, then treat root-cause investigation as a separate calmer piece of work, and always close the loop with a runbook entry or alerting improvement so the same incident is shorter next time.

---

## What improvements or automations have you driven within cloud operations?

A few that stand out. At Stena Metall (Azure) I built Service Principal lifecycle tooling using Azure Graph API, Logic Apps, and Azure Resource Graph — KQL-driven audit of credential events, automated expiring-credential inventory, and a design for client-secret rotation via `addPassword` — and KQL monitoring against Azure Resource Graph that contributed to a ~20% reduction in downtime across supported Azure services. At Cisco (AWS) I built the separate observability environment for the CD 2.0 platform as a Terraform stack — provisioning an EKS cluster, Prometheus Operator via Helm, Grafana, EBS-backed persistent storage, and ALB ingress — turning what had been ad-hoc observability setup into a repeatable IaC pattern reusable across AWS accounts. At Channel 7 (AWS) I automated the security boundary around the platform by implementing SAML 2.0 federation from Azure AD / ADFS into AWS IAM — replacing long-lived IAM user keys with federated role assumption — and evolved the Publish tier into an EC2 Auto Scaling Group so capacity responded to load rather than being manually resized. At Deutsche Telekom (OpenStack) I codified the full Jenkins / Nexus / Tuleap / Rancher / Keycloak / ELK estate in Terraform against the OpenStack provider — networks, subnets, security groups, VMs, and floating IPs — so that when the pilot migrated to a new PAN-NET tenant over a single weekend, the cloud infrastructure itself rebuilt from code and the running Kubernetes workloads were rehomed via Python/shell automation without rebuilding anything from scratch. The common thread: if a team is doing the same thing by hand twice a month, it's a candidate for automation.

---

## What would your dream job look like? Imagine that there's no limitations and dream big!

My dream job is running platform and cloud infrastructure for a team where the work visibly matters — where pipelines I improve make engineers faster, where alerts I tune actually prevent real user pain, and where automation I build makes the whole operation more sustainable instead of just shinier. I'd want a modern stack with room to keep evolving it — AWS, Kubernetes, Terraform, GitOps — and genuine space to integrate GenAI and LLM tooling into operations, because I think that's going to be the defining DevOps shift of this decade and I want to be part of shaping it rather than catching up. I'd want a small, highly capable team where I can own things end-to-end, and where engineering craftsmanship — clear documentation, reliable systems, thoughtful alerting, sensible cost control — is valued rather than treated as overhead. And I'd want it to be somewhere with a purpose beyond itself — a product that solves a real problem for real people. Based in Stockholm, because I live here and I'd like to keep it that way. Honestly, what you've described here isn't far off.

---

## What's important for you in an employer?

A few things matter to me. First, trust and autonomy — I do my best work when I'm treated as a capable adult who can make technical judgement calls without checking in on every decision, and I give that same trust back to the people I work with. Second, engineering quality as a shared value — colleagues who care about doing things properly, who write documentation because it helps the next person, who invest in automation because they respect their own future time. Third, clarity of purpose — I'd rather work somewhere I can explain why the product matters than somewhere with a flashier brand but no real reason for existing. Fourth, honest communication — I'd rather get direct feedback early than polite feedback late, and I try to offer the same. Fifth, sustainable pace — I'm happy to put in serious effort for things that matter, but I think burnout cultures produce worse engineering and I want to work somewhere that understands that. Growth and learning matter too, though I'd rather learn from good colleagues and interesting problems than from a formal training budget.

---

## Vilken typ av tjänst är du intresserad av att börja jobba som hos oss på Aimo?

The Cloud Operations Engineer role is the one I'm applying for, and it's a strong match for where I am and what I'm looking for. The scope — maintaining and evolving AWS and Kubernetes environments, improving CI/CD, strengthening monitoring and observability, and genuinely building "better structure, stronger support, and more sustainable ways of working" — is the kind of day-to-day work I enjoy and am good at. If Aimo also has adjacent Platform Engineer or DevOps Engineer roles where my profile fits better, I'd be open to hearing about them, but my primary interest is this one.

---

## 140-character pitch

Cloud Operations Engineer — AWS, EKS, Terraform, GitLab CI, ELK. 24×7 incident roots, automation-driven improvement. Stockholm.
