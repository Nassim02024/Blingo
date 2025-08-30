from django import forms
from .models import UserStore

class UserStoreForm(forms.ModelForm):
  class Meta:
    model = UserStore
    fields = ['name' , 'store_name' , 'store_type' , 'description' , 'phone_number' , 'address' ,'image']
