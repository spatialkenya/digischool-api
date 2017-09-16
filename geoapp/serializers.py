from rest_framework_gis.serializers import GeoFeatureModelSerializer

from .models import County


class CountySerializer(GeoFeatureModelSerializer):
    """ A class to serialize counties as GeoJSON compatible data """

    class Meta:
        model = County
        geo_field = 'geom'
        fields = '__all__'

    def get_properties(self, instance, fields):
        properties = super(CountySerializer, self).get_properties(instance, fields)
        extent = instance.extent
        properties['extent'] = extent
        return properties
