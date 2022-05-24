from django.shortcuts import render
from .utils.recipes.factory import make_recipe

from .models import Recipe

# Create your views here.
def home(request):
    recipes = Recipe.objects.all().order_by('-id')
    
    context = {
        # [make_recipe() for _ in range(10)]
        'recipes': recipes
    }
    
    return render(request, 'recipes/home.html', context)

def category(request, cat_pk):
    recipes = Recipe.objects.filter(category__id=cat_pk)
    
    context = {
        'recipes': recipes
    }
    
    return render(request, 'recipes/home.html', context)

def recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    
    context = {
        'recipe': recipe,
        'is_detail_page': True,
    }
    
    return render(request, 'recipes/recipe.html', context)
