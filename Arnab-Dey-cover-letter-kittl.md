I'm applying for the Senior DevOps Engineer role on the Platform team. The shape of the work — AWS / EKS / Argo CD / GitHub Actions / Prometheus / Grafana, with **CI reliability, observability, and cost visibility** as named outcomes rather than aspirations — lines up with what I've been doing for the past several years. Stockholm-based, open to relocation to Berlin under EU Blue Card sponsorship.

On Kubernetes specifically: **~7 years total operating Kubernetes**, including **~2 years on EKS** at Cisco where I authored the Terraform for the CD 2.0 continuous-delivery platform on AWS — VPC, EKS cluster, IAM, Jenkins on EKS, ECR, ALB with SSL termination, build-agent fleet — alongside a separate Prometheus Operator + Grafana observability stack. Outside EKS, I helped modernise a ~36-node bare-metal **Rancher-managed RKE** cluster at Volvo, ran **AKS** for a .NET microservices portal at Greenstone, and operate a live **K3s + Argo CD + Prometheus + Grafana + cert-manager + sealed-secrets** reference platform. Deeper EKS-specific tenure than the headline number alone — the broader Kubernetes operator depth reads through.

CI reliability is the second match. My **current Ericsson Tiger Test Tools assignment is dedicated to it** — triaging flaky pipelines and shortening feedback loops across radio-comms smoke and regression testing. At Volvo I designed the **GitOps self-service Databricks pattern** that cut provisioning lead time from days to same-day. At Deutsche Telekom I owned **~46 Jenkins jobs** building a 30-microservice 5G BSS suite, with build-number + git-SHA tagging and Rancher rolling-update orchestration.

On cost visibility — your "Optimize infrastructure costs" responsibility maps cleanly to **FinOps work I shipped at Stena Metall**: subscription budget automation, ACR token expiry inventory, **cost-allocation tagging across landing zones**, Hybrid Benefit enablement. At Volvo, the Databricks defaults (30-minute auto-termination, 1→3 autoscale, single-user security mode) eliminated long-tail idle-cluster spend by construction, not policy.

Security and governance are a recurring thread: custom Azure RBAC role definitions enforcing **separation-of-duties** at Stena, tenant-wide Key Vault compliance audit, Service Principal credential-rotation design, **SAML 2.0 federation eliminating long-lived IAM user keys**, sealed-secrets and cert-manager on the K3s reference platform.

One honest note on tooling: **my IaC daily-driver is Terraform, not Pulumi**. The conceptual model is the same — declarative cloud resources, drift handling, state — and I'd treat Pulumi in TypeScript as a ramp rather than a rebuild. Three and a half years of **24×7 shift-based Linux operations** at HP Enterprise Services, including E.ON's German and UK estate, is where the on-call reflexes come from.

Happy to pick up the thread in a conversation.

Warm regards,
Arnab Dey
