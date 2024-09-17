from django.test import TestCase
from .models import Recipe
from django.urls import reverse

# Create your tests here.
class RecipeModelTest(TestCase):

    # set up non-modified objects used by all test methods
    def setUpTestData():
        Recipe.objects.create(
            name='Tea',
            cooking_time=5, 
            ingredients='Tea Leaves, Sugar, Water'
        )

    # Test Recipe Name
    def test_recipe_name(self):
        recipe = Recipe.objects.get(id=1)
        field_label = recipe._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')
    

    #Test Recipe Name Max Length
    def test_recipe_name_max_length(self):
        recipe= Recipe.objects.get(id=1)
        max_length= recipe._meta.get_field('name').max_length
        self.assertEqual(max_length, 120)

    # Test Ingredients Max Length
    def test_ingredients_max_length(self):
        recipe= Recipe.objects.get(id=1)
        max_length= recipe._meta.get_field('ingredients').max_length
        self.assertEqual(max_length, 350)

    #Test Cooking Time Value
    def test_cooking_time_value(self):
        recipe= Recipe.objects.get(id=1)
        cooking_time_value= recipe.cooking_time
        self.assertEqual(cooking_time_value, 5)

    #Test Recipe Difficulty
    def test_difficulty_calculation(self):
        recipe= Recipe.objects.get(id=1)
        self.assertEqual(recipe.difficulty(), 'Easy')

    #Test for the get_absolute_url function
    def test_get_absolute_url(self):
        recipe = Recipe.objects.get(id=1)
        self.assertEqual(recipe.get_absolute_url(), '/list/1')
