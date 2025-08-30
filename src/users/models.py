from django.db import models
from django.contrib.auth.models import AbstractUser

 
class User(AbstractUser):
  email = models.EmailField(unique=True)
  username = models.CharField(max_length=150, unique=True)
  is_vendor = models.BooleanField(default=False)
  
  USERNAME_FIELD = "email"
  REQUIRED_FIELDS = ['username']
  
  def __str__(self):
      return self.username
  


  
