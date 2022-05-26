from django.shortcuts import get_object_or_404, render
from .utils.recipes.factory import make_recipe

from .models import Recipe, Category

# Create your views here.
def home(request):
    recipes = Recipe.objects.filter(published=True).order_by('-id')
    
    context = {
        # [make_recipe() for _ in range(10)]
        'recipes': recipes,
        'title': 'Home',
    }
    
    return render(request, 'recipes/home.html', context)

def category(request, cat_pk):
    category = get_object_or_404(Category, pk=cat_pk)
    recipes = category.recipe_set.filter(published=True)
    
    context = {
        'recipes': recipes,
        'title': f'{category}',
    }
    
    return render(request, 'recipes/home.html', context)

def recipe(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk, published=True)
    
    context = {
        'recipe': recipe,
        'title': recipe.title,
        'is_detail_page': True,
    }
    
    return render(request, 'recipes/recipe.html', context)
