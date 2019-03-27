from django.shortcuts import render

from .models import Pizza


def index(request):
    return render(request, 'pizzas/index.html')


def pizza(request):
    pizzas = Pizza.objects.all()
    context = {'pizzas': pizzas}
    return render(request, 'pizzas/pizzas.html', context)


def pizza_id(request, pizza_id):
    pizza_db = Pizza.objects.get(id=pizza_id)
    toppings = pizza_db.toppings.all()
    context = {'pizza': pizza_db, 'toppings': toppings}
    return render(request, 'pizzas/pizza_id.html', context)
