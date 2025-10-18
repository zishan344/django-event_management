"""
Test Health Check Endpoint
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'event_management.settings')
django.setup()

from django.test import Client
import json

print("=" * 70)
print("🏥 Testing Health Check Endpoint")
print("=" * 70)

# Create test client
client = Client()

try:
    # Make GET request to health endpoint with proper host
    response = client.get('/health/', HTTP_HOST='127.0.0.1')
    
    print(f"\n📊 Status Code: {response.status_code}")
    print(f"📊 Content Type: {response.get('Content-Type', 'Unknown')}")
    print(f"📊 Raw Response (first 500 chars):")
    print(response.content.decode()[:500])
    
    # Try to parse JSON
    try:
        data = json.loads(response.content)
        print(f"\n📊 JSON Response:")
        print(json.dumps(data, indent=2))
        
        if response.status_code == 200:
            print("\n✅ Health Check: PASSED")
            print(f"   Database: {data['database']['vendor']}")
            print(f"   Connected: {data['database']['connected']}")
            print(f"   Database Name: {data['database']['name']}")
            print(f"   Host: {data['database']['host']}")
        else:
            print("\n❌ Health Check: FAILED")
            print(f"   Error: {data.get('message', 'Unknown error')}")
    except json.JSONDecodeError:
        print("\n⚠️  Response is not JSON (might be HTML error page)")
    
except Exception as e:
    print(f"\n❌ Error testing endpoint: {e}")
    import traceback
    traceback.print_exc()

print("\n" + "=" * 70)
print("💡 To test in browser:")
print("   1. Start server: python manage.py runserver")
print("   2. Visit: http://127.0.0.1:8000/health/")
print("=" * 70)
