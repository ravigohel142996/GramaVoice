@echo off
REM GramaVoice - Quick Start Script for Windows

echo =========================================
echo   GramaVoice - Setup ^& Launch Script
echo =========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed. Please install Python 3.8 or higher.
    exit /b 1
)

echo Python found
echo.

REM Create virtual environment if it doesn't exist
if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
    echo Virtual environment created
) else (
    echo Virtual environment already exists
)

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat

REM Install dependencies
echo Installing dependencies...
python -m pip install -q --upgrade pip
pip install -q -r requirements.txt
echo Dependencies installed
echo.

REM Copy .env.example to .env if not exists
if not exist ".env" (
    echo Creating .env file...
    copy .env.example .env
    echo .env file created
)

REM Create logs directory
if not exist "logs" mkdir logs

echo.
echo =========================================
echo   Starting GramaVoice Application
echo =========================================
echo.

REM Start backend
echo Starting Backend API server...
start "GramaVoice Backend" python backend/app/main.py

REM Wait for backend to start
timeout /t 5 /nobreak >nul

REM Start frontend
echo Starting Frontend application...
start "GramaVoice Frontend" streamlit run frontend/app.py

echo.
echo =========================================
echo   GramaVoice is now running!
echo =========================================
echo.
echo Access the application:
echo   Frontend: http://localhost:8501
echo   Backend API: http://localhost:8000
echo   API Docs: http://localhost:8000/docs
echo.
echo Close the terminal windows to stop the services
echo.

pause
