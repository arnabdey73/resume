# Arnab Dey

Stockholm, Sweden | [arnabdey009@gmail.com](mailto:arnabdey009@gmail.com) | [+46 0764516092](tel:+46764516092)  
[LinkedIn](https://www.linkedin.com/in/arnabdey73) | [GitHub](https://github.com/arnabdey73)  

---

**Patrik Grönman**  
Head of Cloud, Tool Flow Solutions  
Sandvik  

**Subject:** Application for Cloud & Site Reliability Engineer (R0091146)

Dear Patrik,

I am applying for the Cloud & Site Reliability Engineer role within Sandvik's Tool Flow Solutions Cloud Tech organization. The work you describe — scaling a secure, reliable SaaS platform on Azure, building shared CI/CD on GitHub Actions and Azure DevOps, and enabling product teams through self-service — closely mirrors what I have been doing for the last four years at Volvo Cars and Stena Metall, and I would be glad to bring that experience to Sandvik.

At **Stena Metall**, I worked on the central Cloud Office of a mature **Azure CAF Enterprise Scale** estate — roughly 100 subscriptions across a multi-management-group hierarchy supporting production workloads for a multi-billion-SEK industrial group. All infrastructure was delivered as Terraform through Azure DevOps pipelines. I authored two custom Azure RBAC role definitions to enforce separation-of-duties between resource management and backup deletion (a ransomware-resilience control missing from Azure's built-in Contributor), wired them into the CAF archetype framework, and shipped them through the production pipeline. I also led a tenant-wide Key Vault compliance audit, designed Service Principal credential-rotation tooling, and contributed KQL-based monitoring that supported a roughly 20% reduction in downtime across the services I covered. The combination of governance, security, and reliability you describe at Sandvik is the same pattern I worked in at Stena.

At **Volvo Cars Car Safety R&D**, I designed and owned a GitOps self-service pattern for Azure Databricks: data scientists request compute via a GitHub issue, a YAML manifest PR triggers GitHub Actions running `terraform fmt/validate/plan`, and merge runs `terraform apply`. The Terraform module had reliability and cost defaults baked in — single-user security mode, 30-minute auto-termination, autoscale 1→3 — so clusters were cheap and safe by construction rather than policed after the fact. Provisioning lead time fell from days to same-day, and idle-cluster spend was eliminated. This is the kind of self-service capability your JD calls for, built on the GitHub Actions and Terraform stack you use.

On **Bicep**: my IaC depth is in Terraform, but I have ARM template experience from the same era, and Bicep transpiles to ARM with the same resource model. I am comfortable picking it up quickly on the job rather than treating it as a barrier. On the backend-language side, I have hands-on **C#/.NET** experience from leading the DevOps transformation for Greenstone Financial Services' .NET microservices on Azure DevOps, Docker Swarm, and Azure Container Registry, and from PowerShell tooling at Stena that enumerated .NET runtimes across the App Service estate.

What attracts me to this role specifically is that it sits at the intersection of three things I care about: Azure platform engineering at industrial-SaaS scale, security and compliance treated as a first-class concern (custom RBAC, Key Vault, GDPR), and SRE practices applied pragmatically — observability, reliability defaults, incident response — rather than as a separate discipline. I am Stockholm-based, work professionally in English, and would welcome the opportunity to discuss how my background fits the Cloud Tech team.

Thank you for your consideration.

Sincerely,  
**Arnab Dey**
