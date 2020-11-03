from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('how-it-works', views.how_it_works, name='how-it-works'),
    path('testing', views.testing, name='testing'),
    path('testing/gucci', views.testing_gucci, name='testing'),
    path('testing/new-balance', views.testing_new_balance, name='testing'),
    path('contacts', views.contacts, name='contacts'),
    path('done', views.done, name='done'),
]
