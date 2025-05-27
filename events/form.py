from django import forms
from .models import Category, Event

class StyledFormMixin:
    """Mixin to apply style to form fields."""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.apply_styled_widgets()

    default_classes = (
        "px-2 border-2 border-primary w-full focus:outline-none rounded-lg shadow-sm "
        "focus:border-primary focus:ring-primary form-control"
    )
    checkbox_classes = "form-checkbox text-blue-500 focus:ring-primary focus:ring-red-300 form-control"
    select_classes = (
        "border-2 border-gray-300 w-full rounded-lg shadow-sm "
        "focus:border-primary focus:ring-primary"
    )
    file_input_classes = (
        "block w-full mb-5 text-xs text-gray-900 border border-gray-300 rounded-lg cursor-pointer "
        "bg-gray-50 dark:text-gray-400 focus:outline-none dark:bg-gray-700 dark:border-gray-600 "
        "dark:placeholder-gray-400"
    )

    def apply_styled_widgets(self):
        for field_name, field in self.fields.items():
            label = field.label if field.label is not None else ''
            # Add margin for spacing
            field.widget.attrs['class'] = (field.widget.attrs.get('class', '') + ' mb-3').strip()
            if isinstance(field.widget, (forms.TextInput, forms.PasswordInput, forms.EmailInput, forms.Textarea)):
                field.widget.attrs.update({
                    'class': self.default_classes + ' mb-3',
                    'placeholder': f"Enter {label.lower()}" if label else '',
                })
                field.initial = self.initial.get(field_name, '')
            
            elif isinstance(field.widget, forms.SelectDateWidget):
                field.widget.attrs.update({
                    "class": self.select_classes + ' mb-3',
                })
            
            elif isinstance(field.widget, forms.CheckboxSelectMultiple):
                field.widget.attrs.update({
                    "class": "space-y-2 " + self.checkbox_classes + ' mb-3',
                })
            
            elif isinstance(field.widget, forms.FileInput):
                field.widget.attrs.update({
                    "class": self.file_input_classes + ' mb-3',
                })
            
            elif isinstance(field.widget, forms.Select):
                field.widget.attrs.update({
                    "class": self.default_classes + ' mb-3',
                })
                field.initial = self.initial.get(field_name, '')

                if not field.widget.attrs.get('placeholder'):
                    field.widget.attrs['placeholder'] = f"Select {label.lower()}" if label else ''
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
