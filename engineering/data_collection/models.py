from django.db import models

# Create your models here.

# class Material(models.Model):
#     name = models.CharField(max_length=40)
#     uns_number = models.CharField(max_length=40, blank=True, null=True)
#     astm_number = models.CharField(max_length=40, blank=True, null=True)

#     def __str__(self):
#         return self.name

# class Fluid(models.Model):
#     name = models.CharField(max_length=40)
#     specific_gravity = models.FloatField(max_length=40, blank=True, null=True)

#     def __str__(self):
#         return self.name

# class PipeSize(models.Model):
#     name = models.CharField(max_length=40)
#     units = models.CharField(max_length=40)
#     outside_diameter = models.FloatField(max_length=40)
#     inside_diameter = models.FloatField(max_length=40, blank=True, null=True)

#     def __str__(self):
#         return self.name

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