"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

from medicar_api import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('consultas/<int:consulta_id>/', views.delete_appointment),
    url('especialidades/$', views.get_specialty),
    url('medicos/$', views.get_doctors),
    url('agendas/$', views.get_doctors_schedule),
    url('consultas/$', views.make_appointment),
    url('consultas', views.get_appointment),
    url('login/', obtain_jwt_token),
    url('refresh_token', refresh_jwt_token),
    url(r'registration', views.register_user)
]
