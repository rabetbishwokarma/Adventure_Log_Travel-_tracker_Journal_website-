"""
URL configuration for canadatrip project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.urls import path,include
from django.urls import path
from trip_app_1 import views




urlpatterns = [
    path('admin/',admin.site.urls),
    path('accounts/login/',auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/',auth_views.LogoutView.as_view(), name='logout'),
    path('', include(('trip_app_1.urls', 'trip_app_1'), namespace='trip_app_1')),
    path('', views.index, name='index'),
]
