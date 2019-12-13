from django.conf.urls.static import static
from django.urls import path
from django.conf.urls import url
from teydeb_main import settings

from . import views

urlpatterns = [
    path('', views.default.home_page, name='home'),
    path('reference/', views.default.reference, name='reference'),
    path('login/', views.user.login, name='login'),
    path('logout/', views.user.logout, name='logout'),
    path('register/', views.user.register, name='register'),
    path('forgot-password/', views.user.forgot_password, name='forgot-password'),
    path('page_one', views.default.page_one, name='page-one'),
    path('page_two', views.default.page_two, name='page-two')

]
