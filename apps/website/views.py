from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.conf import settings
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import Permission


# Create your views here.
from teydeb_main.settings import BASE_DIR


class user:
    def login(request):
        if request.method == 'POST':  # 1
            user = authenticate(username=request.POST['username'], password=request.POST['password'])
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                return render(request, BASE_DIR + '/templates/website/user/login.html',
                              {"message": "username/password invalid"})
            
        return render(request, BASE_DIR + '/templates/website/user/login.html',
                      {"message": ""})

    def logout(request):
        logout(request)
        return redirect("home")

    def register(request):
        return render(request, BASE_DIR + '/templates/website/user/register.html')
    
    def forgot_password(request):
        return render(request, BASE_DIR + '/templates/website/user/forgot-password.html')
    

class default:
    @login_required
    def home_page(request):
        return render(request, BASE_DIR+'/templates/website/_base.html')

    def reference(request):
        return render(request, BASE_DIR+'/templates/website/_reference.html')

    def page_one(request):
        return render(request, BASE_DIR+'/templates/website/page_one.html')

    def page_two(request):
        return render(request, BASE_DIR+'/templates/website/page_two.html')