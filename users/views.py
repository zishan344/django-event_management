from django.shortcuts import redirect, render, HttpResponse,get_object_or_404
from django.contrib import messages
from django.contrib.auth import login, logout
from .form import RegisterForm, LoginForm, CreateGroupForm
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.http import HttpResponseBadRequest, HttpResponseNotFound

# Create your views here.

def Sign_up(request):
  form = RegisterForm()
  if request.method == 'POST':
    form = RegisterForm(request.POST)
    if form.is_valid():
      user = form.save(commit=False)
      user.set_password(form.cleaned_data['password1'])
      user.is_active = False
      user.save()
      messages.success(
        request, 'A Confirmation mail sent. Please check your email'
      )
      return redirect('sign-in')
    else:
      print("From is not valid")
  return render(request, 'register.html', {"form":form})


def Sign_in(request):
  form = LoginForm()
  if request.method == 'POST':
    print("request method verified")
    form = LoginForm(data=request.POST)
    if form.is_valid():
      user = form.get_user()
      print(f"Authenticated user: {user}")
      if user is not None:
        login(request, user)
        return redirect('home')
      else:
        print("Error: form.get_user() returned None")
    else:
      print("Form errors:", form.errors)
  return render(request, 'login_form.html', {'form': form})


def Sign_out(request):
    logout(request)
    return redirect('sign-in')

def CreateRole (request):
  form = CreateGroupForm()
  print("request coming")
  if request.method == 'POST':
      print("form is post")
      form = CreateGroupForm(data=request.POST)
      if form.is_valid():
          form.save()
          messages.success(request,"Created new role successfully",)
          return redirect('create-role')
      else:
          messages.error(request,"form is not valid")
  return render(request, 'createRole.html', {'form': form})

def activate_user(request, user_id, token):
    user = get_object_or_404(User, id=user_id)

    if default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return redirect('sign-in')
    else:
        return HttpResponseBadRequest('Invalid ID or Token')