from django import template
from ..models import ControlledDocument

register = template.Library()

# system is the current iterate in systems
# current_system is the request.GET curent_system=?...
# current_category is the request.GET current_category?...
@register.simple_tag()
def process_system(system, current_system, current_category):
    kwargs = {}
    kwargs['system__slug'] = system['system__slug']
    kwargs['category__slug'] = current_category
    if not current_system and not current_category:
        return '<a href="?system=' + system['system__slug'] + '" class="filter-button btn btn-primary .btn-sm active" role="button">' + system['system__name'] + '</a><br>'
    elif not current_category and current_system and not system['system__slug'] == current_system:
        return '<a href="?system=' + system['system__slug'] + '"class="filter-button btn btn-primary .btn-sm active" role="button">' + system['system__name'] + '</a><br>'
    elif system['system__slug'] == current_system:
        return '<style>.btn-success {border: 1px solid black} .btn-primary.disabled {background-color: rgb(192,192,192); border-color: rgb(122,122,122) !important}</style><a href="#" class="filter-button btn btn-success .btn-sm inactive" role="button">'+ system['system__name'] + '</a><br>'
    elif ControlledDocument.objects.filter(**kwargs).exists() == True:
        return '<a href="?category=' + current_category + '&system=' + system['system__slug'] + '" class="filter-button btn btn-primary .btn-sm active" role="button">' + system['system__name'] + '</a><br>'
    else: 
        return '<a href="#" class="filter-button btn btn-primary disabled" role="button">'+ system['system__name'] + '</a><br>'
    # what is the precise case you're looking for? 
    # system selected  no category selected. other systems greyed out
    # there is a current system, there is no current category
@register.simple_tag()
def process_category(category, current_category, current_system):
    kwargs = {}
    kwargs['category__slug'] = category['category__slug']
    kwargs['system__slug'] = current_system
    if not current_system and not current_category:
        return '<a href="?category=' + category['category__slug'] + '" class="filter-button btn btn-primary active" role="button">' + category['category__name'] + '</a><br>'
    if not current_system and current_category and not category['category__slug'] == current_category:
        return '<a href="?category=' + category['category__slug'] + '" class="filter-button btn btn-primary active" role="button">' + category['category__name'] + '</a><br>'
    elif category['category__slug'] == current_category:
        return '<style>.btn-success {border: 1px solid black} .btn-primary.disabled {background-color: rgb(192,192,192); border-color: rgb(122,122,122) !important}</style><a href="#" class="filter-button btn btn-success inactive" role="button">'+ category['category__name'] + '</a><br>'
    elif ControlledDocument.objects.filter(**kwargs).exists() == True:
        # If there are matching documents, you want an active link to be generated
        return '<a href="?category=' + category['category__slug'] + '&system=' + current_system + '" class="filter-button btn btn-primary active" role="button">' + category['category__name'] + '</a><br>'
    else: 
        # If there are no matchign documents, it should be displayed but not as a link 
        return '<a href="#" class="filter-button btn btn-primary disabled" role="button">'+ category['category__name'] + '</a><br>'