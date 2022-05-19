from django.shortcuts import render
from django.http import HttpResponse

from .utils.recipes.factory import make_recipe

# Create your views here.
def home(request):
    context = {
        'recipes': [make_recipe() for _ in range(10)]
    }
    
    return render(request, 'recipes/home.html', context)

def recipe(request, pk):
    context = {
        'recipe': make_recipe(),
        'is_detail_page': True,
    }
    
    return render(request, 'recipes/recipe.html', context)
