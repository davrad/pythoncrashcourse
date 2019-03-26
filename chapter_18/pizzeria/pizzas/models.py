from django.db import models


class Topping(models.Model):

    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Pizza(models.Model):

    name = models.CharField(max_length=200)
    toppings = models.ManyToManyField(Topping, blank=True)

    def __str__(self):
        return self.name
