from django.contrib import admin
from django.urls import path , include
from food import views

urlpatterns = [
    path('',views.Home,name="home"),
    path('home',views.Home,name="home"),
    path('about',views.about,name="about"),
    path('contact',views.contactu,name="contact"),
    path('fast',views.fastf,name="fast"),
    path('drink',views.drinks,name="drink"),
    path('rolls',views.rollss,name="rolls"),
    path('menu',views.Menu,name="menu")

]
