from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import JsonResponse
from django.db import connection
from django.views.decorators.http import require_http_methods
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
@require_http_methods(["GET", "HEAD"])
def health_check(request):
    """
    Health check endpoint that tests database connectivity
    Accepts both GET and HEAD requests for monitoring tools like UptimeRobot
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
        
        response_data = {
            'status': 'healthy',
            'timestamp': datetime.now().isoformat(),
            'database': {
                'connected': True,
                'vendor': db_vendor,
                'name': db_name,
                'host': db_host
            },
            'message': 'Database connection successful'
        }
        
        # HEAD requests don't need response body (more efficient for monitoring)
        if request.method == 'HEAD':
            return JsonResponse({}, status=200)
            
        return JsonResponse(response_data, status=200)
        
    except Exception as e:
        error_data = {
            'status': 'unhealthy',
            'timestamp': datetime.now().isoformat(),
            'database': {
                'connected': False,
                'error': str(e)
            },
            'message': 'Database connection failed'
        }
        
        # HEAD requests don't need response body
        if request.method == 'HEAD':
            return JsonResponse({}, status=503)
            
        return JsonResponse(error_data, status=503)
