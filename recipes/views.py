from django.shortcuts import get_object_or_404, render
from .utils.recipes.factory import make_recipe

from .models import Recipe, Category

# Create your views here.
def home(request):
    recipes = Recipe.objects.all().filter(published=True).order_by('-id')
    
    context = {
        # [make_recipe() for _ in range(10)]
        'recipes': recipes,
        'title': 'Home',
    }
    
    return render(request, 'recipes/home.html', context)

def category(request, cat_pk):
    category = get_object_or_404(Category, pk=cat_pk)
    recipes = category.recipe_set.all()
    
    context = {
        'recipes': recipes,
        'title': f'{category} | Category',
    }
    
    return render(request, 'recipes/home.html', context)

def recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    
    context = {
        'recipe': recipe,
        'is_detail_page': True,
    }
    
    return render(request, 'recipes/recipe.html', context)
