#!/bin/bash

# Resume and Cover Letter Generation Script
# Cross-platform script for generating tailored resumes and cover letters

# Color codes for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Use Python 3.11 specifically
PYTHON_CMD="/c/Users/mno527/AppData/Local/Programs/Python/Python311/python"

print_help() {
    echo -e "${BLUE}Resume & Cover Letter Generator${NC}"
    echo ""
    echo "Usage: $0 [COMMAND] [OPTIONS]"
    echo ""
    echo "Commands:"
    echo "  list                                    - List available configurations"
    echo "  configs                                 - Show configuration files"
    echo "  versions                                - Show generated versions"
    echo "  generate [config] [output] [company]    - Generate resume"
    echo "  cover [config] [output] [company]       - Generate cover letter"
    echo "  both [resume-config] [cover-config] [output] [company] - Generate both"
    echo ""
    echo "Examples:"
    echo "  $0 generate devops-engineer.yaml arnab-dey-devops-telia Telia"
    echo "  $0 cover cover-letter-devops.yaml arnab-dey-devops-telia Telia"
    echo "  $0 both devops-engineer.yaml cover-letter-devops.yaml arnab-dey-devops-telia Telia"
}

check_python() {
    if [ ! -f "$PYTHON_CMD" ]; then
        echo -e "${RED}❌ Error: Python 3.11 not found at $PYTHON_CMD${NC}"
        echo "Please check your Python 3.11 installation"
        exit 1
    fi
}

list_configs() {
    echo -e "${BLUE}📋 Available Resume Configurations:${NC}"
    if [ -d "configs" ]; then
        ls configs/*.yaml 2>/dev/null | grep -v "cover-letter" | sed 's/configs\//  /' || echo "  No resume configs found"
    else
        echo "  configs/ directory not found"
    fi
    
    echo ""
    echo -e "${BLUE}📝 Available Cover Letter Configurations:${NC}"
    if [ -d "configs" ]; then
        ls configs/cover-letter*.yaml 2>/dev/null | sed 's/configs\//  /' || echo "  No cover letter configs found"
    else
        echo "  configs/ directory not found"
    fi
}

show_configs() {
    echo -e "${BLUE}📁 Configuration Files:${NC}"
    if [ -d "configs" ]; then
        find configs -name "*.yaml" -type f | sort
    else
        echo "configs/ directory not found"
    fi
}

show_versions() {
    echo -e "${BLUE}📄 Generated Versions:${NC}"
    if [ -d "versions" ]; then
        find versions -name "*.md" -type f | sort
    else
        echo "versions/ directory not found"
    fi
}

generate_resume() {
    local config=$1
    local output=$2
    local company=$3
    
    if [ -z "$config" ] || [ -z "$output" ]; then
        echo -e "${RED}❌ Error: Missing arguments${NC}"
        echo "Usage: $0 generate [config] [output] [company]"
        exit 1
    fi
    
    check_python
    
    echo -e "${YELLOW}🚀 Generating resume...${NC}"
    echo "   Config: $config"
    echo "   Output: $output"
    echo "   Company: ${company:-'General'}"
    echo ""
    
    if [ -n "$company" ]; then
        "$PYTHON_CMD" scripts/generate_resume.py "$config" "$output" --company "$company"
    else
        "$PYTHON_CMD" scripts/generate_resume.py "$config" "$output"
    fi
}

generate_cover_letter() {
    local config=$1
    local output=$2
    local company=$3
    
    if [ -z "$config" ] || [ -z "$output" ]; then
        echo -e "${RED}❌ Error: Missing arguments${NC}"
        echo "Usage: $0 cover [config] [output] [company]"
        exit 1
    fi
    
    check_python
    
    echo -e "${YELLOW}📝 Generating cover letter...${NC}"
    echo "   Config: $config"
    echo "   Output: $output"
    echo "   Company: ${company:-'General'}"
    echo ""
    
    if [ -n "$company" ]; then
        "$PYTHON_CMD" scripts/generate_cover_letter.py "$config" "$output" --company "$company"
    else
        "$PYTHON_CMD" scripts/generate_cover_letter.py "$config" "$output"
    fi
}

generate_both() {
    local resume_config=$1
    local cover_config=$2
    local output=$3
    local company=$4
    
    if [ -z "$resume_config" ] || [ -z "$cover_config" ] || [ -z "$output" ]; then
        echo -e "${RED}❌ Error: Missing arguments${NC}"
        echo "Usage: $0 both [resume-config] [cover-config] [output] [company]"
        exit 1
    fi
    
    echo -e "${BLUE}🎯 Generating complete application package...${NC}"
    echo ""
    
    # Generate resume
    generate_resume "$resume_config" "$output" "$company"
    echo ""
    
    # Generate cover letter
    generate_cover_letter "$cover_config" "$output" "$company"
    echo ""
    
    echo -e "${GREEN}✅ Complete application package generated!${NC}"
    echo -e "${BLUE}📦 Files created:${NC}"
    echo "   Resume: versions/${output}.md"
    echo "   Cover Letter: versions/${output}-cover-letter.md"
}

# Main script logic
case "$1" in
    "list")
        list_configs
        ;;
    "configs")
        show_configs
        ;;
    "versions")
        show_versions
        ;;
    "generate")
        generate_resume "$2" "$3" "$4"
        ;;
    "cover")
        generate_cover_letter "$2" "$3" "$4"
        ;;
    "both")
        generate_both "$2" "$3" "$4" "$5"
        ;;
    *)
        print_help
        ;;
esac
