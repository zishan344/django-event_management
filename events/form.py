from django import forms
from .models import Category, Event
class StyledFormMixin:
    """Mixin to apply style to form fields."""
    default_classes = (
        "px-2 border-2 border-red-300 w-full focus:outline-none rounded-lg shadow-sm "
        "focus:border-red-500 focus:ring focus:ring-red-300 form-control"
    )
    checkbox_classes = "form-checkbox text-blue-500 focus:ring focus:ring-blue-300 form-control"
    select_classes = (
        "border-2 border-gray-300 w-full rounded-lg shadow-sm "
        "focus:border-blue-500 focus:ring focus:ring-blue-300"
    )

    def apply_styled_widgets(self):
        for field_name, field in self.fields.items():
            if isinstance(field.widget, (forms.TextInput, forms.PasswordInput, forms.EmailInput)):
                field.widget.attrs.update({
                    'class': self.default_classes,
                    'placeholder': f"Enter {field.label.lower()}",
                })
            elif isinstance(field.widget, forms.Textarea):
                field.widget.attrs.update({
                    'class': self.default_classes,
                    'placeholder': f"Enter {field.label.lower()}",
                })
                field.widget.attrs['value'] = self.initial.get(field_name, '') 
            elif isinstance(field.widget, forms.SelectDateWidget):
                field.widget.attrs.update({
                    "class": self.select_classes,
                })
            elif isinstance(field.widget, forms.CheckboxSelectMultiple):
                field.widget.attrs.update({
                    "class": "space-y-2" + self.checkbox_classes,
                })
            elif isinstance(field.widget, forms.Select):
                field.widget.attrs.update({
                    "class": self.default_classes,
                })
                field.widget.attrs['value'] = self.initial.get(field_name, '')  


class CategoryModelForm(StyledFormMixin, forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.apply_styled_widgets()
        print(self.initial)
        print("descriptions field",self.fields['description'].initial)
        for field_name, field in self.fields.items():
            # Check if 'instance' contains initial data
            if field_name in self.initial:
                field.widget.attrs['value'] = self.initial[field_name]
            elif self.instance and getattr(self.instance, field_name, None):
                field.widget.attrs['value'] = getattr(self.instance, field_name)



class EventModelForm(StyledFormMixin, forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'description', 'date', 'time', 'location', 'category','image']
        widgets = {
            'date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control',
            }),
            'time': forms.TimeInput(attrs={
                'type': 'time',
                'class': 'form-control',
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.apply_styled_widgets()
        if self.instance:
            self.fields['description'].initial = self.instance.description
            
        for field_name, field in self.fields.items():
            if field_name in self.initial:
                field.widget.attrs['value'] = self.initial[field_name]
        if 'category' in self.fields and hasattr(self.instance, 'category'):
            self.fields['category'].initial = self.instance.category



""" class ParticipantModelForm(StyledFormMixin, forms.ModelForm):
    class Meta:
        model = Participant
        fields = ['name', 'email', 'attend_to']
        labels = {
            'name': "Enter your Name"
        }
        widgets = {
            'attend_to': forms.CheckboxSelectMultiple
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.apply_styled_widgets()
"""
