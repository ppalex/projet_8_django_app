from django.shortcuts import render, redirect
from django.views import View

class FavouriteView(View):

    
    def get(self, request):
        template_name = 'favourites/favourites.html'       
        
        context = {}

        return render(request, template_name, context)


    def post(self, request):
        template_name = 'substitutes/substitute.html'
        context = {}

        if request.method == 'POST':
            if request.POST['favourite_save'] == 'Sauvegarder':
                print('save in substitute in DB')
                
        
        return redirect('substitute')