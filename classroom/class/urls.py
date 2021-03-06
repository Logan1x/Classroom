from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='click'),
    path('join/', views.join, name="join"),
    path('check/', views.check, name="check"),
    path('register/' ,views.register, name="register"),
]