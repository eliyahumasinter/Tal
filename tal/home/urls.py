from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('donate/', views.donate, name='donate'),
    path('getemail/', views.getemail, name='getemail'),
    path('events/', views.events, name='events'),
    path('about/', views.about, name='about'),
]
