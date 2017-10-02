from rest_framework import viewsets
from .models import County, School, Issue
from .serializers import CountySerializer, SchoolSerializer, IssueSerializer


class CountyViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows  to query Counties
    """
    queryset = County.objects.all()
    serializer_class = CountySerializer


class SchoolViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows  to query schools
    """
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    filter_fields = ('name', 'county', 'present_devices', 'class_one_enrollment')


class IssueViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows  to query Issues
    """
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    filter_fields = ('error_code', 'school', 'status', 'date', 'school__county')
