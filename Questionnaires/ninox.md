# Ninox — Questionnaire Notes

**Role:** Senior SRE / DevOps Engineer
**Location model:** Berlin-Mitte, on-site default (Deutschlandticket, dog-friendly office); 30 days remote/year cap
**Stack signals from JD:** Linux · Terraform / Pulumi / Ansible / Packer · Docker / Kubernetes · AWS or Azure or GCP · Grafana / Loki / ELK · Python / Go / Node.js (plus)
**Comp band published:** none
**Visa / relocation:** Berlin relocation on the table (per existing diconium-resume framing — EU Blue Card)

Outstanding gap calls before tailoring the resume (covered separately): Pulumi, Packer, Loki, Node.js framing, Berlin relocation confirmation.

---

## Expected yearly compensation in EUR

**Recommended range:** **€95,000 – €110,000 base annual.**
**Single-figure version (if the form takes only one number):** **€100,000**

### Paste-ready answer

> €95,000 – €110,000 gross annual base. Open to discussing the full package including relocation support, given the move from Stockholm to Berlin.

### Why this number

- **Berlin senior SRE/DevOps band, 2024–2025** sits roughly €80K – €115K at scale-ups. Ninox is mid-sized B2B SaaS (low-code) — solid but not the hyper-growth/AI tier (where Langfuse landed at €90 – 160K).
- **15+ years experience** vs the JD's 5+ floor justifies upper-senior anchoring, not the middle of the band.
- **€10–20K below the Langfuse anchor** (€115 – 135K) — reflects Ninox's more traditional B2B positioning, no equity highlighted in the JD, and Berlin cost-of-living vs Langfuse's remote-first model.
- **Doesn't overreach to staff** (€120K+) where the honest Pulumi / Loki / Node.js gaps would get exposed in interview.
- **Floor at €95K** prevents anchoring mid-senior. **Don't go below €90K** — wastes the senior signal. **Below €85K, walk.**

### Contextual notes (don't paste in the form)

- Berlin cost-of-living is meaningfully lower than Stockholm; €100K Berlin gross has roughly the spending power of ~€110 – 115K Stockholm gross. The "lower number than Langfuse" isn't a step down in real terms.
- Germany's marginal tax rates are higher than Sweden's at this band — net pay differential is smaller than gross differential suggests.
- Ninox didn't publish a band. If the recruiter pushes back hard on €100K, dropping to €90K is still defensible.

---

## Describe a project where you took ownership beyond your formal responsibilities. What motivated you, what challenges did you face, and what was the final impact?

### Primary answer (security-led — fits Ninox's "reliable and secure systems" framing)

> **Project: Custom Azure RBAC role definitions for ransomware resilience — Stena Metall**
>
> My formal role on the central Cloud Office (Governance) was implementing infrastructure and governance changes via Terraform / Azure DevOps pipelines on a mature CAF Enterprise Scale estate of ~100 subscriptions. The day-to-day was pipeline work and role assignments. Designing custom RBAC role *definitions* — and threat-modelling the existing ones — sat upstream, in architecture territory.
>
> Reviewing role assignments tenant-wide, I noticed that Azure's built-in Contributor role grants both resource-management and backup-deletion permissions to the same identity. In a ransomware scenario that means a single compromised identity can encrypt production resources AND delete the backups — the textbook double-extortion blast radius. Built-in Contributor is fine until it's not.
>
> **Motivation.** Ransomware was visible across the industry, and the gap was real, fixable, and not on anyone's roadmap. The cost of being right was low enough to justify proposing a fix.
>
> **Challenges.** Custom RBAC role authoring on Azure requires fine-grained knowledge of resource provider DataActions — which actions exist, which are dangerous, which are legitimately needed for resource and backup operations to keep working. I had to model two separate role surfaces (resource management without backup-delete; backup operations without resource-management) and verify they neither granted nor denied the wrong things. Architecture leadership buy-in was the second layer — the design had to fit cleanly into the existing CAF archetype framework so newly-onboarded subscriptions would inherit the control without breaking anything in flight.
>
> **Impact.** Two custom Azure RBAC role definitions shipped through the production pipeline — 38 commits across the core-governance repo — enforcing separation-of-duties between resource management and backup deletion across the estate, closing the ransomware-resilience gap that built-in Contributor leaves open. The roles are wired into the CAF archetype framework so the control propagates to new subscriptions automatically. I published a sanitised sister repo on GitHub (`iac-azure-core-governance`) so the pattern is reusable beyond Stena.

### Short form of the primary answer (≤1000 characters — for character-limited form fields)

Plain ASCII, no markdown, no em dashes — safe under any character counter (length-by-codepoint, length-by-byte, or .length on UTF-16):

```text
Project: Custom Azure RBAC roles for ransomware resilience.

On a ~100-subscription Azure CAF estate, my Cloud Office work was Terraform/Azure DevOps pipeline delivery. Reviewing role assignments tenant-wide, I noticed Azure's built-in Contributor lets one identity both manage resources and delete backups (the double-extortion blast radius).

Motivation: real gap, fixable, on no one's roadmap.

Challenges: custom RBAC authoring needs fine-grained DataActions knowledge. I modelled two role surfaces (resource-mgmt without backup-delete; backup-ops without resource-mgmt) and got architecture buy-in to wire the design into the CAF archetype framework cleanly.

Impact: two roles shipped via the production pipeline (38 commits), enforcing separation-of-duties across the estate. Wired into CAF archetypes so the control auto-propagates.
```

*Verified count: **844 characters, 844 bytes (UTF-8)** — identical under any counting method since the text is ASCII-only.*

### Alternative answer (reliability + cost + toil-reduction — fits Ninox's automation/SRE framing)

> **Project: GitOps self-service Azure Databricks platform — Volvo Cars Car Safety R&D**
>
> My formal scope on the Volvo Cars MLOps engagement was platform delivery — keeping the Kubernetes/MLOps stack running. Cluster provisioning for the Car Safety data scientists sat outside that scope and was ticket-driven: a request would land in our queue, someone would build a Databricks cluster manually, the cluster would sit half-idle while the requester moved on, and idle spend built up while ownership stayed untraceable. Nobody on the team was assigned to fix it.
>
> **Motivation.** I was watching friction slow down the data scientists my platform existed to support. I'd seen at Cisco that self-service is the difference between an infra team being a bottleneck queue and being a force multiplier. So I designed and shipped a GitOps self-service pattern: GitHub issue → manifest PR → GitHub Actions → `terraform apply`. Governance and cost defaults — auto-termination, autoscale 1→3, single-user security mode, cluster-log shipping — were baked into the Terraform module so clusters were cheap and safe by construction.
>
> **Challenges.** As much social as technical. Convincing a data science org to adopt a PR-based workflow took iteration; the governance defaults had to be tight enough to fix the idle-spend problem without making clusters too restrictive to use; state lifecycle and ownership tracking needed to make clusters easy to find and hard to forget. I calibrated defaults directly with the data scientist users.
>
> **Impact.** Provisioning lead time fell from **days to same-day**. Idle-cluster spend was **eliminated** by auto-termination defaults. Every cluster became traceable to a **PR and a named owner**, putting accountability at the cheapest possible point in the workflow. The pattern was reused for adjacent provisioning work on the engagement, and I published a sanitised sister repo on GitHub so the pattern is reusable beyond Volvo.

### When to pick which

- **Stena (primary)** — when the role / interviewer leans security-conscious or the JD foregrounds "secure systems." Ninox's JD does name secure systems, so Stena is the safer first pick.
- **Volvo (alternative)** — when the conversation is leaning toward reliability, cost discipline, automation, or reducing toil for end-users. Stronger measurable outcomes (days → same-day, idle spend eliminated).
- Both are real ownership-beyond-scope stories. If an interview asks for a *second* example, the unused one slots in directly.
