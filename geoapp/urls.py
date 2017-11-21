from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.authtoken import views as drf_views

from . import views

router = routers.DefaultRouter(trailing_slash=True)
router.register(r'counties', views.CountyViewSet, base_name="counties")
router.register(r'schools', views.SchoolViewSet, base_name="schools")
router.register(r'issues', views.IssueViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^auth/', views.DivaObtainAuthToken.as_view(), name='auth'),
    url(r'^analysis/', views.SchoolAnalysis.as_view(), name='analysis'),
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
