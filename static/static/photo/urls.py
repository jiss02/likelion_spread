from django.urls import path
from . import views

urlpatterns = [
    path('', views.photo, name='photo'),
    path("new/", views.new, name="photonew"),
    path('create/', views.create, name= 'photocreate'),
]
