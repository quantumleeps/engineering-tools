from django import forms
from .models import Run, Point, Location, Group, CollectedRun, CollectedPoint

class RunForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):

        super(RunForm, self).__init__(*args, **kwargs)
        self.fields['points'].queryset = Point.objects.all()
        
        instance = kwargs.get('instance', {})
        if instance:
            self.fields['points'].queryset = Point.objects.filter(group__location=kwargs['instance'].location)

    class Meta:
        model = Run
        fields = '__all__'

class PointForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):

        super(PointForm, self).__init__(*args, **kwargs)
        self.fields['group'].queryset = Point.objects.all()

        instance = kwargs.get('instance', {})
        if instance:
            print(kwargs['instance'].group.location)
            # self.fields['group'].queryset = Point.objects.all()
            self.fields['group'].queryset = Group.objects.filter(location=kwargs['instance'].group.location)

class CollectedRunForm(forms.ModelForm):
    class Meta:
        model = CollectedRun
        fields = [
            'collected_points'
        ]

# class CollectedRunForm(forms.modelForm):
#     class Meta:
#         model = CollectedRun
#         fields = ['points__value']
