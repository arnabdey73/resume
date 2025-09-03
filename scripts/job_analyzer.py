#!/usr/bin/env python3
"""
Job Posting Analyzer
Scrapes and analyzes job postings to automatically tailor resumes and cover letters
"""

import requests
import yaml
import re
import argparse
import sys
from pathlib import Path
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import json
from datetime import datetime
from collections import Counter

# Try to import GPT enhancer (optional)
try:
    from gpt_enhancer import GPTEnhancer
    GPT_AVAILABLE = True
except ImportError:
    GPT_AVAILABLE = False

class JobAnalyzer:
    def __init__(self, base_dir=None, use_gpt=False):
        self.base_dir = Path(base_dir) if base_dir else Path(__file__).parent.parent
        self.load_skill_mappings()
        
        # Initialize GPT enhancer if requested and available
        self.use_gpt = use_gpt and GPT_AVAILABLE
        if self.use_gpt:
            self.gpt_enhancer = GPTEnhancer(base_dir=self.base_dir)
            if not self.gpt_enhancer.api_key:
                print("⚠️ OpenAI API key not found. GPT enhancement disabled.")
                print("💡 Add your API key to .env file or config.yaml")
                self.use_gpt = False
        elif use_gpt and not GPT_AVAILABLE:
            print("⚠️ GPT enhancer not available. Install with: pip install openai")
            self.use_gpt = False
        
    def load_skill_mappings(self):
        """Load mapping of job keywords to your actual skills"""
        mapping_path = self.base_dir / "configs" / "skill-mappings.yaml"
        try:
            with open(mapping_path, 'r', encoding='utf-8') as f:
                self.skill_mappings = yaml.safe_load(f)
        except FileNotFoundError:
            print(f"Warning: Skill mappings file not found at {mapping_path}")
            self.skill_mappings = self.get_default_mappings()
    
    def get_default_mappings(self):
        """Default mapping of job keywords to your actual skills"""
        return {
            "your_skills": {
                "cloud_platforms": ["Azure", "AWS", "OpenStack"],
                "iac_automation": ["Terraform", "ARM templates", "Ansible"],
                "cicd_tools": ["Azure DevOps", "Jenkins", "GitHub Actions", "GitLab CI"],
                "containers": ["Kubernetes", "Docker", "AKS", "Rancher"],
                "monitoring": ["Prometheus", "Grafana", "Azure Monitor", "ELK Stack"],
                "scripting": ["Python", "Bash", "PowerShell"],
                "methodologies": ["Agile", "SAFe", "DevOps", "GitOps"],
                "cost_management": ["Azure Cost Management", "Azure Advisor", "cost optimization"],
                "governance": ["Azure Policies", "Azure CAF", "compliance"]
            },
            "keyword_mappings": {
                "finops": ["cost optimization", "Azure Cost Management", "financial accountability"],
                "cost optimization": ["Azure Cost Management", "Azure Advisor", "cost optimization"],
                "infrastructure as code": ["Terraform", "ARM templates"],
                "ci/cd": ["Azure DevOps", "Jenkins", "GitHub Actions"],
                "containerization": ["Kubernetes", "Docker", "AKS"],
                "cloud architecture": ["Azure", "cloud infrastructure", "solution design"],
                "automation": ["Terraform", "Ansible", "Azure Pipelines"],
                "monitoring": ["Prometheus", "Grafana", "Azure Monitor"],
                "agile": ["Agile", "SAFe", "cross-functional collaboration"]
            }
        }
    
    def scrape_job_posting(self, url):
        """Scrape job posting from various sources"""
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            }
            
            print(f"🌐 Fetching job posting from: {url}")
            response = requests.get(url, headers=headers, timeout=15)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Detect platform and extract accordingly
            domain = urlparse(url).netloc.lower()
            
            if 'linkedin.com' in domain:
                return self.extract_linkedin_job(soup)
            elif 'breezy.hr' in domain:
                return self.extract_breezy_job(soup)
            else:
                return self.extract_generic_job(soup)
                
        except Exception as e:
            print(f"❌ Error scraping job posting: {e}")
            return None
    
    def extract_linkedin_job(self, soup):
        """Extract job details from LinkedIn"""
        job_data = {}
        
        # Job title
        title_selectors = [
            'h1.top-card-layout__title',
            'h1.topcard__title',
            '.job-title',
            'h1'
        ]
        
        for selector in title_selectors:
            title_elem = soup.select_one(selector)
            if title_elem:
                job_data['title'] = title_elem.get_text(strip=True)
                break
        else:
            job_data['title'] = "Unknown Position"
        
        # Company
        company_selectors = [
            'a.topcard__org-name-link',
            '.topcard__flavor--black-link',
            '.job-company-name',
            'h2'
        ]
        
        for selector in company_selectors:
            company_elem = soup.select_one(selector)
            if company_elem:
                job_data['company'] = company_elem.get_text(strip=True)
                break
        else:
            job_data['company'] = "Unknown Company"
        
        # Description
        desc_selectors = [
            '.show-more-less-html__markup',
            '.description__text',
            '.job-description',
            'main'
        ]
        
        for selector in desc_selectors:
            desc_elem = soup.select_one(selector)
            if desc_elem:
                job_data['description'] = desc_elem.get_text(strip=True)
                break
        else:
            job_data['description'] = ""
        
        return job_data
    
    def extract_breezy_job(self, soup):
        """Extract job details from Breezy HR"""
        job_data = {}
        
        # Job title - try multiple selectors
        title_elem = (soup.select_one('h1') or 
                     soup.select_one('.position-name') or
                     soup.select_one('title'))
        if title_elem:
            title_text = title_elem.get_text(strip=True)
            # Clean up title (remove company name if present)
            job_data['title'] = title_text.split(' at ')[0] if ' at ' in title_text else title_text
        else:
            job_data['title'] = "Unknown Position"
        
        # Company
        company_elem = (soup.select_one('.company-name') or 
                       soup.select_one('h2') or
                       soup.select_one('.company'))
        if company_elem:
            job_data['company'] = company_elem.get_text(strip=True)
        else:
            # Try to extract from title if format is "Position at Company"
            title_text = job_data['title']
            if ' at ' in title_text:
                job_data['company'] = title_text.split(' at ')[1]
            else:
                job_data['company'] = "Unknown Company"
        
        # Description
        desc_elem = (soup.select_one('.description') or
                    soup.select_one('.job-description') or
                    soup.select_one('main') or
                    soup.select_one('article'))
        if desc_elem:
            job_data['description'] = desc_elem.get_text(strip=True)
        else:
            # Fallback to all text content
            job_data['description'] = soup.get_text(strip=True)
        
        return job_data
    
    def extract_generic_job(self, soup):
        """Extract job details from generic websites"""
        job_data = {}
        
        # Try to find title in common places
        title_elem = soup.select_one('h1') or soup.select_one('title')
        if title_elem:
            job_data['title'] = title_elem.get_text(strip=True)
        else:
            job_data['title'] = "Unknown Position"
        
        # Company often in h2 or specific classes
        company_elem = (soup.select_one('h2') or 
                       soup.select_one('.company') or
                       soup.select_one('.employer'))
        if company_elem:
            job_data['company'] = company_elem.get_text(strip=True)
        else:
            job_data['company'] = "Unknown Company"
        
        # Description - try main content areas
        desc_elem = (soup.select_one('main') or 
                    soup.select_one('article') or 
                    soup.select_one('.content') or
                    soup.select_one('.description') or
                    soup.select_one('.job-content'))
        if desc_elem:
            job_data['description'] = desc_elem.get_text(strip=True)
        else:
            job_data['description'] = soup.get_text(strip=True)
        
        return job_data
    
    def analyze_keywords(self, text):
        """Extract and analyze keywords from job description"""
        # Clean text
        text = re.sub(r'[^\w\s]', ' ', text.lower())
        text = re.sub(r'\s+', ' ', text)
        
        # Simple tokenization without NLTK dependency
        words = text.split()
        
        # Remove common stopwords
        stopwords = {
            'the', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by',
            'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had',
            'do', 'does', 'did', 'will', 'would', 'could', 'should', 'may', 'might',
            'a', 'an', 'this', 'that', 'these', 'those', 'we', 'you', 'they', 'it'
        }
        
        filtered_words = [w for w in words if w not in stopwords and len(w) > 2]
        
        # Count frequencies
        word_freq = Counter(filtered_words)
        
        # Extract technical terms and skills
        technical_patterns = [
            r'\b(azure|aws|gcp|kubernetes|docker|terraform|ansible)\b',
            r'\b(ci/cd|devops|finops|agile|scrum|safe)\b',
            r'\b(python|bash|powershell|jenkins|github)\b',
            r'\b(monitoring|automation|infrastructure|cloud)\b',
            r'\b(cost\s*optimization|cost\s*management)\b'
        ]
        
        technical_terms = []
        for pattern in technical_patterns:
            matches = re.findall(pattern, text, re.IGNORECASE)
            technical_terms.extend(matches)
        
        return {
            'word_frequency': dict(word_freq.most_common(50)),
            'technical_terms': list(set(technical_terms)),
            'top_keywords': [word for word, count in word_freq.most_common(20)]
        }
    
    def generate_dynamic_content(self, job_data, skill_analysis):
        """Generate dynamic content based on job requirements instead of fixed templates"""
        
        description = job_data.get('description', '').lower()
        title = job_data.get('title', '').lower()
        matched_skills = skill_analysis.get('matched_skills', [])
        
        # Only generate dynamic content if we have substantial job description
        description_length = len(description.split())
        if description_length < 10:
            return None  # Fall back to templates
        
        # Generate dynamic professional summary focus areas
        summary_focus = []
        if any(skill in ['Kubernetes', 'Docker', 'AKS'] for skill in matched_skills):
            summary_focus.append("container orchestration and cloud-native platforms")
        if any(skill in ['Terraform', 'ARM templates', 'Ansible'] for skill in matched_skills):
            summary_focus.append("Infrastructure-as-Code and automation")
        if any(skill in ['Azure DevOps', 'Jenkins', 'GitHub Actions'] for skill in matched_skills):
            summary_focus.append("CI/CD pipeline optimization")
        if 'cost' in description or 'finops' in description:
            summary_focus.append("cost optimization and FinOps practices")
        if 'monitor' in description or 'observability' in description:
            summary_focus.append("monitoring and observability solutions")
        
        # Only return focus areas if we found specific matches
        if not summary_focus:
            summary_focus = None
        
        # Generate enhanced core skills (use all your skills but prioritize matched ones)
        all_your_skills = []
        for category, skills in self.skill_mappings.get('your_skills', {}).items():
            all_your_skills.extend(skills)
        
        # Prioritize matched skills but include comprehensive skill set
        core_skills = []
        # First add matched skills
        for skill in matched_skills[:6]:  # Top 6 matched
            if skill not in core_skills:
                core_skills.append(skill)
        
        # Then add other important skills to maintain comprehensiveness
        important_base_skills = ['Azure', 'Terraform', 'Kubernetes', 'Docker', 'Python', 'Bash', 'PowerShell', 
                               'Prometheus', 'Grafana', 'Ansible', 'GitOps', 'Agile']
        for skill in important_base_skills:
            if skill in all_your_skills and skill not in core_skills and len(core_skills) < 12:
                core_skills.append(skill)
        
        # Generate dynamic experience bullets based on job requirements
        experience_bullets = []
        
        # Cloud platform bullets
        if any(platform in description for platform in ['azure', 'aws', 'cloud']):
            if 'Azure' in matched_skills:
                experience_bullets.append("Automated Azure infrastructure provisioning with Terraform and Azure Pipelines, reducing manual effort by 40%")
            if 'cost' in description:
                experience_bullets.append("Implemented cost optimization strategies using Azure Cost Management and Azure Policies, achieving 30% reduction in non-compliant resources")
        
        # Container/K8s bullets
        if any(tech in description for tech in ['kubernetes', 'docker', 'container', 'k8s']):
            experience_bullets.append("Designed and deployed GitOps-based Kubernetes platform using ArgoCD, Prometheus, and Grafana for scalable infrastructure automation")
        
        # CI/CD bullets
        if any(tech in description for tech in ['ci/cd', 'pipeline', 'jenkins', 'devops']):
            experience_bullets.append("Built robust CI/CD pipelines across Azure DevOps, Jenkins, and GitHub Actions, improving deployment efficiency and reliability")
        
        # Monitoring bullets
        if any(tech in description for tech in ['monitor', 'prometheus', 'grafana', 'observability']):
            experience_bullets.append("Strengthened operational reliability through KQL-driven monitoring and incident resolution, reducing downtime by 20%")
        
        return {
            'summary_focus': summary_focus,
            'experience_bullets': experience_bullets if experience_bullets else None,
            'core_skills': core_skills if len(core_skills) >= 6 else None,  # Only use if substantial
        }

    def map_to_existing_skills(self, job_keywords):
        """Map job requirements to your existing skills"""
        matched_skills = []
        skill_emphasis = {}
        
        # Map keywords to your actual skills
        for keyword in job_keywords['technical_terms'] + job_keywords['top_keywords']:
            keyword_lower = keyword.lower()
            
            # Direct skill matching
            for skill_category, skills in self.skill_mappings['your_skills'].items():
                for skill in skills:
                    if keyword_lower in skill.lower() or skill.lower() in keyword_lower:
                        matched_skills.append(skill)
                        skill_emphasis[skill] = skill_emphasis.get(skill, 0) + 1
            
            # Keyword mapping
            if keyword_lower in self.skill_mappings['keyword_mappings']:
                mapped_skills = self.skill_mappings['keyword_mappings'][keyword_lower]
                matched_skills.extend(mapped_skills)
                for skill in mapped_skills:
                    skill_emphasis[skill] = skill_emphasis.get(skill, 0) + 2
        
        return {
            'matched_skills': list(set(matched_skills)),
            'skill_emphasis': skill_emphasis,
            'priority_skills': sorted(skill_emphasis.items(), key=lambda x: x[1], reverse=True)[:10]
        }
    
    def generate_tailored_config(self, job_data, skill_analysis, output_type='devops'):
        """Generate configuration for tailored resume/cover letter"""
        
        # Determine role type from job title and description
        title_lower = job_data['title'].lower()
        description_lower = job_data.get('description', '').lower()
        
        # Check if leadership skills are explicitly mentioned in job description
        # Only apply leadership emphasis if job explicitly asks for it
        leadership_keywords = ['lead', 'leadership', 'mentor', 'manage', 'team lead', 'technical lead', 'supervise', 'coordinate team']
        has_leadership_requirements = any(keyword in description_lower for keyword in leadership_keywords)
        
        # Also check if description is too minimal (likely scraping issue)
        description_length = len(description_lower.split())
        is_minimal_description = description_length < 10
        
        if 'architect' in title_lower:
            base_config = 'cloud-architect'
        elif 'azure' in title_lower:
            base_config = 'azure-specialist'
        elif ('senior' in title_lower or 'lead' in title_lower) and has_leadership_requirements and not is_minimal_description:
            base_config = 'senior-devops'
        else:
            # Default to regular devops config unless leadership is explicitly required
            base_config = 'devops-engineer'
        
        # Load base configuration
        base_config_path = self.base_dir / "configs" / f"{base_config}.yaml"
        try:
            with open(base_config_path, 'r', encoding='utf-8') as f:
                config = yaml.safe_load(f)
        except FileNotFoundError:
            config = {
                'role': job_data['title'],
                'location': 'Stockholm, Sweden',
                'focus': 'tailored'
            }
        
        # Customize based on job analysis
        config['role'] = job_data['title']
        config['target_company'] = job_data['company']
        config['job_url'] = job_data.get('url', '')
        
        # Generate dynamic content based on job requirements
        dynamic_content = self.generate_dynamic_content(job_data, skill_analysis)
        
        # Update skills based on analysis
        priority_skills = [skill for skill, weight in skill_analysis['priority_skills']]
        config['priority_skills'] = priority_skills[:8]
        config['matched_skills'] = skill_analysis['matched_skills']
        
        # Add dynamic content to config only if substantial
        if dynamic_content:
            if dynamic_content['summary_focus']:
                config['dynamic_summary_focus'] = dynamic_content['summary_focus']
            if dynamic_content['experience_bullets']:
                config['dynamic_experience_bullets'] = dynamic_content['experience_bullets']
            if dynamic_content['core_skills']:
                config['dynamic_core_skills'] = dynamic_content['core_skills']
        
        # Apply GPT enhancement if enabled
        if self.use_gpt:
            print("🤖 Applying GPT enhancements...")
            self.apply_gpt_enhancements(config, job_data, skill_analysis)
        
        # Add job-specific keywords for ATS optimization
        job_technical_terms = job_data.get('technical_terms', [])
        if not job_technical_terms:
            # Extract from keyword analysis if available
            keyword_analysis = self.analyze_keywords(job_data.get('description', ''))
            job_technical_terms = keyword_analysis.get('technical_terms', [])
        
        config['ats_keywords'] = list(set(job_technical_terms + priority_skills))[:15]
        
        return config
    
    def apply_gpt_enhancements(self, config, job_data, skill_analysis):
        """Apply GPT enhancements to config content"""
        
        try:
            # Load base content blocks for current summary
            base_path = self.base_dir / "base" / "core-content-blocks.yaml"
            with open(base_path, 'r', encoding='utf-8') as f:
                content_blocks = yaml.safe_load(f)
            
            # Get current summary
            summary_type = config.get('summary_type', 'devops_focused')
            current_summary = content_blocks.get('summaries', {}).get(summary_type, 'DevOps Engineer with 8+ years of experience')
            
            # Enhance professional summary
            enhanced_summary = self.gpt_enhancer.enhance_professional_summary(
                current_summary, 
                job_data, 
                skill_analysis.get('matched_skills', [])
            )
            
            if enhanced_summary != current_summary:
                config['gpt_enhanced_summary'] = enhanced_summary
            
            # Enhance experience bullets if we have dynamic ones
            if config.get('dynamic_experience_bullets'):
                job_requirements = job_data.get('description', '')[:500]
                role_focus = config.get('focus', 'devops')
                
                enhanced_bullets = self.gpt_enhancer.enhance_experience_bullets(
                    config['dynamic_experience_bullets'],
                    job_requirements,
                    role_focus
                )
                
                if enhanced_bullets:
                    config['gpt_enhanced_bullets'] = enhanced_bullets
                    
        except Exception as e:
            print(f"⚠️ GPT enhancement failed: {e}")

    def save_analysis(self, job_data, analysis, config, output_name):
        """Save analysis results for reference"""
        analysis_data = {
            'job_posting': job_data,
            'keyword_analysis': analysis,
            'generated_config': config,
            'analysis_date': datetime.now().isoformat(),
            'recommendations': {
                'priority_skills': analysis['priority_skills'][:5],
                'ats_keywords': config.get('ats_keywords', []),
                'matched_skills': analysis['matched_skills']
            }
        }
        
        analysis_dir = self.base_dir / "analysis"
        analysis_dir.mkdir(exist_ok=True)
        
        output_path = analysis_dir / f"{output_name}_analysis.json"
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(analysis_data, f, indent=2, ensure_ascii=False)
        
        print(f"📊 Analysis saved: {output_path}")
        return output_path

def main():
    parser = argparse.ArgumentParser(
        description='Analyze job posting and generate tailored resume configuration',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python job_analyzer.py https://linkedin.com/jobs/view/123456789 --output telia-devops
  python job_analyzer.py https://company.breezy.hr/p/123456-job-title --output nordcloud-architect
        """
    )
    
    parser.add_argument('url', help='Job posting URL')
    parser.add_argument('--output', '-o', required=True, help='Output name for generated configs')
    parser.add_argument('--type', '-t', choices=['resume', 'cover', 'both'], default='both', 
                       help='Type of document to generate config for')
    parser.add_argument('--base-dir', help='Base directory path')
    
    args = parser.parse_args()
    
    # Initialize analyzer
    analyzer = JobAnalyzer(args.base_dir)
    
    print(f"🔍 Analyzing job posting: {args.url}")
    
    # Scrape job posting
    job_data = analyzer.scrape_job_posting(args.url)
    if not job_data:
        print("❌ Failed to scrape job posting")
        sys.exit(1)
    
    job_data['url'] = args.url
    
    print(f"✅ Job found: {job_data['title']} at {job_data['company']}")
    
    # Analyze keywords
    print("🔎 Analyzing keywords and requirements...")
    keyword_analysis = analyzer.analyze_keywords(job_data['description'])
    
    # Map to existing skills
    print("🎯 Mapping to your existing skills...")
    skill_analysis = analyzer.map_to_existing_skills(keyword_analysis)
    
    # Generate configurations
    print("⚙️ Generating tailored configurations...")
    config = analyzer.generate_tailored_config(job_data, skill_analysis)
    
    # Save analysis
    analysis_path = analyzer.save_analysis(job_data, skill_analysis, config, args.output)
    
    # Save generated config
    config_dir = analyzer.base_dir / "configs"
    config_path = config_dir / f"{args.output}_tailored.yaml"
    with open(config_path, 'w', encoding='utf-8') as f:
        yaml.dump(config, f, default_flow_style=False, allow_unicode=True)
    
    print(f"📋 Configuration saved: {config_path}")
    
    # Show recommendations
    print("\n🎯 Recommendations:")
    print("Top skills to emphasize:")
    for skill, weight in skill_analysis['priority_skills'][:5]:
        print(f"  • {skill} (weight: {weight})")
    
    print(f"\nMatched skills: {len(skill_analysis['matched_skills'])}")
    print(f"ATS keywords identified: {len(keyword_analysis['technical_terms'])}")
    
    print(f"\n✅ Ready to generate tailored resume with:")
    print(f"   bash resume-enhanced.sh generate {args.output}_tailored.yaml {args.output} \"{job_data['company']}\"")

if __name__ == "__main__":
    main()
