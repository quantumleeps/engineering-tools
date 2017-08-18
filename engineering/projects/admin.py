from django.contrib import admin
from .models import Project, Valve, Instrument, Pump, Tank, Pipe

def duplicate_record(modeladmin, request, queryset):
    for object in queryset:
        object.id = None
        object.save()
duplicate_record.short_description = "Duplicate selected items"

def add_one_to_quantity(modeladmin, request, queryset):
    for object in queryset:
        object.quantity = object.quantity + 1
        object.save()
add_one_to_quantity.short_description = "Increase quantity for each selected by one"

def remove_one_from_quantity(modeladmin, request, queryset):
    for object in queryset:
        object.quantity = object.quantity - 1
        object.save()
remove_one_from_quantity.short_description = "Decrease quantity for each selected by one"

def auto_renumber_selected(modeladmin, request, queryset):
    i = 1
    for object in queryset:
        object.pid_tag_num = i
        i += 1
        object.save()
auto_renumber_selected.short_description = "For each item, assign a new sequential PID Tag Num"

def set_all_quantities_to_one(modeladmin, request, queryset):
    for object in queryset:
        object.quantity = 1
        object.save()
set_all_quantities_to_one.short_description = "For each item, set the quantity to one"

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'projectCode')
    actions = [duplicate_record]

class ValveAdmin(admin.ModelAdmin):
    list_display = ('name', 'project', 'system', 'quantity', 'pid_tag_num', 'pid_tag')
    list_filter = ('system', 'pid_tag_prefix')
    list_editable = ('system', 'pid_tag_num', 'quantity')
    actions = [duplicate_record, add_one_to_quantity, remove_one_from_quantity, auto_renumber_selected, set_all_quantities_to_one]

    def pid_tag(self, obj):
        if obj.quantity > 1:
            return str(obj.pid_tag_prefix) + '-' + str(obj.system.system_number + obj.pid_tag_num - 1) + "-X"
        else:
            return str(obj.pid_tag_prefix) + '-' + str(obj.system.system_number + obj.pid_tag_num - 1)
    ordering = ['system__system_number', 'pid_tag_num']
    
class InstrumentAdmin(admin.ModelAdmin):
    list_display = ('name', 'project', 'system', 'quantity', 'pid_tag_num', 'pid_tag')
    list_filter = ('system', 'pid_tag_prefix')
    list_editable = ('system', 'pid_tag_num', 'quantity')
    actions = [duplicate_record, add_one_to_quantity, remove_one_from_quantity, auto_renumber_selected, set_all_quantities_to_one]

    def pid_tag(self, obj):
        if obj.quantity > 1:
            return str(obj.pid_tag_prefix) + '-' + str(obj.system.system_number + obj.pid_tag_num - 1) + "-X"
        else:
            return str(obj.pid_tag_prefix) + '-' + str(obj.system.system_number + obj.pid_tag_num - 1)
    ordering = ['system__system_number', 'pid_tag_num']

class PumpAdmin(admin.ModelAdmin):
    list_display = ('name', 'project', 'system', 'quantity', 'pid_tag_num', 'pid_tag')
    list_filter = ('system', 'pid_tag_prefix')
    list_editable = ('system', 'pid_tag_num', 'quantity')
    actions = [duplicate_record, add_one_to_quantity, remove_one_from_quantity, auto_renumber_selected, set_all_quantities_to_one]

    def pid_tag(self, obj):
        if obj.quantity > 1:
            return str(obj.pid_tag_prefix) + '-' + str(obj.system.system_number + obj.pid_tag_num - 1) + "-X"
        else:
            return str(obj.pid_tag_prefix) + '-' + str(obj.system.system_number + obj.pid_tag_num - 1)
    ordering = ['system__system_number', 'pid_tag_num']

class TankAdmin(admin.ModelAdmin):
    list_display = ('name', 'project', 'system', 'quantity', 'pid_tag_num', 'pid_tag')
    list_filter = ('system', 'pid_tag_prefix')
    list_editable = ('system', 'pid_tag_num', 'quantity')
    actions = [duplicate_record, add_one_to_quantity, remove_one_from_quantity, auto_renumber_selected, set_all_quantities_to_one]

    def pid_tag(self, obj):
        if obj.quantity > 1:
            return str(obj.pid_tag_prefix) + '-' + str(obj.system.system_number + obj.pid_tag_num - 1) + "-X"
        else:
            return str(obj.pid_tag_prefix) + '-' + str(obj.system.system_number + obj.pid_tag_num - 1)
    ordering = ['system__system_number', 'pid_tag_num']

class PipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'project', 'system', 'quantity', 'pid_tag_num', 'pid_tag')
    list_filter = ('system', 'pid_tag_prefix')
    list_editable = ('system', 'pid_tag_num', 'quantity')
    actions = [duplicate_record, add_one_to_quantity, remove_one_from_quantity, auto_renumber_selected, set_all_quantities_to_one]

    def pid_tag(self, obj):
        if obj.quantity > 1:
            return str(obj.pid_tag_prefix) + '-' + str(obj.system.system_number + obj.pid_tag_num - 1) + "-X"
        else:
            return str(obj.pid_tag_prefix) + '-' + str(obj.system.system_number + obj.pid_tag_num - 1)
    ordering = ['system__system_number', 'pid_tag_num']

admin.site.register(Project, ProjectAdmin)
admin.site.register(Valve, ValveAdmin)
admin.site.register(Instrument, InstrumentAdmin)
admin.site.register(Pump, PumpAdmin)
admin.site.register(Tank, TankAdmin)
admin.site.register(Pipe, PipeAdmin)



