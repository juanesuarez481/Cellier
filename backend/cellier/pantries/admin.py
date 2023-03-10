from django.contrib import admin

from .models import (Unit, Quantity, Ingredient, Recipe, Pantrie)
from .models import (QuantityRecipe, RecipePantrie)


class UnitAdmin(admin.ModelAdmin):
    list_display = ("name", "related_name")


class IngredientAdmin(admin.ModelAdmin):
    list_display = ("name", "related_name")


class IngredientQuantityInline(admin.StackedInline):
    model = QuantityRecipe
    extra = 1


class RecipeAdmin(admin.ModelAdmin):
    inlines = [IngredientQuantityInline,]
    list_display = ("name", "related_name")


admin.site.register(Unit, UnitAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Quantity)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Pantrie)
