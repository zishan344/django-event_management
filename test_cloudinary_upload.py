"""
Django Shell Test for Cloudinary Upload
Run this with: python manage.py shell < test_cloudinary_upload.py
"""

import os
import django
from django.core.files.uploadedfile import SimpleUploadedFile

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'event_management.settings')
django.setup()

from users.models import CustomUser

print("=" * 50)
print("Testing Cloudinary Upload")
print("=" * 50)

# Get a test user
try:
    user = CustomUser.objects.first()
    if user:
        print(f"✓ Found user: {user.username}")
        
        # Create a simple test image
        test_image_content = b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x00\x00\x00\x21\xf9\x04\x01\x00\x00\x00\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x01\x44\x00\x3b'
        test_image = SimpleUploadedFile(
            name='test_image.gif',
            content=test_image_content,
            content_type='image/gif'
        )
        
        # Upload to Cloudinary
        user.profile_image = test_image
        user.save()
        
        print(f"✓ Image uploaded successfully!")
        print(f"✓ Image URL: {user.profile_image.url}")
        print(f"✓ Storage backend: {user.profile_image.storage.__class__.__name__}")
        
        # Check if URL is from Cloudinary
        if 'cloudinary' in user.profile_image.url.lower() or 'res.cloudinary.com' in user.profile_image.url.lower():
            print("✓✓ SUCCESS! Image stored in Cloudinary!")
        else:
            print("✗✗ WARNING! Image NOT in Cloudinary!")
            print(f"   URL: {user.profile_image.url}")
    else:
        print("✗ No users found in database")
        
except Exception as e:
    print(f"✗ Error: {e}")
    import traceback
    traceback.print_exc()

print("=" * 50)
