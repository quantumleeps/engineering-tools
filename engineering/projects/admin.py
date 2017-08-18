from django.contrib import admin
from .models import Project, ProjectSystem, Valve, Instrument, Pump, Tank, Pipe

def duplicate_record(modeladmin, request, queryset):
    for object in queryset:
        object.id = None
        object.save()
duplicate_record.short_description = "Duplicate selected items"

# Register your models here.

class ProjectSystemInline(admin.TabularInline):
    model = ProjectSystem
    actions = [duplicate_record]

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'country')
    inlines = [
        ProjectSystemInline
    ]
    actions = [duplicate_record]

class ProjectSystemAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}
    # pass
# class SystemAdmin(admin.ModelAdmin):
#     list_display = ('name', 'systemNumber')

class ValveAdmin(admin.ModelAdmin):
    # list_display = ('name', 'system', 'pid_tag_number')
    # list_filter = ('system', 'pid_tag_prefix')
    # list_editable = ('system',)
    # actions = [duplicate_record]

    # def system_name(self, obj):
    #     return obj.projectsystem.name

    # def pid_tag_number(self, obj):
    #     return str(obj.pid_tag_prefix) + '-' + str(obj.projectsystem.system_number + obj.pid_tag_num - 1)
    # ordering = ['system__system_number']
    pass
class InstrumentAdmin(admin.ModelAdmin):
    # list_display = ('name', 'system', 'pid_tag_number')
    # list_filter = ('system', 'pid_tag_prefix')
    # list_editable = ('system',)
    # actions = [duplicate_record]

    # def system_name(self, obj):
    #     return obj.projectsystem.name

    # def pid_tag_number(self, obj):
    #     return str(obj.pid_tag_prefix) + '-' + str(obj.projectsystem.system_number + obj.pid_tag_num - 1)
    # ordering = ['system__system_number']
    pass
class PumpAdmin(admin.ModelAdmin):
    # list_display = ('name', 'system', 'pid_tag_number')
    # list_filter = ('system', 'pid_tag_prefix')
    # list_editable = ('system',)
    # actions = [duplicate_record]

    # def system_name(self, obj):
    #     return obj.projectsystem.name

    # def pid_tag_number(self, obj):
    #     return str(obj.pid_tag_prefix) + '-' + str(obj.projectsystem.system_number + obj.pid_tag_num - 1)
    # ordering = ['system__system_number']
    pass

class TankAdmin(admin.ModelAdmin):
    # list_display = ('name', 'system', 'pid_tag_number')
    # list_filter = ('system', 'pid_tag_prefix')
    # list_editable = ('system',)
    # actions = [duplicate_record]

    # def system_name(self, obj):
    #     return obj.projectsystem.name

    # def pid_tag_number(self, obj):
    #     return str(obj.pid_tag_prefix) + '-' + str(obj.projectsystem.system_number + obj.pid_tag_num - 1)
    # ordering = ['system__system_number']
    pass
class PipeAdmin(admin.ModelAdmin):
    # list_display = ('name', 'system', 'pid_tag_number')
    # list_filter = ('system', 'pid_tag_prefix')
    # list_editable = ('system',)
    # actions = [duplicate_record]

    # def system_name(self, obj):
    #     return obj.projectsystem.name

    # def pid_tag_number(self, obj):
    #     return str(obj.pid_tag_prefix) + '-' + str(obj.projectsystem.system_number + obj.pid_tag_num - 1)
    # ordering = ['system__system_number']
    pass

admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectSystem, ProjectSystemAdmin)
admin.site.register(Valve, ValveAdmin)
admin.site.register(Instrument, InstrumentAdmin)
admin.site.register(Pump, PumpAdmin)
admin.site.register(Tank, PumpAdmin)
admin.site.register(Pipe, PumpAdmin)



