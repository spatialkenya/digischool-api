from rest_framework_gis.serializers import GeoFeatureModelSerializer
from rest_framework.serializers import ModelSerializer

from .models import County, School, Issue


class CountySerializer(GeoFeatureModelSerializer):
    """ A class to serialize counties as GeoJSON compatible data """

    class Meta:
        model = County
        geo_field = 'geom'
        fields = '__all__'
        auto_bbox = True


class SchoolSerializer(GeoFeatureModelSerializer):
    """
    serialize schools to geojson
    """

    class Meta:
        model = School
        geo_field = 'geom'
        fields = '__all__'
        depth = 1


class IssueSerializer(ModelSerializer):
    """
    serialize Issues
    """

    class Meta:
        model = Issue
        fields = (
            'id', 'school', 'date', 'status', 'error_code',
            'serial_number', 'agent', 'report', 'technical_report')
        depth = 1
