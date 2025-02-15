from django.shortcuts import redirect, render,get_object_or_404
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.models import Group
from django.contrib.auth.tokens import default_token_generator
from .form import RegisterForm, LoginForm, CreateGroupForm, AssignRoleForm
from django.http import HttpResponseBadRequest
from django.contrib.auth.decorators import login_required,user_passes_test
# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth import get_user_model

User = get_user_model()


def is_admin(user):
    return user.groups.filter(name="Admin").exists()
    

def is_organizer(user):
    return user.groups.filter(name="Organizer").exists()

def is_participant(user):
    return user.groups.filter(name="Participant").exists()



def Sign_up(request):
  form = RegisterForm()
  if request.method == 'POST':
    form = RegisterForm(request.POST,request.FILES)
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

class CreateRoles(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    print("request coming")
    permission_required="Authentication_and_Authorization.add_group"
    login_url='sign-in'
    model = Group
    form_class = CreateGroupForm
    template_name = 'createRole.html'
    success_url = reverse_lazy('create-role')
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request,"Created new role successfully")
        return response


@login_required(login_url="sign-in")
@user_passes_test(is_admin, login_url="no-permission")
def updateRolePermission(request,role_id):
  role = get_object_or_404(Group,id=role_id)
  form = CreateGroupForm(instance = role)
  print("request coming")
  if request.method == 'POST':
      form = CreateGroupForm(data=request.POST, instance=role)
      if form.is_valid():
          form.save()
          messages.success(request,"update role permissions successfully",)
          return redirect('dashboard')
      else:
          messages.error(request,"form is not valid")
  return render(request, 'createRole.html', {'form': form})

@login_required(login_url="sign-in")
@user_passes_test(is_admin, login_url="no-permission")
def deleteRole(request,role_id):
    role = get_object_or_404(Group,id=role_id)
    role.delete()
    messages.success(request,'category deleted successfully')
    return redirect('dashboard')
# change role
@login_required(login_url="sign-in")
@user_passes_test(is_admin, login_url="no-permission")
def ChangeRole(request,user_id):
    user = User.objects.get(id = user_id)
    form = AssignRoleForm()
    if request.method == 'POST':
        form = AssignRoleForm(request.POST)
        if form.is_valid():
            role = form.cleaned_data.get('role')
            user.groups.clear()
            user.groups.add(role)
            messages.success(request, f"User {user.username} has been assigned to the {role}")
            return redirect('dashboard')
    context = {
        "form_title": "Update Role",
        "form": form,
        "btn_content":"Change"
    }
    return render(request,"globalForm.html",context)



def activate_user(request, user_id, token):
    user = get_object_or_404(User, id=user_id)

    if default_token_generator.check_token(user, token):
        user.is_active = True
        participant_group, created = Group.objects.get_or_create(name="Participant")
        user.groups.add(participant_group)
        user.save()
        return redirect('sign-in')
    else:
        return HttpResponseBadRequest('Invalid ID or Token')