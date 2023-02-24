from rest_framework import serializers
from pantries.models import Ingredient, Recipe


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['name', 'quantity', 'quantity_unit']


class RecipeSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many=True)

    class Meta:
        model = Recipe
        fields = ['name', 'ingredients', 'preparation',
                  'preparation_time', 'preparation_time_unit', 'difficulty', 'created_at']