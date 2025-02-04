from django.db import models
from django.contrib.auth.models import User

# category models
class Category(models.Model):
    """ class representing a Category """
    name = models.CharField(max_length=250)
    description = models.TextField()
    def __str__(self):
        return self.name

# event models
class Event(models.Model):
    """ class representing Event """
    name = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=250)
    category = models.ForeignKey('Category',on_delete=models.CASCADE)
    participant = models.ManyToManyField(User,related_name='rsvp_event', blank=True)
    def __str__(self):
        return self.name


