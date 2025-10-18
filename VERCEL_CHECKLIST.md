# ⚠️ VERCEL DEPLOYMENT CHECKLIST

## 🔴 MUST ADD These Environment Variables in Vercel

Go to: **Vercel Dashboard → Your Project → Settings → Environment Variables**

### ✅ Required Variables (Add ALL of these):

```
DEBUG=False
SECRET_KEY=your-secret-key-here
VERCEL_ENV=production

# Database (Supabase)
DB_NAME=postgres
DB_USER=postgres.pexcruhmgmmprreluruc
DB_PASSWORD=4#B8_iVw!Jn+C3K
DB_HOST=aws-1-ap-south-1.pooler.supabase.com
DB_PORT=6543

# Cloudinary (IMPORTANT - For Media Files!)
CLOUDINARY_CLOUD_NAME=your_cloudinary_cloud_name
CLOUDINARY_API_KEY=your_cloudinary_api_key
CLOUDINARY_API_SECRET=your_cloudinary_api_secret

# Email
EMAIL_HOST=smtp.gmail.com
EMAIL_USE_TLS=True
EMAIL_PORT=587
EMAIL_FROM=zishanahmed344@gmail.com
EMAIL_HOST_USER=zishanahmed344@gmail.com
EMAIL_HOST_PASSWORD=lcmh qfid cymj nite
PASSWORD_RESET_TIMEOUT=14400

# Frontend
FRONTEND_URL=https://your-app.vercel.app
```

## 🚨 Current Issue: Cloudinary Not Working

### Problem:
- Error: "Read-only file system" when uploading media files
- Files trying to save to `/var/task/media/` instead of Cloudinary

### Solution:
**You MUST add Cloudinary environment variables to Vercel!**

1. ✅ Get Cloudinary credentials:
   - Go to: https://cloudinary.com/console
   - Copy: Cloud Name, API Key, API Secret

2. ✅ Add to Vercel Environment Variables:
   ```
   CLOUDINARY_CLOUD_NAME = your_cloud_name
   CLOUDINARY_API_KEY = your_api_key
   CLOUDINARY_API_SECRET = your_api_secret
   ```

3. ✅ Also add:
   ```
   VERCEL_ENV = production
   ```

4. ✅ Redeploy after adding variables

## 📝 How to Add Environment Variables:

1. Go to Vercel Dashboard
2. Select your project
3. Click "Settings" tab
4. Click "Environment Variables" in sidebar
5. Add each variable:
   - Name: `CLOUDINARY_CLOUD_NAME`
   - Value: `your_value`
   - Environment: Select all (Production, Preview, Development)
6. Click "Save"
7. Repeat for all variables
8. Go to "Deployments" → Redeploy latest

## ✅ After Adding Variables:

Your app will:
- ✅ Use Cloudinary for media uploads
- ✅ No more "Read-only file system" errors
- ✅ Images will be stored on Cloudinary CDN
- ✅ Fast image loading

## 🔍 Verify Setup:

After deployment:
1. Try uploading a profile picture
2. Check Cloudinary dashboard for the image
3. No errors should appear

---

**Without Cloudinary variables, media uploads WILL FAIL on Vercel!** 🚨
