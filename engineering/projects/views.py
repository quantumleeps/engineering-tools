from django.http import HttpResponse
from .models import Project, System, Instrument, Valve, Pump, Pipe, Tank, Equipment
from django.shortcuts import get_object_or_404, render


def index(request):
    projects = Project.objects.all()
    return render(request, 'projects/home.html', {'projects': projects})

# def filter_bar(request, project_slug)

# def tags_list(request, project_slug):

#     # kwargs = {
#     #     'project__slug': project_slug,
#     # }

#     contents = {}
    
#     contents['project_name'] = get_object_or_404(Project, slug=project_slug)
#     contents['systems'] = System.objects.all()
#     # contents['systems'] = get_object_or_404(System, slug=project_slug)
#     # if system_slug == None and tag_prefix == None:
#     #     pass
#     # elif system_slug != None and tag_prefix != None:
#     #     contents['system_name'] = get_object_or_404(System, slug=system_slug)
#     #     kwargs['system__slug'] = system_slug
#     #     kwargs['pid_tag_prefix'] = tag_prefix
#     # elif system_slug == None and tag_prefix != None:
#     #     kwargs['pid_tag_prefix'] = tag_prefix
#     # else:
#     #     contents['system_name'] = get_object_or_404(System, slug=system_slug)
#     #     kwargs['system__slug'] = system_slug
        
#     # contents['instruments'] = Instrument.objects.filter(kwargs)
#     # contents['valves'] = Valve.objects.filter(kwargs)
#     # contents['tanks'] = Tank.objects.filter(kwargs)
#     # contents['pumps'] = Pump.objects.filter(kwargs)
#     # contents['pipes'] = Pipe.objects.filter(kwargs)
    
#     return render(request, 'projects/tags_list.html', contents)


def tags_list(request, project_slug, system_slug=None, tag_prefix=None):
    
    kwargs = {
        'project__slug': project_slug,
    }

    contents = {}
    contents['systems'] = Project.objects.filter(slug=project_slug)[0].systems.all()
    contents['project_slug'] = project_slug
    contents['project_name'] = get_object_or_404(Project, slug=project_slug)
    contents['tag_prefix'] = tag_prefix
    if system_slug == None and tag_prefix == None:
        pass
    elif system_slug != None and tag_prefix != None:
        contents['system_name'] = get_object_or_404(System, slug=system_slug)
        contents['system_slug'] = system_slug
        kwargs['system__slug'] = system_slug
        kwargs['pid_tag_prefix'] = tag_prefix
    elif system_slug == None and tag_prefix != None:
        kwargs['pid_tag_prefix'] = tag_prefix
    else:
        contents['system_name'] = get_object_or_404(System, slug=system_slug)
        contents['system_slug'] = system_slug
        kwargs['system__slug'] = system_slug
        
    contents['instruments'] = Instrument.objects.filter(**kwargs)
    contents['valves'] = Valve.objects.filter(**kwargs)
    contents['tanks'] = Tank.objects.filter(**kwargs)
    contents['pumps'] = Pump.objects.filter(**kwargs)
    contents['pipes'] = Pipe.objects.filter(**kwargs)
    contents['equipment'] = Equipment.objects.filter(**kwargs)
    
    return render(request, 'projects/tags_list.html', contents)

