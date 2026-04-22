#!/usr/bin/env python
"""
COMPREHENSIVE ERROR DETECTION SCRIPT
Finds ALL errors in the signup/login system
"""
import os
import sys
import django

sys.path.insert(0, r'c:\Users\user\Desktop\aleena project\travel')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'travel.settings')

print("=" * 80)
print("COMPREHENSIVE ERROR DETECTION - SEARCHING FOR ISSUES")
print("=" * 80)

# Check 1: Django Setup
print("\n[CHECK 1] Django Configuration...")
try:
    django.setup()
    print("✓ Django setup successful")
except Exception as e:
    print(f"✗ CRITICAL ERROR - Django setup failed: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

# Check 2: Import all required modules
print("\n[CHECK 2] Importing modules...")
try:
    from django.core.management import call_command
    from django.contrib import messages
    from tour.models import User, Booking
    from tour import views
    import hashlib
    print("✓ All imports successful")
except Exception as e:
    print(f"✗ ERROR importing modules: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

# Check 3: Check database connection
print("\n[CHECK 3] Database Connection...")
try:
    from django.db import connection
    with connection.cursor() as cursor:
        cursor.execute("SELECT 1")
    print("✓ Database connected")
except Exception as e:
    print(f"✗ ERROR connecting to database: {e}")
    sys.exit(1)

# Check 4: List all tables
print("\n[CHECK 4] Checking database tables...")
try:
    from django.db import connection
    cursor = connection.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    print(f"✓ Found {len(tables)} tables:")
    for table in tables:
        print(f"  - {table[0]}")
    
    # Check for critical tables
    table_names = [t[0] for t in tables]
    if 'tour_user' not in table_names:
        print("\n  ⚠️  WARNING: 'tour_user' table NOT found!")
        print("     This is the main issue causing signup to fail!")
        print("\n     FIX THIS IMMEDIATELY:")
        print("     1. Run: python manage.py makemigrations")
        print("     2. Run: python manage.py migrate")
    else:
        print("\n  ✓ tour_user table exists")
        
    if 'tour_booking' not in table_names:
        print("\n  ⚠️  WARNING: 'tour_booking' table NOT found!")
    else:
        print("  ✓ tour_booking table exists")
        
except Exception as e:
    print(f"✗ ERROR checking tables: {e}")
    import traceback
    traceback.print_exc()

# Check 5: Check migrations status
print("\n[CHECK 5] Checking migrations status...")
try:
    from django.db.migrations.loader import MigrationLoader
    loader = MigrationLoader(None, ignore_no_migrations=True)
    
    print("✓ Migrations checked:")
    for app_label in ['tour', 'auth', 'sessions', 'contenttypes']:
        if app_label in loader.migrated_apps:
            print(f"  ✓ {app_label} - migrations applied")
        else:
            print(f"  ⚠️  {app_label} - no migrations")
            
except Exception as e:
    print(f"✗ ERROR checking migrations: {e}")

# Check 6: Test User model
print("\n[CHECK 6] Testing User model...")
try:
    user_count = User.objects.count()
    print(f"✓ User model works")
    print(f"  - Users in database: {user_count}")
    
    if user_count > 0:
        first_user = User.objects.first()
        print(f"  - First user: {first_user.first_name} {first_user.last_name} ({first_user.email})")
except Exception as e:
    print(f"✗ ERROR with User model: {e}")
    import traceback
    traceback.print_exc()

# Check 7: Test creating a user
print("\n[CHECK 7] Testing user creation...")
try:
    # Clean up test user if exists
    User.objects.filter(email='test_diagnostic@example.com').delete()
    
    # Try to create user
    hashed_pwd = hashlib.sha256('TestPass123'.encode()).hexdigest()
    test_user = User.objects.create(
        first_name='Diagnostic',
        last_name='Test',
        email='test_diagnostic@example.com',
        phone='1234567890',
        password=hashed_pwd
    )
    print("✓ User creation successful!")
    print(f"  - Created user ID: {test_user.id}")
    print(f"  - Email: {test_user.email}")
    
    # Try to retrieve it
    retrieved = User.objects.get(email='test_diagnostic@example.com')
    print(f"✓ User retrieval successful!")
    
    # Test password verification
    verify_pwd = hashlib.sha256('TestPass123'.encode()).hexdigest()
    if retrieved.password == verify_pwd:
        print("✓ Password verification works!")
    else:
        print("✗ Password verification FAILED!")
    
    # Clean up
    test_user.delete()
    print("✓ Test user cleaned up")
    
except Exception as e:
    print(f"✗ ERROR creating/testing user: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

# Check 8: Verify views functions exist
print("\n[CHECK 8] Checking view functions...")
try:
    # Check signup
    if hasattr(views, 'signup') and callable(views.signup):
        print("✓ signup function exists and callable")
    else:
        print("✗ signup function ERROR")
    
    # Check login
    if hasattr(views, 'login_views') and callable(views.login_views):
        print("✓ login_views function exists and callable")
    else:
        print("✗ login_views function ERROR")
    
    # Check logout
    if hasattr(views, 'logout_views') and callable(views.logout_views):
        print("✓ logout_views function exists and callable")
    else:
        print("✗ logout_views function ERROR")
        
except Exception as e:
    print(f"✗ ERROR checking views: {e}")

# Check 9: Django validation
print("\n[CHECK 9] Running Django validation...")
try:
    call_command('check', verbosity=0)
    print("✓ Django validation passed - no configuration errors")
except Exception as e:
    print(f"✗ Django validation ERROR: {e}")
    import traceback
    traceback.print_exc()

print("\n" + "=" * 80)
print("ERROR DETECTION COMPLETE")
print("=" * 80)

print("\n✅ SUMMARY:")
print("  - If all checks passed: Try restarting your browser cache")
print("  - If tour_user table missing: Run migrations")
print("  - If other errors: See details above")

print("\n🔧 TO FIX:")
print("  1. python manage.py makemigrations")
print("  2. python manage.py migrate")
print("  3. python manage.py runserver")

print("=" * 80)
