from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name='store'),
    path('order/', views.order, name='order'),
    path('pay/', views.pay, name='pay'),
    path('contact/', views.contact, name='contact'),
    path('search/', views.search, name='search'),
]
