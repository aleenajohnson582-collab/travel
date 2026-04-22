@echo off
echo ========================================
echo   Django Server Startup
echo ========================================
echo.

cd /d "c:\Users\user\Desktop\aleena project\travel"

echo Checking Django installation...
python -m django --version

echo.
echo Running database migrations...
python manage.py migrate

echo.
echo Starting Django development server...
echo Server will run at: http://127.0.0.1:8000/
echo.
echo To stop the server, press CTRL+C
echo.

python manage.py runserver

pause
