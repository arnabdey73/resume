#!/usr/bin/env python3
"""
Generic Smart Resume & Cover Letter Generator
Combines job analysis with document generation for perfectly tailored applications

This is a generic version that can be customized for any user by editing configuration files.
"""

import argparse
import sys
from pathlib import Path
import yaml
import os

# Import our custom modules
try:
    from job_analyzer import JobAnalyzer
    from generate_resume import ResumeGenerator
    from generate_cover_letter import CoverLetterGenerator
except ImportError as e:
    print(f"❌ Import error: {e}")
    print("Make sure all required scripts are in the scripts/ directory")
    print("Run 'bash setup-generic.sh' to set up the environment")
    sys.exit(1)

class SmartGenerator:
    def __init__(self, base_dir=None):
        self.base_dir = Path(base_dir) if base_dir else Path(__file__).parent.parent
        
        # Check if configuration files exist
        self.check_configuration()
        
        self.job_analyzer = JobAnalyzer(base_dir)
        self.resume_generator = ResumeGenerator(base_dir)
        self.cover_generator = CoverLetterGenerator(base_dir)
    
    def check_configuration(self):
        """Check if required configuration files exist"""
        required_files = [
            "configs/personal-info.yaml",
            "configs/skill-mappings.yaml",
            "base/resume-template.md"
        ]
        
        missing_files = []
        for file_path in required_files:
            full_path = self.base_dir / file_path
            if not full_path.exists():
                missing_files.append(file_path)
        
        if missing_files:
            print("❌ Missing configuration files:")
            for file in missing_files:
                print(f"   - {file}")
            print("\n💡 Run 'bash setup-generic.sh' to create these files from examples")
            print("   Then edit them with your personal information and skills")
            sys.exit(1)
    
    def load_personal_config(self):
        """Load personal information from configuration"""
        try:
            config_path = self.base_dir / "configs" / "personal-info.yaml"
            with open(config_path, 'r', encoding='utf-8') as f:
                return yaml.safe_load(f)
        except Exception as e:
            print(f"❌ Error loading personal configuration: {e}")
            print("💡 Edit configs/personal-info.yaml with your details")
            sys.exit(1)
    
    def analyze_and_generate(self, job_url, output_name, doc_type='both'):
        """Complete workflow: analyze job posting and generate tailored documents"""
        
        # Load personal configuration
        personal_config = self.load_personal_config()
        user_name = personal_config.get('personal', {}).get('name', 'User')
        
        print(f"🎯 Smart Generation Workflow for {user_name}")
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
        
        if not keyword_analysis.get('mapped_skills'):
            print("⚠️  No skill mappings found - using default configuration")
        else:
            print(f"✅ Mapped {len(keyword_analysis['mapped_skills'])} relevant skills")
        
        # Step 3: Create role configuration
        print("⚙️  Step 3: Creating optimized role configuration...")
        role_config = self.create_optimized_role_config(job_data, keyword_analysis)
        
        # Save role configuration
        role_config_path = self.base_dir / "configs" / "role-templates" / f"{output_name}.yaml"
        with open(role_config_path, 'w', encoding='utf-8') as f:
            yaml.dump(role_config, f, default_flow_style=False, sort_keys=False)
        print(f"✅ Saved role config: {role_config_path}")
        
        # Step 4: Generate documents
        success = True
        
        if doc_type in ['resume', 'both']:
            print("📄 Step 4a: Generating tailored resume...")
            if self.resume_generator.generate_resume(str(role_config_path), output_name, job_data['company']):
                print(f"✅ Resume generated: versions/{output_name}.md")
            else:
                print("❌ Resume generation failed")
                success = False
        
        if doc_type in ['cover_letter', 'both']:
            print("📧 Step 4b: Generating tailored cover letter...")
            cover_config = self.create_cover_letter_config(job_data, keyword_analysis)
            cover_config_path = self.base_dir / "configs" / "cover-letter-templates" / f"{output_name}.yaml"
            
            with open(cover_config_path, 'w', encoding='utf-8') as f:
                yaml.dump(cover_config, f, default_flow_style=False, sort_keys=False)
            
            if self.cover_generator.generate_cover_letter(str(cover_config_path), output_name, job_data['company']):
                print(f"✅ Cover letter generated: versions/{output_name}-cover-letter.md")
            else:
                print("❌ Cover letter generation failed")
                success = False
        
        # Step 5: Save analysis
        analysis_data = {
            'job_posting': job_data,
            'keyword_analysis': keyword_analysis,
            'generated_configs': {
                'role_config': role_config_path.name if doc_type in ['resume', 'both'] else None,
                'cover_config': cover_config_path.name if doc_type in ['cover_letter', 'both'] else None
            },
            'generation_metadata': {
                'user': user_name,
                'output_name': output_name,
                'doc_type': doc_type,
                'success': success
            }
        }
        
        analysis_path = self.base_dir / "analysis" / f"{output_name}-analysis.json"
        import json
        with open(analysis_path, 'w', encoding='utf-8') as f:
            json.dump(analysis_data, f, indent=2, ensure_ascii=False)
        
        print("-" * 50)
        if success:
            print("🎉 Smart generation completed successfully!")
            print(f"📁 Generated files in: versions/")
            print(f"📊 Analysis saved: {analysis_path}")
        else:
            print("❌ Smart generation completed with errors")
        
        return success
    
    def create_optimized_role_config(self, job_data, keyword_analysis):
        """Create role configuration optimized for the specific job"""
        
        # Load personal info for defaults
        personal_config = self.load_personal_config()
        location = personal_config.get('personal', {}).get('location', 'Your City, State')
        
        # Determine role focus based on job title
        role_focus = self.determine_role_focus(job_data['title'])
        
        # Get mapped skills
        mapped_skills = keyword_analysis.get('mapped_skills', [])
        top_skills = mapped_skills[:6] if mapped_skills else ["Python", "JavaScript", "Cloud platforms"]
        
        # Create experience highlights based on keywords
        experience_highlights = self.create_experience_highlights(keyword_analysis)
        
        role_config = {
            'role': job_data['title'],
            'location': location,
            'focus': role_focus,
            'summary_focus': self.create_summary_focus(job_data, keyword_analysis),
            'core_skills_emphasis': top_skills,
            'experience_highlights': experience_highlights,
            'technical_strengths': self.create_technical_strengths(keyword_analysis),
            'soft_skills_focus': ["Problem-solving", "Team collaboration", "Communication", "Continuous learning"],
            'project_types': self.determine_project_types(role_focus),
            'education_focus': "computer_science"
        }
        
        return role_config
    
    def determine_role_focus(self, job_title):
        """Determine role focus based on job title"""
        title_lower = job_title.lower()
        
        if any(word in title_lower for word in ['frontend', 'front-end', 'react', 'vue', 'angular']):
            return 'frontend'
        elif any(word in title_lower for word in ['backend', 'back-end', 'api', 'server']):
            return 'backend'
        elif any(word in title_lower for word in ['devops', 'infrastructure', 'platform', 'sre']):
            return 'automation'
        elif any(word in title_lower for word in ['data', 'analytics', 'ml', 'ai']):
            return 'data'
        elif any(word in title_lower for word in ['mobile', 'ios', 'android']):
            return 'mobile'
        else:
            return 'fullstack'
    
    def create_summary_focus(self, job_data, keyword_analysis):
        """Create summary focus based on job analysis"""
        role_focus = self.determine_role_focus(job_data['title'])
        
        focus_map = {
            'frontend': 'frontend development and user experience',
            'backend': 'backend development and API design',
            'fullstack': 'full-stack development',
            'automation': 'infrastructure automation and DevOps',
            'data': 'data engineering and analytics',
            'mobile': 'mobile application development'
        }
        
        return focus_map.get(role_focus, 'software development')
    
    def create_experience_highlights(self, keyword_analysis):
        """Create experience highlights based on keyword analysis"""
        highlights = [
            "scalable applications",
            "collaborative development",
            "best practices implementation"
        ]
        
        # Add specific highlights based on mapped skills
        mapped_skills = keyword_analysis.get('mapped_skills', [])
        
        if any('cloud' in skill.lower() for skill in mapped_skills):
            highlights.append("cloud-native solutions")
        
        if any(skill.lower() in ['docker', 'kubernetes', 'ci/cd'] for skill in mapped_skills):
            highlights.append("automated deployment pipelines")
        
        if any('api' in skill.lower() for skill in mapped_skills):
            highlights.append("RESTful API development")
        
        return highlights[:5]  # Limit to 5 highlights
    
    def create_technical_strengths(self, keyword_analysis):
        """Create technical strengths based on analysis"""
        strengths = [
            "Software architecture",
            "Problem solving",
            "Code quality"
        ]
        
        mapped_skills = keyword_analysis.get('mapped_skills', [])
        
        if any('cloud' in skill.lower() for skill in mapped_skills):
            strengths.append("Cloud architecture")
        
        if any(skill.lower() in ['react', 'vue', 'angular'] for skill in mapped_skills):
            strengths.append("Modern web frameworks")
        
        if any('database' in skill.lower() for skill in mapped_skills):
            strengths.append("Database design")
        
        return strengths[:5]
    
    def determine_project_types(self, role_focus):
        """Determine project types based on role focus"""
        project_map = {
            'frontend': ["Web applications", "User interfaces", "Mobile apps"],
            'backend': ["API services", "Database systems", "Microservices"],
            'fullstack': ["Web applications", "API services", "Database systems"],
            'automation': ["CI/CD pipelines", "Infrastructure automation", "Monitoring systems"],
            'data': ["Data pipelines", "Analytics platforms", "ML models"],
            'mobile': ["Mobile applications", "Cross-platform apps", "API integrations"]
        }
        
        return project_map.get(role_focus, ["Web applications", "API services", "Cloud deployments"])
    
    def create_cover_letter_config(self, job_data, keyword_analysis):
        """Create cover letter configuration"""
        
        # Load personal info
        personal_config = self.load_personal_config()
        location = personal_config.get('personal', {}).get('location', 'Your City, State')
        
        # Determine company type
        company_type = self.determine_company_type(job_data['company'])
        
        config = {
            'role': job_data['title'],
            'location': location,
            'opening_type': 'technical_focused',
            'experience_focus': 'software_development',
            'technical_focus': self.get_technical_focus(job_data['title']),
            'company_type': company_type,
            'closing_type': 'enthusiastic'
        }
        
        # Add highlighted technologies if we have mapped skills
        mapped_skills = keyword_analysis.get('mapped_skills', [])
        if mapped_skills:
            config['highlight_technologies'] = mapped_skills[:3]
        
        return config
    
    def determine_company_type(self, company_name):
        """Determine company type based on name"""
        company_lower = company_name.lower()
        
        if any(word in company_lower for word in ['google', 'microsoft', 'amazon', 'apple', 'meta']):
            return 'tech_company'
        elif any(word in company_lower for word in ['consulting', 'consulting', 'accenture', 'deloitte']):
            return 'consulting'
        elif 'startup' in company_lower or len(company_name.split()) == 1:
            return 'startup'
        else:
            return 'enterprise'
    
    def get_technical_focus(self, job_title):
        """Get technical focus for cover letter"""
        role_focus = self.determine_role_focus(job_title)
        
        focus_map = {
            'frontend': 'frontend_focus',
            'backend': 'backend_focus',
            'fullstack': 'fullstack_development',
            'automation': 'infrastructure_automation',
            'data': 'data_engineering',
            'mobile': 'mobile_development'
        }
        
        return focus_map.get(role_focus, 'fullstack_development')

def main():
    parser = argparse.ArgumentParser(description="Generic Smart Resume & Cover Letter Generator")
    parser.add_argument('action', choices=['smart', 'check'], 
                       help='Action to perform')
    parser.add_argument('job_url', nargs='?', help='Job posting URL (for smart action)')
    parser.add_argument('output_name', nargs='?', help='Output file name (for smart action)')
    parser.add_argument('--type', choices=['resume', 'cover_letter', 'both'], 
                       default='both', help='Document type to generate')
    parser.add_argument('--base-dir', help='Base directory for the project')
    
    args = parser.parse_args()
    
    generator = SmartGenerator(args.base_dir)
    
    if args.action == 'check':
        # Just check configuration - this is handled in __init__
        print("✅ Configuration check passed!")
        personal_config = generator.load_personal_config()
        user_name = personal_config.get('personal', {}).get('name', 'Unknown')
        print(f"👤 Configured for: {user_name}")
        return
    
    elif args.action == 'smart':
        if not args.job_url or not args.output_name:
            print("❌ Smart generation requires job_url and output_name")
            parser.print_help()
            sys.exit(1)
        
        success = generator.analyze_and_generate(args.job_url, args.output_name, args.type)
        sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
