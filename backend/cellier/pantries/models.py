from django.db import models


class Ingredient(models.Model):
    LITRE = 'Litre'
    MILILITRE = 'Mililitre'
    GRAMS = 'Grams'
    KILOGRAMS = 'Kilograms'
    UNIT = 'Unit'
    SPOON = 'Spoon'
    PIECE = 'Piece'
    QUANTITY_CHOICES = [
        (LITRE, 'Litre'),
        (MILILITRE, 'Mililitre'),
        (GRAMS, 'Grams'),
        (KILOGRAMS, 'Kilograms'),
        (UNIT, 'Unit'),
        (SPOON, 'Spoon'),
        (PIECE, 'Piece')
    ]
    ingredient_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=120)
    quantity = models.PositiveIntegerField(default=0)
    quantity_unit = models.CharField(
        max_length=10, choices=QUANTITY_CHOICES, default=KILOGRAMS)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Recipe(models.Model):
    SECONDS = 'Seconds'
    MINUTES = 'Minutes'
    HOURS = 'Hours'
    DAYS = 'Days'
    WEEKS = 'Weeks'
    BASIC = 'Basic'
    INTERMEDIATE = 'Intermediate'
    ADVANCED = 'Advanced'
    TIME_UNIT_CHOICES = [
        (SECONDS, 'Seconds'),
        (MINUTES, 'Minutes'),
        (HOURS, 'Hours'),
        (DAYS, 'Days'),
        (WEEKS, 'Weeks')
    ]
    DIFFICULTY_CHOICES = [
        (BASIC, 'Basic'),
        (INTERMEDIATE, 'Intermediate'),
        (ADVANCED, 'Advanced')
    ]
    recipe_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=120)
    ingredients = models.ManyToManyField(
        Ingredient, through='IngredientRecipe'
    )
    preparation = models.TextField(blank=True)
    preparation_time = models.PositiveIntegerField(default=0)
    preparation_time_unit = models.CharField(
        max_length=10, choices=TIME_UNIT_CHOICES, default=MINUTES)
    difficulty = models.CharField(
        max_length=12, choices=DIFFICULTY_CHOICES, default=BASIC)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['difficulty']

    def __str__(self):
        return self.name


class IngredientRecipe(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.ingredient.name+" -> "+self.recipe.name


class Pantrie(models.Model):
    pantrie_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=120)
    recipes = models.ManyToManyField(
        Recipe, through='RecipePantrie'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class RecipePantrie(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    pantrie = models.ForeignKey(Pantrie, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.recipe.name+" -> "+self.pantrie.name
