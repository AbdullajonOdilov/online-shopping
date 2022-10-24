from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View

from .models import Profil
from django.core.mail import send_mail
from django.conf import settings


class LoginView(View):
    def get(self, request):
        return render(request, 'page-user-login.html')

    def post(self, request):
        user = authenticate(username=request.POST.get('login'),
                            password = request.POST.ger('password'))

        if user is None:
            return redirect('/')
        login(request, user)
        return redirect('/asosiy/')

class LogoutView(View):
    def get(self,request):
        logout(request)
        return redirect('/')
class RegisterView(View):
    def get(self,request):
        return render(request,'page-user-register.html')
    def post(self,request):
        if request.POST.get('p1') != request.POST.get('p2'):
            return redirect('/user/register/')
        user = User.objects.create_user(
            username = request.POST.get('f'),
            email = request.POST.get('e'),
            password = request.POST.get('p1'),
            first_name = request.POST.get('f'),
            last_name = request.POST.get('l'),
        )
        Profil.objects.create(
            shahar = request.POST.get('sh'),
            tel = request.POST.get('t'),
            jins = request.POST.get('gender'),
            user = user
        )
        send_mail(
            subject='Welcome message',
            message='Alistyle online store',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[user.email],
            fail_silently=True)

        return redirect('/user/login/')




