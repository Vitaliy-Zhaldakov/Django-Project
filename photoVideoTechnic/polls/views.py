from django.shortcuts import render
from django.http import HttpResponse
from .models import Cameras


# Create your views here.
def index(request):
    selection = Cameras.objects.filter(id=1)
    output = ', '.join(elem for elem in selection)
    return HttpResponse(selection)
