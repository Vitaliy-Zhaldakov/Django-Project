from django.contrib import admin
from .models import MaxResolution, Type, VideoCameras, Cameras, ActionCameras


# Register your models here.
class CamerasAdmin(admin.ModelAdmin):
    list_display = ('manufacturer', 'model', 'type', 'formatPrice')


class VideoCamerasAdmin(admin.ModelAdmin):
    list_display = ('manufacturer', 'model', 'maxResolution', 'formatPrice')


class ActionCamerasAdmin(admin.ModelAdmin):
    list_display = ('manufacturer', 'model', 'maxResolution', 'formatPrice')


admin.site.register(MaxResolution)
admin.site.register(Type)
admin.site.register(VideoCameras, VideoCamerasAdmin)
admin.site.register(Cameras, CamerasAdmin)
admin.site.register(ActionCameras, ActionCamerasAdmin)
