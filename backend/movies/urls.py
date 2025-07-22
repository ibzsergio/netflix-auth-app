from django.urls import path
from .views import MovieListView
urlpatterns = [
path('movies/', MovieListView.as_view()), # localhost:8000/api/movies/
]