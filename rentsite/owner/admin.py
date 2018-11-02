from django.contrib import admin
from .models import Owner


class OwnerAdmin(admin.ModelAdmin):
    list_display = ('owner_id', 'name', 'email', 'phonenumber', 'cash_account')
    ordering = ('owner_id', 'phonenumber', 'cash_account')
    list_display_links = list_display

admin.site.register(Owner, OwnerAdmin)