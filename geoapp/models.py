from __future__ import unicode_literals

from django.contrib.gis.db import models


class County(models.Model):
    county_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    geom = models.MultiPolygonField(srid=4326)

    def __unicode__(self):
        return self.name


class School(models.Model):
    name = models.CharField(max_length=100)
    county = models.ForeignKey(County)
    class_one_enrollment = models.IntegerField()
    present_devices = models.IntegerField()
    sub_county = models.CharField(max_length=50)
    zone = models.CharField(max_length=50)
    emmis_code = models.CharField(max_length=50)
    geom = models.PointField(srid=4326)

    def __unicode__(self):
        return self.name


class Issue(models.Model):
    STATUS_CHOICES = (
        ('closed', 'Closed'),
        ('escalated', 'Escalated'),
        ('resolved', 'Resolved')
    )
    id = models.CharField(max_length=50, primary_key=True)
    school = models.ForeignKey(School)
    date = models.DateTimeField()
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    error_code = models.CharField(max_length=50)
    serial_number = models.CharField(max_length=100)
    agent = models.CharField(max_length=50)
    report = models.TextField()
    technical_report = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.school.name
