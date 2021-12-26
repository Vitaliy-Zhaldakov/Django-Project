from django.conf.urls import url

from .views import technicCreate, technicHome, technicDetail

urlpatterns = [
    url(r'^home/$', technicHome, name='homepage'),
    url(r'^create/$', technicCreate, name='create'),
    url(r'^detail/(?P<id>\d+)/$', technicDetail, name='detail')
]
