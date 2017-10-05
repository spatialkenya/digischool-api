from rest_framework import viewsets
from .models import County, School, Issue
from .serializers import CountySerializer, SchoolSerializer, IssueSerializer
from filters.mixins import (
    FiltersMixin,
)


class CountyViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows  to query Counties
    """
    serializer_class = CountySerializer

    def get_queryset(self):
        queryset = County.objects.all()
        # Set up eager loading to avoid N+1 selects
        queryset = self.get_serializer_class().setup_eager_loading(queryset)
        return queryset


class SchoolViewSet(FiltersMixin, viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows  to query schools
    """
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    filter_mappings = {
        'name': 'name__icontains',
        'county_id': 'county'
    }

    def get_queryset(self):
        queryset = School.objects.select_related('county').all()
        return queryset


class IssueViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows  to query Issues
    """
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    filter_fields = ('error_code', 'school', 'status', 'date', 'school__county')
