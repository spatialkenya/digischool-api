from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import County, School, Issue


class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = '__all__'


class SchoolSerializer(GeoFeatureModelSerializer):
    issues_count = serializers.SerializerMethodField()

    class Meta:
        model = School
        geo_field = 'geom'
        fields = ("school_code",'name', 'present_devices', 'county', "class_one_enrollment",'issues_count')

    @staticmethod
    def get_issues_count(obj):
        return obj.issues.filter(status='Closed').count()


class CountySerializer(serializers.ModelSerializer):
    schools_count = serializers.SerializerMethodField()

    class Meta:
        model = County
        fields = ('name', 'schools_count')

    @staticmethod
    def get_schools_count(obj):
        return obj.schools.count()
