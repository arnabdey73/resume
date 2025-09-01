#!/usr/bin/env python3
"""
Quick test script to verify our resume generation system works
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Test imports
try:
    import yaml
    print("✅ PyYAML imported successfully")
except ImportError as e:
    print(f"❌ PyYAML import failed: {e}")

try:
    import jinja2
    print("✅ Jinja2 imported successfully")
except ImportError as e:
    print(f"❌ Jinja2 import failed: {e}")

# Test our script
try:
    from scripts.generate_resume import ResumeGenerator
    print("✅ ResumeGenerator imported successfully")
    
    # Test generation
    generator = ResumeGenerator()
    config_path = "devops-engineer.yaml"  # Just the filename, not the full path
    output_name = "test-resume"
    
    print(f"📄 Attempting to generate resume: {output_name}")
    result = generator.generate_resume(config_path, output_name)
    
    if result:
        print(f"✅ Resume generated successfully: {result}")
    else:
        print("❌ Resume generation failed")
        
except Exception as e:
    print(f"❌ Error testing resume generation: {e}")
    import traceback
    traceback.print_exc()
