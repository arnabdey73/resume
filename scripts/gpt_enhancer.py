#!/usr/bin/env python3
"""
GPT Content Enhancer
Uses OpenAI API to rewrite and improve resume/cover letter content
"""

import openai
import json
import yaml
from pathlib import Path
import os

class GPTEnhancer:
    def __init__(self, api_key=None, base_dir=None):
        """Initialize GPT enhancer with OpenAI API key"""
        self.base_dir = Path(base_dir) if base_dir else Path(__file__).parent.parent
        
        # Try to get API key from multiple sources
        self.api_key = self._get_api_key(api_key)
        
        if self.api_key:
            openai.api_key = self.api_key
    
    def _get_api_key(self, provided_key):
        """Get API key from various sources"""
        
        # 1. Use provided key
        if provided_key:
            return provided_key
        
        # 2. Check environment variable
        env_key = os.getenv('OPENAI_API_KEY')
        if env_key:
            return env_key
        
        # 3. Check .env file
        env_file = self.base_dir / '.env'
        if env_file.exists():
            try:
                with open(env_file, 'r') as f:
                    for line in f:
                        if line.startswith('OPENAI_API_KEY='):
                            key = line.split('=', 1)[1].strip().strip('"\'')
                            if key and key != 'your-api-key-here':
                                return key
            except Exception as e:
                print(f"Error reading .env file: {e}")
        
        # 4. Check config.yaml
        config_file = self.base_dir / 'config.yaml'
        if config_file.exists():
            try:
                with open(config_file, 'r') as f:
                    config = yaml.safe_load(f)
                    key = config.get('openai', {}).get('api_key')
                    if key and key != 'your-api-key-here':
                        return key
            except Exception as e:
                print(f"Error reading config.yaml: {e}")
        
        return None
        
    def enhance_professional_summary(self, current_summary, job_data, matched_skills):
        """Use GPT to rewrite professional summary for better fit"""
        
        if not self.api_key:
            print("⚠️ No OpenAI API key found. Skipping GPT enhancement.")
            return current_summary
        
        prompt = f"""
You are a professional resume writer. Rewrite this professional summary to be more compelling and tailored for the specific job.

Current Summary: {current_summary}

Job Title: {job_data.get('title', 'Unknown')}
Company: {job_data.get('company', 'Unknown')}
Job Description: {job_data.get('description', 'No description available')[:500]}
Matched Skills: {', '.join(matched_skills[:8])}

Guidelines:
- Keep it to 2-3 sentences
- Use specific metrics where possible
- Make it ATS-friendly with relevant keywords
- Sound professional, not overly promotional
- Focus on value delivery and impact
- Maintain truthfulness to the original content

Rewritten Summary:"""

        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a professional resume writer focused on creating compelling, truthful content."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=200,
                temperature=0.7
            )
            
            enhanced_summary = response.choices[0].message.content.strip()
            print("✅ Professional summary enhanced with GPT")
            return enhanced_summary
            
        except Exception as e:
            print(f"⚠️ GPT enhancement failed: {e}")
            return current_summary
    
    def enhance_experience_bullets(self, bullets, job_requirements, role_focus):
        """Use GPT to rewrite experience bullets for better job alignment"""
        
        if not self.api_key:
            return bullets
        
        bullets_text = '\n'.join([f"- {bullet}" for bullet in bullets])
        
        prompt = f"""
You are a professional resume writer. Rewrite these experience bullets to better align with the job requirements while maintaining truthfulness.

Current Bullets:
{bullets_text}

Job Requirements/Focus: {job_requirements}
Role Focus: {role_focus}

Guidelines:
- Keep the core achievements and metrics accurate
- Emphasize skills that match job requirements
- Use action verbs and quantify impact where possible
- Make it ATS-friendly with relevant keywords
- Maintain 3-4 bullets maximum
- Sound professional and impactful

Rewritten Bullets (return as a simple list):"""

        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a professional resume writer. Return only the bullet points, no additional text."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=300,
                temperature=0.7
            )
            
            enhanced_text = response.choices[0].message.content.strip()
            # Parse bullets from response
            enhanced_bullets = []
            for line in enhanced_text.split('\n'):
                line = line.strip()
                if line.startswith('- ') or line.startswith('• '):
                    enhanced_bullets.append(line[2:])
                elif line and not line.startswith('#'):
                    enhanced_bullets.append(line)
            
            if enhanced_bullets:
                print("✅ Experience bullets enhanced with GPT")
                return enhanced_bullets[:4]  # Max 4 bullets
            
        except Exception as e:
            print(f"⚠️ GPT bullet enhancement failed: {e}")
        
        return bullets
    
    def enhance_cover_letter_paragraph(self, paragraph, job_data, personal_context):
        """Use GPT to rewrite cover letter paragraphs for better personalization"""
        
        if not self.api_key:
            return paragraph
        
        prompt = f"""
You are a professional cover letter writer. Rewrite this paragraph to be more personalized and compelling for the specific job.

Current Paragraph: {paragraph}

Job Context:
- Title: {job_data.get('title', 'Unknown')}
- Company: {job_data.get('company', 'Unknown')}
- Description: {job_data.get('description', 'No description')[:300]}

Personal Context: {personal_context}

Guidelines:
- Make it more personal and specific to this role/company
- Show genuine interest and knowledge
- Maintain professional tone
- Keep to 3-4 sentences
- Be authentic, not generic

Rewritten Paragraph:"""

        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a professional cover letter writer focused on authentic, personalized content."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=200,
                temperature=0.8
            )
            
            enhanced_paragraph = response.choices[0].message.content.strip()
            print("✅ Cover letter paragraph enhanced with GPT")
            return enhanced_paragraph
            
        except Exception as e:
            print(f"⚠️ GPT paragraph enhancement failed: {e}")
            return paragraph

    def setup_api_key(self):
        """Help user set up OpenAI API key"""
        print("\n🔑 GPT Enhancement Setup")
        print("="*40)
        print("To use GPT enhancement, you need an OpenAI API key.")
        print("\nSteps to get API key:")
        print("1. Go to https://platform.openai.com/api-keys")
        print("2. Create a new API key")
        print("3. Set environment variable: OPENAI_API_KEY=your-key-here")
        print("4. Or add it to your .env file")
        print("\nExample:")
        print("export OPENAI_API_KEY='sk-...'")
        print("\n⚠️ Note: GPT API calls cost money based on usage")
