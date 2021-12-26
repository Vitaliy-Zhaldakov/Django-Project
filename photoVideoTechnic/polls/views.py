from django.shortcuts import render, get_object_or_404, redirect
from .models import Cameras
from .forms import CameraForm

# Create your views here.


def technicHome(request):
    homeTable = Cameras.objects.all()
    context = {
        'homeTable': homeTable
    }
    return render(request, 'home.html', context)


def technicDetail(request, id=None):
    camera = get_object_or_404(Cameras, id=id)
    context = {
        'camera': camera
    }
    return render(request, 'technicDetail.html', context)


def technicCreate(request):
    error = ''
    if request.method == 'POST':
        form = CameraForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
        else:
            error = 'Форма была не верной'

    form = CameraForm()

    context = {
        'form': form,
        'error': error

    }
    return render(request, 'technicCreate.html', context)
