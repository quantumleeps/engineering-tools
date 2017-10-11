from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<project_slug>[\w-]+)/$', views.tags_list, name='tags_list'),
    url(r'^(?P<project_slug>[\w-]+):(?P<tag_prefix>[\w-]+)/$', views.tags_list, name='tags_list'),
    url(r'^(?P<project_slug>[\w-]+)/(?P<system_slug>[\w-]+)$', views.tags_list, name='tags_list'),
    url(r'^(?P<project_slug>[\w-]+)/(?P<system_slug>[\w-]+):(?P<tag_prefix>[\w-]+)/$', views.tags_list, name='tags_list'),
    url(r'^(?P<project_slug>[\w-]+)/tag/(?P<pid_tag_slug>[\w-]+)$', views.tag_detail, name='tag_detail')
]


    # url(r'^$', views.home, name='home'),
    # url(r'^list$', views.projects_list, name='projects_list'),
    # url(r'^(?P<project_slug>[\w-]+)/$', views.categories_list, name='categories_list'),
    # url(r'^(?P<project_slug>[\w-]+):instruments$', views.instruments_list, name='instruments_list'),
    # url(r'^(?P<project_slug>[\w-]+):valves$', views.valves_list, name='valves_list'),
    # url(r'^(?P<project_slug>[\w-]+):tanks$', views.tanks_list, name='tanks_list'),
    # url(r'^(?P<project_slug>[\w-]+):pumps$', views.pumps_list, name='pumps_list'),
    # url(r'^(?P<project_slug>[\w-]+):pipes$', views.pipes_list, name='pipes_list'),
    # url(r'^(?P<project_slug>[\w-]+)/(?P<system_slug>[\w-]+)$', views.system_detail, name='system_detail'),
    # url(r'^(?P<project_slug>[\w-]+)/(?P<system_slug>[\w-]+):instruments$', views.specific_instruments_list, name='specific_instruments_list'),
    # url(r'^(?P<project_slug>[\w-]+)/(?P<system_slug>[\w-]+):valves$', views.specific_valves_list, name='specific_valves_list'),
    # url(r'^(?P<project_slug>[\w-]+)/(?P<system_slug>[\w-]+):tanks$', views.specific_tanks_list, name='specific_tanks_list'),
    # url(r'^(?P<project_slug>[\w-]+)/(?P<system_slug>[\w-]+):pumps$', views.specific_pumps_list, name='specific_pumps_list'),
    # url(r'^(?P<project_slug>[\w-]+)/(?P<system_slug>[\w-]+):pipes$', views.specific_pipes_list, name='specific_pipes_list'),