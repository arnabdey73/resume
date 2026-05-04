# Arnab Dey

Stockholm, Sweden (open to relocation to Berlin under EU Blue Card sponsorship) | [arnabdey009@gmail.com](mailto:arnabdey009@gmail.com) | [+46 0764516092](tel:+46764516092)  
[LinkedIn](https://www.linkedin.com/in/arnabdey73) | [GitHub](https://github.com/arnabdey73)  

---

**Lemuel-Hilton Anokye**  
Diconium — applydata / data studio Berlin  

**Subject:** Application for Senior Cloud Engineer (all genders), Berlin

Dear Lemuel-Hilton,

I am applying for the Senior Cloud Engineer role in the Diconium data studio Berlin. The combination you describe — designing and operating production-grade Azure platforms, providing technical leadership and architectural guidance, working closely with engineering teams and stakeholders, and continuously optimising for performance, security, and cost — closely matches the work I have been doing for the last four years at Volvo Cars and Stena Metall through my consulting engagements with Capgemini and AFRY. I am Stockholm-based today and **fully open to relocating to Berlin under EU Blue Card sponsorship**.

What makes the **applydata data studio** context particularly relevant for me: at **Volvo Cars Car Safety R&D** I designed and owned the **Abakus MLOps platform** — a GitOps self-service pattern for Azure Databricks where data scientists request compute via a GitHub issue, a YAML manifest PR triggers GitHub Actions running `terraform fmt/validate/plan`, and merge runs `terraform apply`. The Terraform module had reliability and cost defaults baked in (single-user security mode, 30-minute auto-termination, autoscale 1→3, cluster-log shipping to DBFS), so clusters were cheap and safe by construction rather than policed after the fact. Provisioning lead time fell from days to same-day, idle-cluster spend was eliminated, and every cluster was traceable to a PR, manifest, and named owner. Alongside this I stood up **Kubeflow on Rancher Kubernetes** for ML engineers and built **dual-cloud Terraform rigs** (AWS + Azure) for MLCommons-style object-storage benchmarking. This is the kind of multi-tenant, cost-controlled data platform work your team is built around.

At **Stena Metall** I worked on the central Cloud Office of a mature **Azure CAF Enterprise Scale** estate — roughly 100 subscriptions across a multi-management-group hierarchy supporting production workloads for a multi-billion-SEK industrial group. All infrastructure was delivered as Terraform through Azure DevOps pipelines. I collaborated with architecture leadership on a tenant-wide Key Vault compliance audit, authored two custom Azure RBAC role definitions enforcing separation-of-duties between resource management and backup deletion, designed Service Principal credential rotation around Logic Apps and the Microsoft Graph `addPassword` API, and contributed KQL-based monitoring that supported a roughly 20% reduction in downtime. The pattern of **client-facing Azure infrastructure work in a regulated, multi-stakeholder environment** is what I would bring directly to your engagements.

For the German enterprise context: my **15-month engagement with Deutsche Telekom on a 5G BSS commercial pilot** (running on PAN-NET, DT's OpenStack-based private cloud) gave me direct experience of the technical and stakeholder culture of large German enterprise clients. I owned the DevOps platform side end-to-end — Terraform against the OpenStack provider, ~46 Jenkins jobs building ~30 microservices, Ansible for service configuration, cross-tenant migration when the pilot moved PAN-NET tenants, and operational SOPs used by DT and Tech Mahindra teams across multiple European regions.

On the stack: deep on **Azure Virtual Machines, AKS, Entra ID, Storage, Key Vault**, and the surrounding governance services; **Terraform** at module-library scale; **Python and PowerShell** as my primary scripting languages; **Azure Monitor / Log Analytics / KQL** plus Prometheus and Grafana for observability; cost discipline as a first-class concern (FinOps templates published to my GitHub).

What attracts me to Diconium specifically is the combination of consultancy variety, hands-on technical ownership, and the focus on data and AI as a delivery context — which is exactly the trajectory my last four years have built towards. I would welcome the opportunity to discuss how my background fits the Berlin data studio and the relocation logistics in more detail.

Thank you for your consideration.

Sincerely,  
**Arnab Dey**
