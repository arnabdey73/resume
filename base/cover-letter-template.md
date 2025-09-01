# Cover Letter Template
# Generated on: {{ generation_date }}
# Role: {{ config.role }}
# Company: {{ company_name or 'Target Company' }}
---

<div align="center">
	<h1><b>Arnab Dey</b></h1>
	<p>
		{{ config.location }} | <a href="tel:+46764516092">+46 764516092</a> | <a href="mailto:arnabdey009@gmail.com">arnabdey009@gmail.com</a><br>
		<a href="https://www.linkedin.com/in/arnabdey73">LinkedIn</a> | <a href="https://github.com/arnabdey73">GitHub</a>
	</p>
</div>

---

**{{ generation_date }}**

**Hiring Manager**  
{% if company_name %}{{ company_name }}{% else %}[Company Name]{% endif %}

**Re: {{ config.role }} Position**

Dear Hiring Manager,

{{ content_blocks.openings[config.opening_type] }}

{{ content_blocks.experience_paragraphs[config.experience_focus] }}

{{ content_blocks.technical_paragraphs[config.technical_focus] }}

{% if company_name and company_name in content_blocks.company_specific %}
{{ content_blocks.company_specific[company_name] }}
{% else %}
{{ content_blocks.generic_company_interest[config.company_type] }}
{% endif %}

{{ content_blocks.closings[config.closing_type] }}

Sincerely,  
**Arnab Dey**

---
*This cover letter was generated automatically and tailored for {{ config.role }} at {% if company_name %}{{ company_name }}{% else %}your organization{% endif %}.*
