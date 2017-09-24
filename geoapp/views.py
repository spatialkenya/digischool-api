from rest_framework import viewsets

from .models import County
from .serializers import CountySerializer


class CountyViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows  to view or Counties  .
    """
    queryset = County.objects.all()
    serializer_class = CountySerializer



