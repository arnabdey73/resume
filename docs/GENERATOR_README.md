# Resume Generator System

This repository contains an automated resume generation system that creates tailored resumes for different roles and companies using YAML configurations and Jinja2 templates.

## 🚀 Quick Start

1. **Run setup** (first time only):
   ```bash
   ./setup.sh
   ```

2. **Generate a resume**:
   ```bash
   ./resume.sh generate devops-engineer.yaml arnab-dey-devops-telia Telia
   ```

3. **List available configurations**:
   ```bash
   ./resume.sh list
   ```

## 📁 Directory Structure

```
resume/
├── 📁 base/                     # Templates and content blocks
│   ├── arnab-dey-template.md    # Main Jinja2 template
│   └── core-content-blocks.yaml # Reusable content sections
├── 📁 configs/                  # Role-specific configurations
│   ├── devops-engineer.yaml     # DevOps Engineer focus
│   ├── cloud-architect.yaml     # Cloud Architect focus
│   ├── azure-specialist.yaml    # Azure Specialist focus
│   └── senior-devops.yaml       # Senior roles focus
├── 📁 scripts/                  # Generation scripts
│   └── generate_resume.py       # Main generator script
├── 📁 versions/                 # Generated resumes (auto-created)
├── 📁 Backlog/                  # Archive of previous versions
├── setup.sh                     # One-time setup script (cross-platform)
├── resume.sh                    # Quick command wrapper (cross-platform)
├── git-resume.sh                # Git management helper (cross-platform)
└── README.md                    # This file
```

## 🎯 Available Role Configurations

- **devops-engineer.yaml** - Focus on CI/CD, automation, Linux, Kubernetes
- **cloud-architect.yaml** - Focus on architecture, cost optimization, governance
- **azure-specialist.yaml** - Focus on Azure services, governance, monitoring
- **senior-devops.yaml** - Focus on leadership, strategy, mentoring

## 💻 Usage Examples

### Generate resumes for different companies

```bash
# DevOps Engineer for Telia
./resume.sh generate devops-engineer.yaml arnab-dey-devops-telia Telia

# Cloud Architect for Nordcloud
./resume.sh generate cloud-architect.yaml arnab-dey-architect-nordcloud Nordcloud

# Azure Specialist for Microsoft
./resume.sh generate azure-specialist.yaml arnab-dey-azure-microsoft Microsoft

# Senior DevOps for general application
./resume.sh generate senior-devops.yaml arnab-dey-senior-general
```

### Management commands

```bash
# List all available configurations
./resume.sh list

# Show configuration files
./resume.sh configs

# Show generated versions
./resume.sh versions
```

### Git management

```bash
# Initialize git repository
./git-resume.sh init

# Create role-specific branches
./git-resume.sh branch devops-engineer
./git-resume.sh branch cloud-architect

# Tag specific applications
./git-resume.sh tag telia-devops-v1.0 "Applied to Telia DevOps Engineer role"
./git-resume.sh tag nordcloud-architect-v1.0 "Applied to Nordcloud Cloud Architect role"

# List branches and tags
./git-resume.sh list

# Compare versions
./git-resume.sh compare v1.0-base telia-devops-v1.0
```

## 🔧 Manual Usage

If you prefer direct Python execution:

```bash
# List configurations
python scripts\generate_resume.py --list

# Generate resume
python scripts\generate_resume.py devops-engineer.yaml arnab-dey-devops-telia --company Telia

# Help
python scripts\generate_resume.py --help
```

## 📝 Git Integration

This system works perfectly with Git branching and tagging:

```bash
# Create company-specific branches
git checkout -b telia-applications
git checkout -b nordcloud-applications

# Tag specific applications
git tag -a "telia-devops-v1.0" -m "Applied to Telia DevOps Engineer role"
git tag -a "nordcloud-architect-v1.0" -m "Applied to Nordcloud Cloud Architect role"
```

## 🛠️ Customization

### Adding a new role configuration:

1. Create a new YAML file in `configs/` folder
2. Define role, focus, skills, and keywords
3. Run generation with the new config

### Modifying content blocks:

1. Edit `base/core-content-blocks.yaml`
2. Add new sections or modify existing ones
3. Update template if needed

### Customizing the template:

1. Edit `base/arnab-dey-template.md`
2. Use Jinja2 syntax for dynamic content
3. Test with different configurations

## 📊 Generated Resume Features

- ✅ **Centered header** with clickable phone number
- ✅ **Role-specific professional summary**
- ✅ **Tailored core skills section**
- ✅ **Experience bullets optimized for role focus**
- ✅ **Company name and generation date tracking**
- ✅ **Consistent formatting and structure**

## 🔍 Troubleshooting

**Python not found**: Install Python 3.8+ and add to PATH
**Package import errors**: Run `setup.bat` again
**Template errors**: Check YAML syntax in config files
**Generation fails**: Verify all required files exist in correct directories

Generated on: 2025-09-01
