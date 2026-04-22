from django.shortcuts import render
from .models import Bus, Booking

# 1️⃣ Home Page
def home(request):
    return render(request, 'home.html')


# 2️⃣ Bus List Page
def buses(request):
    buses = Bus.objects.all()
    return render(request, 'buses.html', )

# 3️⃣ Booking Page (handles form + submission)
def booking(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        seats = request.POST.get('seats')
        bus_id = request.POST.get('bus_id')

        bus = Bus.objects.get(id=bus_id)

        booking = Booking.objects.create(
            bus=bus,
            name=name,
            phone=phone,
            email=email,
            seats=seats
        )

        # 👉 Goes to confirmation page
        return render(request, 'confirmation.html', {'booking': booking})

    # 👉 When opening booking page
    bus_id = request.GET.get('bus_id')
    return render(request, 'booking.html', {'bus_id': bus_id})


# 4️⃣ Confirmation Page (optional)
def confirmation(request):
    return render(request, 'confirmation.html')