from django.db import models
from users.models import User  # تأكد أن هذا هو نموذج المستخدم المخصص لديك

chosetypestore = (
  ("men" , "men"),
  ("food" , "food"),
  ("women" , "women"),
  ("kids" , "kids"),
  ("accessories" , "accessories"),
  ("shoes" , "shoes"),
  ("bags" , "bags"),
  ("jewelry" , "jewelry"),
  ("home" , "home"),
  ("beauty" , "beauty"),
)
class UserStore(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    store_name = models.CharField(max_length=100)
    store_type = models.CharField(choices= chosetypestore  , default='food')
    description = models.TextField(max_length=200 , blank=True, null=True)
    phone_number = models.CharField(max_length=10 , blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='store_images/', blank=True, null=True)
 
    def __str__(self):
        return self.store_name
