from django.db import models

class Location(models.Model):
    state_or_county = models.CharField(max_length=30)
    def __str__(self):

        return self.state_or_county

class TouristSite(models.Model):
    name   = models.CharField(max_length=100 ,blank = True, null= True)
    area   = models.CharField(max_length=30)
    location = models.ForeignKey(Location, on_delete = models.CASCADE)
    county = models.CharField(max_length=30)
    price  = models.IntegerField()
    description = models.TextField(blank = True, null= True)
    def __str__(self):
        return self.name