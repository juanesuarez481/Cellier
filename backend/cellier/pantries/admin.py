from django.contrib import admin

from .models import Unit, Quantity, Ingredient, Recipe, Pantrie
from .models import Quantity, IngredientQuantityRecipe, RecipePantrie


class IngredientAdmin(admin.ModelAdmin):
    list_display = ("name", "related_name")


class RecipeAdmin(admin.ModelAdmin):
    list_display = ("name", "preparation_time",
                    "difficulty", "get_ingredients",
                    "preparation", "related_name")

    def get_ingredients(self, obj):
        return ", ".join([i.name for i in obj.ingredients.all()])


admin.site.register(Unit)
admin.site.register(Quantity)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(IngredientQuantityRecipe)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Pantrie)
admin.site.register(RecipePantrie)
