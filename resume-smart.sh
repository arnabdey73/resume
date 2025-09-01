#!/bin/bash

# Generic Smart Resume & Cover Letter Generator
# Configurable system for any user - edit configs/ to customize

set -e

# Configuration
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PYTHON_CMD="python3"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Check if Python command exists
if ! command -v $PYTHON_CMD &> /dev/null; then
    if command -v python &> /dev/null; then
        PYTHON_CMD="python"
    else
        echo -e "${RED}❌ Python not found. Please install Python 3.8+ and try again.${NC}"
        exit 1
    fi
fi

# Functions
check_setup() {
    echo -e "${BLUE}Checking setup...${NC}"
    
    # Check if configuration files exist
    local required_files=(
        "configs/personal-info.yaml"
        "configs/skill-mappings.yaml"
        "base/resume-template.md"
    )
    
    local missing_files=()
    for file in "${required_files[@]}"; do
        if [ ! -f "$file" ]; then
            missing_files+=("$file")
        fi
    done
    
    if [ ${#missing_files[@]} -gt 0 ]; then
        echo -e "${RED}❌ Missing required configuration files:${NC}"
        for file in "${missing_files[@]}"; do
            echo -e "   ${RED}✗${NC} $file"
        done
        echo -e "\n${YELLOW}💡 Run 'bash setup-generic.sh' to create these files${NC}"
        echo -e "${YELLOW}   Then edit them with your personal information${NC}"
        exit 1
    fi
    
    # Check if scripts directory exists
    if [ ! -d "scripts" ]; then
        echo -e "${RED}❌ scripts/ directory not found${NC}"
        exit 1
    fi
    
    # Check if Python packages are installed
    if ! $PYTHON_CMD -c "import requests, bs4, yaml, jinja2" 2>/dev/null; then
        echo -e "${RED}❌ Required Python packages not installed${NC}"
        echo -e "${YELLOW}💡 Run 'bash setup-generic.sh' to install them${NC}"
        exit 1
    fi
    
    echo -e "${GREEN}✅ Setup check passed${NC}"
}

show_help() {
    cat << EOF
${GREEN}Smart Resume & Cover Letter Generator${NC}

${BLUE}USAGE:${NC}
  bash resume-smart.sh [COMMAND] [OPTIONS]

${BLUE}COMMANDS:${NC}
  ${GREEN}smart${NC} [job-url] [output-name]    Generate from job posting URL
  ${GREEN}generate${NC} [role-config] [output]   Generate from role template
  ${GREEN}both${NC} [role-config] [cover-config] [output] [company]
                                     Generate both resume and cover letter
  ${GREEN}setup${NC}                           Check configuration setup
  ${GREEN}help${NC}                            Show this help message

${BLUE}EXAMPLES:${NC}
  # Smart generation from job posting
  bash resume-smart.sh smart https://linkedin.com/jobs/view/123456 my-application

  # Generate resume from role template
  bash resume-smart.sh generate configs/role-templates/software-engineer.yaml my-resume

  # Generate both resume and cover letter
  bash resume-smart.sh both configs/role-templates/devops-engineer.yaml configs/cover-letter-templates/devops.yaml cloud-role "Cloud Company"

  # Check setup
  bash resume-smart.sh setup

${BLUE}SMART GENERATION:${NC}
  Smart generation analyzes job postings and creates perfectly tailored documents:
  - Scrapes job requirements from career sites
  - Maps requirements to your actual skills (from skill-mappings.yaml)
  - Creates optimized configurations
  - Generates ATS-friendly documents

${BLUE}CONFIGURATION:${NC}
  - ${YELLOW}configs/personal-info.yaml${NC}     Your personal information
  - ${YELLOW}configs/skill-mappings.yaml${NC}    Your skills and keyword mappings
  - ${YELLOW}base/resume-template.md${NC}        Resume template (Jinja2)
  - ${YELLOW}configs/role-templates/${NC}        Role-specific configurations
  - ${YELLOW}configs/cover-letter-templates/${NC} Cover letter configurations

${BLUE}OUTPUT:${NC}
  - Generated documents: ${YELLOW}versions/${NC}
  - Analysis reports: ${YELLOW}analysis/${NC}

EOF
}

smart_generate() {
    local job_url="$1"
    local output_name="$2"
    local doc_type="${3:-both}"
    
    if [ -z "$job_url" ] || [ -z "$output_name" ]; then
        echo -e "${RED}❌ Smart generation requires job URL and output name${NC}"
        echo -e "${YELLOW}Usage: bash resume-smart.sh smart [job-url] [output-name]${NC}"
        exit 1
    fi
    
    echo -e "${GREEN}🎯 Starting smart generation...${NC}"
    echo -e "Job URL: ${BLUE}$job_url${NC}"
    echo -e "Output: ${BLUE}$output_name${NC}"
    echo -e "Type: ${BLUE}$doc_type${NC}"
    echo ""
    
    # Run the smart generator
    cd scripts
    $PYTHON_CMD smart_generator.py smart "$job_url" "$output_name" --type "$doc_type"
    local exit_code=$?
    cd ..
    
    if [ $exit_code -eq 0 ]; then
        echo -e "\n${GREEN}🎉 Smart generation completed successfully!${NC}"
        echo -e "${BLUE}📁 Check the versions/ directory for your generated documents${NC}"
    else
        echo -e "\n${RED}❌ Smart generation failed${NC}"
        exit 1
    fi
}

manual_generate() {
    local role_config="$1"
    local output_name="$2"
    local company_name="$3"
    
    if [ -z "$role_config" ] || [ -z "$output_name" ]; then
        echo -e "${RED}❌ Manual generation requires role config and output name${NC}"
        echo -e "${YELLOW}Usage: bash resume-smart.sh generate [role-config] [output-name] [company-name]${NC}"
        exit 1
    fi
    
    if [ ! -f "$role_config" ]; then
        echo -e "${RED}❌ Role configuration file not found: $role_config${NC}"
        exit 1
    fi
    
    echo -e "${GREEN}📄 Generating resume...${NC}"
    echo -e "Config: ${BLUE}$role_config${NC}"
    echo -e "Output: ${BLUE}$output_name${NC}"
    if [ -n "$company_name" ]; then
        echo -e "Company: ${BLUE}$company_name${NC}"
    fi
    echo ""
    
    # Run the resume generator
    cd scripts
    $PYTHON_CMD generate_resume.py "$role_config" "$output_name" "$company_name"
    local exit_code=$?
    cd ..
    
    if [ $exit_code -eq 0 ]; then
        echo -e "\n${GREEN}✅ Resume generated successfully!${NC}"
        echo -e "${BLUE}📁 Check: versions/$output_name.md${NC}"
    else
        echo -e "\n${RED}❌ Resume generation failed${NC}"
        exit 1
    fi
}

generate_both() {
    local role_config="$1"
    local cover_config="$2"
    local output_name="$3"
    local company_name="$4"
    
    if [ -z "$role_config" ] || [ -z "$cover_config" ] || [ -z "$output_name" ] || [ -z "$company_name" ]; then
        echo -e "${RED}❌ Both generation requires role config, cover config, output name, and company name${NC}"
        echo -e "${YELLOW}Usage: bash resume-smart.sh both [role-config] [cover-config] [output-name] [company-name]${NC}"
        exit 1
    fi
    
    echo -e "${GREEN}📄📧 Generating resume and cover letter...${NC}"
    
    # Generate resume
    manual_generate "$role_config" "$output_name" "$company_name"
    
    # Generate cover letter
    echo -e "\n${GREEN}📧 Generating cover letter...${NC}"
    cd scripts
    $PYTHON_CMD generate_cover_letter.py "$cover_config" "$output_name" "$company_name"
    local exit_code=$?
    cd ..
    
    if [ $exit_code -eq 0 ]; then
        echo -e "\n${GREEN}🎉 Both documents generated successfully!${NC}"
        echo -e "${BLUE}📁 Resume: versions/$output_name.md${NC}"
        echo -e "${BLUE}📁 Cover letter: versions/$output_name-cover-letter.md${NC}"
    else
        echo -e "\n${RED}❌ Cover letter generation failed${NC}"
        exit 1
    fi
}

setup_check() {
    echo -e "${GREEN}🔧 Configuration Check${NC}"
    echo -e "${GREEN}=====================${NC}\n"
    
    check_setup
    
    # Run Python configuration check
    cd scripts
    $PYTHON_CMD smart_generator.py check
    cd ..
    
    echo -e "\n${GREEN}🎉 Setup is complete and ready to use!${NC}"
    echo -e "\n${BLUE}Next steps:${NC}"
    echo -e "1. Try smart generation: ${YELLOW}bash resume-smart.sh smart [job-url] [output-name]${NC}"
    echo -e "2. Or manual generation: ${YELLOW}bash resume-smart.sh generate configs/role-templates/software-engineer.yaml test-output${NC}"
}

# Main script logic
main() {
    case "${1:-help}" in
        "smart")
            check_setup
            smart_generate "$2" "$3" "$4"
            ;;
        "generate")
            check_setup
            manual_generate "$2" "$3" "$4"
            ;;
        "both")
            check_setup
            generate_both "$2" "$3" "$4" "$5"
            ;;
        "setup")
            setup_check
            ;;
        "help"|"-h"|"--help")
            show_help
            ;;
        *)
            echo -e "${RED}❌ Unknown command: $1${NC}"
            echo ""
            show_help
            exit 1
            ;;
    esac
}

# Run main function with all arguments
main "$@"
