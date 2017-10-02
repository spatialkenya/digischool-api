from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import County, School, Issue


class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = ('error_code', 'date', 'status')


class SchoolSerializer(GeoFeatureModelSerializer):
    issues_count = serializers.SerializerMethodField()

    class Meta:
        model = School
        geo_field = 'geom'
        fields = ("school_code", 'name', 'present_devices', 'county', "class_one_enrollment", 'issues_count')

    @staticmethod
    def get_issues_count(obj):
        return obj.issues.filter(status='Closed').count()


class CountySerializer(GeoFeatureModelSerializer):
    class Meta:
        model = County
        geo_field = 'geom'
        auto_bbox = True
        fields = "__all__"

    def get_properties(self, instance, fields):
        properties = super(CountySerializer, self).get_properties(instance, fields)
        school_count = instance.schools.count()
        properties['schools'] = school_count
        return properties
