from django.shortcuts import render
from django.views import View

from cars.choice import CAR_CLASS, RENT_TYPE


RENT_TYPE_SLUG_MAP = {'pochasovaya': 'Hourly',
                      'posutochnaya': 'Daily',
                      'dolgosrochnaya': 'Longterm',
                      }


CAR_CLASS_SLUG_MAP = {'econom-class': 'Econom',
                      'sredniy-class': 'Middle',
                      'biznes-class': 'Business',
                      'premium-class': 'Premium'
                      }


class RentType(View):
    template_name = 'mainapp/index.html'

    def get(self, request):
        return render(request, self.template_name)


class CarClass(View):
    template_name = 'mainapp/car_class.html'

    def get(self, request, rent_type):

        if rent_type not in RENT_TYPE_SLUG_MAP:
            return render(request, 'mainapp/page404.html')
        return render(request, self.template_name)


class CarList(View):
    template_name = 'mainapp/car_list.html'

    def get(self, request, rent_type, car_class):
        if rent_type not in RENT_TYPE_SLUG_MAP or car_class not in CAR_CLASS_SLUG_MAP:
            return render(request, 'mainapp/page404.html')
        # cars = Car.ojects.filter(rent_type=rent_type, car_class=car_class)
        context = {'cars': {}}
        return render(request, self.template_name, context=context)
