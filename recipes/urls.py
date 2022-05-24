from django.urls import path
from . import views


app_name = 'recipes'

urlpatterns = [
    path('', views.home, name='home'),
    path('recipes/category/<int:cat_pk>/', views.category, name='category'),
    path('recipes/<int:pk>/', views.recipe, name='recipe')
]