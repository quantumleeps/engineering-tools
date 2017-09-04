from django import forms
from .models import Run, Point, Location

class RunForm(forms.ModelForm):

# Model.objects.filter(field_lookup=value).latest()


# get the first location in the list of locations


    def __init__(self, *args, **kwargs):

        # latest_location = Location.objects.filter().latest()
        super(RunForm, self).__init__(*args, **kwargs)
        self.fields['points'].queryset = Point.objects.all()
        
        instance = kwargs.get('instance', {})
        print(instance)
        if instance:
            self.fields['points'].queryset = Point.objects.filter(group__location=kwargs['instance'].location)

    #     self.fields['points'].queryset = Point.objects.all()
    #     initial = kwargs.get('initial', {})
    #     initial['points'] = Point.objects.filter()
    #     kwargs['initial'] = initial
    #     super(RunForm, self).__init__(*args, **kwargs)
    #     # super(RunForm, self).__init__(*args, **kwargs)
    #     # if 'instance' in kwargs:
    #     #     if kwargs['instance'].location:
    #     #         self.fields['points'].queryset = Point.objects.filter(group__location=kwargs['instance'].location)
    #     # else: 
    #     #     pass

    class Meta:
        model = Run
        fields = '__all__'