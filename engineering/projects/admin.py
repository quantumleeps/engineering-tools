from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from .models import Project, System, Valve, Instrument, Pump, Tank, Pipe, Equipment, PumpOperatingPoint, PumpPart, DocumentCategory, ControlledDocument
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

def save_in_place(modeladmin, request, queryset):
    for object in queryset:
        object.save()
save_in_place.short_description = "Perform a save in place of selected items"

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
    list_display = ('name', 'system', 'project', 'full_pid_tag_number', 'ready_for_quote')
    list_filter = ('project', 'system', 'pid_tag_prefix','ready_for_quote')
    history_list_display = ['name', 'system', 'full_pid_tag_number']
    list_editable = ('system', 'ready_for_quote',)
    actions = [duplicate_record, fix_case, save_in_place]
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
    actions = [duplicate_record, fix_case, save_in_place]
    def system_number(self, obj):
        return obj.system.systemNumber

    def system_name(self, obj):
        return obj.system.name

    def pid_tag_number(self, obj):
        return str(obj.pid_tag_prefix) + '-' + str(obj.system.systemNumber + obj.pid_tag_num - 1)
        # return str(obj.system.systemNumber + self.pidTagNum)
    ordering = ['system__systemNumber']

class PumpOperatingPointInline(admin.TabularInline):
    model = PumpOperatingPoint
    extra = 2

class PumpPartInline(admin.TabularInline):
    model = PumpPart
    extra = 2

class PumpHistoryAdmin(SimpleHistoryAdmin):
    list_display = ('name', 'system', 'system_number', 'full_pid_tag_number')
    list_filter = ('system', 'pid_tag_prefix')
    history_list_display = ['name', 'system', 'full_pid_tag_number']
    list_editable = ('system',)
    actions = [duplicate_record, fix_case, save_in_place]
    inlines = [PumpOperatingPointInline, PumpPartInline]
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
    actions = [duplicate_record, fix_case, save_in_place]
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
    actions = [duplicate_record, fix_case, save_in_place]
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
    actions = [duplicate_record, fix_case, save_in_place]
    def system_number(self, obj):
        return obj.system.systemNumber

    def system_name(self, obj):
        return obj.system.name

    def pid_tag_number(self, obj):
        return str(obj.pid_tag_prefix) + '-' + str(obj.system.systemNumber + obj.pid_tag_num - 1)
        # return str(obj.system.systemNumber + self.pidTagNum)
    ordering = ['system__systemNumber']

class DocumentCategoryHistoryAdmin(SimpleHistoryAdmin):
    list_display = ('name', 'code')
    history_list_display = ['name', 'code']

class ControlledDocumentHistoryAdmin(SimpleHistoryAdmin):
    list_display = ('description', 'project', 'drawing_title', 'system', 'category')
    history_list_display = ['description', 'project', 'drawing_title']
    list_filter = ('system', 'category')

admin.site.register(DocumentCategory, DocumentCategoryHistoryAdmin)
admin.site.register(ControlledDocument, ControlledDocumentHistoryAdmin)
admin.site.register(Project, ProjectHistoryAdmin)
admin.site.register(System, SystemHistoryAdmin)
admin.site.register(Valve, ValveHistoryAdmin)
admin.site.register(Instrument, InstrumentHistoryAdmin)
admin.site.register(Pump, PumpHistoryAdmin)
admin.site.register(Tank, TankHistoryAdmin)
admin.site.register(Pipe, PipeHistoryAdmin)
admin.site.register(Equipment, EquipmentHistoryAdmin)



admin.site.site_title = 'CWCO Engineering Admin Page'
admin.site.site_header = 'CWCO Engineering Admin Page'