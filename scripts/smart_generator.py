#!/usr/bin/env python3
"""
Smart Resume & Cover Letter Generator
Combines job analysis with document generation for perfectly tailored applications
"""

import argparse
import sys
from pathlib import Path
import yaml

# Import our custom modules
try:
    from job_analyzer import JobAnalyzer
    from generate_resume import ResumeGenerator
    from generate_cover_letter import CoverLetterGenerator
except ImportError as e:
    print(f"❌ Import error: {e}")
    print("Make sure all required scripts are in the scripts/ directory")
    sys.exit(1)

class SmartGenerator:
    def __init__(self, base_dir=None):
        self.base_dir = Path(base_dir) if base_dir else Path(__file__).parent.parent
        self.job_analyzer = JobAnalyzer(base_dir)
        self.resume_generator = ResumeGenerator(base_dir)
        self.cover_generator = CoverLetterGenerator(base_dir)
    
    def analyze_and_generate(self, job_url, output_name, doc_type='both'):
        """Complete workflow: analyze job posting and generate tailored documents"""
        
        print(f"🎯 Smart Generation Workflow Starting...")
        print(f"Job URL: {job_url}")
        print(f"Output: {output_name}")
        print(f"Type: {doc_type}")
        print("-" * 50)
        
        # Step 1: Analyze job posting
        print("🔍 Step 1: Analyzing job posting...")
        job_data = self.job_analyzer.scrape_job_posting(job_url)
        if not job_data:
            print("❌ Failed to analyze job posting")
            return False
        
        job_data['url'] = job_url
        print(f"✅ Found: {job_data['title']} at {job_data['company']}")
        
        # Step 2: Extract and map skills
        print("🔎 Step 2: Extracting requirements and mapping to your skills...")
        keyword_analysis = self.job_analyzer.analyze_keywords(job_data['description'])
        skill_analysis = self.job_analyzer.map_to_existing_skills(keyword_analysis)
        
        print(f"✅ Mapped {len(skill_analysis['matched_skills'])} relevant skills")
        
        # Step 3: Generate tailored configuration
        print("⚙️ Step 3: Creating optimized configuration...")
        config = self.job_analyzer.generate_tailored_config(job_data, skill_analysis)
        
        # Save configuration
        config_name = f"{output_name}_smart"
        config_path = self.base_dir / "configs" / f"{config_name}.yaml"
        with open(config_path, 'w', encoding='utf-8') as f:
            yaml.dump(config, f, default_flow_style=False, allow_unicode=True)
        
        print(f"✅ Configuration saved: {config_path}")
        
        # Step 4: Generate cover letter config if needed
        cover_config_name = None
        if doc_type in ['cover', 'both']:
            cover_config = self.create_cover_letter_config(config, job_data, skill_analysis)
            cover_config_name = f"cover-letter-{config_name}"
            cover_config_path = self.base_dir / "configs" / f"{cover_config_name}.yaml"
            with open(cover_config_path, 'w', encoding='utf-8') as f:
                yaml.dump(cover_config, f, default_flow_style=False, allow_unicode=True)
            print(f"✅ Cover letter config saved: {cover_config_path}")
        
        # Step 5: Generate documents
        print("📄 Step 4: Generating tailored documents...")
        
        success = True
        if doc_type in ['resume', 'both']:
            try:
                self.resume_generator.generate_resume(f"{config_name}.yaml", output_name, job_data['company'])
                print("✅ Resume generated successfully")
            except Exception as e:
                print(f"❌ Resume generation failed: {e}")
                success = False
        
        if doc_type in ['cover', 'both']:
            try:
                self.cover_generator.generate_cover_letter(f"{cover_config_name}.yaml", output_name, job_data['company'])
                print("✅ Cover letter generated successfully")
            except Exception as e:
                print(f"❌ Cover letter generation failed: {e}")
                success = False
        
        # Step 6: Save analysis
        print("📊 Step 5: Saving analysis for reference...")
        self.job_analyzer.save_analysis(job_data, skill_analysis, config, output_name)
        
        # Step 7: Show summary
        self.show_generation_summary(job_data, skill_analysis, output_name, doc_type)
        
        return success
    
    def create_cover_letter_config(self, resume_config, job_data, skill_analysis):
        """Create cover letter configuration based on resume config and job analysis"""
        
        # Determine cover letter style based on role
        title_lower = job_data['title'].lower()
        description_lower = job_data.get('description', '').lower()
        
        # Check if leadership skills are explicitly mentioned in job description
        leadership_keywords = ['lead', 'leadership', 'mentor', 'manage', 'team lead', 'technical lead', 'supervise', 'coordinate team']
        has_leadership_requirements = any(keyword in description_lower for keyword in leadership_keywords)
        
        # Also check if description is too minimal (likely scraping issue)
        description_length = len(description_lower.split())
        is_minimal_description = description_length < 10
        
        if 'architect' in title_lower:
            opening_type = "architect_focused"
            experience_focus = "cloud_architecture"
            technical_focus = "azure_focus"
            closing_type = "technical"
        elif ('senior' in title_lower or 'lead' in title_lower) and has_leadership_requirements and not is_minimal_description:
            opening_type = "senior_focused"
            experience_focus = "technical_leadership"
            technical_focus = "infrastructure_focus"
            closing_type = "enthusiastic"
        else:
            opening_type = "devops_focused"
            experience_focus = "devops_automation"
            technical_focus = "cicd_focus"
            closing_type = "standard"
        
        # Determine company type
        company_lower = job_data['company'].lower()
        if any(word in company_lower for word in ['consult', 'advisor', 'partner']):
            company_type = "consultancy"
        elif any(word in company_lower for word in ['startup', 'scale', 'growth']):
            company_type = "startup"
        else:
            company_type = "enterprise"
        
        cover_config = {
            'role': job_data['title'],
            'location': resume_config.get('location', 'Stockholm, Sweden'),
            'opening_type': opening_type,
            'experience_focus': experience_focus,
            'technical_focus': technical_focus,
            'company_type': company_type,
            'closing_type': closing_type,
            'target_company': job_data['company'],
            'priority_skills': [skill for skill, weight in skill_analysis['priority_skills'][:5]],
            'ats_keywords': resume_config.get('ats_keywords', [])
        }
        
        return cover_config
    
    def show_generation_summary(self, job_data, skill_analysis, output_name, doc_type):
        """Show summary of what was generated"""
        print("\n" + "="*60)
        print("🎉 SMART GENERATION COMPLETE!")
        print("="*60)
        
        print(f"📋 Job Details:")
        print(f"   Title: {job_data['title']}")
        print(f"   Company: {job_data['company']}")
        print(f"   URL: {job_data['url']}")
        
        print(f"\n🎯 Skills Analysis:")
        print(f"   Matched Skills: {len(skill_analysis['matched_skills'])}")
        print(f"   Top Priority Skills:")
        for skill, weight in skill_analysis['priority_skills'][:5]:
            print(f"     • {skill} (emphasis: {weight})")
        
        print(f"\n📄 Generated Files:")
        if doc_type in ['resume', 'both']:
            print(f"   Resume: versions/{output_name}.md")
        if doc_type in ['cover', 'both']:
            print(f"   Cover Letter: versions/{output_name}-cover-letter.md")
        
        print(f"\n📊 Analysis Files:")
        print(f"   Job Analysis: analysis/{output_name}_analysis.json")
        print(f"   Configuration: configs/{output_name}_smart.yaml")
        if doc_type in ['cover', 'both']:
            print(f"   Cover Config: configs/cover-letter-{output_name}_smart.yaml")
        
        print(f"\n✨ Your application is now perfectly tailored for this role!")
        print("="*60)

def main():
    parser = argparse.ArgumentParser(
        description='Smart generator: Analyze job posting and create tailored application',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python smart_generator.py https://linkedin.com/jobs/view/123456 --output telia-devops --type both
  python smart_generator.py https://nordcloud-career.breezy.hr/p/37592336774701 --output nordcloud-architect
        """
    )
    
    parser.add_argument('job_url', help='Job posting URL to analyze')
    parser.add_argument('--output', '-o', required=True, help='Output name for generated files')
    parser.add_argument('--type', '-t', choices=['resume', 'cover', 'both'], default='both',
                       help='Type of documents to generate (default: both)')
    parser.add_argument('--base-dir', help='Base directory path')
    
    args = parser.parse_args()
    
    # Initialize smart generator
    generator = SmartGenerator(args.base_dir)
    
    # Run the complete workflow
    success = generator.analyze_and_generate(args.job_url, args.output, args.type)
    
    if not success:
        print("\n❌ Generation completed with errors")
        sys.exit(1)
    else:
        print("\n✅ Smart generation completed successfully!")

if __name__ == "__main__":
    main()
