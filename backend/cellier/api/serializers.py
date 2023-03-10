from rest_framework import serializers
from pantries.models import Unit, Quantity, Ingredient, Recipe


class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = ['name', 'related_name']


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['name', 'related_name']


class QuantitySerializer(serializers.ModelSerializer):
    unit = UnitSerializer()
    ingredient = IngredientSerializer()

    class Meta:
        model = Quantity
        fields = ['value', 'unit', 'ingredient']


class RecipeSerializer(serializers.ModelSerializer):
    quantities = QuantitySerializer(many=True)

    class Meta:
        model = Recipe
        fields = ['name', 'related_name', 'preparation',
                  'preparation_time', 'difficulty',
                  'quantities', 'created_at']
