from django.conf.urls import url

from . import views, xlsx_views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<project_slug>[\w-]+)/$', views.tags_list, name='tags_list'),
    url(r'^(?P<project_slug>[\w-]+):(?P<tag_prefix>[\w-]+)/$', views.tags_list, name='tags_list'),
    url(r'^(?P<project_slug>[\w-]+)/(?P<system_slug>[\w-]+)$', views.tags_list, name='tags_list'),
    url(r'^(?P<project_slug>[\w-]+)/(?P<system_slug>[\w-]+):(?P<tag_prefix>[\w-]+)/$', views.tags_list, name='tags_list'),
    url(r'^(?P<project_slug>[\w-]+)/tag/(?P<pid_tag_slug>[\w-]+)$', views.tag_detail, name='tag_detail'),
    url(r'^(?P<project_slug>[\w-]+)/valves/$', views.valve_spec, name='valve_spec'),
    url(r'^(?P<project_slug>[\w-]+)/valves-xlsx/$', xlsx_views.valve_rfq_xlsx_view, name='valve_rfq_xlsx_view'),
    url(r'^(?P<project_slug>[\w-]+)/controlled-documents/$', views.controlled_document_list, name='controlled_document_list')
]