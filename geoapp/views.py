from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from .models import County
from .serializers import CountySerializer


class CountyViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows  to view or edit Counties  .
    """
    queryset = County.objects.all()
    pagination_class = None
    serializer_class = CountySerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('name',)



