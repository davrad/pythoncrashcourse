from django.conf.urls import url

from . import views

app_name = 'meal_plans'

urlpatterns = [
    # Meal Plans
    url(r'^$', views.index, name='index'),
]
