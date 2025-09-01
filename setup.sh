#!/bin/bash

# Generic Smart Resume Generator Setup Script
# This script sets up the environment for any user

set -e

echo "🚀 Setting up Smart Resume Generator..."

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Check if Python is installed
check_python() {
    echo -e "${BLUE}Checking Python installation...${NC}"
    
    if command -v python3 &> /dev/null; then
        PYTHON_CMD="python3"
    elif command -v python &> /dev/null; then
        PYTHON_CMD="python"
    else
        echo -e "${RED}❌ Python not found. Please install Python 3.8+ and try again.${NC}"
        exit 1
    fi
    
    # Check Python version
    PYTHON_VERSION=$($PYTHON_CMD --version 2>&1 | cut -d' ' -f2)
    echo -e "${GREEN}✅ Found Python $PYTHON_VERSION${NC}"
    
    # Check if version is 3.8+
    if $PYTHON_CMD -c "import sys; exit(0 if sys.version_info >= (3, 8) else 1)" 2>/dev/null; then
        echo -e "${GREEN}✅ Python version is compatible${NC}"
    else
        echo -e "${RED}❌ Python 3.8+ required. Found $PYTHON_VERSION${NC}"
        exit 1
    fi
}

# Install Python packages
install_packages() {
    echo -e "${BLUE}Installing required Python packages...${NC}"
    
    $PYTHON_CMD -m pip install --upgrade pip
    $PYTHON_CMD -m pip install requests beautifulsoup4 pyyaml jinja2
    
    echo -e "${GREEN}✅ Python packages installed${NC}"
}

# Create directory structure
create_directories() {
    echo -e "${BLUE}Creating directory structure...${NC}"
    
    mkdir -p configs/role-templates
    mkdir -p configs/cover-letter-templates
    mkdir -p versions
    mkdir -p analysis
    mkdir -p base
    
    echo -e "${GREEN}✅ Directories created${NC}"
}

# Copy example configurations
setup_configs() {
    echo -e "${BLUE}Setting up configuration files...${NC}"
    
    # Copy personal info if it doesn't exist
    if [ ! -f "configs/personal-info.yaml" ]; then
        cp examples/personal-info-example.yaml configs/personal-info.yaml
        echo -e "${YELLOW}📋 Created configs/personal-info.yaml - PLEASE EDIT WITH YOUR DETAILS${NC}"
    fi
    
    # Copy skills mapping if it doesn't exist
    if [ ! -f "configs/skill-mappings.yaml" ]; then
        cp examples/skill-mappings-example.yaml configs/skill-mappings.yaml
        echo -e "${YELLOW}📋 Created configs/skill-mappings.yaml - PLEASE EDIT WITH YOUR SKILLS${NC}"
    fi
    
    # Copy example role templates
    cp examples/software-engineer-example.yaml configs/role-templates/software-engineer.yaml
    cp examples/devops-engineer-example.yaml configs/role-templates/devops-engineer.yaml
    cp examples/cover-letter-software-engineer-example.yaml configs/cover-letter-templates/software-engineer.yaml
    
    # Copy base templates if they don't exist
    if [ ! -f "base/resume-template.md" ]; then
        cp examples/resume-template-example.md base/resume-template.md
        echo -e "${YELLOW}📋 Created base/resume-template.md - CUSTOMIZE AS NEEDED${NC}"
    fi
    
    echo -e "${GREEN}✅ Configuration files set up${NC}"
}

# Create basic content blocks file
create_content_blocks() {
    if [ ! -f "base/content-blocks.yaml" ]; then
        cat > base/content-blocks.yaml << 'EOL'
# Content blocks for resume generation
# Customize these blocks with your actual experience

professional_summaries:
  software_engineer: "Experienced software engineer with expertise in full-stack development"
  devops_engineer: "DevOps engineer specializing in cloud infrastructure and automation"
  data_scientist: "Data scientist with strong background in machine learning and analytics"

experience_templates:
  senior_level:
    - "Led development of scalable applications"
    - "Mentored junior team members"
    - "Designed system architecture"
  
  mid_level:
    - "Developed and maintained applications"
    - "Collaborated with cross-functional teams"
    - "Implemented best practices"
  
  junior_level:
    - "Contributed to feature development"
    - "Learned new technologies quickly"
    - "Supported team objectives"

achievements:
  performance:
    - "Improved system performance by X%"
    - "Reduced deployment time by X minutes"
    - "Optimized database queries for faster response"
  
  leadership:
    - "Led team of X developers"
    - "Mentored X junior engineers"
    - "Established coding standards"
  
  business_impact:
    - "Increased user engagement by X%"
    - "Reduced operational costs by X%"
    - "Delivered project X weeks ahead of schedule"
EOL
        echo -e "${GREEN}✅ Created base/content-blocks.yaml${NC}"
    fi
}

# Make scripts executable
setup_scripts() {
    echo -e "${BLUE}Setting up scripts...${NC}"
    
    # Make shell scripts executable
    chmod +x *.sh
    
    echo -e "${GREEN}✅ Scripts configured${NC}"
}

# Test the setup
test_setup() {
    echo -e "${BLUE}Testing the setup...${NC}"
    
    # Test Python imports
    if $PYTHON_CMD -c "import requests, bs4, yaml, jinja2" 2>/dev/null; then
        echo -e "${GREEN}✅ All Python packages importable${NC}"
    else
        echo -e "${RED}❌ Some Python packages failed to import${NC}"
        exit 1
    fi
    
    # Test script existence
    if [ -f "resume-smart.sh" ]; then
        echo -e "${GREEN}✅ Main script found${NC}"
    else
        echo -e "${RED}❌ Main script not found${NC}"
        exit 1
    fi
    
    echo -e "${GREEN}✅ Setup test passed${NC}"
}

# Show next steps
show_next_steps() {
    echo -e "\n${GREEN}🎉 Setup completed successfully!${NC}\n"
    
    echo -e "${YELLOW}📝 NEXT STEPS:${NC}"
    echo -e "1. Edit ${BLUE}configs/personal-info.yaml${NC} with your personal details"
    echo -e "2. Edit ${BLUE}configs/skill-mappings.yaml${NC} with your actual skills"
    echo -e "3. Customize ${BLUE}base/resume-template.md${NC} if needed"
    echo -e "4. Test with: ${BLUE}bash resume-smart.sh generate configs/role-templates/software-engineer.yaml test-output${NC}"
    echo -e "5. Try smart generation: ${BLUE}bash resume-smart.sh smart [job-url] [output-name]${NC}\n"
    
    echo -e "${GREEN}📚 Documentation: README-GENERIC.md${NC}"
    echo -e "${GREEN}📁 Examples: examples/ directory${NC}\n"
    
    echo -e "${BLUE}Happy job hunting! 🚀${NC}"
}

# Main execution
main() {
    echo -e "${GREEN}Smart Resume Generator Setup${NC}"
    echo -e "${GREEN}============================${NC}\n"
    
    check_python
    install_packages
    create_directories
    setup_configs
    create_content_blocks
    setup_scripts
    test_setup
    show_next_steps
}

# Run main function
main
