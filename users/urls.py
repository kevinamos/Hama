from django.conf.urls import url, include

from rest_framework.routers import DefaultRouter
from rest_framework import renderers

from users.views import *

router = DefaultRouter()

router.register(r'^user', UserViewset)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]