from django.shortcuts import render


def index(request):
    return render(request, 'pizzas/index.html')
