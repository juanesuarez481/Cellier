
from django.urls import path
from . import views

urlpatterns = [
    path('', views.ApiOverview, name='home'),
    path('recipes/', views.view_recipes, name='view_recipes'),
    path('ingredients/', views.view_ingredients, name='view_ingredients'),
    path('quantities/', views.view_quantities, name='view_quantities'),
    path('units/', views.view_units, name='view_units'),
    path('nutrition/', views.view_nutrition, name='view_nutrition'),
    path('info/', views.view_info, name='view_info')
]
