from django.contrib import admin
from .models import Project, System, Valve, Instrument, Pump, Tank, Pipe, Equipment
from titlecase import titlecase

def duplicate_record(modeladmin, request, queryset):
    for object in queryset:
        object.id = None
        object.save()
duplicate_record.short_description = "Duplicate selected items"

def fix_case(modeladmin, request, queryset):
    for object in queryset:
        object.name = titlecase(object.name)
        object.save()
fix_case.short_description = "Fix capitalization"

# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'country')

class SystemAdmin(admin.ModelAdmin):
    list_display = ('name', 'systemNumber')

class ValveAdmin(admin.ModelAdmin):
    # list_display = ('name', 'system', 'system_number', 'pidTagPrefix', 'pidTagNum')
    list_display = ('name', 'system', 'project', 'pid_tag_number')
    list_filter = ('project', 'system', 'pid_tag_prefix',)
    list_editable = ('system',)
    actions = [duplicate_record, fix_case]
    def system_number(self, obj):
        return obj.system.systemNumber

    def system_name(self, obj):
        return obj.system.name

    def pid_tag_number(self, obj):
        return str(obj.pid_tag_prefix) + '-' + str(obj.system.systemNumber + obj.pid_tag_num - 1)
        # return str(obj.system.systemNumber + self.pidTagNum)
    ordering = ['system__systemNumber']

class InstrumentAdmin(admin.ModelAdmin):
    list_display = ('name', 'system', 'project', 'pid_tag_number',)
    list_filter = ('project', 'system', 'pid_tag_prefix',)
    list_editable = ('system',)
    actions = [duplicate_record, fix_case]
    def system_number(self, obj):
        return obj.system.systemNumber

    def system_name(self, obj):
        return obj.system.name

    def pid_tag_number(self, obj):
        return str(obj.pid_tag_prefix) + '-' + str(obj.system.systemNumber + obj.pid_tag_num - 1)
        # return str(obj.system.systemNumber + self.pidTagNum)
    ordering = ['system__systemNumber']

class PumpAdmin(admin.ModelAdmin):
    list_display = ('name', 'system', 'system_number', 'pid_tag_number')
    list_filter = ('system', 'pid_tag_prefix')
    list_editable = ('system',)
    actions = [duplicate_record, fix_case]
    def system_number(self, obj):
        return obj.system.systemNumber

    def system_name(self, obj):
        return obj.system.name

    def pid_tag_number(self, obj):
        return str(obj.pid_tag_prefix) + '-' + str(obj.system.systemNumber + obj.pid_tag_num - 1)
        # return str(obj.system.systemNumber + self.pidTagNum)
    ordering = ['system__systemNumber']


class TankAdmin(admin.ModelAdmin):
    list_display = ('name', 'system', 'system_number', 'pid_tag_number')
    list_filter = ('system', 'pid_tag_prefix')
    list_editable = ('system',)
    actions = [duplicate_record, fix_case]
    def system_number(self, obj):
        return obj.system.systemNumber

    def system_name(self, obj):
        return obj.system.name

    def pid_tag_number(self, obj):
        return str(obj.pid_tag_prefix) + '-' + str(obj.system.systemNumber + obj.pid_tag_num - 1)
        # return str(obj.system.systemNumber + self.pidTagNum)
    ordering = ['system__systemNumber']

class PipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'system', 'system_number', 'pid_tag_number')
    list_filter = ('system', 'pid_tag_prefix')
    list_editable = ('system',)
    actions = [duplicate_record, fix_case]
    def system_number(self, obj):
        return obj.system.systemNumber

    def system_name(self, obj):
        return obj.system.name

    def pid_tag_number(self, obj):
        return str(obj.pid_tag_prefix) + '-' + str(obj.system.systemNumber + obj.pid_tag_num - 1)
        # return str(obj.system.systemNumber + self.pidTagNum)
    ordering = ['system__systemNumber']

class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'system', 'system_number', 'pid_tag_number')
    list_filter = ('system', 'pid_tag_prefix')
    list_editable = ('system',)
    actions = [duplicate_record, fix_case]
    def system_number(self, obj):
        return obj.system.systemNumber

    def system_name(self, obj):
        return obj.system.name

    def pid_tag_number(self, obj):
        return str(obj.pid_tag_prefix) + '-' + str(obj.system.systemNumber + obj.pid_tag_num - 1)
        # return str(obj.system.systemNumber + self.pidTagNum)
    ordering = ['system__systemNumber']


admin.site.register(Project, ProjectAdmin)
admin.site.register(System, SystemAdmin)
admin.site.register(Valve, ValveAdmin)
admin.site.register(Instrument, InstrumentAdmin)
admin.site.register(Pump, PumpAdmin)
admin.site.register(Tank, TankAdmin)
admin.site.register(Pipe, PipeAdmin)
admin.site.register(Equipment, EquipmentAdmin)



