#!/bin/bash

# Resume Generator - Quick Commands
# Cross-platform shell script for Windows (bash) and macOS

# Use Python 3.11 specifically
PYTHON_CMD="/c/Users/mno527/AppData/Local/Programs/Python/Python311/python"

# Check if Python 3.11 is available
if [ ! -f "$PYTHON_CMD" ]; then
    echo "❌ Error: Python 3.11 not found at $PYTHON_CMD"
    echo "Please check your Python 3.11 installation"
    exit 1
fi

show_usage() {
    echo "Resume Generator - Quick Commands"
    echo
    echo "Usage:"
    echo "  ./resume.sh list                                    - List available configurations"
    echo "  ./resume.sh generate [config] [output] [company]    - Generate resume"
    echo "  ./resume.sh configs                                 - Show config files"
    echo "  ./resume.sh versions                                - Show generated versions"
    echo
    echo "Examples:"
    echo "  ./resume.sh generate devops-engineer.yaml arnab-dey-devops-telia Telia"
    echo "  ./resume.sh generate cloud-architect.yaml arnab-dey-architect-nordcloud Nordcloud"
    echo "  ./resume.sh generate azure-specialist.yaml arnab-dey-azure-general"
}

list_configs() {
    echo "📝 Available configurations:"
    $PYTHON_CMD scripts/generate_resume.py --list
}

generate_resume() {
    local config="$1"
    local output="$2"
    local company="$3"
    
    if [ -z "$config" ] || [ -z "$output" ]; then
        echo "❌ Error: Config and output parameters are required"
        show_usage
        exit 1
    fi
    
    if [ -n "$company" ]; then
        $PYTHON_CMD scripts/generate_resume.py "$config" "$output" --company "$company"
    else
        $PYTHON_CMD scripts/generate_resume.py "$config" "$output"
    fi
}

show_configs() {
    echo "📁 Configuration files:"
    if [ -d "configs" ]; then
        ls -1 configs/*.yaml 2>/dev/null | sed 's|configs/||' || echo "No configuration files found"
    else
        echo "No configs directory found"
    fi
}

show_versions() {
    echo "📁 Generated versions:"
    if [ -d "versions" ]; then
        ls -1 versions/*.md 2>/dev/null | sed 's|versions/||' || echo "No generated resumes found"
    else
        echo "No versions directory found"
    fi
}

# Main command processing
case "$1" in
    "list")
        list_configs
        ;;
    "generate")
        generate_resume "$2" "$3" "$4"
        ;;
    "configs")
        show_configs
        ;;
    "versions")
        show_versions
        ;;
    "help"|"--help"|"-h")
        show_usage
        ;;
    "")
        show_usage
        ;;
    *)
        echo "❌ Unknown command: $1"
        echo
        show_usage
        exit 1
        ;;
esac
