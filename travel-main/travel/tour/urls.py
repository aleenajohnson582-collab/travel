from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('result/', views.result, name='result'),
    path('booking/', views.booking, name='booking'),
    path('confirmation/', views.confirmation, name='confirmation'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('messages/', views.view_messages, name='view_messages'),
    path('admin-login/', views.admin_login, name='admin_login'),
    path('approve/<int:id>/', views.approve_booking, name='approve_booking'),
    path('my-bookings/', views.view_booking, name='view_booking'),

]
