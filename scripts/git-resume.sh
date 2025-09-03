#!/bin/bash

# Git Resume Management Script
# Helps manage branches and tags for resume versions

# Colors for better output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

show_usage() {
    echo -e "${BLUE}Git Resume Management${NC}"
    echo
    echo "Usage:"
    echo "  ./git-resume.sh init                           - Initialize git repository"
    echo "  ./git-resume.sh branch [branch-name]           - Create and switch to new branch"
    echo "  ./git-resume.sh tag [tag-name] [message]       - Tag current state"
    echo "  ./git-resume.sh list                           - List all branches and tags"
    echo "  ./git-resume.sh compare [tag1] [tag2]          - Compare two versions"
    echo "  ./git-resume.sh switch [branch-name]           - Switch to branch"
    echo "  ./git-resume.sh status                         - Show git status"
    echo
    echo "Examples:"
    echo "  ./git-resume.sh branch devops-engineer"
    echo "  ./git-resume.sh tag telia-devops-v1.0 'Applied to Telia DevOps role'"
    echo "  ./git-resume.sh compare v1.0-base telia-devops-v1.0"
}

init_repo() {
    if [ -d ".git" ]; then
        echo -e "${YELLOW}⚠️ Git repository already exists${NC}"
        return
    fi
    
    echo -e "${BLUE}🚀 Initializing git repository...${NC}"
    git init
    git add .
    git commit -m "Initial resume repository setup"
    git tag -a "v1.0-base" -m "Base resume template - initial version"
    echo -e "${GREEN}✅ Git repository initialized with base tag${NC}"
}

create_branch() {
    local branch_name="$1"
    if [ -z "$branch_name" ]; then
        echo -e "${RED}❌ Error: Branch name required${NC}"
        exit 1
    fi
    
    echo -e "${BLUE}🌿 Creating and switching to branch: $branch_name${NC}"
    git checkout -b "$branch_name"
    echo -e "${GREEN}✅ Branch '$branch_name' created and active${NC}"
}

create_tag() {
    local tag_name="$1"
    local message="$2"
    
    if [ -z "$tag_name" ]; then
        echo -e "${RED}❌ Error: Tag name required${NC}"
        exit 1
    fi
    
    if [ -z "$message" ]; then
        message="Tagged on $(date '+%Y-%m-%d %H:%M:%S')"
    fi
    
    echo -e "${BLUE}🏷️ Creating tag: $tag_name${NC}"
    git add .
    git commit -m "Updates for $tag_name" || echo "No changes to commit"
    git tag -a "$tag_name" -m "$message"
    echo -e "${GREEN}✅ Tag '$tag_name' created${NC}"
}

list_all() {
    echo -e "${BLUE}📋 Git Repository Status${NC}"
    echo
    echo -e "${YELLOW}Current branch:${NC}"
    git branch --show-current 2>/dev/null || echo "Not in a git repository"
    echo
    echo -e "${YELLOW}All branches:${NC}"
    git branch -a 2>/dev/null || echo "No branches found"
    echo
    echo -e "${YELLOW}All tags:${NC}"
    git tag -l 2>/dev/null || echo "No tags found"
}

compare_versions() {
    local tag1="$1"
    local tag2="$2"
    
    if [ -z "$tag1" ] || [ -z "$tag2" ]; then
        echo -e "${RED}❌ Error: Two tags required for comparison${NC}"
        exit 1
    fi
    
    echo -e "${BLUE}🔍 Comparing $tag1 vs $tag2${NC}"
    git diff "$tag1".."$tag2"
}

switch_branch() {
    local branch_name="$1"
    if [ -z "$branch_name" ]; then
        echo -e "${RED}❌ Error: Branch name required${NC}"
        exit 1
    fi
    
    echo -e "${BLUE}🔄 Switching to branch: $branch_name${NC}"
    git checkout "$branch_name"
}

show_status() {
    echo -e "${BLUE}📊 Git Status${NC}"
    git status
}

# Main command processing
case "$1" in
    "init")
        init_repo
        ;;
    "branch")
        create_branch "$2"
        ;;
    "tag")
        create_tag "$2" "$3"
        ;;
    "list")
        list_all
        ;;
    "compare")
        compare_versions "$2" "$3"
        ;;
    "switch")
        switch_branch "$2"
        ;;
    "status")
        show_status
        ;;
    "help"|"--help"|"-h")
        show_usage
        ;;
    "")
        show_usage
        ;;
    *)
        echo -e "${RED}❌ Unknown command: $1${NC}"
        echo
        show_usage
        exit 1
        ;;
esac
