from rest_framework import viewsets
from .serializers import MovieSerializer
from .models import Moviedata

class MovieViewSet(viewsets.ModelViewSet):
    serializer_class = MovieSerializer
    queryset = Moviedata.objects.all()

class ScifiViewSet(viewsets.ModelViewSet):
    serializer_class = MovieSerializer
    queryset = Moviedata.objects.filter(typ='scifi')

class ComedyViewSet(viewsets.ModelViewSet):
    serializer_class = MovieSerializer
    queryset = Moviedata.objects.filter(typ='comedy')