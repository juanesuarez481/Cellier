from django.db import models


class Unit(models.Model):
    TEMPERATURE = 'T'
    CELCIUS = '°C'
    FARENHEIT = '°F'

    TIME = 't'
    SECONDS = 's'
    MINUTES = 'm'
    HOURS = 'h'
    DAYS = 'd'
    WEEKS = 'w'

    VOLUME = 'V'
    LITRE = 'l'
    MILILITRE = 'ml'

    MASS = 'M'
    GRAMS = 'g'
    KILOGRAMS = 'Kg'

    AMOUNT = 'Z'
    UNIT = 'u'
    SPOON = 'sp'

    UNIT_CHOICES = [
        (TEMPERATURE, (
            (CELCIUS, 'Celcius'),
            (FARENHEIT, 'Farenheit')
        )),
        (TIME, (
            (SECONDS, 'Seconds'),
            (MINUTES, 'Minutes'),
            (HOURS, 'Hours'),
            (DAYS, 'Days'),
            (WEEKS, 'Weeks')
        )),
        (MASS, (
            (GRAMS, 'Grams'),
            (KILOGRAMS, 'Kilograms'),
        )),
        (VOLUME, (
            (LITRE, 'Litre'),
            (MILILITRE, 'Mililitre')
        )),
        (AMOUNT, (
            (UNIT, 'Unit'),
            (SPOON, 'Spoon')
        ))
    ]
    unit_id = models.BigAutoField(primary_key=True)
    name = models.CharField(
        max_length=18, choices=UNIT_CHOICES, default=UNIT, unique=True)
    description = models.TextField(blank=True)
    related_name = models.CharField(max_length=120, default="N/A")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Quantity(models.Model):
    quantity_id = models.BigAutoField(primary_key=True)
    value = models.FloatField(default=0)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    error = models.FloatField(default=0)
    related_name = models.CharField(max_length=120, default="N/A")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['value', 'unit']

    def __str__(self):
        return str(self.value)+' '+self.unit.name


class Ingredient(models.Model):
    ingredient_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=120)
    related_name = models.CharField(max_length=120, default="N/A")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Recipe(models.Model):
    BASIC = 'Basic'
    INTERMEDIATE = 'Intermediate'
    ADVANCED = 'Advanced'
    DIFFICULTY_CHOICES = [
        (BASIC, 'Basic'),
        (INTERMEDIATE, 'Intermediate'),
        (ADVANCED, 'Advanced')
    ]
    recipe_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=120)
    ingredients = models.ManyToManyField(
        Ingredient, through='IngredientQuantityRecipe'
    )
    preparation = models.TextField(blank=True)
    preparation_time = models.PositiveIntegerField(default=0)
    difficulty = models.CharField(
        max_length=12, choices=DIFFICULTY_CHOICES, default=BASIC)
    related_name = models.CharField(max_length=120, default="N/A")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['difficulty']

    def __str__(self):
        return self.name


class IngredientQuantityRecipe(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.ForeignKey(Quantity, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.ingredient.name+' ( '+str(self.quantity.value)+' '+self.quantity.unit.name+' ) -> '+self.recipe.name


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
