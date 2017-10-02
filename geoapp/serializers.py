from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import County, School, Issue


class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = ('error_code', 'date', 'status')

    @staticmethod
    def setup_eager_loading(queryset):
        """ Perform necessary eager loading of data. """
        queryset = queryset.select_related('school')
        # queryset = queryset.prefetch_related('issue')
        return queryset


class SchoolSerializer(GeoFeatureModelSerializer):
    # issues = IssueSerializer(many=True)
    #
    # issues_count = serializers.SerializerMethodField()

    class Meta:
        model = School
        geo_field = 'geom'
        fields = ("school_code", 'name', 'present_devices', "class_one_enrollment")


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

    @staticmethod
    def setup_eager_loading(queryset):
        """ Perform necessary eager loading of data. """
        queryset = queryset.prefetch_related('schools')
        return queryset
