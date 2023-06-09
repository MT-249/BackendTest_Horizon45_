"""
URL configuration for driver project.

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
from truckapp.views import index
from django.urls import path
from django.urls import include, path
from truckapp.views import DriverListAPIView, DriverRetrieveAPIView, DriverCreateAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index,name="index"),
    path('drivers/', DriverListAPIView.as_view(), name='driver-list'),
    path('drivers/<int:pk>/', DriverRetrieveAPIView.as_view(), name='driver-detail'),
    path('drivers/create/', DriverCreateAPIView.as_view(), name='driver-create'),
    path('api/', include('truckapp.urls')),
]
