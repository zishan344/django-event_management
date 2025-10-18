"""
Test Cloudinary Connection
Run this to verify Cloudinary is properly configured
"""
import os
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'event_management.settings')
django.setup()

import cloudinary
import cloudinary.uploader

def test_cloudinary():
    print("Testing Cloudinary Connection...")
    print(f"Cloud Name: {cloudinary.config().cloud_name}")
    print(f"API Key: {cloudinary.config().api_key}")
    
    if not cloudinary.config().cloud_name:
        print("❌ ERROR: CLOUDINARY_CLOUD_NAME not set!")
        return False
    
    if not cloudinary.config().api_key:
        print("❌ ERROR: CLOUDINARY_API_KEY not set!")
        return False
        
    if not cloudinary.config().api_secret:
        print("❌ ERROR: CLOUDINARY_API_SECRET not set!")
        return False
    
    print("✅ Cloudinary credentials are configured!")
    print("\nYou can now upload images and they will be stored on Cloudinary.")
    return True

if __name__ == "__main__":
    test_cloudinary()
