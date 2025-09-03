#!/bin/bash

# Smart Resume & Cover Letter Generation Script
# Includes job posting analysis and intelligent document generation

# Color codes for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
NC='\033[0m' # No Color

# Set Python command to system default
PYTHON_CMD="/c/Users/mno527/AppData/Local/Programs/Python/Python311/python"

print_help() {
    echo -e "${BLUE}Smart Resume & Cover Letter Generator${NC}"
    echo ""
    echo "Usage: $0 [COMMAND] [OPTIONS]"
    echo ""
    echo -e "${PURPLE}Smart Commands:${NC}"
    echo "  smart [job-url] [output-name]           - Analyze job & generate tailored docs"
    echo "  analyze [job-url] [output-name]         - Only analyze job posting"
    echo ""
    echo -e "${BLUE}Manual Commands:${NC}"
    echo "  generate [config] [output] [company]    - Generate resume manually"
    echo "  cover [config] [output] [company]       - Generate cover letter manually"
    echo "  both [resume-config] [cover-config] [output] [company] - Generate both manually"
    echo ""
    echo -e "${YELLOW}Utility Commands:${NC}"
    echo "  list                                    - List available configurations"
    echo "  configs                                 - Show configuration files"
    echo "  versions                                - Show generated versions"
    echo "  analysis                                - Show job analysis files"
    echo ""
    echo -e "${GREEN}Examples:${NC}"
    echo "  $0 smart https://linkedin.com/jobs/view/123456 telia-devops"
    echo "  $0 smart https://nordcloud-career.breezy.hr/p/37592336774701 nordcloud-architect"
    echo "  $0 analyze https://company.com/careers/job-posting my-analysis"
    echo ""
    echo -e "${PURPLE}Smart Generation Features:${NC}"
    echo "  • Automatically scrapes job postings from LinkedIn, Breezy HR, and other sites"
    echo "  • Analyzes job requirements and maps them to your existing skills"
    echo "  • Generates ATS-optimized resume and cover letter"
    echo "  • Creates detailed analysis reports for reference"
    echo "  • Only emphasizes skills you actually have (no fake additions)"
}

check_python() {
    if [ ! -f "$PYTHON_CMD" ]; then
        echo -e "${RED}❌ Python not found at: $PYTHON_CMD${NC}"
        echo "Please check your Python installation or update the PYTHON_CMD in this script"
        exit 1
    fi
}

check_dependencies() {
    echo -e "${YELLOW}🔍 Checking dependencies...${NC}"
    
    # Check if required Python packages are installed
    if ! "$PYTHON_CMD" -c "import requests, bs4, yaml" 2>/dev/null; then
        echo -e "${RED}❌ Missing required packages${NC}"
        echo "Installing required packages..."
        "$PYTHON_CMD" -m pip install requests beautifulsoup4 pyyaml jinja2
        if [ $? -ne 0 ]; then
            echo -e "${RED}❌ Failed to install packages${NC}"
            exit 1
        fi
        echo -e "${GREEN}✅ Packages installed successfully${NC}"
    else
        echo -e "${GREEN}✅ All dependencies available${NC}"
    fi
}

smart_generate() {
    local job_url=$1
    local output_name=$2
    local doc_type=${3:-"both"}
    
    if [ -z "$job_url" ] || [ -z "$output_name" ]; then
        echo -e "${RED}❌ Error: Missing arguments${NC}"
        echo "Usage: $0 smart [job-url] [output-name] [type]"
        echo "Example: $0 smart https://linkedin.com/jobs/view/123456 telia-devops both"
        exit 1
    fi
    
    check_python
    check_dependencies
    
    echo -e "${PURPLE}🤖 Starting Smart Generation...${NC}"
    echo -e "${BLUE}Job URL:${NC} $job_url"
    echo -e "${BLUE}Output:${NC} $output_name"
    echo -e "${BLUE}Type:${NC} $doc_type"
    echo ""
    
    # Create required directories
    mkdir -p analysis configs versions
    
    # Run smart generator
    "$PYTHON_CMD" scripts/smart_generator.py "$job_url" --output "$output_name" --type "$doc_type"
    
    if [ $? -eq 0 ]; then
        echo ""
        echo -e "${GREEN}🎉 Smart generation completed successfully!${NC}"
        echo -e "${BLUE}Check the 'versions' folder for your tailored documents.${NC}"
    else
        echo -e "${RED}❌ Smart generation failed${NC}"
        exit 1
    fi
}

analyze_only() {
    local job_url=$1
    local output_name=$2
    
    if [ -z "$job_url" ] || [ -z "$output_name" ]; then
        echo -e "${RED}❌ Error: Missing arguments${NC}"
        echo "Usage: $0 analyze [job-url] [output-name]"
        exit 1
    fi
    
    check_python
    check_dependencies
    
    echo -e "${YELLOW}🔍 Analyzing job posting only...${NC}"
    
    # Create required directories
    mkdir -p analysis configs
    
    # Run job analyzer only
    "$PYTHON_CMD" scripts/job_analyzer.py "$job_url" --output "$output_name"
}

list_analysis() {
    echo -e "${BLUE}📊 Job Analysis Files:${NC}"
    if [ -d "analysis" ]; then
        find analysis -name "*_analysis.json" -type f | sort | sed 's/analysis\//  /'
    else
        echo "  No analysis files found"
    fi
}

# Include all the original functions from resume-enhanced.sh
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
    
    echo ""
    echo -e "${PURPLE}🤖 Smart Generated Configurations:${NC}"
    if [ -d "configs" ]; then
        ls configs/*_smart.yaml 2>/dev/null | sed 's/configs\//  /' || echo "  No smart configs found"
    fi
}

show_configs() {
    echo -e "${BLUE}📁 All Configuration Files:${NC}"
    if [ -d "configs" ]; then
        find configs -name "*.yaml" -type f | sort
    else
        echo "configs/ directory not found"
    fi
}

show_versions() {
    echo -e "${BLUE}📄 Generated Documents:${NC}"
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
    "smart")
        smart_generate "$2" "$3" "$4"
        ;;
    "analyze")
        analyze_only "$2" "$3"
        ;;
    "list")
        list_configs
        ;;
    "configs")
        show_configs
        ;;
    "versions")
        show_versions
        ;;
    "analysis")
        list_analysis
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
