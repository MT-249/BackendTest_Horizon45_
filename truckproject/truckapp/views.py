from django.shortcuts import render
from .forms import driverForm

def index(request):
    return render(request, "index.html")

def contact_view(request):
    form = driverForm()
    # Other view logic...
    return render(request, 'T-rucker.html', {'form': form})

from rest_framework import generics
from .models import Driver
from .serializers import DriverSerializer

class DriverListAPIView(generics.ListAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer

class DriverCreateAPIView(generics.CreateAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer