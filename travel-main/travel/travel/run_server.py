#!/usr/bin/env python
"""
Quick start script for the Django project
"""
import os
import sys
import subprocess

# Change to project directory
project_dir = r"c:\Users\user\Desktop\aleena project\travel"
os.chdir(project_dir)

print("=" * 50)
print("  Django Server Startup")
print("=" * 50)
print()

# Check Django
print("✓ Checking Django installation...")
os.system("python -m django --version")

# Run migrations
print("\n✓ Running database migrations...")
os.system("python manage.py migrate")

# Start server
print("\n✓ Starting Django development server...")
print("\n  Server will run at: http://127.0.0.1:8000/")
print("  Press CTRL+C to stop the server\n")

os.system("python manage.py runserver")
