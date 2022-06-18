"""WaterBudget URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from WaterBudget import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.HomeView.as_view(),name="Home"),
    path('userhome/',views.RegisteredHomeView.as_view(),name="RegisteredHome"),
    path('login/',views.LoginView.as_view(),name="Login"),
    path('logout/',views.Logout,name="Logout"),
    path('register/',views.RegistrationView.as_view(),name="Register"),
    path('login/forgotpassword/',views.ForgotPasswordView.as_view(),name="ForgotPassword"),
    path('',include("groundwater.urls")),
    path('',include("waterbudgetapp.urls")),
    path('',include("Information.urls")),
    path('',include('CropRecommendation.urls'))
]
