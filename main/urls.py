from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('how-it-works/', views.how_it_works, name='how-it-works'),
    path('testing/', views.testing, name='testing'),
    path('contacts/', views.contacts, name='contacts'),
]
