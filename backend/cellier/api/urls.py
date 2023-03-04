
from django.urls import path
from . import views

urlpatterns = [
    path('', views.ApiOverview, name='home'),
    path('all/', views.view_items, name='view_items'),
    path('ingredients/', views.view_ingredients, name='view_ingredients')
]
