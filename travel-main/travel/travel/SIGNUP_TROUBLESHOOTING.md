# SIGNUP TROUBLESHOOTING GUIDE

## 🔧 Quick Fix Steps (Choose One)

### **Option 1: Run Diagnostic First (RECOMMENDED)**

This will tell you exactly what's wrong:

```powershell
cd "c:\Users\user\Desktop\aleena project\travel"
python DIAGNOSE_SIGNUP.py
```

Then follow the recommendations.

---

### **Option 2: Run Migration Fix (If User Table Missing)**

```powershell
cd "c:\Users\user\Desktop\aleena project\travel"
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

Visit: http://localhost:8000/signup/

---

### **Option 3: Fresh Database Reset**

If you want a completely clean start:

```powershell
cd "c:\Users\user\Desktop\aleena project\travel"

# Delete old database
Remove-Item db.sqlite3 -Force

# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Start server
python manage.py runserver
```

---

## ✅ Testing Signup

1. Open http://localhost:8000/signup/
2. Fill in the form:
   - First Name: John
   - Last Name: Doe
   - Email: john@example.com
   - Phone: 9876543210
   - Password: SecurePass123
   - Confirm: SecurePass123
3. Click "Create Account"
4. Should see success message and redirect to home

---

## ❌ Common Issues & Fixes

### **Issue 1: "User matching query does not exist"**
- **Cause:** User table doesn't exist
- **Fix:** Run `python manage.py migrate`

### **Issue 2: "Passwords do not match"**
- **Cause:** Password fields don't match
- **Fix:** Ensure both password fields are identical

### **Issue 3: "Email is already registered"**
- **Cause:** Email already exists in database
- **Fix:** Use a different email address

### **Issue 4: "Password must be at least 8 characters"**
- **Cause:** Password is too short
- **Fix:** Use 8+ character password

### **Issue 5: Form not submitting at all**
- **Cause:** CSRF token missing or database error
- **Fix:** Check browser console for errors, run diagnostic

---

## 🚀 Next Steps

1. **Run diagnostic:** `python DIAGNOSE_SIGNUP.py`
2. **Follow its recommendations**
3. **Test signup**
4. **Let me know if any issues remain**

