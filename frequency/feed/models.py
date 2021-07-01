from decimal import Decimal
from django.db import models
from django.utils.datetime_safe import datetime



class Instrument(models.Model):
    title     = models.CharField(max_length=120)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated   = models.DateTimeField(auto_now=True)
    track     = models.ForeignKey('Track', on_delete=models.CASCADE)

    def __str__(self):
        return 'title:{} track:{}'.format(self.title, self.track)


class EQ(models.Model):
    frequency  = models.DecimalField(decimal_places=3, max_digits=20)
    instrument = models.ForeignKey(Instrument,on_delete=models.CASCADE)
    track      = models.ForeignKey('Track', on_delete=models.CASCADE)
    boost      = models.DecimalField(decimal_places=2, max_digits=10)
    cut        = models.DecimalField(decimal_places=2, max_digits=10)
    updated    = models.DateTimeField(auto_now=True)


    def __str__(self):
        return 'frequency:{} instrument:{} track:{} boost:{} cut:{}'.format(self.frequency, self.instrument, self.track, self.boost, self.cut)


class Track(models.Model):
    title       = models.CharField(max_length=100)
    description = models.TextField(max_length=250, null=True)
    artist      = models.CharField(max_length=250)
    timestamp   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'title:{} description:{} artist:{}'.format(self.title, self.description, self.artist)








    
