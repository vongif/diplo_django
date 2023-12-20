from rest_framework import viewsets
from .models import LibrosRestApi
from .serializer import LibrosRestApiSerializer


class LibrosRestApiViewSet(viewsets.ModelViewSet):
    queryset=LibrosRestApi.objects.all()
    serializer_class=LibrosRestApiSerializer


