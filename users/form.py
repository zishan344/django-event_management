from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User,Permission,Group
from events.form import StyledFormMixin


class RegisterForm(StyledFormMixin,UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name',
                'password1', 'password2', 'email']

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.apply_styled_widgets()  

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

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

