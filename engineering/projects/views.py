from django.http import HttpResponse
from .models import Project, System, Instrument, Valve, Pump, Pipe, Tank, Equipment
from django.shortcuts import get_object_or_404, render

def find_used_systems(systems):
    used_systems = []
    for system in systems:
        if Instrument.objects.filter(system=system).exists():
            used_systems.append(system)
        elif Valve.objects.filter(system=system).exists():
            used_systems.append(system)
        elif Pump.objects.filter(system=system).exists():
            used_systems.append(system)            
        elif Tank.objects.filter(system=system).exists():
            used_systems.append(system)
        elif Pipe.objects.filter(system=system).exists():
            used_systems.append(system)
        elif Equipment.objects.filter(system=system).exists():
            used_systems.append(system)
    return used_systems

def index(request):
    projects = Project.objects.all()
    return render(request, 'projects/home.html', {'projects': projects})

def tags_list(request, project_slug, system_slug=None, tag_prefix=None):
    
    kwargs = {
        'project__slug': project_slug,
    }
    # currently there's a bug that if you select a system when adding an instrument that isn't in
    # the project, it'll still display on the page. Need to filter what shows on the page to only
    # be systems that are in the project's system list
    # need to check that the instrument's system is part of the project's systems:
    contents = {}
    contents['systems'] = find_used_systems(get_object_or_404(Project, slug=project_slug).systems.all())
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
        
    contents['instruments'] = Instrument.objects.filter(**kwargs).order_by('system__systemNumber', 'full_pid_tag_number')
    contents['valves'] = Valve.objects.filter(**kwargs).order_by('system__systemNumber', 'full_pid_tag_number')
    contents['tanks'] = Tank.objects.filter(**kwargs).order_by('system__systemNumber', 'full_pid_tag_number')
    contents['pumps'] = Pump.objects.filter(**kwargs).order_by('system__systemNumber', 'full_pid_tag_number')
    contents['pipes'] = Pipe.objects.filter(**kwargs).order_by('system__systemNumber', 'full_pid_tag_number')
    contents['equipment'] = Equipment.objects.filter(**kwargs).order_by('system__systemNumber', 'full_pid_tag_number')
    
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
