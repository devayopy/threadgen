@echo off
echo Setting up X Thread Generator...

REM Create virtual environment
echo Creating virtual environment...
python -m venv venv
if %errorlevel% neq 0 (
    echo Failed to create virtual environment. Make sure Python is installed.
    exit /b 1
)

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate
if %errorlevel% neq 0 (
    echo Failed to activate virtual environment.
    exit /b 1
)

REM Install dependencies
echo Installing dependencies...
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo Failed to install dependencies.
    exit /b 1
)

echo Setup completed successfully!
echo.
echo To run the application:
echo 1. Ensure your virtual environment is activated: venv\Scripts\activate
echo 2. Run the application: python run.py
echo 3. Open your browser and go to: http://127.0.0.1:5000/
echo.
echo Note: Make sure to update your .env file with your actual OpenAI API key and social links.

REM Keep the window open
pause 