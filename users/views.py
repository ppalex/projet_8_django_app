from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login
from django.contrib import messages

from django.contrib.messages.views import SuccessMessageMixin
from .forms import CustomUserCreationForm

from django.views import View
from django.contrib.auth.views import LoginView, LogoutView


class RegisterView(View):

    register_form = CustomUserCreationForm
    template_name = 'users/register.html'

    def get(self, request):
        form = self.register_form(request.GET)
        context = {'form' : form}

        return render(request, self.template_name, context)

    def post(self, request):
        form = self.register_form(request.POST)   
        
        if form.is_valid():
            
            form.save()           
            
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(username=username, password=password)
            messages.success(request, "Votre compte a été créé")

            return redirect('index')

        return self.get(request)



class CustomLoginView(SuccessMessageMixin, LoginView):
    
    success_url = '/'
    success_message = "Vous êtes connectés %(username)s"


class CustomLogoutView(SuccessMessageMixin, LogoutView):
    
    success_url = '/'
    success_message = "Vous êtes déconnectés"



class ProfileView(View):
    template_name = 'users/profile.html'

    def get(self, request):   
        

        return render(request, self.template_name)
