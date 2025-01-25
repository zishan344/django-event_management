from django.db import models

# Create your models here.
class Event(models.Model):
    """ class representing Event """
    name = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=250)
    category = models.ForeignKey('Category',on_delete=models.CASCADE)
    def __str__(self):
        return self.name 

class Participant(models.Model):
    """Class representing a Participant"""
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    attend_to= models.ManyToManyField(Event,related_name='event')
    def __str__(self):
        return self.name 

    # many to many relationships with event

class Category(models.Model):
    """ class representing a Category """
    name = models.CharField(max_length=250)
    description = models.TextField()
    def __str__(self):
        return self.name
