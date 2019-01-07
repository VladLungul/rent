from django.urls import path
from . import views


app_name = 'mainapp'


urlpatterns = [
    path('', views.RentType.as_view(), name='index'),
    path('<str:rent_type>/', views.CarClass.as_view(), name='car_class'),
    path('<str:rent_type>/<str:car_class>/', views.CarList.as_view(), name='car-list'),
]
