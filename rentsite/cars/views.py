from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View

from .forms import CarForm

# Create your views here.
class CarView(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')
    redirect_field_name = 'redirect_to'

    def get(self, request):
        form = CarForm()
        return render(request, 'cars/addCar.html', context={'form': form})

    
    def post(self, request):
        form = CarForm(request.POST, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('profile'))
        return render(request, 'cars/addCar.html', context={'form': form})