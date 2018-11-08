from django.contrib import admin
from .models import Owner, BlackList


class OwnerAdmin(admin.ModelAdmin):
    list_display = ('owner_id', 'name', 'email', 'phonenumber', 'cash_account', 'approve')
    ordering = ('owner_id', 'phonenumber', 'cash_account', 'approve')
    list_display_links = list_display

class BlackListAdmin(admin.ModelAdmin):
    list_display = ('blackownerid', 'owner_phonenumber', 'carsinblacklistvin')
    ordering = ('blackownerid', 'owner_phonenumber', 'carsinblacklistvin')
    list_display_links = list_display


admin.site.register(Owner, OwnerAdmin)
admin.site.register(BlackList, BlackListAdmin)