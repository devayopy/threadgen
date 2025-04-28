@echo off
echo Testing OpenAI API key...

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

REM Run the test script
echo Running OpenAI API test...
python test_openai.py
if %errorlevel% neq 0 (
    echo API key test failed. Please check the error message above.
    pause
    exit /b 1
) else (
    echo API key test passed successfully!
    echo You can now run the application with run.bat
)

pause 