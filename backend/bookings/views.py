from django.shortcuts import render
from django.http import HttpResponse
from .forms import BookingForm

# Create your views here.

def index(request):
    return HttpResponse("We are good BOOKINGS")

def create_booking(request):
    if request.method == "POST":
        form = BookingForm(request.POST)

        if form.is_valid():
            pass

    else: 
        form = BookingForm()

    context = {
        "form": form
    }

    return render(
        request,
        "bookings/create.html",
        context=context
    )