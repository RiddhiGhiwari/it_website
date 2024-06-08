# myapp/urls.py

from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about/',views.about,name='about'),
    path('index/',views.index,name='index'),
    path('services/',views.services,name='services'),
    path('contact/',views.contact,name='contact'),
    path('blog/',views.blog,name='blog'),
    path('careers/',views.careers,name='careers'),
    path('contact/save_contact/',views.savecontact,name='savecontact')


]
