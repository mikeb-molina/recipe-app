from django.db import models

# Create your models here.
class Recipe (models.Model):
    name = models.CharField(max_length=120)
    cooking_time = models.IntegerField(help_text = 'In minutes')
    ingredients = models.CharField(max_length=350, help_text='Enter Ingredients seperated by Comma')
    difficulty = None

    def difficulty(self):
        ingredients = self.ingredients.split(", ")
        if self.cooking_time < 10 and len(ingredients) < 4:
            return "Easy"
        elif self.cooking_time < 10 and len(ingredients) >= 4:
            return "Medium"
        elif self.cooking_time >= 10 and len(ingredients) < 4:
            return "Intermediate"
        elif self.cooking_time >= 10 and len(ingredients) >= 4:
            return "Hard"
        return "Unknown"

    def __str__(self):
        return str(self.name)