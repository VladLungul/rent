from django.conf.urls import url
from . import views

urlpatterns = [
    url('register/', views.RegisterFormView),
    url('', views.update_profile, name='profile'),
]