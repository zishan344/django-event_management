from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import JsonResponse
from django.db import connection
from django.views.decorators.http import require_GET
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime

# Create your views here.
def NoPermissions(request):
  return render(request,"no_permission.html")

class EventureContact(TemplateView):
  template_name ='contact.html'
  
class EventureAboutus(TemplateView):
  template_name ='aboutus.html'


@csrf_exempt
@require_GET
def health_check(request):
    """
    Health check endpoint that tests database connectivity
    Returns: JSON response with status and database info
    """
    try:
        # Test database connection by executing a simple query
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
            cursor.fetchone()
        
        # Get database information
        db_vendor = connection.vendor
        db_name = connection.settings_dict.get('NAME', 'Unknown')
        db_host = connection.settings_dict.get('HOST', 'localhost')
        
        return JsonResponse({
            'status': 'healthy',
            'timestamp': datetime.now().isoformat(),
            'database': {
                'connected': True,
                'vendor': db_vendor,
                'name': db_name,
                'host': db_host
            },
            'message': 'Database connection successful'
        }, status=200)
        
    except Exception as e:
        return JsonResponse({
            'status': 'unhealthy',
            'timestamp': datetime.now().isoformat(),
            'database': {
                'connected': False,
                'error': str(e)
            },
            'message': 'Database connection failed'
        }, status=503)
