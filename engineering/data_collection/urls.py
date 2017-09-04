from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^pick-run/', views.pick_run),
    url(r'^collect-data/(?P<run_id>[0-9]+)/$', views.collect_data, name="collect"),
]