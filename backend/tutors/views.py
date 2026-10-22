from django.shortcuts import render, get_object_or_404
from .models import TutorProfile

# Create your views here.

def index(request):

    tutors = TutorProfile.objects.all()

    context = {
        "tutors": tutors
    }
    return render(request, template_name="tutors/tutors.html", context=context)


def tutor_detail(request, tutor_id):
    tutor = get_object_or_404(TutorProfile, pk=tutor_id) #Find the TUTOR with this primary key. If it doesn't exist, return an HTTP 404 response rather than allowing an unhandled DoesNotExist exception.
    context = {
        "tutor": tutor,
        "subjects": tutor.subjects.all(),
        "availability_slots": tutor.availability_slots.all()
    }

    return render(
        request,
        "tutors/detail.html",
        context=context
    )