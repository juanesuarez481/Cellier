from rest_framework import serializers
from pantries.models import Unit, Quantity, Ingredient, Recipe, Info, Fact, Nutrition


class FactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fact
        fields = ['name', 'description']


class InfoSerializer(serializers.ModelSerializer):
    facts = FactSerializer(many=True)

    class Meta:
        model = Info
        fields = ['name', 'origin',
                  'availability', 'facts']


class NutritionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nutrition
        fields = ['name', 'water', 'fiber', 'vitamins',
                  'minerals', 'carbs', 'lipids', 'proteins']


class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = ['name', 'related_name']


class IngredientSerializer(serializers.ModelSerializer):
    info = InfoSerializer()
    nutrition = NutritionSerializer()

    class Meta:
        model = Ingredient
        fields = ['name', 'related_name', 'info', 'nutrition']


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
