from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.core.mail import send_mail


class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User 
        fields = ("username", "email", "password1")

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
            send_mail(
                'Welcome',
                'Successful registration',
                'from@example.com',
                ['user.email'],
                fail_silently=False,
            )
        return user
