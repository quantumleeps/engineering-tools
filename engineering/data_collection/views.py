from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect

from .models import Location, Run, Group
from .forms import CollectedRunForm
from django.views.generic.edit import FormView

def index(request):
    locations = Location.objects.all()
    context = {'locations': locations}
    return render(request, 'data_collection/index.html', context)

def pick_run(request):
    runs = Run.objects.all()
    context = {'runs': runs}
    return render(request, 'data_collection/pick-run.html', context)

def collect_data(request, run_id):
    form = CollectedRunForm()
    if request.method == "POST":
        print(request.POST)
    run = get_object_or_404(Run, pk=run_id)
    points = run.points
    groups = points.values('group__name').distinct()
    context = {
        'run': run,
        'groups': groups,
    }
    return render(request, 'data_collection/collect_data.html', context)

def post_collected_run(request, run_id):
    instance = get_object_or_404(Run, pk=run_id)
    # print(instance.points.distinct().values())
    if request.method == "POST":
        context = {
            'instance': instance
        }
        # what are the steps to have an instantiated new collectedrun 
        # with all the collected points?
        # what you're doing is creating a new collected run and that is
        # what you're editing, not a "run"
        # you create the collected run and create all the collected
        # points so then all you're doing after that is performing
        # an update on points and and update on the overall
        # you only perform an update if the value has changed
        # Value can change during a data run. you're going to want to
        # autoupdate every 20 seconds or whenever a field is left
    else: 
        print('not a post')
        context = {
            'instance': instance
        }
    return render(request, 'data_collection/make_run.html', context)