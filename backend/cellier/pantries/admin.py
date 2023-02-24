from django.contrib import admin

from .models import Ingredient, Recipe, Pantrie, IngredientRecipe, RecipePantrie


class IngredientAdmin(admin.ModelAdmin):
    list_display = ("name", "get_quantity")

    def get_quantity(self, obj):
        return str(obj.quantity)+" "+obj.quantity_unit


class RecipeAdmin(admin.ModelAdmin):
    list_display = ("name", "get_preparation_time",
                    "difficulty", "get_ingredients",
                    "preparation")

    def get_preparation_time(self, obj):
        return str(obj.preparation_time)+" "+str(obj.preparation_time_unit)

    def get_ingredients(self, obj):
        return ", ".join([i.name for i in obj.ingredients.all()])


admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Pantrie)
admin.site.register(IngredientRecipe)
admin.site.register(RecipePantrie)
