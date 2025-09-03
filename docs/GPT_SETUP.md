# GPT Enhancement Setup Guide

## 🤖 Adding GPT Integration to Your Resume Generator

You can now use OpenAI's GPT-4o to enhance your resume and cover letter content for better personalization and natural language.

## 📋 Setup Steps

### 1. Install OpenAI Package
```bash
pip install openai
```

### 2. Get OpenAI API Key
1. Go to [OpenAI API Keys](https://platform.openai.com/api-keys)
2. Create a new API key
3. Copy the key (starts with `sk-...`)

### 3. Configure API Key (Choose One Method)

**Option A: config.yaml file (Recommended)**
```yaml
# config.yaml
openai:
  api_key: "sk-your-api-key-here"
  model: "gpt-4o"
  max_tokens: 300
  temperature: 0.7
```

**Option B: .env file**
```bash
# .env
OPENAI_API_KEY=sk-your-api-key-here
```

**Option C: Environment Variable**
```bash
export OPENAI_API_KEY='sk-your-api-key-here'
```

## 🚀 Usage

### With GPT Enhancement
```bash
# Generate with GPT enhancements
bash resume-smart.sh smart https://linkedin.com/jobs/view/123456 company-role --gpt

# Examples
bash resume-smart.sh smart https://apply.workable.com/newcode/j/2AF4EC2A9B newcode-devops both --gpt
bash resume-smart.sh smart https://careers.nordcloud.com/jobs/architect nordcloud-architect resume --gpt
```

### Without GPT (Default)
```bash
# Regular generation (no GPT)
bash resume-smart.sh smart https://linkedin.com/jobs/view/123456 company-role
```

## ✨ What GPT Enhancement Does

### Professional Summary
- Rewrites summary to be more compelling and job-specific
- Uses natural language that doesn't sound AI-generated
- Incorporates job-specific keywords naturally
- Maintains truthfulness to your experience

### Experience Bullets
- Enhances bullet points to better match job requirements
- Improves language flow and impact
- Maintains your actual achievements and metrics
- Emphasizes relevant skills for the specific role

### Cover Letter Paragraphs
- Personalizes content for specific company/role
- Makes generic paragraphs more engaging
- Shows genuine interest and knowledge
- Maintains professional authenticity

## 💰 Cost Considerations

**Current Model: GPT-4o**
- Input: $2.50 per 1M tokens ($0.0025 per 1K)
- Output: $10.00 per 1M tokens ($0.01 per 1K)
- **Cost per resume:** ~$0.005 (half a cent)
- **50 resumes/month:** ~$0.25

**Model Alternatives:**
- `gpt-3.5-turbo`: ~$0.001 per resume (cheaper but lower quality)
- `gpt-4-turbo`: Similar cost to gpt-4o
- Enhancement only runs when substantial job description is available
- Falls back to templates if GPT fails or is unavailable

## 🔧 Configuration Options

You can customize GPT behavior in `config.yaml`:

```yaml
openai:
  model: "gpt-4o"          # or "gpt-3.5-turbo", "gpt-4-turbo"
  max_tokens: 300          # Max response length
  temperature: 0.7         # Creativity level (0.0-1.0)

generation:
  use_gpt_by_default: false    # Set to true to always use GPT
  fallback_to_templates: true  # Fallback if GPT fails
```

## 🔧 Troubleshooting

### Import Error

If you see "Import openai could not be resolved":

```bash
pip install openai
```

### API Key Issues

If you see "OpenAI API key not found":

- Check environment variable: `echo $OPENAI_API_KEY`
- Verify config.yaml has correct format and API key
- Verify .env file exists and has correct format
- Restart terminal after setting environment variable

### Enhancement Failures

If you see "GPT enhancement failed":

- Check API key is valid and has credits
- Verify internet connection
- System will fall back to regular generation

## 🛡️ Security Notes

- Never commit API keys to git repositories
- Use environment variables or .env files (add .env to .gitignore)
- Monitor API usage on OpenAI dashboard
- Set spending limits on your OpenAI account

## 📊 Example Output

**Before GPT:**
> DevOps Engineer with 8+ years of experience in cloud infrastructure and automation.

**After GPT-4o Enhancement:**
> Senior DevOps Engineer with 8+ years of proven expertise in Azure cloud architecture, CI/CD pipeline optimization, and Infrastructure-as-Code automation. Specialized in delivering scalable, cost-effective solutions that reduce operational overhead while maintaining enterprise-grade security and compliance standards.

The GPT enhancement makes content more natural, specific, and compelling while maintaining accuracy about your experience.

## 📁 File Organization

**Main Scripts:**
- `resume-smart.sh` - Main script for GPT-enhanced generation
- `scripts/` - All utility scripts and Python modules

**Configuration:**
- `config.yaml` - Main configuration (API keys, model settings)
- `.env` - Alternative API key storage
- `configs/` - Job-specific configuration templates

**Content:**
- `base/` - Resume and cover letter templates
- `docs/` - Documentation and setup guides
