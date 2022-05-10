from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'recipes/home.html')

def contact(request):
    return render(request, 'recipes/contact.html')

def about(request):
    return render(request, 'recipes/about.html')