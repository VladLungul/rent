from django.contrib import admin
from .models import Car, Rent_type

class CarAdmin(admin.ModelAdmin):
    list_display = ('car_id', 'manufacturer', 'model', 'grade', 'year', 'fuel_type', 'engine_capacity',
                    'car_class', 'rent_type', 'price', 'discount', 'active', 'create_date',
                    'update_date', 'city', 'owner')
    ordering = ('car_id', 'rent_type')
    list_display_links = list_display

class RenttypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = list_display

admin.site.register(Car, CarAdmin)
admin.site.register(Rent_type, RenttypeAdmin)