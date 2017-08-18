from django.contrib import admin
from .models import Material, Fluid, PipeSize, System, ConnectionType

def duplicate_record(modeladmin, request, queryset):
    for object in queryset:
        object.id = None
        object.save()
duplicate_record.short_description = "Duplicate selected items"

# Register your models here.

class MaterialAdmin(admin.ModelAdmin):
    list_display = ('name', 'uns_number', 'astm_number')
    actions = [duplicate_record]
    ordering = ['astm_number', 'name']

class FluidAdmin(admin.ModelAdmin):
    list_display = ('name', 'specific_gravity')
    actions = [duplicate_record]
    ordering = ['name']

class PipeSizeAdmin(admin.ModelAdmin):
    list_display = ('name', 'units', 'outside_diameter')
    actions = [duplicate_record]
    ordering = ['outside_diameter']

class SystemAdmin(admin.ModelAdmin):
    list_display = ('name',)
    # list_display = ('name', 'system_number', 'system_code')
    # list_editable = ('name',)
    # actions = [duplicate_record]
    # def system_number(self, obj):
    #     return obj.system.systemNumber

    # def system_name(self, obj):
    #     return obj.system.name

    # def pid_tag_number(self, obj):
    #     return str(obj.pid_tag_prefix) + '-' + str(obj.system.systemNumber + obj.pid_tag_num - 1)
    #     # return str(obj.system.systemNumber + self.pidTagNum)
    # ordering = ['system_number']


admin.site.register(Material, MaterialAdmin)
admin.site.register(Fluid, FluidAdmin)
admin.site.register(PipeSize, PipeSizeAdmin)
admin.site.register(System, SystemAdmin)
admin.site.register(ConnectionType)
