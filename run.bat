@echo off
echo Starting X Thread Generator...

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

REM Run the Flask application
echo Starting Flask server...
python run.py
if %errorlevel% neq 0 (
    echo Application exited with an error.
    pause
    exit /b 1
)

pause 