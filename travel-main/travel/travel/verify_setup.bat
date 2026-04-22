@echo off
REM Simple Django Setup Test

cd /d "c:\Users\user\Desktop\aleena project\travel"

echo.
echo ================================================
echo        DJANGO PROJECT VERIFICATION
echo ================================================
echo.

echo 1. Checking Python...
python --version
if %errorlevel% neq 0 (
    echo ERROR: Python not found. Please install Python.
    pause
    exit /b 1
)

echo.
echo 2. Checking Django...
python -m django --version
if %errorlevel% neq 0 (
    echo ERROR: Django not installed. Running: pip install django
    pip install django
)

echo.
echo 3. Running Django Check...
python manage.py check

echo.
echo 4. Creating database tables...
python manage.py migrate --run-syncdb

echo.
echo ================================================
echo ALL CHECKS COMPLETE!
echo ================================================
echo.
echo To start the server, run this in Command Prompt:
echo   python manage.py runserver
echo.
echo Then open your browser to: http://localhost:8000/
echo.
pause
