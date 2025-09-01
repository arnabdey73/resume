<div align="center">
	<h1><b>Arnab Dey</b></h1>
	<p>
		{{ config.location }} | <a href="tel:+46764516092">+46 764516092</a> | <a href="mailto:arnabdey009@gmail.com">arnabdey009@gmail.com</a><br>
		<a href="https://www.linkedin.com/in/arnabdey73">LinkedIn</a> | <a href="https://github.com/arnabdey73">GitHub</a>
	</p>
</div>

---

## **Professional Summary**
{{ content_blocks.summaries[config.summary_type] }}

---

## **Core Skills**
{% for skill_category in content_blocks.skills[config.skills_profile] %}
- {{ skill_category }}
{% endfor %}

---

## **Professional Experience**

### **DevOps Engineer – AFRY Digital Solutions AB** *(May 2025 – Present)*
{% for bullet in content_blocks.experience.afry[config.focus] %}
- {{ bullet }}
{% endfor %}

---

### **Cloud Engineer – Stena Metall AB** *(Aug 2024 – Jan 2025)*
{% for bullet in content_blocks.experience.stena[config.focus] %}
- {{ bullet }}
{% endfor %}

---

### **Senior Software Engineer (DevOps) – Capgemini Sverige AB** *(Sep 2021 – Jul 2024)*
**Assignment: Volvo Cars Safety Department**
{% for bullet in content_blocks.experience.capgemini_volvo[config.focus] %}
- {{ bullet }}
{% endfor %}

**Internal Initiatives**
{% for bullet in content_blocks.experience.capgemini_internal[config.focus] %}
- {{ bullet }}
{% endfor %}

---

### **Senior Business Consultant (DevOps) – Tech Mahindra** *(Feb 2017 – Sep 2021)*
**Assignment: Deutsche Telekom**
{% for bullet in content_blocks.experience.tech_mahindra[config.focus] %}
- {{ bullet }}
{% endfor %}

---

### **Senior AEM Administrator (Cloud) – ICF Next** *(Sep 2015 – Jan 2017)*
{% for bullet in content_blocks.experience.icf_next[config.focus] %}
- {{ bullet }}
{% endfor %}

---

### **Unix/Linux Systems Administrator – Hewlett Packard Enterprise** *(Nov 2011 – Aug 2015)*
{% for bullet in content_blocks.experience.hpe[config.focus] %}
- {{ bullet }}
{% endfor %}

---

## **Education**
- **B.Tech in Computer Science** – West Bengal University of Technology, Kolkata, India (2005 – 2009)

---

## **Certifications**
- **Microsoft Certified: Azure Fundamentals** (Issued March 2023) – Credential ID: 801D970BAA49297
{% if config.focus == 'finops' %}
- **FinOps Certified Practitioner** (In Progress)
{% endif %}

---

## **Languages**
- English: Bilingual / Native Proficiency
- Swedish: SFI C Level Proficiency

---

{% if company_name %}
*Generated for {{ company_name }} application on {{ generation_date }}*
{% endif %}
