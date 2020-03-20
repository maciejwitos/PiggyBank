from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, DeleteView, FormView
from app.forms import SigneUpForm
from app.models import *
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic.edit import DeletionMixin
from django.http import HttpResponse


class SignUp(View):

    def get(self, request):
        form = SigneUpForm()
        return render(request, 'user/register.html', {'form': form})

    def post(self, request):
        form = SigneUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/dashboard/')

        return render(request, 'user/register.html', {'form': form})


class UserDetails(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):
        return render(request, 'user/details.html')
