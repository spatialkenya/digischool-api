from django.conf.urls import url, include
from . import views
from django.contrib import admin

urlpatterns = [
    url(r'^$', views.home, name='index'),
    url(r'^api/v1/', include('geoapp.urls')),
    url(r'^jet/', include('jet.urls', 'jet')),  # Django JET URLS
    url(r'^admin/', include(admin.site.urls)),
]
