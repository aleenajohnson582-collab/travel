import email
from urllib import request

from django import forms
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Booking, Contact
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import loginform
from django.contrib.admin.views.decorators import staff_member_required


def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == "POST":
        data = request.POST
        fname = data.get("first_name", "").strip()
        lname = data.get("last_name", "").strip()
        email = data.get("email", "").strip().lower()
        password = data.get("password", "")
        confirm_password = data.get("confirm_password", "")

        if not all([fname, lname, email, password, confirm_password]):
            messages.error(request, "All fields are required.")

        elif password != confirm_password:
            messages.error(request, "Passwords do not match.")

        elif User.objects.filter(username=email).exists():
            messages.error(request, "Email already registered.")

        else:
            user = User.objects.create_user(
                username=email,
                email=email,
                password=password,
                first_name=fname,
                last_name=lname
            )

            login(request, user)
            messages.success(request, "Account created successfully!")
            return redirect('home')

    return render(request, "signup.html")


def result(request):
    buses = [
        {'id': 1, 'name': 'Fast Travel', 'time': '08:30', 'price': 500, 'seats': 20, 'tag': 'Popular'},
        {'id': 2, 'name': 'Super Fast', 'time': '12:00', 'price': 700, 'seats': 15, 'tag': 'Premium'},
        {'id': 3, 'name': 'Comfort Plus', 'time': '18:45', 'price': 600, 'seats': 10, 'tag': 'Comfort'},
    ]

    return render(request, 'result.html', {'buses': buses})


@login_required
def booking(request):
    bus_id = request.GET.get('bus')

    buses = [
        {'id': 1, 'name': 'Fast Travel', 'time': '08:30'},
        {'id': 2, 'name': 'Super Fast', 'time': '12:00'},
        {'id': 3, 'name': 'Comfort Plus', 'time': '18:45'},
    ]

    selected_bus = None

    if bus_id:
        selected_bus = next((b for b in buses if str(b['id']) == bus_id), None)

    if request.method == 'POST':
        name = request.POST.get('name')
        from_place = request.POST.get('from')
        to_place = request.POST.get('to')
        travel_date = request.POST.get('date')
        seats = request.POST.get('seats')
        bus_name = request.POST.get('bus_name')
        travel_time = request.POST.get('travel_time')

        if not all([name, from_place, to_place, travel_date, seats]):
            messages.error(request, "All required fields must be filled.")
            return redirect(request.path)

        try:
            Booking.objects.create(
               name=name,
               from_place=from_place,
               to_place=to_place,
               travel_date=travel_date,
               seats=int(seats),
               bus_name=bus_name,
               travel_time=travel_time
           )
            

            messages.success(request, "Booking confirmed!")
            return redirect('confirmation')

        except Exception as e:
            messages.error(request, f"Error: {str(e)}")
            return redirect(request.path)

    return render(request, 'booking.html', {'selected_bus': selected_bus})



@login_required
def confirmation(request):
    booking = Booking.objects.last()

    return render(request, 'confirmation.html', {
        'booking': booking
    })

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        Contact.objects.create(
            name=name,
            email=email,
            message=message
        )

        return redirect('home')

    return render(request, 'contact.html')


@staff_member_required

def view_messages(request):
    messages = Contact.objects.all()
    return render(request, 'messages.html', {'messages': messages})



def admin_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_superuser:
            login(request, user)
            return redirect("dashboard")  # change to your page
        else:
            return render(request, "admin_login.html", {"error": "Invalid credentials"})

    return render(request, "admin_login.html")


def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Invalid credentials")

    return render(request, "login.html")


def logout_view(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect('index')


def index(request):
    return render(request, 'index.html')


