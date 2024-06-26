"""
URL configuration for LabConnect project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.views.generic import RedirectView
from Agenda.views import login_user, submit_login, logout_user, agenda, agendamento, data_analysis

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', agenda, name='agenda'),
    path('agendamento', agendamento, name='agendamento'),
    path('login_user', login_user, name='login_user'),
    path('login/submit', submit_login, name='submit_login'),
    path('logout', logout_user, name='logout_user'),
    path('data-analysis', data_analysis, name= 'data-analysis'),
]
