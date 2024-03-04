from django.shortcuts import render
from .models import Plant

# Add the following import
from django.http import HttpResponse

# Define the home view
def home(request):
  return HttpResponse('<h1>Hello plants')

def about(request):
  return render(request, 'about.html')



def plant_index(request):
  plants = Plant.objects.all()
  return render(request, 'plants/index.html', { 'plants': plants })