from django.contrib import admin
from .models import Material, Fluid, PipeSize

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

admin.site.register(Material, MaterialAdmin)
admin.site.register(Fluid, FluidAdmin)
admin.site.register(PipeSize, PipeSizeAdmin)

