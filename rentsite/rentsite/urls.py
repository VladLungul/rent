from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('authenticate/', include('authentication_app.urls')),
    path('', include('mainapp.urls')),
]
