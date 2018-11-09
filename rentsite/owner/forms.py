from django import forms
from .models import Profile
from django.contrib.auth.models import User

#class OwnerRegistrationForm(forms.ModelForm):
#    class Meta:
#        model = Owner
#        fields = ('name', 'phonenumber', 'email', 'password', 'city',
#                  'registration_photo', 'ident_code', 'owner_type')
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('owner_type', 'registration_photo')
