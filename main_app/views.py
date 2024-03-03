from django.shortcuts import render

# Add the following import
from django.http import HttpResponse

# Define the home view
def home(request):
  return HttpResponse('<h1>Hello plants')

def about(request):
  return render(request, 'about.html')


class Plant:
  def __init__(self, name, species, description):
    self.name = name
    self.species = species
    self.description = description

plants = [
  Plant('Farah', 'fern', 'Long & leafy'),
  Plant('Carrie', 'cactus', 'Short & sharp'),
]

def plant_index(request):
  return render(request, 'plants/index.html', { 'plants': plants })