#!/usr/bin/env python
"""
Fix signup by running database setup
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

print("=" * 60)
print("FIXING SIGNUP ISSUE - Running Database Setup")
print("=" * 60)

# Step 1: Make migrations
print("\n[Step 1/3] Making migrations...")
try:
    call_command('makemigrations', verbosity=2)
    print("✓ Migrations created successfully")
except Exception as e:
    print(f"✗ Error making migrations: {e}")
    sys.exit(1)

# Step 2: Apply migrations
print("\n[Step 2/3] Applying migrations...")
try:
    call_command('migrate', verbosity=2)
    print("✓ Migrations applied successfully")
except Exception as e:
    print(f"✗ Error applying migrations: {e}")
    sys.exit(1)

# Step 3: Verify database
print("\n[Step 3/3] Verifying database...")
try:
    from tour.models import User
    user_count = User.objects.count()
    print(f"✓ Database verified. Current users in database: {user_count}")
except Exception as e:
    print(f"✗ Error verifying database: {e}")
    sys.exit(1)

print("\n" + "=" * 60)
print("✓ SIGNUP FIX COMPLETE!")
print("=" * 60)
print("\nYour signup should now work properly!")
print("Run: python manage.py runserver")
print("Then visit: http://localhost:8000/signup/")
