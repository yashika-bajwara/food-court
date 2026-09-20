from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('menu/', views.menu, name='menu'),
    path('order/', views.order, name='order'),
    path('success/<int:order_id>/', views.success, name='success'),
    path('contact/', views.contact, name='contact'),
]