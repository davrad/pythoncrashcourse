from django.conf.urls import url

from . import views

app_name = 'pizzas'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^pizza/$', views.pizza, name='pizza'),
    url(r'^pizza/(?P<pizza_id>\d+)/$', views.pizza_id, name='pizza_id'),
]
