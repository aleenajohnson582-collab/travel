@echo off
REM Fix Create Account Issue - Generate and Apply Migrations
REM This script will create the missing User table in the database

echo.
echo ========================================
echo FIXING CREATE ACCOUNT ISSUE
echo ========================================
echo.

cd /d "c:\Users\user\Desktop\aleena project\travel"

echo [1/3] Creating new migrations for User model...
python manage.py makemigrations
if %errorlevel% neq 0 (
    echo ERROR: Failed to create migrations
    pause
    exit /b 1
)

echo.
echo [2/3] Applying migrations to database...
python manage.py migrate
if %errorlevel% neq 0 (
    echo ERROR: Failed to apply migrations
    pause
    exit /b 1
)

echo.
echo [3/3] Checking Django setup...
python manage.py check
if %errorlevel% neq 0 (
    echo ERROR: Django configuration issues detected
    pause
    exit /b 1
)

echo.
echo ========================================
echo ✓ SUCCESS! Database is now fixed!
echo ========================================
echo.
echo Your "Create Account" should now work!
echo.
echo Next: Run the server with:
echo   python manage.py runserver
echo.
pause
