from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View

from .forms import CarForm
from . import models


class CarsView(View):
    def get(self, request):
        cars = models.Car.objects.filter(owner=request.user)
        return render(request, 'cars/car-list.html', {'cars': cars})        


class CarsAddView(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')
    redirect_field_name = 'redirect_to'

    def get(self, request):
        form = CarForm()
        return render(request, 'cars/addCar.html', context={'form': form})

    def post(self, request):
        files = request.FILES.getlist('imgs')
        print(request.FILES)
        print('post', files)
        form = CarForm(request.POST, request.FILES or None)
        if form.is_valid():
            car = form.save(commit=False)
            car.owner = request.user
            car.save()
            for file in files:
                models.CarImage.objects.create(car=car, image=file)
            return redirect(reverse_lazy('profile'))
        return render(request, 'cars/addCar.html', context={'form': form})
