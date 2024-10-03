from django.db import models


class Worldcities(models.Model):
    id = models.TextField(blank=True, null=False, primary_key=True)
    city = models.TextField()
    lat = models.FloatField()
    lng = models.FloatField()
    country = models.TextField()

    class Meta:
        managed = False
        db_table = "worldcities"
