from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.urls import reverse_lazy
from django.shortcuts import render
from django.shortcuts import redirect

from .forms import ProfileForm


class ProfileView(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')
    redirect_field_name = 'redirect_to'

    def get(self, request):
        profile = request.user.userprofile
        form = ProfileForm(instance=profile)
        return render(request, 'userprofile/profile.html', context={'form': form})

    def post(self, request):
        profile = request.user.userprofile
        form = ProfileForm(request.POST, request.FILES or None, instance=profile)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('profile'))
        return render(request, 'userprofile/profile.html', context={'form': form})


class CabinetView(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')
    redirect_field_name = 'redirect_to'
    
    def get(self, request):
        return render(request, 'userprofile/cabinet.html')
