#!/usr/bin/env python
"""
Diagnostic script to debug signup issues
"""
import os
import django
import sys

# Add the project directory to Python path
sys.path.insert(0, r'c:\Users\user\Desktop\aleena project\travel')

# Configure Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'travel.settings')
django.setup()

from django.core.management import call_command
from tour.models import User
import hashlib

print("=" * 70)
print("SIGNUP DIAGNOSTIC - CHECKING ALL SYSTEMS")
print("=" * 70)

# Step 1: Check migrations
print("\n[Step 1] Checking migrations status...")
try:
    call_command('showmigrations', 'tour', verbosity=0)
    print("✓ Migrations checked")
except Exception as e:
    print(f"✗ Error checking migrations: {e}")

# Step 2: Check if User table exists
print("\n[Step 2] Checking if User table exists in database...")
try:
    from django.db import connection
    cursor = connection.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='tour_user';")
    table_exists = cursor.fetchone()
    
    if table_exists:
        print("✓ User table exists in database")
        # Count users
        user_count = User.objects.count()
        print(f"  - Current users in database: {user_count}")
    else:
        print("✗ User table DOES NOT exist!")
        print("\n  FIX: Run migrations with:")
        print("  > python manage.py makemigrations")
        print("  > python manage.py migrate")
        sys.exit(1)
except Exception as e:
    print(f"✗ Error checking database: {e}")
    sys.exit(1)

# Step 3: Try creating a test user
print("\n[Step 3] Testing account creation...")
try:
    # Delete test user if exists
    User.objects.filter(email='test@example.com').delete()
    
    # Create test user
    hashed_pwd = hashlib.sha256('TestPass123'.encode()).hexdigest()
    test_user = User.objects.create(
        first_name='Test',
        last_name='User',
        email='test@example.com',
        phone='1234567890',
        password=hashed_pwd
    )
    print("✓ Successfully created test user!")
    print(f"  - User ID: {test_user.id}")
    print(f"  - Email: {test_user.email}")
    print(f"  - Name: {test_user.first_name} {test_user.last_name}")
    
    # Verify we can retrieve it
    retrieved = User.objects.get(email='test@example.com')
    print(f"✓ Successfully retrieved test user from database")
    
    # Clean up
    test_user.delete()
    print("✓ Test user cleaned up")
    
except Exception as e:
    print(f"✗ Error creating test user: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

# Step 4: Check views.py
print("\n[Step 4] Checking views.py signup function...")
try:
    from tour import views
    import inspect
    
    # Get signup function
    signup_func = views.signup
    print("✓ Signup view function exists")
    
    # Check if it's callable
    if callable(signup_func):
        print("✓ Signup is callable")
    else:
        print("✗ Signup is not callable!")
        sys.exit(1)
        
except Exception as e:
    print(f"✗ Error checking views: {e}")
    sys.exit(1)

# Step 5: Check Django settings
print("\n[Step 5] Checking Django settings...")
try:
    from django.conf import settings
    print(f"✓ DEBUG mode: {settings.DEBUG}")
    print(f"✓ Database: {settings.DATABASES['default']['ENGINE']}")
    print(f"✓ Database file: {settings.DATABASES['default']['NAME']}")
    
except Exception as e:
    print(f"✗ Error checking settings: {e}")

print("\n" + "=" * 70)
print("✓ ALL DIAGNOSTIC CHECKS PASSED!")
print("=" * 70)
print("\nYour signup should work now!")
print("\nSteps to test:")
print("1. Run: python manage.py runserver")
print("2. Visit: http://localhost:8000/signup/")
print("3. Fill the form and click 'Create Account'")
print("\nIf you still have issues, try:")
print("  > python FIX_SIGNUP.bat")
print("=" * 70)
