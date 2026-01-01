from django.db import models

class User(models.Model):
    
    first_name = models.CharField(null=False,max_length=30, default='john')
    last_name = models.CharField(null=False,max_length=30, default='brian')
    dob = models.DateField(null=True)


# Define your first model from here:
