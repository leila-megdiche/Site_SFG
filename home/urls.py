from django.urls import path

from . import views

urlpatterns = [
    path("", views.Home, name="index"),
    path("Home/", views.Home, name="index"),
    path('about/', views.AboutUs, name='about'),
    path('project/', views.project, name='project'),
    path('quote/', views.quote, name='quote'),
    path('contact/', views.contact, name='contact'),
    path('service/', views.service, name='service'),
    path('team/', views.team, name='team'),
    path('ereur/', views.ereur, name='ereur'),
    path('testimonial/', views.testimonial, name='testimonial'),
    path('feature/', views.feature, name='feature'),
]