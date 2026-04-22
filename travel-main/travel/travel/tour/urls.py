from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.home, name='home'),            # Home page
    path('buses/', views.buses, name='buses'),    # Bus list page ✅
    path('booking/', views.booking, name='booking'),       # Home page  # Booking form
    path('confirmation/', views.booking, name='confirmation'),  # same view handles it
]
    


    