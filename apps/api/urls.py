from django.urls import path

from . import views

urlpatterns = [
    path('upload/', views.simple_upload, name='simple_upload'),
]
#if settings.DEBUG:
#    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
