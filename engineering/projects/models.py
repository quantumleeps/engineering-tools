from django.db import models

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=40)
    country = models.CharField(max_length=40)
    projectCode = models.CharField(max_length=4)

    def __str__(self):
        return self.projectCode

class System(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    systemNumber = models.IntegerField(default=0)
    systemCode = models.CharField(max_length=4)
    
    def __str__(self):
        return self.systemCode

# class Instrument

# class Valve

# class Equipment