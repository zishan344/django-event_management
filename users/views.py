from django.shortcuts import redirect, render, HttpResponse,get_object_or_404
from django.contrib import messages
from django.contrib.auth import login, logout
from .form import RegisterForm, LoginForm
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


def activate_user(request, user_id, token):
    user = get_object_or_404(User, id=user_id)
    print("User coming:", user)

    if default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return redirect('sign-in')  # Ensure 'sign-in' exists in your URL patterns
    else:
        return HttpResponseBadRequest('Invalid ID or Token')
""" def activateEmail(request,user,to_email):
  mail_subject ='Activate Your user account'
  message = f'Hi {user.username},\n\nPlease activate your account by clicking the link below:\n{activation_url}\n\nThank You!'
  email = EmailMessage(mail_subject,message,to[to_email])
  if email.send():
    messages.success(request,f'Dear <b>{user}</b>, please go to you email <b>{to_email}</b> inbox and click on received activation link to confirm and complete the registration. <b>Note:</b> Check your spam folder.')
  else:
    messages.error(request, f'Problem sending confirmation email to {to_email}, check if you typed it correctly.') """


""" def activate (request, uidb64,token):
  User = get_user_model()
  try:
    uid = force_str(urlsafe_base64_decode(uidb64))
    user = User.objects.get(pk=uid)
  except (TypeError, ValueError, OverflowError, User.DoesNotExist):
    user = None
  if user is not None and account_activation_token.check_token(user,token):
    user.is_active = True
    user.save()
    messages.success(request,"Thank you for your email confirmation. Now you can login your account.")
    return redirect('sign-in')
  else:
    messages.error(request, 'Activation link is invalid!')
  return redirect('home') """