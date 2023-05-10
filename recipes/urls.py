from django.urls import path
from recipes.views import home, contato, quemsomos


urlpatterns = [
    path('', home),
    path('contato/', contato),
    path('quemsomos/', quemsomos),
]