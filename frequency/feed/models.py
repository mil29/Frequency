from decimal import Decimal
from django.db import models
from django.utils.datetime_safe import datetime
from django.urls import reverse
from users.models import User




class Instrument(models.Model):
    title     = models.CharField(max_length=120)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated   = models.DateTimeField(auto_now=True)
    track     = models.ForeignKey('Track', on_delete=models.CASCADE)
    artist    = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return 'title:{} track:{} artist:{}'.format(self.title, self.track, self.artist)


class EQ(models.Model):
    frequency   = models.DecimalField(decimal_places=3, max_digits=20)
    description = models.TextField(max_length=250, null=True, blank=True) 
    boost       = models.DecimalField(decimal_places=2, max_digits=10, default=0)
    cut         = models.DecimalField(decimal_places=2, max_digits=10, default=0)
    updated     = models.DateTimeField(auto_now=True)
    instrument  = models.ForeignKey(Instrument,on_delete=models.CASCADE)
    track       = models.ForeignKey('Track', on_delete=models.CASCADE)
    user_name   = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return 'frequency:{} instrument:{} track:{} boost:{} cut:{} user_name:{} description:{}'.format(self.frequency, self.instrument, self.track, self.boost, self.cut, self.user_name, self.description)


class Track(models.Model):
    title       = models.CharField(max_length=100)
    description = models.TextField(max_length=250, null=True, blank=True)
    artist      = models.CharField(max_length=250)
    timestamp   = models.DateTimeField(auto_now_add=True)
    updated     = models.DateTimeField(auto_now=True)
    user        = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return 'title:{} description:{} artist:{} user:{}'.format(self.title, self.description, self.artist, self.user)




    










    
