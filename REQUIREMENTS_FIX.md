# 🔧 Requirements.txt Management Guide

## ⚠️ Common Issue: Conflicting PostgreSQL Packages

### ❌ WRONG - Multiple psycopg packages:
```
psycopg-binary==3.2.4        # ❌ Remove
psycopg2==2.9.10              # ❌ Remove
psycopg2-binary==2.9.10       # ❌ Wrong version
```

### ✅ CORRECT - Single package:
```
psycopg2-binary==2.9.9        # ✅ This works on Vercel!
```

## 📋 Why This Error Happens:

1. **Multiple PostgreSQL drivers conflict** with each other
2. **psycopg2** (without binary) tries to compile from source
3. **Vercel doesn't have** PostgreSQL development libraries
4. **psycopg2-binary 2.9.9** is pre-compiled and works perfectly

## 🚀 How to Update Requirements Safely:

### Method 1: Manual Update (Recommended)
```bash
# Edit requirements.txt manually
# Keep only: psycopg2-binary==2.9.9
```

### Method 2: Fresh Install
```bash
# Activate virtual environment
source event-env/Scripts/activate  # Windows Git Bash

# Uninstall all psycopg packages
pip uninstall psycopg psycopg2 psycopg2-binary psycopg-binary -y

# Install only the correct one
pip install psycopg2-binary==2.9.9

# Regenerate requirements
pip freeze > requirements.txt
```

### Method 3: Clean Requirements
```bash
# Create clean requirements file
pip install pipreqs
pipreqs . --force
```

## 📦 Current Working Requirements:

Your `requirements.txt` should have:
```
asgiref==3.8.1
certifi==2025.10.5
charset-normalizer==3.4.4
cloudinary==1.44.1
dj-database-url==2.3.0
Django==5.1.5
django-cloudinary-storage==0.3.0
django-debug-toolbar==5.0.1
idna==3.11
pillow==11.1.0
psycopg2-binary==2.9.9          # ← Only this one for PostgreSQL!
python-dotenv==1.0.0
requests==2.32.5
six==1.17.0
sqlparse==0.5.3
typing_extensions==4.12.2
tzdata==2025.1
urllib3==2.5.0
whitenoise==6.6.0
```

## ✅ Quick Fix Checklist:

- [ ] Remove `psycopg-binary`
- [ ] Remove `psycopg2` (without binary)
- [ ] Keep only `psycopg2-binary==2.9.9`
- [ ] Add `whitenoise==6.6.0` if missing
- [ ] Commit and push
- [ ] Wait for Vercel deployment

## 🔍 How to Check for Issues:

```bash
# Check for duplicate packages
pip list | grep psycopg

# Should only show:
# psycopg2-binary  2.9.9
```

## 📝 Remember:

1. **Never** install both `psycopg2` and `psycopg2-binary`
2. **Always** use `psycopg2-binary` for production
3. **Version 2.9.9** is tested and works on Vercel
4. **Commit** requirements.txt after any package changes

---

**Your requirements.txt is now fixed and deployment should work!** ✅
