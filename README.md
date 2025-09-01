# 🤖 Smart Resume & Cover Letter Generator

> **Generate perfectly tailored resumes and cover letters in minutes from any job posting URL!**

An intelligent automation system that analyzes job postings and creates ATS-optimized application documents. Simply paste a job URL, and get a professional resume and cover letter tailored specifically to that position.

## ✨ What This Tool Does

🎯 **Analyzes job postings** from LinkedIn, company websites, and career sites  
🧠 **Extracts key requirements** using AI-powered keyword analysis  
📝 **Generates tailored documents** that match the job description perfectly  
🔍 **ATS-optimized** to pass automated resume screening systems  
💯 **100% truthful** - only emphasizes skills you actually possess  

## 🚀 Quick Start Guide

### **Step 1: One-Time Setup (5 minutes)**

#### 🛠️ **Install the System**

```bash
# Clone the generic branch directly
git clone -b generic https://github.com/arnabdey73/resume.git smart-resume-generator
cd smart-resume-generator

# Install Python dependencies
bash setup.sh
# OR manually: pip install requests beautifulsoup4 pyyaml jinja2
```

#### ⚙️ **Configure Your Profile**

Copy the example files and add your information:

```bash
# Copy configuration templates
cp examples/personal-info-example.yaml configs/personal-info.yaml
cp examples/skill-mappings-example.yaml configs/skill-mappings.yaml

# Edit with your details
nano configs/personal-info.yaml    # Add your name, contact info, etc.
nano configs/skill-mappings.yaml   # Add your actual skills and experience
```

## 🚀 How to Use This Tool

### **🎯 The 2-Step Process**

**Step 1: Setup (one time only)** 
```bash
git clone -b generic https://github.com/arnabdey73/resume.git smart-resume-generator
cd smart-resume-generator
bash setup.sh
```

**Step 2: Generate applications (30 seconds each)**
```bash
bash resume-smart.sh smart [JOB_URL] [OUTPUT_NAME]
```

**That's it!** You'll get a perfectly tailored resume and cover letter.

### **💡 Real Example**

```bash
# Step 1: Setup (first time only)
git clone -b generic https://github.com/arnabdey73/resume.git smart-resume-generator
cd smart-resume-generator
bash setup.sh
cp examples/personal-info-example.yaml configs/personal-info.yaml
# Edit configs/personal-info.yaml with your details

# Step 2: Generate application 
bash resume-smart.sh smart https://linkedin.com/jobs/view/123456789 my-dream-job

# Result: Gets you my-dream-job-resume.md and my-dream-job-cover-letter.md
```

#### 🌟 **Smart Generation (Recommended)**

Just paste any job posting URL and get a tailored application:

```bash
# One command generates both resume and cover letter
bash resume-smart.sh smart [JOB_URL] [OUTPUT_NAME]

# Real examples:
bash resume-smart.sh smart https://linkedin.com/jobs/view/123456789 my-google-application
bash resume-smart.sh smart https://startup.com/careers/senior-dev startup-backend-role
bash resume-smart.sh smart https://company.com/jobs/devops-engineer devops-position
```

**That's it!** ✨ Your tailored resume and cover letter will be in the `versions/` folder.

#### 📝 **Manual Generation**

For more control, use specific templates:

```bash
# Generate resume only
bash resume-smart.sh generate configs/role-templates/software-engineer.yaml my-resume "Company Name"

# Generate both resume and cover letter
bash resume-smart.sh both configs/role-templates/software-engineer.yaml configs/cover-letter-templates/software-engineer.yaml my-application "Company Name"
```

## 📋 What You Get

### **Generated Files**
- 📄 `[output-name]-resume.md` - ATS-optimized resume
- 💌 `[output-name]-cover-letter.md` - Personalized cover letter  
- 📊 `analysis/[output-name]-analysis.json` - Detailed job analysis report

### **Key Features**
- ✅ **Keywords matched** to job requirements
- ✅ **Skills emphasized** that you actually possess
- ✅ **Company-specific** customization when possible
- ✅ **Role-appropriate** tone and formatting
- ✅ **ATS-friendly** formatting for automated screening

## 🎯 Supported Job Sites

✅ **LinkedIn Jobs** - linkedin.com/jobs/view/  
✅ **Company Career Pages** - Most direct company websites  
✅ **Breezy HR** - *.breezy.hr job postings  
✅ **General URLs** - Any webpage with job descriptions  

## 🔧 Available Templates

### **Built-in Role Templates**
- 💻 **Software Engineer** (Frontend, Backend, Full-stack)
- ☁️ **DevOps Engineer** (Platform, Cloud, Infrastructure)
- 🧪 **QA Engineer** (Manual, Automation, Performance Testing)

### **Creating Custom Templates**

1. Copy an existing template from `configs/role-templates/`
2. Modify the skills and focus areas
3. Test: `bash resume-smart.sh generate your-template.yaml test-output`

## 📁 Project Structure

```
smart-resume-generator/
├── 📜 resume-smart.sh           # Main script - your entry point
├── ⚙️ setup.sh                 # One-time setup script
├── scripts/                    # Core processing scripts
│   ├── job_analyzer.py          # Analyzes job postings
│   ├── smart_generator.py       # Smart automation workflow  
│   ├── generate_resume.py       # Resume generation
│   └── generate_cover_letter.py # Cover letter generation
├── configs/                    # Your personal configuration
│   ├── personal-info.yaml      # 👤 Your details (name, contact, etc.)
│   ├── skill-mappings.yaml     # 🛠️ Your skills and experience
│   ├── role-templates/          # 📋 Job role configurations
│   └── cover-letter-templates/  # 💌 Cover letter styles
├── base/                       # Template files
│   ├── resume-template.md       # Resume formatting template
│   └── cover-letter-template.md # Cover letter template
├── examples/                   # Example configurations
├── versions/                   # 📄 Generated resumes & cover letters
├── analysis/                   # 📊 Job analysis reports
└── docs/                       # 📚 Additional documentation
```

## ⚡ Usage Examples

### **Quick Examples**

```bash
# Generate for any job posting
bash resume-smart.sh smart https://linkedin.com/jobs/view/3848234234 netflix-backend

# Generate for startup position  
bash resume-smart.sh smart https://jobs.lever.co/company/software-engineer startup-swe

# Generate for DevOps role
bash resume-smart.sh smart https://company.com/careers/devops devops-specialist
```

### **Advanced Usage**

```bash
# Use specific role template
bash resume-smart.sh generate configs/role-templates/qa-engineer.yaml qa-position "TestCorp"

# Generate full application package
bash resume-smart.sh both configs/role-templates/software-engineer.yaml configs/cover-letter-templates/tech-company.yaml full-application "BigTech Inc"
```

## 🛠️ Configuration Guide

### **personal-info.yaml** - Your Basic Information

```yaml
personal:
  name: "Your Full Name"
  location: "City, Country"
  phone: "+1-234-567-8900"
  email: "your.email@domain.com"
  linkedin: "https://linkedin.com/in/yourprofile"
  github: "https://github.com/yourusername"

professional_summary:
  experience_years: 5
  industry_focus: "Software Development"
  key_strengths:
    - "Full-Stack Development"
    - "Cloud Architecture"
    - "Team Leadership"
```

### **skill-mappings.yaml** - Your Skills & Experience

```yaml
your_skills:
  programming_languages:
    - "Python"
    - "JavaScript"
    - "Java"
  
  frameworks:
    - "React"
    - "Django"
    - "Spring Boot"
  
  cloud_platforms:
    - "AWS"
    - "Azure"

keyword_mappings:
  # Maps job keywords to your actual skills
  "full stack":
    - "React"
    - "Django"
    - "Full-Stack Development"
  
  "cloud":
    - "AWS"
    - "Cloud Architecture"
    - "Infrastructure"
```

## 🎯 Getting Great Results

### **For Best Results:**

1. ✅ **Keep skills honest** - Only list skills you actually have
2. ✅ **Update regularly** - Add new skills as you learn them  
3. ✅ **Use specific URLs** - Direct job posting links work best
4. ✅ **Review output** - Always review generated documents before submitting

### **Common Use Cases:**

- 🎯 **Job Applications** - Perfect for individual applications
- 📊 **A/B Testing** - Generate multiple versions for different approaches
- 🔄 **Regular Updates** - Keep your resume current with new positions
- 📈 **Skill Tracking** - See which skills are most in-demand

## 🆘 Troubleshooting

### **Common Issues:**

**"Job posting not found"**
- ✅ Make sure the URL is accessible publicly
- ✅ Try copying the direct job posting URL
- ✅ Some sites require login - try a different URL format

**"No skills matched"**  
- ✅ Update your `skill-mappings.yaml` with more skills
- ✅ Add keyword mappings for job-specific terms
- ✅ Check the analysis report in `analysis/` folder for insights

**"Generation failed"**
- ✅ Check your configuration files for syntax errors
- ✅ Ensure all required fields are filled in `personal-info.yaml`
- ✅ Run `bash setup.sh` to reinstall dependencies

## 📚 Additional Documentation

📁 **[Complete Documentation](docs/)** - Detailed guides and technical documentation

- 📖 **[Setup Guide](docs/GENERIC-SUMMARY.md)** - Detailed setup instructions
- 🎨 **[Template Guide](docs/QA-TEMPLATES-SUMMARY.md)** - Creating custom templates  
- 🧹 **[Migration Guide](docs/CLEANUP-SUMMARY.md)** - Updating from older versions
- 📋 **[Project Documentation](docs/GENERIC-PROJECT-DOCS.md)** - Technical details

## 🤝 Contributing

We welcome contributions! See issues and discussions on GitHub.

1. Fork the repository
2. Clone the generic branch: `git clone -b generic https://github.com/yourusername/resume.git`
3. Create a feature branch: `git checkout -b feature-name`  
4. Make changes and test thoroughly
5. Submit a pull request to the generic branch with clear description

## 📄 License

MIT License - feel free to use this tool for personal and commercial projects.

---

## 🎉 Success Stories

> *"Got my dream job at a Fortune 500 company! This tool made my application stand out."* - Software Engineer

> *"Saved me hours of resume customization. The ATS optimization really works!"* - DevOps Engineer  

> *"Finally, a tool that doesn't add fake skills to my resume."* - QA Engineer

**Ready to land your dream job?** 🚀

Get started in 5 minutes and start generating perfectly tailored applications!

```bash
git clone -b generic https://github.com/arnabdey73/resume.git smart-resume-generator
cd smart-resume-generator && bash setup.sh
```
