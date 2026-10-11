from django.http import HttpResponse

def health_check(request):
    return HttpResponse("Django APP is OKKKKKKKK")