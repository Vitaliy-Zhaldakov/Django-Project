from django.forms import ModelForm
from .models import Cameras


class CameraForm(ModelForm):
    class Meta:
        model = Cameras
        fields = ['manufacturer', 'model', 'type', 'price']
