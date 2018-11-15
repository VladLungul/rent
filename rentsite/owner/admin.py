from django.contrib import admin
from .models import Profile


#class ProfileAdmin(admin.ModelAdmin):
#    list_display = ('first_name', 'last_name', 'email')
   # ordering = ('owner_id', 'phonenumber', 'cash_account', 'approve')
#    list_display_links = list_display

#class BlackListAdmin(admin.ModelAdmin):
#    list_display = ('blackownerid', 'owner_phonenumber', 'carsinblacklistvin')
#    ordering = ('blackownerid', 'owner_phonenumber', 'carsinblacklistvin')
#    list_display_links = list_display


admin.site.register(Profile)
#admin.site.register(BlackList, BlackListAdmin)