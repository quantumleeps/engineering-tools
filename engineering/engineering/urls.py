from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^projects/', include('projects.urls')),
    url(r'^data-collection/', include('data_collection.urls')),
    url(r'^admin/', admin.site.urls),
]