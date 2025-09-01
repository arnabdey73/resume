#!/usr/bin/env python3
"""
Resume Generator Script
Generates tailored resumes based on YAML configurations and Jinja2 templates
"""

import yaml
import argparse
import sys
from pathlib import Path
from jinja2 import Template, Environment, FileSystemLoader
from datetime import datetime

class ResumeGenerator:
    def __init__(self, base_dir=None):
        self.base_dir = Path(base_dir) if base_dir else Path(__file__).parent.parent
        self.env = Environment(loader=FileSystemLoader(str(self.base_dir)))
        
    def load_config(self, config_file):
        """Load configuration from YAML file"""
        config_path = self.base_dir / "configs" / config_file
        try:
            with open(config_path, 'r', encoding='utf-8') as f:
                return yaml.safe_load(f)
        except FileNotFoundError:
            print(f"❌ Error: Configuration file {config_path} not found")
            sys.exit(1)
        except yaml.YAMLError as e:
            print(f"❌ Error parsing YAML config: {e}")
            sys.exit(1)
    
    def load_content_blocks(self):
        """Load reusable content blocks"""
        content_path = self.base_dir / "base" / "core-content-blocks.yaml"
        try:
            with open(content_path, 'r', encoding='utf-8') as f:
                return yaml.safe_load(f)
        except FileNotFoundError:
            print(f"⚠️ Warning: Content blocks file not found at {content_path}")
            return {}
        except yaml.YAMLError as e:
            print(f"❌ Error parsing content blocks YAML: {e}")
            sys.exit(1)
    
    def generate_resume(self, config_file, output_name, company_name=None):
        """Generate a resume based on configuration"""
        
        print(f"🚀 Starting resume generation...")
        print(f"   Config: {config_file}")
        print(f"   Output: {output_name}.md")
        if company_name:
            print(f"   Company: {company_name}")
        
        # Load configuration and content
        config = self.load_config(config_file)
        content_blocks = self.load_content_blocks()
        
        # Load template
        template_path = "base/arnab-dey-template.md"
        try:
            template = self.env.get_template(template_path)
        except Exception as e:
            print(f"❌ Error loading template: {e}")
            sys.exit(1)
        
        # Prepare template variables
        template_vars = {
            'config': config,
            'content_blocks': content_blocks,
            'company_name': company_name,
            'generation_date': datetime.now().strftime("%Y-%m-%d"),
            'generation_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        # Render template
        try:
            resume_content = template.render(**template_vars)
        except Exception as e:
            print(f"❌ Error rendering template: {e}")
            sys.exit(1)
        
        # Ensure output directory exists
        output_dir = self.base_dir / "versions"
        output_dir.mkdir(exist_ok=True)
        
        # Write output
        output_path = output_dir / f"{output_name}.md"
        try:
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(resume_content)
            print(f"✅ Resume generated successfully!")
            
            # Show summary
            print(f"\n📋 Generation Summary:")
            print(f"   Role: {config.get('role', 'Unknown')}")
            print(f"   Location: {config.get('location', 'Unknown')}")
            print(f"   Focus: {config.get('focus', 'Unknown')}")
            print(f"   Company: {company_name or 'General'}")
            print(f"   Output: {output_path}")
            print(f"   Size: {output_path.stat().st_size} bytes")
            
        except Exception as e:
            print(f"❌ Error writing file: {e}")
            sys.exit(1)

    def list_configs(self):
        """List available configuration files"""
        configs_dir = self.base_dir / "configs"
        if not configs_dir.exists():
            print("❌ No configs directory found")
            return
        
        config_files = list(configs_dir.glob("*.yaml"))
        if not config_files:
            print("❌ No configuration files found")
            return
        
        print("📝 Available configurations:")
        for config_file in sorted(config_files):
            try:
                with open(config_file, 'r', encoding='utf-8') as f:
                    config = yaml.safe_load(f)
                role = config.get('role', 'Unknown')
                focus = config.get('focus', 'Unknown')
                print(f"   {config_file.name} - {role} ({focus})")
            except:
                print(f"   {config_file.name} - (Error loading)")

def main():
    parser = argparse.ArgumentParser(
        description='Generate tailored resume based on configuration',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python generate_resume.py devops-engineer.yaml arnab-dey-devops-telia --company Telia
  python generate_resume.py cloud-architect.yaml arnab-dey-architect-nordcloud --company Nordcloud
  python generate_resume.py azure-specialist.yaml arnab-dey-azure-microsoft --company Microsoft
  python generate_resume.py --list  # List available configurations
        """
    )
    
    parser.add_argument('config', nargs='?', help='Configuration file name (e.g., devops-engineer.yaml)')
    parser.add_argument('output', nargs='?', help='Output filename (without .md extension)')
    parser.add_argument('--company', '-c', help='Company name for customization')
    parser.add_argument('--base-dir', help='Base directory path (default: script parent directory)')
    parser.add_argument('--list', '-l', action='store_true', help='List available configurations')
    
    args = parser.parse_args()
    
    # Initialize generator
    generator = ResumeGenerator(args.base_dir)
    
    # Handle list command
    if args.list:
        generator.list_configs()
        return
    
    # Validate required arguments
    if not args.config or not args.output:
        parser.print_help()
        return
    
    # Generate resume
    generator.generate_resume(args.config, args.output, args.company)

if __name__ == "__main__":
    main()
