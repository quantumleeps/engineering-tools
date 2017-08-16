from django.contrib import admin
from .models import Project, System, Valve, Instrument

def duplicate_record(modeladmin, request, queryset):
    for object in queryset:
        object.id = None
        object.save()
duplicate_record.short_description = "Duplicate selected items"

# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'country')

class SystemAdmin(admin.ModelAdmin):
    list_display = ('name', 'systemNumber')

class ValveAdmin(admin.ModelAdmin):
    # list_display = ('name', 'system', 'system_number', 'pidTagPrefix', 'pidTagNum')
    list_display = ('name', 'system', 'system_number', 'pid_tag_number')
    list_filter = ('system', 'pidTagPrefix')
    list_editable = ('system',)
    actions = [duplicate_record]
    def system_number(self, obj):
        return obj.system.systemNumber

    def system_name(self, obj):
        return obj.system.name

    def pid_tag_number(self, obj):
        return str(obj.pidTagPrefix) + '-' + str(obj.system.systemNumber + obj.pidTagNum - 1)
        # return str(obj.system.systemNumber + self.pidTagNum)
    ordering = ['system__systemNumber']

class InstrumentAdmin(admin.ModelAdmin):
    list_display = ('name', 'system', 'system_number', 'pid_tag_number')
    list_filter = ('system', 'pidTagPrefix')
    list_editable = ('system',)
    actions = [duplicate_record]
    def system_number(self, obj):
        return obj.system.systemNumber

    def system_name(self, obj):
        return obj.system.name

    def pid_tag_number(self, obj):
        return str(obj.pidTagPrefix) + '-' + str(obj.system.systemNumber + obj.pidTagNum - 1)
        # return str(obj.system.systemNumber + self.pidTagNum)
    ordering = ['system__systemNumber']

admin.site.register(Project, ProjectAdmin)
admin.site.register(System, SystemAdmin)
admin.site.register(Valve, ValveAdmin)
admin.site.register(Instrument, InstrumentAdmin)


