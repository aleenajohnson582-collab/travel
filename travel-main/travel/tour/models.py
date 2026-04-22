from django.db import models
from django.contrib.auth.models import User

from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.user.username
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # ✅ ADD THIS

    name = models.CharField(max_length=100)
    is_approved = models.BooleanField(default=False)
    from_place = models.CharField(max_length=100)
    to_place = models.CharField(max_length=100)
    travel_date = models.DateField()
    seats = models.IntegerField()
    bus_name = models.CharField(max_length=100)
    travel_time = models.TimeField()

    def __str__(self):
        return self.name
 
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    
    def __str__(self):
        return self.name