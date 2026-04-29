Dear Linnea,

I'm applying for the Senior Platform Engineer role at Bannerflow. The shape of the role — a small platform team owning the infrastructure underneath a real product, building tooling that takes friction out of the way for product teams — is the work I find most satisfying, and the stack maps almost exactly to what I've been building for the past several years: Azure, Kubernetes, Terraform, GitHub Actions, ArgoCD, Helm.

The clearest example of "remove the bottleneck, don't become it" in my CV is the Databricks platform I designed at Volvo Cars. Data scientists were waiting days to get compute. I rebuilt the flow as a GitHub Actions / Terraform GitOps pattern — a YAML manifest PR runs `terraform plan` for review, merge triggers `terraform apply` — with governance-friendly defaults baked into the module (auto-termination, single-user security, autoscale, log shipping). Provisioning dropped to same-day, every cluster traced to a PR and a named owner, idle-cluster spend was eliminated. That's the platform-team mindset I'd bring to Bannerflow.

On the rest of the stack: Kubernetes is the layer I work in daily — Rancher RKE for Volvo's HPC platform, Kubeflow and Prometheus Operator via Helm, and a public K3s + ArgoCD + cert-manager + sealed-secrets reference platform I maintain on GitHub. On Azure I've operated at CAF Enterprise Scale (~100 subscriptions at Stena Metall), authored two custom RBAC role definitions enforcing separation-of-duties for backup deletion — a DR-integrity control missing from the built-in Contributor role. C#/.NET pipelines aren't my deepest territory but I've shipped them — Azure DevOps for .NET microservices at Greenstone, App Service .NET runtime audits at Stena Metall — and I'd ramp on the Bannerflow product specifics quickly.

On AI: I use Claude Code daily for scripting and review, and ran an internal AI-powered Resume Builder Agent as a side project (sanitized public repo). It's a daily tool, not a novelty — and I think a platform team is exactly where AI tooling pays off, since most of what we do is repetitive in pattern but high-stakes in detail.

Stockholm-based, comfortable with the hybrid cadence, and would welcome the chance to talk through where my background fits the team.

Warm regards,
Arnab Dey
+46 0764516092 | arnabdey009@gmail.com | linkedin.com/in/arnabdey73
