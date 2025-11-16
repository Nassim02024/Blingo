
from django import forms

from core.models import Vendor
class creatvendor(forms.ModelForm):
  title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control' , 'placeholder': 'name'}))
  address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control' , 'placeholder': 'address'}))
  contact = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control' , 'placeholder': '+213 '}))
  days_to_return = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control' , 'placeholder': 'days_to_return'}))
  image = forms.ImageField(widget = forms.FileInput(attrs = {'class':'form-control'}))

  class Meta:
     model = Vendor
     fields = ['title', 'address' , 'contact', 'days_to_return' , 'image']
