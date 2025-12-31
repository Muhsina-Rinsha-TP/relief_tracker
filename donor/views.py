from django.shortcuts import render
from volunteer.models import RequiredItem

def donor_home(request):
    items = RequiredItem.objects.all()
    return render(request, 'donor/donor_home.html', {'items': items})


# Create your views here.
