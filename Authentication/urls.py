from django.contrib import admin
from django.urls import path
from Authentication import views


urlpatterns = [
    path('signup',views.signup, name ='signup'),
    path('login',views.login, name ='login'),
]
