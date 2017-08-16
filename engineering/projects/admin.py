from django.contrib import admin
from .models import Project, System, Valve, Instrument

# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'country')

class SystemAdmin(admin.ModelAdmin):
    list_display = ('name', 'systemNumber')

class ValveAdmin(admin.ModelAdmin):
    list_display = ('name', 'system', 'pidTagPrefix', 'pidTagNum')

class InstrumentAdmin(admin.ModelAdmin):
    list_display = ('name', 'system', 'pidTagPrefix', 'pidTagNum')


admin.site.register(Project, ProjectAdmin)
admin.site.register(System, SystemAdmin)
admin.site.register(Valve, ValveAdmin)
admin.site.register(Instrument, InstrumentAdmin)
