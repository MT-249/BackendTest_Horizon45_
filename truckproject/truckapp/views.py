from django.shortcuts import render
from .forms import driverForm

def index(request):
    return render(request, "index.html")

def contact_view(request):
    form = driverForm()
    # Other view logic...
    return render(request, 'T-rucker.html', {'form': form})


