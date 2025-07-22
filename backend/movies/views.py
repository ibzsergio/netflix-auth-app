# movies/views.py
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Movie
from .serializers import MovieSerializer
class MovieListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        movies = Movie.objects.all() # obtiene todas las películas
        serializer = MovieSerializer(movies, many=True) # las convierte a JSON
        return Response(serializer.data)