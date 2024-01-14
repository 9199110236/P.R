from django.shortcuts import render,redirect
from django.views import View
from .form import UserRegistrationForm

class RegisterView(View):
    def get(self,request):
        form = UserRegistrationForm()
        return render(request,'account/register.html',{'form':form})
    def post(self,request):
        pass

# Create your views here.
