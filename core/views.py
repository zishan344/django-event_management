from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
def NoPermissions(request):
  return render(request,"no_permission.html")

class EventureContact(TemplateView):
  template_name ='contact.html'
  
class EventureAboutus(TemplateView):
  template_name ='aboutus.html'
