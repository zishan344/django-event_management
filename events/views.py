from django.http import HttpResponse
from django.template import loader

def events(request):
    """ events request"""
    template = loader.get_template('test.html')
    return HttpResponse(template.render())