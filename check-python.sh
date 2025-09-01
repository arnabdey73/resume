#!/bin/bash

echo "🐍 Python Version Detector"
echo "=========================="

# Common Python executable names to check
PYTHON_EXES=("python3.12" "python3.11" "python3.10" "python3.9" "python3" "python")

echo "Checking for available Python versions:"
echo

FOUND_VERSIONS=()

for py_exe in "${PYTHON_EXES[@]}"; do
    if command -v "$py_exe" &> /dev/null; then
        version=$($py_exe --version 2>&1)
        location=$(which "$py_exe")
        echo "✅ $py_exe: $version"
        echo "   Location: $location"
        FOUND_VERSIONS+=("$py_exe:$version:$location")
        echo
    fi
done

if [ ${#FOUND_VERSIONS[@]} -eq 0 ]; then
    echo "❌ No Python installations found"
    exit 1
fi

echo "=========================="
echo "Available Python versions: ${#FOUND_VERSIONS[@]}"
echo
echo "To use a specific version, you can:"
echo "1. Update your PATH to prioritize the desired version"
echo "2. Use the full path to the Python executable"
echo "3. Create an alias (e.g., alias python=/path/to/python3.12)"

# Find the latest version
echo
echo "💡 Recommendation:"
echo "Use the highest version number from the list above"
