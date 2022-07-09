from distutils.command.upload import upload
import email
from operator import imod
import profile
from pyexpat import model
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200, null=True, blank=True)
    profile_pic = models.ImageField(null=True, blank=True, upload_to = "Profile")
    bio = models.TextField(null=True, blank=True)

    def __str__(self):
        name = str(self.first_name)
        if self.last_name:
            name = " " + str(self.last_name )
        return name