from django.contrib.gis.db import models


class County(models.Model):
    county_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    geom = models.MultiPolygonField(srid=4326)

    class Meta:
        verbose_name_plural = "Counties"

    def __unicode__(self):
        return self.name


class School(models.Model):
    name = models.CharField(max_length=50)
    county = models.ForeignKey(County, related_name='schools', on_delete=models.CASCADE)
    class_one_enrollment = models.IntegerField()
    present_devices = models.IntegerField()
    zone = models.CharField(max_length=50)
    emmis_code = models.CharField(max_length=100, blank=True, null=True)
    school_code = models.CharField(primary_key=True, max_length=50)
    geom = models.PointField(srid=4326)

    def __unicode__(self):
        return self.name


class Issue(models.Model):
    ticket_number = models.CharField(max_length=20, primary_key=True)
    error_code = models.CharField(max_length=50)
    school = models.ForeignKey(School, related_name='issues', on_delete=models.CASCADE)
    report = models.TextField()
    status = models.CharField(max_length=50)
    serial_number = models.CharField(max_length=100)
    date = models.DateField()
    technical_report = models.TextField(blank=True)

    def __unicode__(self):
        return self.ticket_number + self.school.name
