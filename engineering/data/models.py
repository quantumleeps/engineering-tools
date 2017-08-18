from django.db import models

# Create your models here.

class Material(models.Model):
    name = models.CharField(max_length=40)
    uns_number = models.CharField(max_length=40, blank=True, null=True)
    astm_number = models.CharField(max_length=40, blank=True, null=True)

    def __str__(self):
        return self.name

class Fluid(models.Model):
    name = models.CharField(max_length=40)
    specific_gravity = models.FloatField(max_length=40, blank=True, null=True)

    def __str__(self):
        return self.name

class PipeSize(models.Model):
    name = models.CharField(max_length=40)
    units = models.CharField(max_length=40)
    outside_diameter = models.FloatField(max_length=40)
    inside_diameter = models.FloatField(max_length=40, blank=True, null=True)

    def __str__(self):
        return self.name

class BuiltinSystem(models.Model):
    name = models.CharField(max_length=40)
    system_number = models.IntegerField(default=0)
    system_code = models.CharField(max_length=40)
    
    def __str__(self):
        return u'%s (%s)' % (self.name, self.system_number)