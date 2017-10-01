from django.contrib.gis import admin
from leaflet.admin import LeafletGeoAdmin

from .models import County, School, Issue

admin.site.site_header = "DiVA Admin"
admin.site.register(County, LeafletGeoAdmin)
admin.site.register(School, LeafletGeoAdmin)
admin.site.register(Issue)
