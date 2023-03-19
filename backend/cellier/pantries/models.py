from django.db import models


class Fact(models.Model):
    info_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=120, default='N/A')
    description = models.TextField(blank=True, default='N/A')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Info(models.Model):
    info_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=120, default='N/A')
    origin = models.CharField(max_length=120, default='N/A')
    availability = models.CharField(max_length=120, default='N/A')
    facts = models.ManyToManyField(Fact, through='FactInfo')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['info_id']

    def __str__(self):
        return self.name


class FactInfo(models.Model):
    fact = models.ForeignKey(
        Fact, on_delete=models.CASCADE)
    info = models.ForeignKey(Info, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.fact.name+' de '+self.info.name


class Nutrition(models.Model):
    nutrition_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=120, default='N/A')
    water = models.CharField(max_length=120, default='N/A')
    fiber = models.CharField(max_length=120, default='N/A')
    vitamins = models.CharField(max_length=120, default='N/A')
    minerals = models.CharField(max_length=120, default='N/A')
    carbs = models.CharField(max_length=120, default='N/A')
    lipids = models.CharField(max_length=120, default='N/A')
    proteins = models.CharField(max_length=120, default='N/A')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['nutrition_id']

    def __str__(self):
        return self.name


class Unit(models.Model):
    TEMPERATURE = 'Temperature'
    CELCIUS = 'Celcius'
    FARENHEIT = 'Farenheit'

    TIME = 'Time'
    SECONDS = 'Seconds'
    MINUTES = 'Minutes'
    HOURS = 'Hours'
    DAYS = 'Days'
    WEEKS = 'Weeks'

    VOLUME = 'Volume'
    LITRE = 'Litre'
    MILILITRE = 'Mililitre'

    MASS = 'Mass'
    GRAMS = 'Grams'
    KILOGRAMS = 'Kilograms'

    AMOUNT = 'Amount'
    UNIT = 'Unit'
    SPOON = 'Spoon'

    UNIT_CHOICES = [
        (TEMPERATURE, (
            (CELCIUS, '°C'),
            (FARENHEIT, '°F')
        )),
        (TIME, (
            (SECONDS, 's'),
            (MINUTES, 'm'),
            (HOURS, 'h'),
            (DAYS, 'd'),
            (WEEKS, 'w')
        )),
        (MASS, (
            (GRAMS, 'g'),
            (KILOGRAMS, 'kg'),
        )),
        (VOLUME, (
            (LITRE, 'l'),
            (MILILITRE, 'ml')
        )),
        (AMOUNT, (
            (UNIT, 'u'),
            (SPOON, 'spn')
        ))
    ]
    unit_id = models.BigAutoField(primary_key=True)
    name = models.CharField(
        max_length=18, choices=UNIT_CHOICES, default=UNIT, unique=True)
    related_name = models.CharField(max_length=120, default="N/A")
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    ingredient_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=120)
    related_name = models.CharField(max_length=120, default="N/A")
    info = models.ForeignKey(Info, on_delete=models.CASCADE)
    nutrition = models.ForeignKey(Nutrition, on_delete=models.CASCADE)
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
    ingredient = models.ForeignKey(
        Ingredient, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['value']

    def __str__(self):
        return str(self.value)+' '+self.unit.name+' '+self.ingredient.name


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
    related_name = models.CharField(max_length=120, default="N/A")
    preparation = models.TextField(blank=True)
    preparation_time = models.FloatField(default=0)
    difficulty = models.CharField(
        max_length=12, choices=DIFFICULTY_CHOICES, default=BASIC)
    quantities = models.ManyToManyField(Quantity, through='QuantityRecipe')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['difficulty']

    def __str__(self):
        return self.name


class QuantityRecipe(models.Model):
    quantity = models.ForeignKey(
        Quantity, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.quantity.value)+' '+self.quantity.unit.name+' de '+self.quantity.ingredient.name


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
