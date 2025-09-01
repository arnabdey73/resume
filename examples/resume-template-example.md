# Generic Resume Template
# This is a Jinja2 template that generates resumes based on configuration
# Customize this template to match your preferred resume format

<div align="center">

# {{ personal.name }}

{{ personal.location }} | {{ personal.phone }} | {{ personal.email }}

{% if personal.linkedin %}[LinkedIn]({{ personal.linkedin }}){% endif %}{% if personal.github %} | [GitHub]({{ personal.github }}){% endif %}{% if personal.website %} | [Website]({{ personal.website }}){% endif %}

</div>

---

## Professional Summary

{% if role_config.summary_focus %}
{{ professional_summary.experience_years }}+ years of experience in {{ role_config.summary_focus }}, specializing in {{ role_config.core_skills_emphasis | join(", ") }}. Proven track record in {{ role_config.experience_highlights | join(", ") }}.
{% else %}
{{ professional_summary.experience_years }}+ years of experience in {{ professional_summary.industry_focus }}, with expertise in {{ professional_summary.key_strengths | join(", ") }}.
{% endif %}

{% if company_name %}
**Key strengths relevant to {{ company_name }}:**
{% if role_config.technical_strengths %}
{% for strength in role_config.technical_strengths %}
- {{ strength }}
{% endfor %}
{% endif %}
{% endif %}

---

## Technical Skills

{% if role_config.core_skills_emphasis %}
**Core Technologies:** {{ role_config.core_skills_emphasis | join(" • ") }}
{% endif %}

**Programming Languages:** {{ skills.programming_languages | join(" • ") }}

**Web Technologies:** {{ skills.web_technologies | join(" • ") }}

**Cloud Platforms:** {{ skills.cloud_platforms | join(" • ") }}

**DevOps & Tools:** {{ skills.devops_tools | join(" • ") }}

**Databases:** {{ skills.databases | join(" • ") }}

**Frameworks:** {{ skills.frameworks | join(" • ") }}

---

## Professional Experience

### Senior {{ role_config.role or "Software Engineer" }}
**Your Current Company** | *2022 - Present*

{% if role_config.experience_highlights %}
{% for highlight in role_config.experience_highlights %}
- Developed and maintained {{ highlight }} serving thousands of users
{% endfor %}
{% else %}
- Developed and maintained scalable applications serving thousands of users
- Designed and implemented RESTful APIs and microservices architecture
- Collaborated with cross-functional teams to deliver high-quality software solutions
- Mentored junior developers and conducted code reviews
{% endif %}

### {{ role_config.role or "Software Engineer" }}
**Previous Company** | *2020 - 2022*

- Built responsive web applications using modern frameworks
- Implemented automated testing and CI/CD pipelines
- Optimized application performance and database queries
- Participated in agile development processes and sprint planning

### Junior {{ role_config.role or "Developer" }}
**Earlier Company** | *2018 - 2020*

- Contributed to feature development and bug fixes
- Learned and applied best practices in software development
- Collaborated with senior developers on complex projects
- Gained experience with version control and deployment processes

---

## Key Projects

{% if role_config.project_types %}
{% for project_type in role_config.project_types %}
### {{ project_type | title }} Platform
- **Technologies:** {{ role_config.core_skills_emphasis[:3] | join(", ") }}
- **Impact:** Improved system efficiency and user experience
- **Role:** {{ role_config.focus | title }} development and architecture design
{% endfor %}
{% else %}
### E-commerce Platform
- **Technologies:** Python, React, PostgreSQL, AWS
- **Impact:** Increased sales by 30% through improved user experience
- **Role:** Full-stack development and database optimization

### API Gateway Service
- **Technologies:** Node.js, Docker, Kubernetes, MongoDB
- **Impact:** Reduced response times by 50% and improved system reliability
- **Role:** Backend development and microservices architecture
{% endif %}

---

## Education

**Bachelor of Science in Computer Science**
*University Name* | *Graduation Year*

{% if role_config.education_focus == "bootcamp" %}
**Full-Stack Web Development Bootcamp**
*Bootcamp Name* | *Year*
{% endif %}

---

## Certifications

{% if 'AWS' in (role_config.core_skills_emphasis or []) %}
- AWS Certified Solutions Architect
{% endif %}
{% if 'Azure' in (role_config.core_skills_emphasis or []) %}
- Microsoft Azure Fundamentals
{% endif %}
{% if 'Kubernetes' in (role_config.core_skills_emphasis or []) %}
- Certified Kubernetes Administrator (CKA)
{% endif %}

---

## Additional Information

{% if role_config.soft_skills_focus %}
**Key Strengths:** {{ role_config.soft_skills_focus | join(" • ") }}
{% endif %}

**Languages:** English (Native), [Add your languages]

**Interests:** Technology trends, open source contribution, continuous learning
