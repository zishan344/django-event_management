from django import template
from datetime import datetime
from django.utils import timezone

register = template.Library()


@register.filter
def humanized_date(value):
    if value:
        today = datetime.now().date()
        value = timezone.localtime(value)
        if value.date() == today:
            return f"Today at {value.strftime('%I:%M %p')}"
        if value.date() == today.replace(day=today.day - 1):
            return f"Yesterday at {value.strftime('%I:%M %p')}"
        else:
            return f"{value.date().strftime('%B %d')}, {value.strftime('%I:%M %p')}"
    return "No login record available"


@register.filter(name='add_class')
def add_class(field, css_class):
    """
    Add CSS classes to form fields
    Usage: {{ form.field|add_class:"my-class another-class" }}
    """
    return field.as_widget(attrs={"class": css_class})