from django.http import HttpResponse
from django.shortcuts import render

def health_check(request):
    return HttpResponse("Django APP is OKKKKKKKK")