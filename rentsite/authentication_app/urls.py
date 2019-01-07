from django.urls import path
from . import views

app_name = 'auth'


urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('edit/', views.password_edit, name='password_edit'),
]

