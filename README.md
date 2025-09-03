
# Arnab Dey – Smart Resume & Cover Letter Generator

Welcome to my automated resume and cover letter generation system. This repository contains both my professional documents and an intelligent system that can analyze job postings and generate perfectly tailored applications automatically.

## 🤖 Smart Generation Features

### **Automated Job Analysis**
- **Web Scraping**: Analyzes job postings from LinkedIn, Breezy HR, and other career sites
- **Keyword Intelligence**: Extracts technical requirements using natural language processing
- **Skill Mapping**: Maps job requirements to my existing skills (no fake skills added)
- **ATS Optimization**: Optimizes keyword placement for applicant tracking systems

### **Intelligent Document Generation**
- **Role-Specific Content**: Automatically adjusts tone and focus for DevOps, Architect, or Azure Specialist roles
- **Company Customization**: Includes company-specific content for known organizations
- **GPT Enhancement**: Optional AI-powered content enhancement for more natural, compelling language
- **Truthful Enhancement**: Only emphasizes skills I actually possess while maximizing relevance

## ⚡ Setup & Requirements

### **Quick Setup**
```bash
# Install Python dependencies
pip install requests beautifulsoup4 pyyaml jinja2

# Optional: Install OpenAI for GPT enhancement
pip install openai
```

### **GPT Enhancement Setup**
For AI-powered content enhancement, see [GPT Setup Guide](docs/GPT_SETUP.md):
- Get OpenAI API key from [platform.openai.com](https://platform.openai.com/api-keys)
- Add to `config.yaml` or `.env` file
- Use `--gpt` flag for enhanced generation

## 🚀 Quick Start - Generate from Job Posting

### **Smart Generation (Recommended)**
```bash
# Analyze any job posting and generate tailored resume + cover letter
bash resume-smart.sh smart https://linkedin.com/jobs/view/123456789 company-role-name

# With GPT-4o enhancement (requires API key)
bash resume-smart.sh smart https://linkedin.com/jobs/view/123456789 company-role-name both --gpt

# Examples:
bash resume-smart.sh smart https://nordcloud-career.breezy.hr/p/37592336774701 nordcloud-architect
bash resume-smart.sh smart https://telia.com/careers/senior-devops-engineer telia-devops both --gpt
```

### **What It Does:**
1. **Scrapes the job posting** (title, company, requirements)
2. **Analyzes keywords** and technical requirements
3. **Maps requirements** to my existing skills in `configs/skill-mappings.yaml`
4. **Creates optimized configurations** with priority skills
5. **Generates tailored resume** with emphasized relevant skills
6. **Generates tailored cover letter** with company-specific content
7. **Saves detailed analysis** for future reference

### **Analysis Only (for research)**
```bash
# Just analyze a job posting without generating documents
bash resume-smart.sh analyze https://company.com/careers/job-posting analysis-name
```

## 📁 System Architecture

```text
├── scripts/
│   ├── job_analyzer.py           # Web scraping and keyword analysis
│   ├── smart_generator.py        # Complete automation workflow
│   ├── generate_resume.py        # Resume generation engine
│   └── generate_cover_letter.py  # Cover letter generation engine
├── configs/
│   ├── skill-mappings.yaml       # Maps job keywords to my actual skills
│   ├── devops-engineer.yaml      # DevOps role configuration
│   ├── cloud-architect.yaml      # Architect role configuration
│   └── cover-letter-*.yaml       # Cover letter configurations
├── base/
│   ├── arnab-dey-template.md     # Jinja2 resume template
│   ├── core-content-blocks.yaml # Reusable content blocks
│   └── cover-letter-template.md # Cover letter template
├── versions/                     # Generated documents
├── analysis/                     # Job analysis reports
└── Backlog/                     # Archive of previous versions
```

## �️ Manual Generation (Traditional)

```bash
# Generate resume only
bash resume-smart.sh generate devops-engineer.yaml output-name "Company Name"

# Generate cover letter only
bash resume-smart.sh cover cover-letter-devops.yaml output-name "Company Name"

# Generate both resume and cover letter
bash resume-smart.sh both devops-engineer.yaml cover-letter-devops.yaml output-name "Company Name"

# List available configurations
bash resume-smart.sh list

# Show all generated documents
bash resume-smart.sh versions
```

### **Available Configurations**

- **Resume Configs**: `devops-engineer.yaml`, `cloud-architect.yaml`, `azure-specialist.yaml`, `senior-devops.yaml`
- **Cover Letter Configs**: `cover-letter-devops.yaml`, `cover-letter-architect.yaml`

## � Example Results

### **Smart Analysis Output**
```
🎯 Top priority skills for Nordcloud Azure Architect role:
   • Azure Cost Management (emphasis weight: 13)
   • cost optimization (emphasis weight: 9)
   • Azure Monitor (emphasis weight: 8)
   • Azure DevOps (emphasis weight: 7)
   • Azure Advisor (emphasis weight: 6)

✅ Generated Files:
   Resume: versions/nordcloud-architect.md
   Cover Letter: versions/nordcloud-architect-cover-letter.md
   Analysis: analysis/nordcloud-architect_analysis.json
```

## 📄 Static Documents (Legacy)

For recruiters and hiring managers, pre-generated documents are available in the `versions/` and `Backlog/` folders:

### **Current Versions**
- **`arnab-dey-devops-general.md`** - General DevOps Engineer resume
- **`complete-application-telia.md`** - Complete Telia application package
- **`architect-application-nordcloud.md`** - Nordcloud architect application

### **Backlog Archive**

- **Arnab-Dey-Cloud-DevOps-Engineer.md / .pdf**: Resume tailored for Cloud and DevOps Engineer positions, highlighting experience with Azure, CI/CD, Kubernetes, and automation tools.
- **Arnab-Dey-DevOps-Engineer.md / .pdf**: Resume focused on DevOps Engineer roles, emphasizing DevOps toolchain, automation, and platform engineering skills.
- **arnab-dey-resume.md / .pdf / .docx**: General resume covering overall IT, Cloud, and DevOps experience, suitable for a wide range of technical roles.
- **arnab-dey-cover-letter.md / .pdf**: Customizable cover letter template for job applications in Cloud/DevOps, demonstrating motivation and relevant skills.

## 🔧 System Requirements

- **Python 3.11+** (for smart generation)
- **Required packages**: `requests`, `beautifulsoup4`, `pyyaml`, `jinja2`
- **Bash** (for running scripts on Windows/macOS)

## 📖 How It Works

### **Smart Generation Process**

1. **Web Scraping**: The system fetches job postings from LinkedIn, Breezy HR, and other career sites
2. **Content Analysis**: Uses natural language processing to extract keywords and requirements
3. **Skill Mapping**: Maps job requirements to my existing skills defined in `configs/skill-mappings.yaml`
4. **Configuration Generation**: Creates optimized configurations emphasizing relevant skills
5. **Document Generation**: Uses Jinja2 templates to generate tailored resume and cover letter
6. **Analysis Storage**: Saves detailed analysis for future reference and optimization

### **Key Benefits**

- ✅ **100% Truthful** - Only emphasizes skills I actually possess
- ✅ **ATS Optimized** - Perfect keyword placement for applicant tracking systems
- ✅ **Company Aware** - Customizes content for specific companies (Nordcloud, Telia, Microsoft)
- ✅ **Role Adaptive** - Adjusts tone and focus for DevOps, Architect, Azure Specialist roles
- ✅ **Time Saving** - Generates perfect application packages in minutes instead of hours

---

## 📚 Documentation

- **[GPT Setup Guide](docs/GPT_SETUP.md)** - Complete setup for AI-powered content enhancement
- **[Technical Reference Guide](docs/TECHNICAL_GUIDE.md)** - Traditional generation, customization, and advanced configuration
- **[Main README](README.md)** - This file, overview and quick start

---

## 👤 About Me

I am Arnab Dey, a Cloud & DevOps Engineer with experience in designing, deploying, and managing scalable cloud solutions. My expertise includes Azure, AWS, CI/CD, automation, and infrastructure as code.

---

## 📜 Changelog

- **September 1, 2025**: Implemented Smart Resume Generation System
  - Added job posting analysis and web scraping capabilities
  - Integrated intelligent keyword mapping and ATS optimization
  - Created automated resume and cover letter generation from job URLs
  - Added company-specific customization (Nordcloud, Telia, Microsoft)
  - Implemented truthful skill enhancement (no fake skills added)
- **August 27, 2025**: Professional README added, changelog moved to bottom, and updated with latest changes
- Resume Updated
- Updating resume once again
- Adding cover letter
- Added docx resume
- Skipped AI and came back to Markdown
- Added a more concise CV with help from chatGPT
