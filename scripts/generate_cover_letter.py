#!/usr/bin/env python3
"""
Cover Letter Generator Script
Generates tailored cover letters based on YAML configurations and Jinja2 templates
"""

import yaml
import argparse
import sys
from pathlib import Path
from jinja2 import Template, Environment, FileSystemLoader
from datetime import datetime

class CoverLetterGenerator:
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
        content_path = self.base_dir / "base" / "cover-letter-content-blocks.yaml"
        try:
            with open(content_path, 'r', encoding='utf-8') as f:
                return yaml.safe_load(f)
        except FileNotFoundError:
            print(f"⚠️ Warning: Content blocks file not found at {content_path}")
            return {}
        except yaml.YAMLError as e:
            print(f"❌ Error parsing content blocks: {e}")
            return {}
    
    def generate_cover_letter(self, config_file, output_name, company_name=None):
        """Generate a cover letter based on configuration"""
        
        print("🚀 Starting cover letter generation...")
        print(f"   Config: {config_file}")
        print(f"   Output: {output_name}-cover-letter.md")
        
        # Load configuration and content
        config = self.load_config(config_file)
        content_blocks = self.load_content_blocks()
        
        # Load template
        template_path = self.base_dir / "base" / "cover-letter-template.md"
        try:
            template = self.env.get_template("base/cover-letter-template.md")
        except Exception as e:
            print(f"❌ Error: Template file not found at {template_path}")
            print(f"   Details: {e}")
            sys.exit(1)
        
        # Prepare template variables
        template_vars = {
            'config': config,
            'content_blocks': content_blocks,
            'company_name': company_name,
            'generation_date': datetime.now().strftime("%B %d, %Y"),
            'generation_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        # Render template
        try:
            cover_letter_content = template.render(**template_vars)
        except Exception as e:
            print(f"❌ Error rendering template: {e}")
            sys.exit(1)
        
        # Ensure output directory exists
        output_dir = self.base_dir / "versions"
        output_dir.mkdir(exist_ok=True)
        
        # Write output
        output_path = output_dir / f"{output_name}-cover-letter.md"
        try:
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(cover_letter_content)
            
            # Get file size
            file_size = output_path.stat().st_size
            
            print("✅ Cover letter generated successfully!")
            print(f"\n📋 Generation Summary:")
            print(f"   Role: {config.get('role', 'Unknown')}")
            print(f"   Location: {config.get('location', 'Unknown')}")
            print(f"   Company: {company_name or 'General'}")
            print(f"   Output: {output_path}")
            print(f"   Size: {file_size} bytes")
            
            return str(output_path)
            
        except Exception as e:
            print(f"❌ Error writing file: {e}")
            sys.exit(1)

def main():
    parser = argparse.ArgumentParser(
        description='Generate tailored cover letter based on configuration',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python generate_cover_letter.py cover-letter-devops.yaml arnab-dey-devops-telia --company Telia
  python generate_cover_letter.py cover-letter-architect.yaml arnab-dey-architect-nordcloud --company Nordcloud
        """
    )
    
    parser.add_argument('config', help='Configuration file name (e.g., cover-letter-devops.yaml)')
    parser.add_argument('output', help='Output filename (without -cover-letter.md extension)')
    parser.add_argument('--company', '-c', help='Company name for customization')
    parser.add_argument('--base-dir', help='Base directory path (default: script parent directory)')
    
    args = parser.parse_args()
    
    # Generate cover letter
    generator = CoverLetterGenerator(args.base_dir)
    generator.generate_cover_letter(args.config, args.output, args.company)

if __name__ == "__main__":
    main()
