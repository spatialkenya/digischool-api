from django.db.models import Sum
from filters.mixins import (
    FiltersMixin,
)
from rest_framework import viewsets
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import County, School, Issue
from .serializers import CountySerializer, SchoolSerializer, IssueSerializer


class DivaObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(DivaObtainAuthToken, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        profile = {'username': token.user.username, 'email': token.user.email}
        context = {
            'token': token.key,
            'profile': profile
        }
        return Response(context)


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


class SchoolAnalysis(APIView):
    def get(self, request):
        schools = School.objects.all()
        schools_total = schools.count()
        class_one_total = schools.aggregate(class_one_total=Sum("class_one_enrollment"))
        total_devices = schools.aggregate(total_devices=Sum("present_devices"))
        data = {
            "schools_total": schools_total,
            "class_one_total": class_one_total["class_one_total"],
            "total_devices": total_devices["total_devices"]
        }
        return Response(data)
