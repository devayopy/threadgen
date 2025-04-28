@echo off
echo Fixing dependencies for X Thread Generator...

REM Check if virtual environment exists
if not exist venv (
    echo Virtual environment not found. Please run setup.bat first.
    pause
    exit /b 1
)

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate
if %errorlevel% neq 0 (
    echo Failed to activate virtual environment.
    exit /b 1
)

REM Uninstall problematic packages
echo Uninstalling werkzeug...
pip uninstall -y werkzeug
if %errorlevel% neq 0 (
    echo Warning: Failed to uninstall werkzeug, continuing anyway...
)

REM Install dependencies with specific versions
echo Reinstalling dependencies with correct versions...
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo Failed to install dependencies.
    pause
    exit /b 1
)

echo Dependencies fixed successfully!
echo You can now run the application with run.bat
pause 