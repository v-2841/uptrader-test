from django.urls import path

from menu import views


app_name = 'menu'
urlpatterns = [
    path('', views.home, name='home'),
]
