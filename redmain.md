1. Setup Project

  - projects ecomersprj

  - Cmats new app core

  - Install Apps in Settings

  - Configure Static and Media Files in settings and Urls.py

  - Create a new view, urla and template then runserve

  - Configure template inheritance and partials

2. Configure Admin Page, Superuser and partials

  - install Jazzmin (pip intall django-jazzmin)

  - Add jazzmin is INSTALLED APPS

  - Add Jazzmier Config Code in Settings.av

  - Create database Postgres

  - Login To admin sitting

3. Custom User Model

  - Create new app userauths

  - install apps in settings

  - create custom class User in models.py

  - add AUTH_USER_MODEL in settings.py

  - comment out django.contrib.admin and admin url in settings.py

  - run makemigrations and migrate 

  - create new superuser

  - register user  model in admin.py

  - login to admin with email and password

4. user Registration system

 - Create new form class UserRegisterForm(UserCreationForm): in forms.py

  - write view to register (def registerView(request):) user

  - Configure templates to show form

  - login to website from frontend



5. User Login System

 - Write view to login (def loginView(request):)

 - Configure templates to grab input filed

 - login website from frontend

6. User Logout System

  - Write view to logout (def logoutView(request):)

  - Configure URL

  - test the Feature

7. Alerts in Django

  - Grab Alert Seppet from Bootstrap (vertion 4)

  - Capy and Paste CDN

  - Write alert conditional statement in template

8. Django Context Processor for Template

  - Create noe file contex_process.py in core app 

  - install in setting.py TEMPLATES Section list as "core.context processors.default"

  - Now Add Core for context Processor

9. Product Model Structure

  - Create new Model Class and Add filed for product

  - Register Model in admin.py

10. 
  
  - Create logic to Display only featured Product in Home Page

  - Create new view list All the Active Product from the DB

  - configure URL and Template

11. Category List View

  - Create New view to List All active categories

  - Configure Urts.py and Template

12. Product Category List View

  - Create New view to List All The Active products from the DB depending on the category selected.

  - Configure Urts.py and Template

13. Product Detail View

  - Create New view to showcase the Details of a selected Product using pid

  - Configure Urts.py and Template

14. Product Rating and Review

 - Get all reviews in Product Detail and Lists them out in the Templates

 - Calculate the average rating of the product

style="color:rgb(194, 192, 192);"
  
  




