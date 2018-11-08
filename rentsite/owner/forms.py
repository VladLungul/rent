from django import forms
from .models import Owner

class OwnerRegistrationForm(forms.ModelForm):
    class Meta:
        model = Owner
        fields = ('name', 'phonenumber', 'email', 'password', 'city',
                  'registration_photo', 'ident_code', 'owner_type')
