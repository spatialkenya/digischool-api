from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.authtoken import views as drf_views


from . import views

router = routers.DefaultRouter(trailing_slash=True)
router.register(r'counties', views.CountyViewSet)
router.register(r'schools', views.SchoolViewSet)
router.register(r'issues', views.IssueViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^auth/', drf_views.obtain_auth_token, name='auth'),
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
