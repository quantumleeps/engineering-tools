from django.contrib import admin
from .models import Project, System, Valve, Instrument

# Register your models here.

admin.site.register(Project)
admin.site.register(System)
admin.site.register(Valve)
admin.site.register(Instrument)
