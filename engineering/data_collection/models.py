from django.db import models


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

    def __str__(self):
        
        return str(self.location) + ' - ' + str(self.name)

class CollectedPoint(models.Model):
    point = models.ForeignKey(Point, on_delete=models.CASCADE)
    value = models.FloatField(blank=True, null=True)

class CollectedRun(models.Model):
    pass