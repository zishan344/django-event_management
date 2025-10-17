# Django Event Management - Vercel Deployment Guide

## 📋 Prerequisites
- Vercel account
- GitHub repository connected to Vercel

## 🚀 Deployment Steps

### 1. Environment Variables in Vercel Dashboard
Add these environment variables in your Vercel project settings:

```
DEBUG=False
SECRET_KEY=your-production-secret-key-here
DJANGO_SETTINGS_MODULE=event_management.settings
```

### 2. Deploy
```bash
# Commit all changes
git add .
git commit -m "Configure for Vercel deployment"
git push origin master
```

Vercel will automatically deploy your application.

### 3. Important Notes
- Static files are served via WhiteNoise
- Debug toolbar is disabled in production
- SQLite is used for the database (consider upgrading to PostgreSQL for production)
- Media files are handled in-memory on Vercel (consider using cloud storage like AWS S3 or Cloudinary)

## 🔧 Local Development
```bash
# Activate virtual environment
source event-env/Scripts/activate  # Windows Git Bash
# or
event-env\Scripts\activate  # Windows CMD

# Set DEBUG=True for local development
export DEBUG=True  # Linux/Mac
# or
set DEBUG=True  # Windows CMD

# Run development server
python manage.py runserver
```

## ⚠️ Production Considerations
1. Use PostgreSQL instead of SQLite
2. Use cloud storage (S3, Cloudinary) for media files
3. Set strong SECRET_KEY in environment variables
4. Monitor application logs in Vercel dashboard

## 📚 Resources
- [Vercel Python Documentation](https://vercel.com/docs/frameworks/python)
- [Django Deployment Checklist](https://docs.djangoproject.com/en/stable/howto/deployment/checklist/)
