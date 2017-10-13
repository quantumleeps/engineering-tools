from django.http import HttpResponse
from .models import Project, System, Instrument, Valve, Pump, Pipe, Tank, Equipment
from django.shortcuts import get_object_or_404, render

def index(request):
    projects = Project.objects.all()
    return render(request, 'projects/home.html', {'projects': projects})

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
        
    contents['instruments'] = Instrument.objects.filter(**kwargs).order_by('system__systemNumber', '-full_pid_tag_number')
    contents['valves'] = Valve.objects.filter(**kwargs).order_by('system__systemNumber', '-full_pid_tag_number')
    contents['tanks'] = Tank.objects.filter(**kwargs).order_by('system__systemNumber', '-full_pid_tag_number')
    contents['pumps'] = Pump.objects.filter(**kwargs).order_by('system__systemNumber', '-full_pid_tag_number')
    contents['pipes'] = Pipe.objects.filter(**kwargs).order_by('system__systemNumber', '-full_pid_tag_number')
    contents['equipment'] = Equipment.objects.filter(**kwargs).order_by('system__systemNumber', '-full_pid_tag_number')
    
    return render(request, 'projects/tags_list.html', contents)

def tag_detail(request, project_slug, pid_tag_slug):
    
    kwargs = {
        'project__slug': project_slug,
        'full_pid_tag_number__contains': pid_tag_slug,
    }

    contents = {
        'project_slug': project_slug,
        'pid_tag': pid_tag_slug.upper(),
    }

    contents['project'] = get_object_or_404(Project, slug=project_slug)


    lookups = [
        Instrument,
        Pump,
        Valve,
        Tank,
        Pipe,
        Equipment
    ]

    for lookup in lookups:
        try:   
            contents['item'] = get_object_or_404(lookup, full_pid_tag_number=pid_tag_slug.upper())
            contents['type'] = lookup.__name__
            print(lookup.__name__)
            contents['error'] = None
            break
        except:
            contents['error'] = "Couldn't locate the tag. May be 2 tags with same P&ID number"
            continue


    return render(request, 'projects/tag_detail.html', contents)
