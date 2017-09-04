from django.contrib import admin
from .models import Location, Group, Point, Run, CollectedPoint, CollectedRun
from .forms import RunForm

class RunAdmin(admin.ModelAdmin):
    model = Run
    # def formfield_for_manytomany(self, db_field, request, **kwargs):
    #     if db_field.name == 'points':
    #         kwargs['initial'] = [Run.objects.get_current()]
    #         return db_field.formfield(**kwargs)

    #     return super(RunAdmin, self).formfield_for_manytomany(db_field, request, **kwargs)


    # def formfield_for_manytomany(self, db_field, request, **kwargs):
    #     if db_field.name == "points":
    #         kwargs["queryset"] = Point.objects.filter()
    #     return super().formfield_for_manytomany(db_field, request, **kwargs)
    list_filter = ['location']
    filter_horizontal = ('points',)
    form = RunForm




admin.site.register(Location)
admin.site.register(Group)
admin.site.register(Point)
admin.site.register(Run, RunAdmin)
admin.site.register(CollectedPoint)
admin.site.register(CollectedRun)

