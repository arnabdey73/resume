@echo off
echo Installing required Python packages...

REM Install packages using specific Python 3.11
"C:\Users\mno527\AppData\Local\Programs\Python\Python311\python.exe" -m pip install pyyaml jinja2

echo.
echo Testing package installation...
"C:\Users\mno527\AppData\Local\Programs\Python\Python311\python.exe" -c "import yaml; import jinja2; print('✅ All packages installed successfully')"

echo.
echo Generating first resume...
"C:\Users\mno527\AppData\Local\Programs\Python\Python311\python.exe" test_generation.py

pause
