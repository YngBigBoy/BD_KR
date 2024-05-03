from django.shortcuts import render
from django.views import View
import json

# Create your views here.
class RegisterView(View):
    def get(self, request):
        return render(request, 'authentication/register.html')

class UserNameValidationView(View):
    def get(self, request):
        return render(request, 'authentication/register.html')
class LoginView(View):
    def get(self, request):
        return render(request, 'authentication/login.html')

