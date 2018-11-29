from django.urls import path
from .views import ProfileView
from cars.views import CarView


urlpatterns = [
    path('profile/', ProfileView.as_view(), name='profile'),
    path('cars/add/', CarView.as_view(), name='addCar')
]