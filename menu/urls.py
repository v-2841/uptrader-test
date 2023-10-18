from django.urls import re_path

from menu import views


app_name = 'menu'
urlpatterns = [
    re_path(r'^', views.home, name='home'),
]
