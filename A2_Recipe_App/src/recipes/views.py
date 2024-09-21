from django.shortcuts import render
from django.views.generic import ListView, DetailView 
from .models import Recipe
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import RecipeSearchForm
from .utils import get_recipe_name_from_id, get_chart
import pandas as pandas
from django.urls import reverse



# Create your views here.
def welcome(request):
    return render(request, 'recipes/recipes_home.html')

class RecipeListView(LoginRequiredMixin, ListView):
    model = Recipe

    def get(self, request):
        form= RecipeSearchForm()
        recipes = Recipe.objects.all()
        return render(request, 'recipes/recipes_list.html', {'form': form, 'recipes': recipes})

    
    def post(self, request):
        form = RecipeSearchForm(request.POST)
        recipes = Recipe.objects.all()
        chart = None

        if form.is_valid():
            recipe_name = form.cleaned_data.get('recipe_name')
            chart_type = form.cleaned_data.get('chart_type')

            qs = Recipe.objects.filter(Q(name__icontains=recipe_name) | Q(ingredients__icontains=recipe_name))
            if qs.exists():
                recipes = pd.DataFrame(qs.values())
                recipes['difficulty'] = recipes.apply(lambda row: get_recipe_name_from_id(row['id']).difficulty, axis=1)
                chart= get_chart(chart_type, recipes, labels=recipes['id'].values)
            else:
                recipes = pd.DataFrame()

        context = {
            'fomr': form,
            'recipes': recipes,
            'chart': chart
        }
        return render(request, 'recipes/recipes_list.html', context)

class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = "recipes/recipes_details.html"