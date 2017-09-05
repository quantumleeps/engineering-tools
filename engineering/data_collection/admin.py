# from django.contrib import admin
from .models import Location, Group, Point, Run, CollectedPoint, CollectedRun
from .forms import RunForm, PointForm
from django.contrib import admin
import nested_admin



# class GroupAdmin(admin.ModelAdmin):
#     list_filter = ['location']
#     inlines = [PointInline]

class PointInline(nested_admin.NestedTabularInline):
    model = Point
    extra = 0

class GroupInline(nested_admin.NestedStackedInline):
    model = Group
    extra = 0
    inlines = [PointInline]

class LocationAdmin(nested_admin.NestedModelAdmin):
    inlines = [GroupInline]

class RunAdmin(admin.ModelAdmin):
    model = Run
    list_filter = ['location']
    filter_horizontal = ('points','data_collectors',)
    form = RunForm

admin.site.register(Location, LocationAdmin)
admin.site.register(Run, RunAdmin)
admin.site.register(CollectedPoint)
