from django.contrib import admin

from .models import (Unit, Quantity, Ingredient, Recipe,
                     Pantrie, Info, Fact, Nutrition)
from .models import (QuantityRecipe, FactInfo)


class InfoFactsInline(admin.StackedInline):
    model = FactInfo
    extra = 1


class InfoAdmin(admin.ModelAdmin):
    inlines = [InfoFactsInline,]
    list_display = ("name", "origin")


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


admin.site.register(Info, InfoAdmin)
admin.site.register(Fact)
admin.site.register(Nutrition)
admin.site.register(Unit, UnitAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Quantity)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Pantrie)
