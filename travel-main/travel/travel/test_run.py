#!/usr/bin/env python
"""
Test script to check Django setup
"""
import os
import sys
import django

# Add the project directory to path
sys.path.insert(0, os.path.dirname(__file__))

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'travel.settings')
django.setup()

print("✓ Django setup successful!")

# Test imports
try:
    from tour.models import User, Booking
    print("✓ Models imported successfully!")
except Exception as e:
    print(f"✗ Error importing models: {e}")
    sys.exit(1)

# Test views
try:
    from tour.views import home, login_views, logout_views
    print("✓ Views imported successfully!")
except Exception as e:
    print(f"✗ Error importing views: {e}")
    sys.exit(1)

print("\n✓ All tests passed! Your Django project is ready to run.")
print("\nTo run the server, use: python manage.py runserver")
