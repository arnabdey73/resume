# Technical Reference Guide - Resume Generator

This technical guide covers traditional generation methods, system customization, and advanced configuration options for the resume generator system. For quick start and smart generation, see the [main README](../README.md).

## 🔧 Traditional Generation Methods

### Python Script Generation

Direct Python script usage for role-specific resume generation:

```bash
# Generate resume with specific role config
python scripts/generate_resume.py devops-engineer.yaml output-name --company "Company Name"

# Generate cover letter
python scripts/generate_cover_letter.py cover-letter-devops.yaml output-name --company "Company Name"

# List available configurations
python scripts/generate_resume.py --list

# Help and options
python scripts/generate_resume.py --help
```

### Available Role Configurations

**Resume Configurations:**
- `devops-engineer.yaml` - CI/CD, automation, Linux, Kubernetes focus
- `cloud-architect.yaml` - Architecture, cost optimization, governance focus
- `azure-specialist.yaml` - Azure services, governance, monitoring focus
- `senior-devops.yaml` - Leadership, strategy, mentoring focus

**Cover Letter Configurations:**
- `cover-letter-devops.yaml` - DevOps and automation focus
- `cover-letter-architect.yaml` - Architecture and leadership focus

## 📁 System Architecture

### Directory Structure

```text
resume/
├── 📄 README.md                 # Main documentation & smart generation
├── 🚀 resume-smart.sh           # Smart job analysis & GPT generation
├── ⚙️ config.yaml               # GPT & API configuration
├── 🔒 .env                      # API key storage
├── 📁 base/                     # Templates and content blocks
│   ├── arnab-dey-template.md    # Main Jinja2 template
│   ├── core-content-blocks.yaml # Reusable content sections
│   ├── cover-letter-template.md # Cover letter template
│   └── cover-letter-content-blocks.yaml
├── 📁 configs/                  # Role-specific configurations
│   ├── devops-engineer.yaml     # DevOps Engineer focus
│   ├── cloud-architect.yaml     # Cloud Architect focus
│   ├── azure-specialist.yaml    # Azure Specialist focus
│   ├── senior-devops.yaml       # Senior roles focus
│   └── skill-mappings.yaml      # Job requirement mappings
├── 📁 scripts/                  # All generation scripts
│   ├── job_analyzer.py          # Smart job analysis & content generation
│   ├── smart_generator.py       # Orchestrates smart generation
│   ├── gpt_enhancer.py          # GPT-4o integration
│   ├── generate_resume.py       # Traditional generator
│   ├── generate_cover_letter.py # Cover letter generator
│   └── [legacy utility scripts]
├── 📁 docs/                     # Documentation
│   ├── GPT_SETUP.md            # GPT configuration guide
│   └── TECHNICAL_GUIDE.md       # This technical guide
├── 📁 versions/                 # Generated resumes (auto-created)
├── 📁 analysis/                 # Job analysis outputs
└── 📁 Backlog/                  # Archive of previous versions
```

### Key Components

**Generation Scripts:**
- `job_analyzer.py` - Web scraping and intelligent content generation
- `smart_generator.py` - Orchestrates the smart generation pipeline
- `gpt_enhancer.py` - OpenAI GPT-4o integration for content enhancement
- `generate_resume.py` - Traditional YAML-based resume generation
- `generate_cover_letter.py` - Traditional cover letter generation

**Configuration System:**
- `config.yaml` - Main system configuration (GPT settings, API keys)
- `configs/*.yaml` - Role-specific generation configurations
- `base/*.yaml` - Content blocks and template data

## 💻 Traditional Generation Examples

```bash
# DevOps Engineer for specific company
python scripts/generate_resume.py devops-engineer.yaml arnab-dey-devops-telia --company Telia

# Cloud Architect role
python scripts/generate_resume.py cloud-architect.yaml arnab-dey-architect-nordcloud --company Nordcloud

# Azure Specialist
python scripts/generate_resume.py azure-specialist.yaml arnab-dey-azure-microsoft --company Microsoft

# Senior DevOps for general application
python scripts/generate_resume.py senior-devops.yaml arnab-dey-senior-general

# Cover letter generation
python scripts/generate_cover_letter.py cover-letter-devops.yaml company-role --company "Company Name"

# List available configurations
python scripts/generate_resume.py --list
```

## 🛠️ Customization & Configuration

### Adding a New Role Configuration

1. Create a new YAML file in `configs/` directory
2. Define the role configuration structure:

```yaml
role:
  title: "Senior Cloud Engineer"
  focus: "cloud infrastructure and automation"
  industry_focus: "enterprise cloud solutions"

skills:
  primary:
    - "Azure"
    - "Terraform"
    - "Kubernetes"
  secondary:
    - "GitOps"
    - "Monitoring"

keywords:
  technical:
    - "infrastructure as code"
    - "cloud governance"
  soft:
    - "collaboration"
    - "mentoring"

company_customizations:
  default:
    emphasis: "technical expertise"
  known_companies:
    Microsoft:
      emphasis: "Azure expertise and enterprise solutions"
```

3. Test with the new configuration:

```bash
python scripts/generate_resume.py your-new-config.yaml test-output --company "Test Company"
```

### Modifying Content Blocks

Edit `base/core-content-blocks.yaml` to customize content sections:

```yaml
professional_summary:
  devops_focus: |
    DevOps Engineer with {experience_years}+ years of experience in {primary_skills}.
    Proven track record in {achievements} and {focus_areas}.

experience_bullets:
  leadership:
    - "Led cross-functional teams of {team_size} engineers"
    - "Mentored {mentee_count} junior developers"
  
  technical:
    azure:
      - "Implemented Azure {service} resulting in {improvement}"
      - "Optimized {azure_resource} reducing costs by {percentage}%"
```

### Customizing Templates

Edit `base/arnab-dey-template.md` using Jinja2 syntax:

```jinja2
## Professional Summary
{% if gpt_enhanced_summary %}
{{ gpt_enhanced_summary }}
{% elif dynamic_summary %}
{{ dynamic_summary }}
{% else %}
{{ config.professional_summary[config.role.focus] }}
{% endif %}

## Core Skills
{% for category, skills in organized_skills.items() %}
**{{ category }}**: {{ skills | join(', ') }}
{% endfor %}
```

### Configuration Priority

The system uses the following priority order:

1. **GPT-enhanced content** (if `--gpt` flag used and API available)
2. **Dynamic content** (generated from job analysis)
3. **Template content** (from YAML configurations)
4. **Fallback content** (default templates)

## 📊 Traditional Generation Features

- ✅ **Role-specific professional summary** based on YAML configuration
- ✅ **Tailored core skills section** mapped to job requirements
- ✅ **Experience bullets optimized** for role focus
- ✅ **Consistent formatting** and structure
- ✅ **Company-specific customization** options

## 🔍 Troubleshooting

**Exit code 127**: Check Python path in `resume-smart.sh`

**Import errors**: Install dependencies:

```bash
pip install requests beautifulsoup4 pyyaml jinja2 openai
```

**Template errors**: Check YAML syntax in config files

**Generation fails**: Verify all required files exist in correct directories

**Python script errors**: Use absolute paths and check file permissions

**Configuration not found**: Ensure YAML files are in `configs/` directory

**Template rendering errors**: Check Jinja2 syntax in template files

## 📈 Migration Notes

If you have old scripts from previous versions:

- Legacy scripts moved to `scripts/` directory
- Use `resume-smart.sh` for new intelligent generation  
- Traditional generation still available via Python scripts
- Configuration files remain compatible

## 🔗 Related Documentation

- **[Main README](../README.md)** - Quick start and smart generation
- **[GPT Setup Guide](GPT_SETUP.md)** - AI enhancement configuration

---

Generated on: 2025-09-03
