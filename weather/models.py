from django.db import models

class Weather(models.Model):
    now_dt = models.DateTimeField()
    temp = models.SmallIntegerField()
    feels_like = models.SmallIntegerField()

