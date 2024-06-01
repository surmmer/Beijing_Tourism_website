from django.urls import path
from . import views

urlpatterns = [
    path('', views.sign_in, name='sign_in'),
    path('sign_in/', views.sign_in, name='sign_in'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('information/', views.information, name='information'),
    path('scenery/', views.scenery, name='scenery'),
    path('food/', views.food, name='food'),
    path('index/', views.index, name='index'),
]
