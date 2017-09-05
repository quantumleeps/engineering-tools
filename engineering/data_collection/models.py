from django.db import models
from django.contrib.auth.models import User

class Location(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=40)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.location) + ' - ' + str(self.name)

class Point(models.Model):
    name = models.CharField(max_length=40)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    units = models.CharField(max_length=40, blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    lowlow = models.FloatField(blank=True, null=True)
    highhigh = models.FloatField(blank=True, null=True)

    def __str__(self):
        return str(self.group.location) + ' - ' + str(self.group.name) + ' - ' + str(self.name)

class Run(models.Model):
    name = models.CharField(max_length=40)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    points = models.ManyToManyField(Point, blank=True, null=True)
    data_collectors = models.ManyToManyField(User, blank=True, null=True)

    def __str__(self):
        return str(self.location) + ' - ' + str(self.name)

class CollectedPoint(models.Model):
    point = models.ForeignKey(Point, on_delete=models.CASCADE)
    value = models.FloatField(blank=True, null=True)
    modified = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    
class CollectedRun(models.Model):
    collected_points = models.ManyToManyField(CollectedPoint, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    submitted = models.DateTimeField(auto_now=True)