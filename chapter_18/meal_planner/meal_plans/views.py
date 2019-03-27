from django.shortcuts import render


def index(request):
    return render(request, 'meal_plans/index.html')
