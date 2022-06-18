from django.views.generic.base import View
from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from django.contrib.auth import logout


def Logout(request):
    logout(request)
    return redirect('Home')


class HomeView(View):
    def get(self, request):
        if request.method == "GET":
            template_name = "UnregisteredHome.html"
            # return render(template_name=template_name)
            return render(request, 'UnregisteredHome.html')


class RegisteredHomeView(View):
    def get(self, request):
        if request.user.is_authenticated:
            template_name = "Home.html"
            template_page = render(request, template_name)
            return HttpResponse(template_page)
        else:
            return redirect('Login')


class LoginView(View):
    def get(self, request):
        template_name = "Login.html"
        template_page = render(request, template_name)
        return HttpResponse(template_page)

    def post(self, request):
        template_name = "Login.html"
        username = request.POST['username']
        password = request.POST['password']
        print(username, password)
        # query = User.objects.get(username=username, password=password)
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('RegisteredHome')
        else:
            context = {'login_error': True}
            template_page = render(request, template_name, context)
            return HttpResponse(template_page)


class RegistrationView(View):
    def get(self, request):
        template_name = "Registration.html"
        template_page = render(request, template_name)
        return HttpResponse(template_page)

    def post(self, request):
        template_name = "Registration.html"
        username = request.POST['username']
        firstName = request.POST['first_name']
        lastName = request.POST['last_name']
        password = request.POST['password']
        email_address = request.POST['email_address']
        email_address_unique = User.objects.filter(email=email_address).exists()
        username_unique = User.objects.filter(username=username).exists()
        confirm_password = request.POST['confirm_password']
        if password != confirm_password:
            password_notmatch = True
        else:
            password_notmatch = False
        if password != confirm_password or username_unique or email_address_unique:
            context = {'registered_status': False,
                       'password_error': password_notmatch,
                       'email_error': email_address_unique,
                       'username_error': username_unique}
            template_Page = render(request, template_name, context)
            return HttpResponse(template_Page)
        else:
            User.objects.create_user(username=username, first_name=firstName, last_name=lastName, email=email_address,
                                     password=password, is_active=True, is_staff=True, is_superuser=True)
            context = {'registered_status': True}
            template_Page = render(request, template_name, context)
            return HttpResponse(template_Page)


class ForgotPasswordView(View):
    def get(self, request):
        if request.method == "GET":
            template_name = "ForgotPassword.html"
            return render(template_name)
