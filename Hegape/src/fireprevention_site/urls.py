"""fireprevention_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from fpxlsxrw  import views as viewsfpxlsxrw
from userauth import views as viewuser
from django.views.generic import TemplateView

urlpatterns = [
    path('',viewuser.login , name='root'),
    path('home',viewsfpxlsxrw.bienvenido , name='home'),
    path('admin/', admin.site.urls),
    path('lawea/', viewsfpxlsxrw.print_lawea, name='print_lawea'),
    path('readxlsx/', viewsfpxlsxrw.read_excel, name='read_excel'),
    path('login',viewuser.login , name='login'),
    path('register',viewuser.register, name='register'),
    path('logout/', viewuser.logout_view, name='logout'),
    path('static/css/style.css', TemplateView.as_view(template_name='css/style.css', content_type='text/css')),
    
]
