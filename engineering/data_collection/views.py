from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect

from .models import Location, Run
# from .forms import NameForm

def index(request):
    locations = Location.objects.all()
    context = {'locations': locations}
    return render(request, 'data_collection/index.html', context)

def pick_run(request):
    runs = Run.objects.all()
    context = {'runs': runs}
    return render(request, 'data_collection/pick-run.html', context)

