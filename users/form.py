from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm, PasswordChangeForm, PasswordResetForm
from django.contrib.auth.models import Permission,Group
from events.form import StyledFormMixin
from .models import CustomUser
from django.contrib.auth import get_user_model

User = get_user_model()


class RegisterForm(StyledFormMixin,UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name',
                'password1', 'password2', 'email','phoneNumber','profile_image']

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.apply_styled_widgets()  

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None



class EditProfileForm(StyledFormMixin, forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ["username",'email', 'first_name', 'last_name', 'phoneNumber', 'profile_image']

class ChangePasswordForm(StyledFormMixin,PasswordChangeForm):
    "ChangePasswordForm handle custom change password form"

class CustomPasswordResetForm(StyledFormMixin,PasswordResetForm):
    "it's handle custom password reset form"

class LoginForm(StyledFormMixin,AuthenticationForm):
  def __init__(self, *arg, **kwargs):
        super().__init__(*arg, **kwargs)
        self.apply_styled_widgets()  



class AssignRoleForm(StyledFormMixin,forms.Form):
    role = forms.ModelChoiceField(
        queryset=Group.objects.all(),
        empty_label='Select a Role'
    )




class CreateGroupForm(StyledFormMixin,forms.ModelForm):
    permissions = forms.ModelMultipleChoiceField(
        queryset=Permission.objects.all(),
        widget =forms.CheckboxSelectMultiple,
        required=False,
        label='Assign Permission'
    )
    class Meta:
        model = Group
        fields = ['name', 'permissions']
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.apply_styled_widgets()
        for field_name, field in self.fields.items():
            if field_name in self.initial:
                field.widget.attrs['value'] = self.initial[field_name]

