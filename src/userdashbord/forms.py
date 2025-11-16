from django import forms
from core.models import Product , Category

untiy_choices =(
  ('kg','kg'),
  ('g','g'),
  ("قطعة" , "قطعة"),
  ("دلو" , "دلو"),
  ("علبة" , "علبة"),
  ("قارورة" , "قارورة"),
  ("كيس" , "كيس"),
  ("رطل" , "رطل"),
  ("l" , "l"),
  ("m" , "m"),
)

catecory_choices = (
  ("البقوليات" , "البقوليات"),
  ("المشروبات" , "المشروبات"),
  ("عجائن" , "عجائن"),
  ("مواد التنظيف" , "مواد التنظيف"),
  ("طبخ و الماكولات" , "طبخ و الماكولات"),
  ("الخبز والحلويات" , "الخبز والحلويات"),
  ("اللحوم و مشتقاتها" , "اللحوم و مشتقاتها"),
  ("الفواكه والخضروات" , "الفواكه والخضروات"),
  ("المعلبات و المؤكولات الجاهزة"  , "المعلبات و المؤكولات الجاهزة" ),
  ("الحليب و مشتقاته", "الحليب و مشتقاته"),
  ("الزيوت و التوابل" , "الزيوت و التوابل"),
  ("المكسرات" , "المكسرات"),
  ("منتجات الاطفال" , "منتجات الاطفال"),
  ("منتجات المنزلية" , "منتجات المنزلية"),
  ("منتجات كهربائية" , "منتجات كهربائية"),
  ("منتجات الصحية" , "منتجات الصحية"),
  ("التجميل" , "التجميل"),
  ("الادوات المدرسية" , "الادوات المدرسية"),
)


STOCK_CHOICES = (
  ("yes" , "yes"),
  ("no" , "no"),
)

STATUS_CHOICES =  (
  ("draft" , "Draft"),
  ("disabled" , "Disabled"),
  ("rejected" , "Rejected"),
  ("in_review" , "In_review"),
  ("published" , "Published"),
)

 
class AddProductForms(forms.ModelForm):
  title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control' , 'placeholder': 'Enter product Name'}))
  category = forms.ModelChoiceField(queryset=Category.objects.all(),widget=forms.Select(attrs={'class': 'form-control'}))
  unity = forms.ChoiceField(choices = untiy_choices , widget=forms.Select(attrs={'class': 'form-select'}) ) 
  price = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control' , 'placeholder': 'Enter product price'}))
  old_price = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control' , 'placeholder': 'Enter product old_price'}))
  in_stock = forms.ChoiceField(choices=STOCK_CHOICES, widget=forms.Select(attrs={'class': 'form-select'}))
  product_status = forms.ChoiceField(choices=STATUS_CHOICES, widget=forms.Select(attrs={'class': 'form-select'}))
  image = forms.ImageField(widget = forms.FileInput(attrs = {'class':'form-control'}))
  class Meta:
     model = Product
     fields = ['title', 'image' , 'category', 'unity' , 'product_status', 'in_stock' , 'price', 'old_price']
