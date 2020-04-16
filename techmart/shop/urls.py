from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index' ),
    path('contact/', views.contact, name='contact' ),
    path('about/', views.about, name='about' ),
    path('product/<int:id>', views.Product, name='Product' ),
    path('check_out/', views.check_out, name='check_out' ),
    path('tracker/', views.tracker, name='tracker' ),
]