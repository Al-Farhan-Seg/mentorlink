from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from .forms import BookingForm


# Create your views here.


def index(request):
    return HttpResponse("We are good BOOKINGS")

@login_required
def create_booking(request):
    if request.user.role != "student":
        raise PermissionDenied

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