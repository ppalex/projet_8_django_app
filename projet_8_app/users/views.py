from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

from .forms import CustomUserCreationForm

from django.contrib.auth.views import LoginView
from django.views import View

class RegisterView(View):

    register_form = CustomUserCreationForm
    template_name = 'users/register.html'

    def get(self, request):
        form = self.register_form()
        context = {'form' : form}

        return render(request, self.template_name, context)

    def post(self, request):
        form = self.register_form(request.POST)
        print('register')

        print(form)
        if form.is_valid():

            print('form valided')
            form.save()           
            print('form saved')
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(username=username, password=password)
            messages.success(request, "Votre compte a été créé")

            return redirect('index')

        return self.get(request)



class LoginView(SuccessMessageMixin, LoginView):
    template_name = 'auth/login.html'
    
    success_message = "You were successfully logged in!"

   



class ProfileView(View):
    pass
