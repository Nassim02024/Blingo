from django.db import models
import uuid
from users.models import User  # تأكد أن هذا هو نموذج المستخدم المخصص لديك
from cloudinary.models import CloudinaryField

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
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='stores')
    title = models.CharField(max_length=100)
    # store_type = models.CharField(choices= chosetypestore  , default='food')
    contact = models.CharField(max_length=10 , blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    days_to_return = models.CharField(max_length=100)
    image = CloudinaryField('image', blank=True, null=True)
 
    def __str__(self):
        return self.title