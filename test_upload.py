"""
Quick test to verify Cloudinary upload
"""
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'event_management.settings')
django.setup()

from django.core.files.uploadedfile import SimpleUploadedFile
from users.models import CustomUser
from PIL import Image
import io

print("=" * 60)
print("Testing Cloudinary Direct Upload")
print("=" * 60)

# Get a test user
user = CustomUser.objects.first()
if not user:
    print("❌ No users found in database")
    exit(1)

print(f"\n📝 Testing with user: {user.username}")

# Create a simple test image
img = Image.new('RGB', (200, 200), color='blue')
img_io = io.BytesIO()
img.save(img_io, format='PNG')
img_io.seek(0)

# Create uploaded file
test_file = SimpleUploadedFile(
    "test_upload.png",
    img_io.read(),
    content_type="image/png"
)

# Save old image reference
old_image = str(user.profile_image) if user.profile_image else None
print(f"📷 Old image: {old_image}")

# Assign and save
user.profile_image = test_file
user.save()

# Refresh from database
user.refresh_from_db()

# Check new image
print(f"📷 New image: {user.profile_image}")
print(f"🔗 New image URL: {user.profile_image.url}")

# Verify URL
if user.profile_image.url.startswith('https://res.cloudinary.com/'):
    print("\n✅ SUCCESS! Image uploaded to Cloudinary!")
    print(f"✅ Cloudinary URL: {user.profile_image.url}")
elif user.profile_image.url.startswith('/media/'):
    print("\n❌ FAILED! Still using local storage")
    print(f"❌ Local URL: {user.profile_image.url}")
    print("\n🔍 Checking configuration...")
    from django.conf import settings
    print(f"   DEFAULT_FILE_STORAGE: {settings.DEFAULT_FILE_STORAGE}")
    print(f"   CLOUDINARY_STORAGE: {settings.CLOUDINARY_STORAGE}")
else:
    print(f"\n⚠️  Unknown URL format: {user.profile_image.url}")

print("\n" + "=" * 60)
