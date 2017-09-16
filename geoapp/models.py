from __future__ import unicode_literals

from django.contrib.gis.db import models


class County(models.Model):
    name = models.CharField(max_length=100)
    geom = models.MultiPolygonField(srid=4326)

    @property
    def extent(self):
        return self.geom.extent

    def __unicode__(self):
        return self.name

