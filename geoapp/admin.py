from django.contrib.gis import admin
from leaflet.admin import LeafletGeoAdmin

from .models import County

admin.site.site_header = "DiVA Admin"
admin.site.register(County,LeafletGeoAdmin)