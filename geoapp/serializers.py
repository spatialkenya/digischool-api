from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import County, School, Issue
from django.db.models import Sum


from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email',)


class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = ('error_code', 'date', 'status','school')

    @staticmethod
    def setup_eager_loading(queryset):
        """ Perform necessary eager loading of data. """
        queryset = queryset.select_related('school')
        # queryset = queryset.prefetch_related('issue')
        return queryset


class SchoolSerializer(GeoFeatureModelSerializer):
    county = serializers.StringRelatedField()

    class Meta:
        model = School
        geo_field = 'geom'
        fields = ("school_code", 'name', 'present_devices', "class_one_enrollment", 'county')


class CountySerializer(GeoFeatureModelSerializer):
    class Meta:
        model = County
        geo_field = 'geom'
        auto_bbox = True
        fields = "__all__"

    def get_properties(self, instance, fields):
        properties = super(CountySerializer, self).get_properties(instance, fields)
        school_count = instance.schools.count()
        devices_count = instance.schools.aggregate(Sum('present_devices'))
        properties['schools'] = school_count
        properties['devices'] = devices_count['present_devices__sum']
        return properties

    @staticmethod
    def setup_eager_loading(queryset):
        """ Perform necessary eager loading of data. """
        queryset = queryset.prefetch_related('schools')
        return queryset
