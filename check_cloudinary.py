# Quick Django Shell Test for Cloudinary
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'event_management.settings')
django.setup()

from django.conf import settings
import cloudinary

print("=" * 60)
print("Cloudinary Configuration Test")
print("=" * 60)

# Check Django settings
print("\n1. Django Settings:")
print(f"   DEFAULT_FILE_STORAGE: {settings.DEFAULT_FILE_STORAGE}")
print(f"   CLOUDINARY_STORAGE: {settings.CLOUDINARY_STORAGE}")

# Check cloudinary config
print("\n2. Cloudinary Config:")
config = cloudinary.config()
print(f"   Cloud Name: {config.cloud_name}")
print(f"   API Key: {config.api_key}")
print(f"   Secure: {config.secure}")

# Check if cloudinary_storage is available
try:
    from cloudinary_storage.storage import MediaCloudinaryStorage
    storage = MediaCloudinaryStorage()
    print("\n3. MediaCloudinaryStorage:")
    print(f"   ✅ Storage class loaded successfully")
    print(f"   Storage: {storage}")
except Exception as e:
    print(f"\n3. ❌ Error loading storage: {e}")

# Check users with profile images
from users.models import CustomUser
print("\n4. Users with Profile Images:")
users = CustomUser.objects.exclude(profile_image='').exclude(profile_image__isnull=True)[:3]
if users:
    for user in users:
        print(f"   - {user.username}: {user.profile_image.name}")
        if user.profile_image:
            try:
                print(f"     URL: {user.profile_image.url}")
            except Exception as e:
                print(f"     Error getting URL: {e}")
else:
    print("   No users with profile images found")

print("\n" + "=" * 60)
print("Test Complete!")
print("=" * 60)
