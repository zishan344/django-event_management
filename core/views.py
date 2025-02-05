from django.shortcuts import render

# Create your views here.
def NoPermissions(request):
  return render(request,"no_permission.html")