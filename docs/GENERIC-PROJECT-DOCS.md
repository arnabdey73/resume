# Generic Smart Resume Generator - Project Documentation

## Overview

This is a generic, configurable version of the Smart Resume & Cover Letter Generator that can be customized by any user. The system analyzes job postings and generates perfectly tailored application documents using the user's actual skills and experience.

## What Makes This Generic

### Personal Information
- All personal details are stored in `configs/personal-info.yaml`
- No hardcoded names, locations, or contact information
- Easy to customize for any user

### Skills & Experience
- User skills defined in `configs/skill-mappings.yaml`
- Keyword mappings show how job requirements relate to user's actual skills
- Completely truthful - only emphasizes skills the user actually possesses

### Templates
- Resume template in `base/resume-template.md` uses Jinja2 for dynamic content
- Cover letter template can be customized
- Role-specific templates in `configs/role-templates/`

## Directory Structure

```
generic-smart-resume-generator/
├── README-GENERIC.md              # Main documentation
├── setup-generic.sh               # Setup script for new users
├── resume-generic.sh              # Main generation script
├── scripts/
│   ├── job_analyzer_generic.py    # Generic job analysis
│   ├── smart_generator_generic.py # Complete workflow automation
│   ├── generate_resume.py         # Resume generation
│   └── generate_cover_letter.py   # Cover letter generation
├── configs/
│   ├── personal-info.yaml         # User's personal information
│   ├── skill-mappings.yaml        # User's skills and keyword mappings
│   ├── role-templates/            # Role-specific configurations
│   └── cover-letter-templates/    # Cover letter configurations
├── base/
│   ├── resume-template.md          # Jinja2 resume template
│   ├── content-blocks.yaml        # Reusable content blocks
│   └── cover-letter-template.md   # Cover letter template
├── examples/                       # Example configurations
│   ├── personal-info-example.yaml
│   ├── skill-mappings-example.yaml
│   ├── software-engineer-example.yaml
│   ├── devops-engineer-example.yaml
│   └── resume-template-example.md
├── versions/                       # Generated documents
└── analysis/                       # Job analysis reports
```

## Key Features

### 1. **100% Configurable**
- No hardcoded personal information
- All user data in YAML configuration files
- Easy to set up for different users

### 2. **Skill Mapping System**
- Maps job posting keywords to user's actual skills
- Maintains honesty while optimizing for ATS systems
- Supports complex skill relationships

### 3. **Multi-Site Job Analysis**
- Supports LinkedIn, Breezy HR, Greenhouse, Lever, Workday
- Generic parser for unknown sites
- Intelligent keyword extraction

### 4. **Role Adaptability**
- Automatically detects role type (frontend, backend, DevOps, etc.)
- Adjusts tone and emphasis accordingly
- Company-specific customization

### 5. **ATS Optimization**
- Keyword placement optimization
- Industry-standard formatting
- Truthful skill enhancement

## Setup Process

1. **Clone/Download**: Get the generic version
2. **Run Setup**: `bash setup-generic.sh` installs dependencies and creates config files
3. **Customize**: Edit `configs/personal-info.yaml` and `configs/skill-mappings.yaml`
4. **Test**: Try generation with example templates
5. **Use**: Generate applications from job postings

## Usage Examples

### Smart Generation
```bash
# Analyze job posting and generate tailored documents
bash resume-generic.sh smart https://company.com/jobs/software-engineer my-application

# Generate only resume
bash resume-generic.sh smart https://company.com/jobs/devops-engineer devops-role resume

# Generate only cover letter
bash resume-generic.sh smart https://company.com/jobs/frontend-dev frontend-role cover_letter
```

### Manual Generation
```bash
# Generate from existing role template
bash resume-generic.sh generate configs/role-templates/software-engineer.yaml my-resume

# Generate both documents
bash resume-generic.sh both configs/role-templates/devops.yaml configs/cover-letter-templates/devops.yaml my-app "Company Name"
```

## Configuration Guide

### Personal Information (`configs/personal-info.yaml`)
```yaml
personal:
  name: "Your Full Name"
  location: "Your City, State"
  phone: "+1 (234) 567-8900"
  email: "your.email@domain.com"
  linkedin: "https://linkedin.com/in/yourprofile"
  github: "https://github.com/yourusername"
  website: "https://yourwebsite.com"  # optional

professional_summary:
  experience_years: 5
  industry_focus: "Software Development"
  key_strengths:
    - "Full-Stack Development"
    - "Cloud Architecture"
    - "Team Leadership"
```

### Skills Mapping (`configs/skill-mappings.yaml`)
```yaml
your_skills:
  programming_languages:
    - "Python"
    - "JavaScript"
    - "Java"
  # ... more categories

keyword_mappings:
  "full stack development":
    - "React"
    - "Node.js"
    - "Python"
    - "database design"
  # ... more mappings
```

## Customization Options

### Template Customization
- Modify `base/resume-template.md` for different layouts
- Add custom Jinja2 blocks for dynamic content
- Create industry-specific templates

### Role Templates
- Create templates for specific roles in `configs/role-templates/`
- Define skill emphasis and experience highlights
- Customize for different seniority levels

### Company-Specific Optimization
- Add company focus in `skill-mappings.yaml`
- Automatic tone and emphasis adjustment
- Custom keyword prioritization

## Best Practices

### 1. **Honest Skill Mapping**
- Only include skills you actually possess
- Map job keywords to your real experience
- Use the system to emphasize, not fabricate

### 2. **Regular Updates**
- Keep skill mappings current as you learn new technologies
- Update personal information as needed
- Refresh role templates based on job market trends

### 3. **Testing**
- Test with known job postings before real applications
- Verify generated documents for accuracy
- Review keyword mapping effectiveness

## Troubleshooting

### Common Issues
1. **Missing Dependencies**: Run `bash setup-generic.sh`
2. **Configuration Errors**: Check YAML syntax in config files
3. **Scraping Failures**: Some sites may block automated access
4. **Template Errors**: Verify Jinja2 syntax in templates

### Getting Help
- Check example configurations in `examples/` directory
- Review error messages for specific guidance
- Ensure all required fields are filled in configuration files

## Contributing

To contribute to the generic version:
1. Fork the repository
2. Create feature branch
3. Test with multiple user configurations
4. Ensure no hardcoded personal information
5. Submit pull request

## License

MIT License - see LICENSE file for details.
