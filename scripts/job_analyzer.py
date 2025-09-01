#!/usr/bin/env python3
"""
Generic Job Posting Analyzer
Scrapes and analyzes job postings to automatically tailor resumes and cover letters

This is a generic version that reads configuration from files rather than hardcoded values.
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

class JobAnalyzer:
    def __init__(self, base_dir=None):
        self.base_dir = Path(base_dir) if base_dir else Path(__file__).parent.parent
        self.load_skill_mappings()
        
    def load_skill_mappings(self):
        """Load mapping of job keywords to user's actual skills from configuration"""
        mapping_path = self.base_dir / "configs" / "skill-mappings.yaml"
        try:
            with open(mapping_path, 'r', encoding='utf-8') as f:
                self.skill_mappings = yaml.safe_load(f)
        except FileNotFoundError:
            print(f"❌ Skill mappings file not found at {mapping_path}")
            print("💡 Run 'bash setup-generic.sh' to create configuration files")
            sys.exit(1)
    
    def scrape_job_posting(self, url):
        """Scrape job posting from various career sites"""
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            }
            
            response = requests.get(url, headers=headers, timeout=30)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Determine site type and extract accordingly
            domain = urlparse(url).netloc.lower()
            
            if 'linkedin.com' in domain:
                return self.parse_linkedin_job(soup, url)
            elif 'breezy.hr' in domain:
                return self.parse_breezy_job(soup, url)
            elif 'greenhouse.io' in domain:
                return self.parse_greenhouse_job(soup, url)
            elif 'lever.co' in domain:
                return self.parse_lever_job(soup, url)
            elif 'workday.com' in domain:
                return self.parse_workday_job(soup, url)
            else:
                # Generic parsing for unknown sites
                return self.parse_generic_job(soup, url)
                
        except Exception as e:
            print(f"❌ Error scraping job posting: {e}")
            return None
    
    def parse_linkedin_job(self, soup, url):
        """Parse LinkedIn job posting"""
        try:
            # Extract job title
            title_elem = soup.find('h1', class_='top-card-layout__title') or soup.find('h1')
            title = title_elem.get_text(strip=True) if title_elem else "Unknown Position"
            
            # Extract company name
            company_elem = soup.find('a', class_='topcard__org-name-link') or soup.find('span', class_='topcard__flavor')
            company = company_elem.get_text(strip=True) if company_elem else "Unknown Company"
            
            # Extract location
            location_elem = soup.find('span', class_='topcard__flavor--bullet')
            location = location_elem.get_text(strip=True) if location_elem else "Unknown Location"
            
            # Extract job description
            desc_elem = soup.find('div', class_='show-more-less-html__markup') or soup.find('div', class_='description__text')
            description = desc_elem.get_text(strip=True) if desc_elem else ""
            
            return {
                'title': title,
                'company': company,
                'location': location,
                'description': description,
                'source': 'LinkedIn'
            }
        except Exception as e:
            print(f"❌ Error parsing LinkedIn job: {e}")
            return None
    
    def parse_breezy_job(self, soup, url):
        """Parse Breezy HR job posting"""
        try:
            title = soup.find('h1').get_text(strip=True) if soup.find('h1') else "Unknown Position"
            company = soup.find('h2').get_text(strip=True) if soup.find('h2') else "Unknown Company"
            
            # Location might be in various places
            location_elem = soup.find('div', class_='location') or soup.find('span', string=re.compile(r'Location|Remote'))
            location = location_elem.get_text(strip=True) if location_elem else "Unknown Location"
            
            # Description is usually in a div with job description content
            desc_elem = soup.find('div', class_='description') or soup.find('div', id='description')
            if not desc_elem:
                # Fallback: get all text content
                desc_elem = soup.find('body')
            
            description = desc_elem.get_text(strip=True) if desc_elem else ""
            
            return {
                'title': title,
                'company': company,
                'location': location,
                'description': description,
                'source': 'Breezy HR'
            }
        except Exception as e:
            print(f"❌ Error parsing Breezy job: {e}")
            return None
    
    def parse_greenhouse_job(self, soup, url):
        """Parse Greenhouse job posting"""
        try:
            title = soup.find('h1', class_='app-title').get_text(strip=True) if soup.find('h1', class_='app-title') else "Unknown Position"
            company = soup.find('span', class_='company-name').get_text(strip=True) if soup.find('span', class_='company-name') else "Unknown Company"
            location = soup.find('div', class_='location').get_text(strip=True) if soup.find('div', class_='location') else "Unknown Location"
            
            desc_elem = soup.find('div', id='content')
            description = desc_elem.get_text(strip=True) if desc_elem else ""
            
            return {
                'title': title,
                'company': company,
                'location': location,
                'description': description,
                'source': 'Greenhouse'
            }
        except Exception as e:
            print(f"❌ Error parsing Greenhouse job: {e}")
            return None
    
    def parse_lever_job(self, soup, url):
        """Parse Lever job posting"""
        try:
            title = soup.find('h2').get_text(strip=True) if soup.find('h2') else "Unknown Position"
            company = soup.find('div', class_='company-name').get_text(strip=True) if soup.find('div', class_='company-name') else "Unknown Company"
            location = soup.find('div', class_='location').get_text(strip=True) if soup.find('div', class_='location') else "Unknown Location"
            
            desc_elem = soup.find('div', class_='section-wrapper')
            description = desc_elem.get_text(strip=True) if desc_elem else ""
            
            return {
                'title': title,
                'company': company,
                'location': location,
                'description': description,
                'source': 'Lever'
            }
        except Exception as e:
            print(f"❌ Error parsing Lever job: {e}")
            return None
    
    def parse_workday_job(self, soup, url):
        """Parse Workday job posting"""
        try:
            title = soup.find('h1', {'data-automation-id': 'jobPostingHeader'}).get_text(strip=True) if soup.find('h1', {'data-automation-id': 'jobPostingHeader'}) else "Unknown Position"
            company = "Company"  # Workday doesn't always show company name clearly
            location = soup.find('dd', {'data-automation-id': 'locations'}).get_text(strip=True) if soup.find('dd', {'data-automation-id': 'locations'}) else "Unknown Location"
            
            desc_elem = soup.find('div', {'data-automation-id': 'jobPostingDescription'})
            description = desc_elem.get_text(strip=True) if desc_elem else ""
            
            return {
                'title': title,
                'company': company,
                'location': location,
                'description': description,
                'source': 'Workday'
            }
        except Exception as e:
            print(f"❌ Error parsing Workday job: {e}")
            return None
    
    def parse_generic_job(self, soup, url):
        """Generic parser for unknown job sites"""
        try:
            # Try to find title - usually h1 or first heading
            title_elem = soup.find('h1') or soup.find('h2') or soup.find('[class*="title"]') or soup.find('[class*="job"]')
            title = title_elem.get_text(strip=True) if title_elem else "Unknown Position"
            
            # Try to find company - look for common patterns
            company_elem = (soup.find('[class*="company"]') or 
                          soup.find('[class*="employer"]') or 
                          soup.find('h2'))
            company = company_elem.get_text(strip=True) if company_elem else "Unknown Company"
            
            # Try to find location
            location_elem = (soup.find('[class*="location"]') or 
                           soup.find('[class*="address"]'))
            location = location_elem.get_text(strip=True) if location_elem else "Unknown Location"
            
            # Get all text as description
            description = soup.get_text(strip=True)
            
            return {
                'title': title,
                'company': company,
                'location': location,
                'description': description,
                'source': 'Generic Parser'
            }
        except Exception as e:
            print(f"❌ Error with generic parsing: {e}")
            return None
    
    def extract_keywords(self, text):
        """Extract relevant keywords from job description"""
        # Convert to lowercase for analysis
        text_lower = text.lower()
        
        # Common technical keywords to look for
        technical_keywords = [
            # Programming languages
            'python', 'java', 'javascript', 'typescript', 'c#', 'c++', 'go', 'rust', 'ruby', 'php',
            # Web technologies
            'react', 'vue', 'angular', 'node.js', 'express', 'django', 'flask', 'spring',
            # Cloud platforms
            'aws', 'azure', 'gcp', 'google cloud', 'cloud', 'serverless',
            # DevOps tools
            'docker', 'kubernetes', 'jenkins', 'terraform', 'ansible', 'ci/cd',
            # Databases
            'postgresql', 'mysql', 'mongodb', 'redis', 'elasticsearch',
            # Methodologies
            'agile', 'scrum', 'kanban', 'devops', 'microservices'
        ]
        
        found_keywords = []
        for keyword in technical_keywords:
            if keyword in text_lower:
                found_keywords.append(keyword)
        
        # Also extract phrases that might be requirements
        requirement_patterns = [
            r'(\d+)\+?\s*years?\s+of\s+experience',
            r'experience\s+with\s+([^.,]+)',
            r'proficient\s+in\s+([^.,]+)',
            r'knowledge\s+of\s+([^.,]+)',
            r'skilled?\s+in\s+([^.,]+)'
        ]
        
        requirements = []
        for pattern in requirement_patterns:
            matches = re.finditer(pattern, text_lower)
            for match in matches:
                requirements.append(match.group(0))
        
        return {
            'technical_keywords': found_keywords,
            'requirements': requirements
        }
    
    def analyze_keywords(self, job_description):
        """Analyze job description and map to user's skills"""
        if not self.skill_mappings:
            print("⚠️  No skill mappings loaded")
            return {'mapped_skills': [], 'priority_keywords': [], 'unmapped_keywords': []}
        
        # Extract keywords from description
        keywords = self.extract_keywords(job_description)
        
        # Get user's skills from configuration
        your_skills = self.skill_mappings.get('your_skills', {})
        keyword_mappings = self.skill_mappings.get('keyword_mappings', {})
        
        # Flatten user's skills into a single list
        all_user_skills = []
        for category, skills in your_skills.items():
            if isinstance(skills, list):
                all_user_skills.extend(skills)
        
        # Map job requirements to user's skills
        mapped_skills = []
        priority_keywords = []
        
        # Check direct skill matches
        job_text_lower = job_description.lower()
        for skill in all_user_skills:
            if skill.lower() in job_text_lower:
                mapped_skills.append(skill)
        
        # Check keyword mappings
        for job_keyword, skill_list in keyword_mappings.items():
            if job_keyword.lower() in job_text_lower:
                priority_keywords.append(job_keyword)
                for skill in skill_list:
                    if skill not in mapped_skills:
                        mapped_skills.append(skill)
        
        # Find unmapped technical keywords
        unmapped_keywords = []
        for keyword in keywords['technical_keywords']:
            # Check if this keyword maps to any of user's skills
            mapped = False
            for job_keyword, skill_list in keyword_mappings.items():
                if keyword in job_keyword.lower():
                    mapped = True
                    break
            
            if not mapped and keyword not in [skill.lower() for skill in all_user_skills]:
                unmapped_keywords.append(keyword)
        
        return {
            'mapped_skills': list(set(mapped_skills)),  # Remove duplicates
            'priority_keywords': list(set(priority_keywords)),
            'unmapped_keywords': list(set(unmapped_keywords)),
            'extracted_keywords': keywords
        }
    
    def create_analysis_report(self, job_data, keyword_analysis):
        """Create a comprehensive analysis report"""
        report = {
            'job_posting': job_data,
            'analysis_date': datetime.now().isoformat(),
            'keyword_analysis': keyword_analysis,
            'recommendations': self.generate_recommendations(job_data, keyword_analysis)
        }
        
        return report
    
    def generate_recommendations(self, job_data, keyword_analysis):
        """Generate recommendations based on analysis"""
        recommendations = []
        
        mapped_skills = keyword_analysis.get('mapped_skills', [])
        unmapped_keywords = keyword_analysis.get('unmapped_keywords', [])
        
        if mapped_skills:
            recommendations.append(f"Emphasize these {len(mapped_skills)} relevant skills: {', '.join(mapped_skills[:5])}")
        
        if unmapped_keywords:
            recommendations.append(f"Consider learning these trending technologies: {', '.join(unmapped_keywords[:3])}")
        
        # Company-specific recommendations
        company_focus = self.skill_mappings.get('company_focus', {})
        company_name = job_data.get('company', '').lower()
        
        for company_pattern, focus_data in company_focus.items():
            if company_pattern.lower() in company_name:
                emphasize_skills = focus_data.get('emphasize', [])
                if emphasize_skills:
                    recommendations.append(f"For {job_data['company']}, emphasize: {', '.join(emphasize_skills)}")
                break
        
        return recommendations

def main():
    parser = argparse.ArgumentParser(description="Generic Job Posting Analyzer")
    parser.add_argument('job_url', help='URL of the job posting to analyze')
    parser.add_argument('--output', '-o', help='Output file for analysis report')
    parser.add_argument('--base-dir', help='Base directory for configuration files')
    
    args = parser.parse_args()
    
    analyzer = JobAnalyzer(args.base_dir)
    
    print(f"🔍 Analyzing job posting: {args.job_url}")
    
    # Scrape job posting
    job_data = analyzer.scrape_job_posting(args.job_url)
    if not job_data:
        print("❌ Failed to scrape job posting")
        sys.exit(1)
    
    print(f"✅ Found: {job_data['title']} at {job_data['company']}")
    
    # Analyze keywords
    keyword_analysis = analyzer.analyze_keywords(job_data['description'])
    
    # Create analysis report
    report = analyzer.create_analysis_report(job_data, keyword_analysis)
    
    # Print summary
    print(f"\n📊 Analysis Summary:")
    print(f"Mapped skills: {len(keyword_analysis['mapped_skills'])}")
    print(f"Priority keywords: {len(keyword_analysis['priority_keywords'])}")
    print(f"Unmapped keywords: {len(keyword_analysis['unmapped_keywords'])}")
    
    if keyword_analysis['mapped_skills']:
        print(f"\n✅ Your relevant skills:")
        for skill in keyword_analysis['mapped_skills'][:10]:
            print(f"  • {skill}")
    
    if keyword_analysis['unmapped_keywords']:
        print(f"\n⚠️  Skills mentioned but not in your profile:")
        for keyword in keyword_analysis['unmapped_keywords'][:5]:
            print(f"  • {keyword}")
    
    # Save report if requested
    if args.output:
        output_path = Path(args.output)
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        print(f"\n💾 Analysis report saved: {output_path}")

if __name__ == "__main__":
    main()
