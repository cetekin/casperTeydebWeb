from django.conf.urls.static import static
from django.urls import path
from django.conf.urls import url
from teydeb_main import settings

from . import views

urlpatterns = [
    path('', views.index, name='home'),


]
