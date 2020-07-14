from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name='store'),
    path('order/', views.store, name='order'),
    path('pay/', views.store, name='pay'),
    path('contact/', views.store, name='contact'),
    path('search/', views.store, name='search'),
]
