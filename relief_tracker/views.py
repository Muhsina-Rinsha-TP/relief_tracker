from django.http import HttpResponse

def home(request):
    return HttpResponse("Relief Supply Chain Tracker is Running Successfully!")
