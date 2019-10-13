from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from rest_framework import renderers
from rest_framework_simplejwt import views as jwt_views

from users.views import *

router = DefaultRouter()

router.register(r'^user', UserViewset)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    url('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh')
]



