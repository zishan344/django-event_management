"""
Populate Database with Categories and Events
This script creates sample categories and events with images from media folder
"""

import os
import django
from pathlib import Path

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'event_management.settings')
django.setup()

from events.models import Category, Event
from django.core.files import File
from datetime import datetime, timedelta
import random

print("=" * 70)
print("🚀 Starting Database Population")
print("=" * 70)

# Sample categories data
CATEGORIES_DATA = [
    {
        'name': 'Technology',
        'description': 'Technology conferences, workshops, and hackathons. Learn about latest tech trends, AI, ML, and software development.'
    },
    {
        'name': 'Business',
        'description': 'Business conferences, networking events, and entrepreneurship workshops. Connect with industry leaders and investors.'
    },
    {
        'name': 'Education',
        'description': 'Educational seminars, training programs, and academic conferences. Enhance your knowledge and skills.'
    },
    {
        'name': 'Entertainment',
        'description': 'Music concerts, comedy shows, cultural festivals, and entertainment events. Enjoy and have fun!'
    },
    {
        'name': 'Sports',
        'description': 'Sports tournaments, marathons, fitness workshops, and athletic competitions. Stay active and healthy!'
    },
    {
        'name': 'Arts & Culture',
        'description': 'Art exhibitions, cultural festivals, theater performances, and creative workshops. Explore creativity!'
    },
]

# Sample events data with corresponding images
EVENTS_DATA = [
    # Technology Events
    {
        'name': 'AI & Machine Learning Summit 2025',
        'description': 'Join us for the biggest AI conference of the year! Learn from industry experts about the latest developments in artificial intelligence, machine learning, and deep learning. Network with professionals and discover cutting-edge technologies.',
        'category': 'Technology',
        'location': 'Dhaka Convention Center, Bangladesh',
        'days_from_now': 15,
        'time': '09:00',
        'image': 'media/event_images/qwen6.png'
    },
    {
        'name': 'Web Development Bootcamp',
        'description': 'Intensive 3-day workshop covering modern web development technologies including React, Node.js, Python Django, and cloud deployment. Hands-on projects and expert mentorship included.',
        'category': 'Technology',
        'location': 'Tech Hub, Chittagong',
        'days_from_now': 7,
        'time': '10:00',
        'image': 'media/event_images/nl-model-2.jpg'
    },
    {
        'name': 'Cybersecurity Conference',
        'description': 'Learn about the latest cybersecurity threats, best practices, and protection strategies. Expert talks on ethical hacking, network security, and data protection.',
        'category': 'Technology',
        'location': 'Virtual Event',
        'days_from_now': 20,
        'time': '14:00',
        'image': 'media/event_images/sifi.jpg'
    },
    
    # Business Events
    {
        'name': 'Startup Pitch Competition',
        'description': 'Aspiring entrepreneurs showcase their innovative ideas to investors and industry experts. Win funding, mentorship, and business support. Great networking opportunity!',
        'category': 'Business',
        'location': 'Startup Bangladesh Hub, Dhaka',
        'days_from_now': 10,
        'time': '15:00',
        'image': 'media/event_images/nl-p-1.jpg'
    },
    {
        'name': 'Digital Marketing Workshop',
        'description': 'Master digital marketing strategies including SEO, social media marketing, content creation, and email campaigns. Learn from successful digital marketers.',
        'category': 'Business',
        'location': 'Marketing Academy, Sylhet',
        'days_from_now': 12,
        'time': '11:00',
        'image': 'media/event_images/nl_model.jpg'
    },
    
    # Education Events
    {
        'name': 'University Fair 2025',
        'description': 'Explore higher education opportunities from top universities worldwide. Meet admission officers, attend seminars, and get guidance on study abroad programs.',
        'category': 'Education',
        'location': 'International Convention City Bashundhara',
        'days_from_now': 25,
        'time': '09:00',
        'image': 'media/event_images/images.jpg'
    },
    {
        'name': 'Python Programming for Beginners',
        'description': 'Learn Python programming from scratch! Perfect for absolute beginners. Covers basics, data structures, and real-world projects. Certification provided.',
        'category': 'Education',
        'location': 'Code Academy, Dhaka',
        'days_from_now': 5,
        'time': '16:00',
        'image': 'media/event_images/testimg.webp'
    },
    
    # Entertainment Events
    {
        'name': 'Summer Music Festival 2025',
        'description': 'The biggest music festival of the year featuring top local and international artists! Three days of non-stop music, food, and entertainment.',
        'category': 'Entertainment',
        'location': 'Army Stadium, Dhaka',
        'days_from_now': 30,
        'time': '18:00',
        'image': 'media/event_images/online-event-entertainment-concept-background-260nw-1731583732.webp'
    },
    {
        'name': 'Comedy Night Live',
        'description': 'Laugh out loud with the funniest comedians in town! Stand-up comedy show featuring special guest performers. Food and beverages available.',
        'category': 'Entertainment',
        'location': 'Star Cineplex, Dhaka',
        'days_from_now': 8,
        'time': '20:00',
        'image': 'media/event_images/testImg3.webp'
    },
    
    # Sports Events
    {
        'name': 'Dhaka Marathon 2025',
        'description': 'Annual charity marathon supporting education for underprivileged children. Multiple race categories: 5K, 10K, Half Marathon, and Full Marathon. Registration includes t-shirt and medal!',
        'category': 'Sports',
        'location': 'Manik Mia Avenue, Dhaka',
        'days_from_now': 40,
        'time': '06:00',
        'image': 'media/event_images/a_realistic_scene.png'
    },
    {
        'name': 'Football Tournament',
        'description': 'Inter-university football championship. Teams from across the country compete for the trophy. Exciting matches, prizes, and lots of fun!',
        'category': 'Sports',
        'location': 'Bangabandhu National Stadium',
        'days_from_now': 18,
        'time': '15:30',
        'image': 'media/event_images/istockphoto-499517325-612x612.jpg'
    },
    
    # Arts & Culture Events
    {
        'name': 'Pohela Boishakh Celebration',
        'description': 'Traditional Bengali New Year celebration with cultural programs, music, dance, and traditional food. Showcase of Bengali art and heritage.',
        'category': 'Arts & Culture',
        'location': 'Ramna Batamul, Dhaka',
        'days_from_now': 35,
        'time': '08:00',
        'image': 'media/event_images/an_imaginative_scene_in_the_world.png'
    },
    {
        'name': 'Art Exhibition - Modern Bangladesh',
        'description': 'Contemporary art exhibition featuring works from emerging and established Bangladeshi artists. Paintings, sculptures, and installations exploring modern themes.',
        'category': 'Arts & Culture',
        'location': 'National Art Gallery, Dhaka',
        'days_from_now': 14,
        'time': '10:00',
        'image': 'media/event_images/images_1.jpg'
    },
]


def create_categories():
    """Create categories in database"""
    print("\n📁 Creating Categories...")
    print("-" * 70)
    
    created_categories = {}
    
    for cat_data in CATEGORIES_DATA:
        category, created = Category.objects.get_or_create(
            name=cat_data['name'],
            defaults={'description': cat_data['description']}
        )
        
        if created:
            print(f"✅ Created: {category.name}")
        else:
            print(f"⚠️  Already exists: {category.name}")
        
        created_categories[cat_data['name']] = category
    
    print(f"\n📊 Total Categories: {Category.objects.count()}")
    return created_categories


def create_events(categories):
    """Create events with images from media folder"""
    print("\n🎉 Creating Events...")
    print("-" * 70)
    
    base_dir = Path(__file__).resolve().parent
    created_count = 0
    skipped_count = 0
    
    for event_data in EVENTS_DATA:
        # Check if event already exists
        if Event.objects.filter(name=event_data['name']).exists():
            print(f"⚠️  Already exists: {event_data['name']}")
            skipped_count += 1
            continue
        
        # Calculate event date
        event_date = datetime.now().date() + timedelta(days=event_data['days_from_now'])
        
        # Get category
        category = categories[event_data['category']]
        
        # Get image path
        image_path = base_dir / event_data['image']
        
        # Create event with CloudinaryField
        event = Event.objects.create(
            name=event_data['name'],
            description=event_data['description'],
            category=category,
            location=event_data['location'],
            date=event_date,
            time=event_data['time']
        )
        
        # Upload image to Cloudinary using cloudinary uploader
        if image_path.exists():
            try:
                import cloudinary.uploader
                # Upload to Cloudinary
                upload_result = cloudinary.uploader.upload(
                    str(image_path),
                    folder='event_images',
                    public_id=None,  # Auto-generate
                    overwrite=False
                )
                # Set the Cloudinary public_id to the event
                event.image = upload_result['public_id']
                event.save()
                print(f"✅ Created: {event.name}")
                print(f"   📸 Image uploaded: {upload_result['secure_url']}")
            except Exception as e:
                print(f"✅ Created: {event.name}")
                print(f"   ⚠️  Image upload failed: {e}")
        else:
            print(f"✅ Created: {event.name} (Image file not found: {image_path})")
        
        created_count += 1
    
    print(f"\n📊 Events Created: {created_count}")
    print(f"📊 Events Skipped: {skipped_count}")
    print(f"📊 Total Events: {Event.objects.count()}")


def display_summary():
    """Display summary of created data"""
    print("\n" + "=" * 70)
    print("📋 DATABASE SUMMARY")
    print("=" * 70)
    
    print("\n📁 Categories:")
    for category in Category.objects.all():
        event_count = Event.objects.filter(category=category).count()
        print(f"   • {category.name}: {event_count} events")
    
    print("\n🎉 Upcoming Events (Next 10):")
    upcoming_events = Event.objects.filter(
        date__gte=datetime.now().date()
    ).order_by('date')[:10]
    
    for event in upcoming_events:
        has_image = "✓" if event.image else "✗"
        print(f"   • {event.name}")
        print(f"     Date: {event.date} | Location: {event.location}")
        print(f"     Category: {event.category.name} | Image: {has_image}")
        if event.image:
            print(f"     Image URL: {event.image.url}")
        print()


def main():
    """Main function"""
    try:
        # Step 1: Create categories
        categories = create_categories()
        
        # Step 2: Create events
        create_events(categories)
        
        # Step 3: Display summary
        display_summary()
        
        print("=" * 70)
        print("✅ Database population completed successfully!")
        print("=" * 70)
        
        print("\n💡 Next Steps:")
        print("   1. Start your Django server: python manage.py runserver")
        print("   2. Visit: http://127.0.0.1:8000/events/")
        print("   3. Check Cloudinary dashboard for uploaded images")
        print("   4. Images are automatically uploaded to Cloudinary!")
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
