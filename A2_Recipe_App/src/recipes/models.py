from django.db import models
from django.shortcuts import reverse
from django.utils import timezone


difficulty_choices = (
    ('Easy', 'easy'),
    ('Medium', 'medium'),
    ('Intermediate,' 'intermediate'),
    ('Hard', 'hard'),
)

# Create your models here.
class Recipe (models.Model):
    name = models.CharField(max_length=120)
    cooking_time = models.IntegerField(help_text = 'In minutes')
    ingredients = models.CharField(max_length=350, help_text='Enter Ingredients seperated by Comma')
    difficulty = models.CharField( max_length=120, choices=difficulty_choices, default='Easy')
    pic = models.ImageField(upload_to='recipes', default='no_picture.jpg')
    date_created = models.DateField(default=timezone.now)

    def get_absolute_url(self):
        return reverse ('recipes:detail', kwargs={'pk': self.pk})

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


    def save(self, *args, **kwargs):
        self.difficulty()
        super().save(*args, **kwargs)