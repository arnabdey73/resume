#!/bin/bash

echo "🚀 Setting up Resume Generator..."

# Use Python 3.11 specifically
PYTHON_CMD="/c/Users/mno527/AppData/Local/Programs/Python/Python311/python"
PIP_CMD="/c/Users/mno527/AppData/Local/Programs/Python/Python311/Scripts/pip"

# Check if Python 3.11 is available
if [ ! -f "$PYTHON_CMD" ]; then
    echo "❌ Error: Python 3.11 not found at $PYTHON_CMD"
    echo "Please check your Python 3.11 installation"
    exit 1
fi

# Check if pip is available
if [ ! -f "$PIP_CMD" ]; then
    echo "⚠️ pip not found at $PIP_CMD, using python -m pip instead"
    PIP_CMD="$PYTHON_CMD -m pip"
fi

# Install required packages
echo "📦 Installing Python packages..."
$PIP_CMD install pyyaml jinja2

if [ $? -ne 0 ]; then
    echo "❌ Error installing packages"
    exit 1
fi

echo "✅ Python packages installed successfully!"
echo

# Verify installation
echo "🔍 Verifying installation..."
$PYTHON_CMD -c "import yaml, jinja2; print('✅ All packages imported successfully')"

if [ $? -ne 0 ]; then
    echo "❌ Package verification failed"
    exit 1
fi

echo
echo "🎉 Setup complete!"
echo
echo "📝 Available commands:"
echo "   ./resume.sh list"
echo "   ./resume.sh generate devops-engineer.yaml arnab-dey-devops-telia Telia"
echo "   ./resume.sh generate cloud-architect.yaml arnab-dey-architect-nordcloud Nordcloud"
echo
