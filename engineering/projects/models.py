from django.db import models
from simple_history.models import HistoricalRecords
from django.template.defaultfilters import slugify

# Create your models here.



class System(models.Model):
    name = models.CharField(max_length=40)
    systemNumber = models.IntegerField(default=0)
    systemCode = models.CharField(max_length=40)
    slug = models.SlugField(blank=True, null=True)
    history = HistoricalRecords()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(System, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name
    
class Project(models.Model):
    name = models.CharField(max_length=40)
    systems = models.ManyToManyField(System)
    country = models.CharField(max_length=40)
    projectCode = models.CharField(max_length=40)
    slug = models.SlugField(blank=True, null=True)
    history = HistoricalRecords()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Project, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Instrument(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    system = models.ForeignKey(System, on_delete=models.CASCADE)
    name = models.CharField(max_length=60)
    pid_tag_prefix = models.CharField(max_length=5)
    pid_tag_num = models.IntegerField(default=1)
    brand_name = models.CharField(max_length=60, blank=True, null=True)
    model_number = models.CharField(max_length=200, blank=True, null=True)
    detailed_description = models.CharField(max_length=60, blank=True, null=True)
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
    lower_instrument_range = models.CharField(max_length=40, blank=True, null=True)
    upper_instrument_range = models.CharField(max_length=40, blank=True, null=True)
    lower_process_range = models.CharField(max_length=40, blank=True, null=True)
    upper_process_range = models.CharField(max_length=40, blank=True, null=True)
    instrument_range_units = models.CharField(max_length=40, blank=True, null=True)
    low_setpoint = models.CharField(max_length=40, blank=True, null=True)
    low_low_setpoint = models.CharField(max_length=40, blank=True, null=True)
    high_setpoint = models.CharField(max_length=40, blank=True, null=True)
    high_high_setpoint = models.CharField(max_length=40, blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)
    full_pid_tag_number = models.CharField(max_length=40, blank=True, null=True)
    history = HistoricalRecords()

    def make_pid_tag_number(self):
        return self.pid_tag_prefix + '-' + str(self.system.systemNumber + self.pid_tag_num - 1)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.make_pid_tag_number() + '-' + str(self.project.name))
        self.full_pid_tag_number = self.make_pid_tag_number()
        super(Instrument, self).save(*args, **kwargs)

class Valve(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    system = models.ForeignKey(System, on_delete=models.CASCADE)
    name = models.CharField(max_length=60)
    detailed_description = models.CharField(max_length=60, blank=True, null=True)
    pid_tag_prefix = models.CharField(max_length=5)
    pid_tag_num = models.IntegerField(default=1)
    material = models.ForeignKey('data.Material', blank=True, null=True, on_delete=models.CASCADE)
    fluid = models.ForeignKey('data.Fluid', blank=True, null=True, on_delete=models.CASCADE)
    connection_size = models.ForeignKey('data.PipeSize', blank=True, null=True, on_delete=models.CASCADE)
    connection_type = models.CharField(max_length=40, blank=True, null=True)
    pipe_flange_class = models.CharField(max_length=40, blank=True, null=True)
    vendor = models.CharField(max_length=40, blank=True, null=True)
    valve_model = models.CharField(max_length=40, blank=True, null=True)
    pressure = models.CharField(max_length=40, blank=True, null=True)
    temperature = models.CharField(max_length=40, blank=True, null=True)
    service = models.CharField(max_length=40, blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)
    full_pid_tag_number = models.CharField(max_length=40, blank=True, null=True)
    history = HistoricalRecords()

    def make_pid_tag_number(self):
        return self.pid_tag_prefix + '-' + str(self.system.systemNumber + self.pid_tag_num - 1)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.make_pid_tag_number() + '-' + str(self.project.name))
        self.full_pid_tag_number = self.make_pid_tag_number()
        super(Valve, self).save(*args, **kwargs)

class Equipment(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    system = models.ForeignKey(System, on_delete=models.CASCADE)
    name = models.CharField(max_length=60)    
    detailed_description = models.CharField(max_length=60, blank=True, null=True)
    pid_tag_prefix = models.CharField(max_length=5)
    pid_tag_num = models.IntegerField(default=1)
    slug = models.SlugField(blank=True, null=True)
    full_pid_tag_number = models.CharField(max_length=40, blank=True, null=True)
    history = HistoricalRecords()

    def make_pid_tag_number(self):
        return self.pid_tag_prefix + '-' + str(self.system.systemNumber + self.pid_tag_num - 1)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.make_pid_tag_number() + '-' + str(self.project.name))
        self.full_pid_tag_number = self.make_pid_tag_number()
        super(Equipment, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Piece of Equipment'
        verbose_name_plural = 'Equipment'
        
class Pump(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    system = models.ForeignKey(System, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    pid_tag_prefix = models.CharField(max_length=5)
    pid_tag_num = models.IntegerField(default=1)
    full_pid_tag_number = models.CharField(max_length=40, blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)
    style = models.CharField(max_length=40, blank=True, null=True)
    history = HistoricalRecords()

    def make_pid_tag_number(self):
        return self.pid_tag_prefix + '-' + str(self.system.systemNumber + self.pid_tag_num - 1)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.make_pid_tag_number() + '-' + str(self.project.name))
        self.full_pid_tag_number = self.make_pid_tag_number()
        super(Pump, self).save(*args, **kwargs)

class PumpOperatingPoint(models.Model):
    name = models.CharField(max_length=25)
    pump = models.ForeignKey(Pump, on_delete=models.CASCADE, blank=True, null=True)
    diff_pressure = models.FloatField(null=True)
    diff_pressure_units = models.CharField(max_length=20, default="psid")
    flow = models.FloatField(null=True)
    flow_units = models.CharField(max_length=20, default="usgpm")
    eff = models.FloatField(null=True)

class PumpPart(models.Model):
    name = models.CharField(max_length=25)
    pump = models.ForeignKey(Pump, on_delete=models.CASCADE, blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    material = models.CharField(max_length=40, blank=True, null=True)  # need to associate this with ASTM numbers that are registered materials
    standard = models.CharField(max_length=40, blank=True, null=True)
    note = models.CharField(max_length=100, blank=True, null=True)

class Tank(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    system = models.ForeignKey(System, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    pid_tag_prefix = models.CharField(max_length=5)
    pid_tag_num = models.IntegerField(default=1)
    material = models.CharField(max_length=40, blank=True, null=True)
    capacity = models.IntegerField(default=1, blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)
    full_pid_tag_number = models.CharField(max_length=40, blank=True, null=True)
    history = HistoricalRecords()
    
    def make_pid_tag_number(self):
        return self.pid_tag_prefix + '-' + str(self.system.systemNumber + self.pid_tag_num - 1)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.make_pid_tag_number() + '-' + str(self.project.name))
        self.full_pid_tag_number = self.make_pid_tag_number()
        super(Tank, self).save(*args, **kwargs)

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
    full_pid_tag_number = models.CharField(max_length=40, blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)
    history = HistoricalRecords()
    
    def make_pid_tag_number(self):
        return self.pid_tag_prefix + '-' + str(self.system.systemNumber + self.pid_tag_num - 1)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.make_pid_tag_number() + '-' + str(self.project.name))
        self.full_pid_tag_number = self.make_pid_tag_number()
        super(Pipe, self).save(*args, **kwargs)

class DocumentCategory(models.Model):
    name = models.CharField(max_length=60)
    code = models.CharField(max_length=1)
    history = HistoricalRecords()

    class Meta:
        verbose_name = 'Document Category'
        verbose_name_plural = 'Document Categories'

    def __str__(self):
        return self.code + ' - ' + self.name

class ControlledDocument(models.Model):
    project = models.ForeignKey(Project)
    system = models.ForeignKey(System)
    system_drawing_number = models.IntegerField(default=0)
    description = models.CharField(max_length=60)
    category = models.ForeignKey(DocumentCategory)
    original_file_format = models.CharField(max_length=35, blank=True, null=True)
    released_file_format = models.CharField(max_length=35, blank=True, null=True)
    revision_number = models.CharField(max_length=10)
    notes = models.CharField(max_length=60, blank=True, null=True)
    owner = models.CharField(max_length=60, blank=True, null=True)
    status = models.CharField(max_length=60, blank=True, null=True)
    drawing_title = models.CharField(max_length=60, blank=True, null=True)
    history = HistoricalRecords()

    def save(self, *args, **kwargs):
        self.drawing_title = self.project.projectCode + '-' + self.category.code + '-' + str(self.system.systemNumber) + '-' + str(self.system_drawing_number).zfill(3)
        super(ControlledDocument, self).save(*args, **kwargs)

    def __str__(self):
        return self.description