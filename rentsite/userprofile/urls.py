from django.urls import path
from .views import ProfileView, CabinetView
from cars.views import CarsView, CarsAddView


app_name = 'cabinet'


urlpatterns = [
    path('', CabinetView.as_view(), name='cabinet'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('cars/', CarsView.as_view(), name='cars'),
    path('cars/add/', CarsAddView.as_view(), name='add-car')
]
