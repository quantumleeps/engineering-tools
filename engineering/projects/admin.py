from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from .models import Project, System, Valve, Instrument, Pump, Tank, Pipe, Equipment, PumpOP, PumpPart
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

class ProjectHistoryAdmin(SimpleHistoryAdmin):
    list_display = ('name', 'country')
    history_list_display = ['name', 'country']
    filter_horizontal = ['systems']

class SystemHistoryAdmin(SimpleHistoryAdmin):
    list_display = ('name', 'systemNumber')
    history_list_display = ['name', 'systemNumber']

class ValveHistoryAdmin(SimpleHistoryAdmin):
    # list_display = ('name', 'system', 'system_number', 'pidTagPrefix', 'pidTagNum')
    list_display = ('name', 'system', 'project', 'full_pid_tag_number')
    list_filter = ('project', 'system', 'pid_tag_prefix',)
    history_list_display = ['name', 'system', 'full_pid_tag_number']
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

class InstrumentHistoryAdmin(SimpleHistoryAdmin):
    list_display = ('name', 'system', 'project', 'full_pid_tag_number',)
    list_filter = ('project', 'system', 'pid_tag_prefix',)
    history_list_display = ['name', 'system', 'full_pid_tag_number']
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

class PumpOPInline(admin.TabularInline):
    model = PumpOP
    extra = 2

class PumpPartInline(admin.TabularInline):
    model = PumpPart
    extra = 2

class PumpHistoryAdmin(SimpleHistoryAdmin):
    list_display = ('name', 'system', 'system_number', 'full_pid_tag_number')
    list_filter = ('system', 'pid_tag_prefix')
    history_list_display = ['name', 'system', 'full_pid_tag_number']
    list_editable = ('system',)
    actions = [duplicate_record, fix_case]
    inlines = [PumpOPInline, PumpPartInline]
    def system_number(self, obj):
        return obj.system.systemNumber

    def system_name(self, obj):
        return obj.system.name

    def pid_tag_number(self, obj):
        return str(obj.pid_tag_prefix) + '-' + str(obj.system.systemNumber + obj.pid_tag_num - 1)
        # return str(obj.system.systemNumber + self.pidTagNum)
    ordering = ['system__systemNumber']


class TankHistoryAdmin(SimpleHistoryAdmin):
    list_display = ('name', 'system', 'system_number', 'full_pid_tag_number')
    list_filter = ('system', 'pid_tag_prefix')
    history_list_display = ['name', 'system', 'full_pid_tag_number']
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

class PipeHistoryAdmin(SimpleHistoryAdmin):
    list_display = ('name', 'system', 'system_number', 'full_pid_tag_number')
    list_filter = ('system', 'pid_tag_prefix')
    history_list_display = ['name', 'system', 'full_pid_tag_number']
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

class EquipmentHistoryAdmin(SimpleHistoryAdmin):
    list_display = ('name', 'system', 'system_number', 'full_pid_tag_number')
    list_filter = ('system', 'pid_tag_prefix')
    history_list_display = ['name', 'system', 'full_pid_tag_number']
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


admin.site.register(Project, ProjectHistoryAdmin)
admin.site.register(System, SystemHistoryAdmin)
admin.site.register(Valve, ValveHistoryAdmin)
admin.site.register(Instrument, InstrumentHistoryAdmin)
admin.site.register(Pump, PumpHistoryAdmin)
admin.site.register(Tank, TankHistoryAdmin)
admin.site.register(Pipe, PipeHistoryAdmin)
admin.site.register(Equipment, EquipmentHistoryAdmin)



