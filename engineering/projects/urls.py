from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<project_slug>[\w-]+)/$', views.tags_list, name='tags_list'),
    url(r'^(?P<project_slug>[\w-]+):(?P<tag_prefix>[\w-]+)/$', views.tags_list, name='tags_list'),
    url(r'^(?P<project_slug>[\w-]+)/(?P<system_slug>[\w-]+)$', views.tags_list, name='tags_list'),
    url(r'^(?P<project_slug>[\w-]+)/(?P<system_slug>[\w-]+):(?P<tag_prefix>[\w-]+)/$', views.tags_list, name='tags_list'),
    url(r'^(?P<project_slug>[\w-]+)/tag/(?P<pid_tag_slug>[\w-]+)$', views.tag_detail, name='tag_detail'),
    url(r'^(?P<project_slug>[\w-]+)/valves/$', views.valve_spec, name='valve_spec'),
]