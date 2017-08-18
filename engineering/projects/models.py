from django.db import models

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=40)
    country = models.CharField(max_length=40)
    projectCode = models.CharField(max_length=40)

    def __str__(self):
        return self.name

# This will become inline with Project
class System(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    systemNumber = models.IntegerField(default=0)
    systemCode = models.CharField(max_length=40)
    
    def __str__(self):
        return self.project

class Instrument(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    system = models.ForeignKey(System, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    pid_tag_prefix = models.CharField(max_length=5)
    pid_tag_num = models.IntegerField(default=1)
    analog_input = models.BooleanField(default=False)
    analog_output = models.BooleanField(default=False)
    digital_input = models.BooleanField(default=False)
    digital_output= models.BooleanField(default=False)
    instrument_voltage = models.CharField(max_length=40, blank=True, null=True)
    instrument_type = models.CharField(max_length=40, blank=True, null=True)
    material = models.ForeignKey('data.Material', blank=True, null=True, on_delete=models.CASCADE)
    fluid = models.ForeignKey('data.Fluid', blank=True, null=True, on_delete=models.CASCADE)
    connection_size = models.ForeignKey('data.PipeSize', blank=True, null=True, on_delete=models.CASCADE)
    process_connection_type = models.CharField(max_length=40, blank=True, null=True)
    detailed_description = models.CharField(max_length=40, blank=True, null=True)
    lower_instrument_range = models.CharField(max_length=40, blank=True, null=True)
    upper_instrument_range = models.CharField(max_length=40, blank=True, null=True)
    lower_process_range = models.CharField(max_length=40, blank=True, null=True)
    upper_process_range = models.CharField(max_length=40, blank=True, null=True)
    instrument_range_units = models.CharField(max_length=40, blank=True, null=True)
    low_setpoint = models.CharField(max_length=40, blank=True, null=True)
    low_low_setpoint = models.CharField(max_length=40, blank=True, null=True)
    high_setpoint = models.CharField(max_length=40, blank=True, null=True)
    high_high_setpoint = models.CharField(max_length=40, blank=True, null=True)

class Valve(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    system = models.ForeignKey(System, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    pid_tag_prefix = models.CharField(max_length=5)
    pid_tag_num = models.IntegerField(default=1)
    material = models.ForeignKey('data.Material', blank=True, null=True, on_delete=models.CASCADE)
    fluid = models.ForeignKey('data.Fluid', blank=True, null=True, on_delete=models.CASCADE)
    connection_size = models.ForeignKey('data.PipeSize', blank=True, null=True, on_delete=models.CASCADE)
    connection_type = models.CharField(max_length=40, blank=True, null=True)
    pipe_flange_class = models.CharField(max_length=40, blank=True, null=True)
    vendor = models.CharField(max_length=40, blank=True, null=True)
    valve_model = models.CharField(max_length=40, blank=True, null=True)
    detailed_description = models.CharField(max_length=40, blank=True, null=True)
    pressure = models.CharField(max_length=40, blank=True, null=True)
    temperature = models.CharField(max_length=40, blank=True, null=True)
    service = models.CharField(max_length=40, blank=True, null=True)

class Pump(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    system = models.ForeignKey(System, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    pid_tag_prefix = models.CharField(max_length=5)
    pid_tag_num = models.IntegerField(default=1)

class Tank(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    system = models.ForeignKey(System, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    pid_tag_prefix = models.CharField(max_length=5)
    pid_tag_num = models.IntegerField(default=1)
    material = models.CharField(max_length=40, blank=True, null=True)
    capacity = models.IntegerField(default=1, blank=True, null=True)

class Pipe(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    system = models.ForeignKey(System, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    pid_tag_prefix = models.CharField(max_length=5)
    pid_tag_num = models.IntegerField(default=1)
    material = models.CharField(max_length=40, blank=True, null=True)
    size = models.CharField(max_length=40, blank=True, null=True)
    connection_type_side_a = models.CharField(max_length=40, blank=True, null=True)
    connection_type_side_b = models.CharField(max_length=40, blank=True, null=True)