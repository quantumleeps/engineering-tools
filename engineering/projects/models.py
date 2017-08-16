from django.db import models

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=40)
    country = models.CharField(max_length=40)
    projectCode = models.CharField(max_length=40)

    def __str__(self):
        return self.projectCode

class System(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    systemNumber = models.IntegerField(default=0)
    systemCode = models.CharField(max_length=40)
    
    def __str__(self):
        return self.systemCode

class Instrument(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    system = models.ForeignKey(System, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    pid_tag_prefix = models.CharField(max_length=5)
    pid_tag_num = models.IntegerField(default=1)
    instrument_voltage = models.CharField(max_length=40, blank=True, null=True)
    instrument_type = models.CharField(max_length=40, blank=True, null=True)
    material = models.CharField(max_length=40, blank=True, null=True)
    fluid = models.CharField(max_length=40, blank=True, null=True)
    connection_size = models.CharField(max_length=40, blank=True, null=True)
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
    material = models.CharField(max_length=40, blank=True, null=True)
    size = models.CharField(max_length=40, blank=True, null=True)
    connection_type = models.CharField(max_length=40, blank=True, null=True)
    pipe_flange_class = models.CharField(max_length=40, blank=True, null=True)
    vendor = models.CharField(max_length=40, blank=True, null=True)
    valve_model = models.CharField(max_length=40, blank=True, null=True)
    detailed_description = models.CharField(max_length=40, blank=True, null=True)
    pressure = models.CharField(max_length=40, blank=True, null=True)
    temperature = models.CharField(max_length=40, blank=True, null=True)
    # material = models.CharField(max_length=40, default='e.g. PVC with EPDM')
    # size = models.CharField(max_length=40, default='e.g. 2"')
    # installtype = models.CharField(max_length=40, default='e.g., Flanged')
    # pipeflangeclass = models.CharField(max_length=40, default='e.g. 150#')
    # vendor = models.CharField(max_length=40, default='e.g. Asahi')
    # valvemodel = models.CharField(max_length=40, default='e.g. Type 57')
    # detailedDescription = models.CharField(max_length=255, default='e.g. This valve isolates ER concentrate')
    # pressure = models.CharField(max_length=40, default='e.g. 80 psig')
    # temperature = models.CharField(max_length=40, default='e.g. 80 deg F')
    service = models.CharField(max_length=40, blank=True, null=True)