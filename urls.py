from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name= 'home-page'),
    path('contact-us/', views.Contact_Us, name='Contact_Us')
]
