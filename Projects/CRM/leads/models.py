from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Lead(models.Model):
    source_choices = (
        ('Email','Email'),
        ('Web','Website'),
        ('Google','Google'),
        ('Newsletter','Newsletter')
    )
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    is_contacted = models.BooleanField(default=False)
    source = models.CharField(choices= source_choices, max_length=100)
    profile_picture = models.ImageField(blank=True,null=True)
    special_files = models.FileField(blank=True,null=True)
    email = models.EmailField(max_length=254)
    # Relation Key 
    ## Set to cascade if you want to delete 
    agent = models.ForeignKey("Agent", on_delete=models.SET_DEFAULT,default = 'Queued')
    
    # Relational Tables
    
class Agent(models.Model):
    user = models.OneToOneField("User",on_delete=models.CASCADE)

#When adding custom user class add it to the settings under AUTH_USER_MODEL variable
class User(AbstractUser):
    pass