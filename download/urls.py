from django.urls import path, include
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'$^', views.index, name="index"),
    url(r'^submit$', views.submit, name="submit"),
    url(r'^download$', views.download, name="download"),
]
