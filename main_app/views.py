from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Plant
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin



class Home(LoginView):
  template_name = 'home.html'

def about(request):
  return render(request, 'about.html')

@login_required
def plant_index(request):
  plants = Plant.objects.filter(user=request.user)
  return render(request, 'plants/index.html', { 'plants': plants })

@login_required
def plant_detail(request, plant_id):
  plant = Plant.objects.get(id=plant_id)
  return render(request, 'plants/detail.html', { 'plant': plant })

class PlantCreate(LoginRequiredMixin, CreateView):
  model = Plant
  fields = ['name', 'species', 'description', 'waterNeeded', 'sunHoursNeeded']
  success_url = '/plants/'
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class PlantUpdate(LoginRequiredMixin, UpdateView):
  model = Plant
  fields = fields = ['name', 'species', 'description', 'waterNeeded', 'sunHoursNeeded']

class PlantDelete(LoginRequiredMixin, DeleteView):
  model = Plant
  success_url = '/plants/'

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('plant-index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)