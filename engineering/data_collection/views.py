from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect

from .models import Location, Run, Group
# from .forms import NameForm

def index(request):
    locations = Location.objects.all()
    context = {'locations': locations}
    return render(request, 'data_collection/index.html', context)

def pick_run(request):
    runs = Run.objects.all()
    context = {'runs': runs}
    return render(request, 'data_collection/pick-run.html', context)

def collect_data(request, run_id):
    run = get_object_or_404(Run, pk=run_id)
    points = run.points
    groups = points.values('group__name').distinct()
    return render(request, 'data_collection/collect_data.html', {'run': run, 'groups': groups})

# favorites = Favorite.objects.filter(user=request.user)
# color_ids = favorites.values_list('item__color', flat=True).distinct()


# def get_name(request):
#     # if this is a POST request we need to process the form data
#     if request.method == 'POST':
#         # create a form instance and populate it with data from the request:
#         form = NameForm(request.POST)
#         # check whether it's valid:
#         if form.is_valid():
#             # process the data in form.cleaned_data as required
#             # ...
#             # redirect to a new URL:
#             return HttpResponseRedirect('/thanks/')

#     # if a GET (or any other method) we'll create a blank form
#     else:
#         form = NameForm()

#     return render(request, 'name.html', {'form': form})