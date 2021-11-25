from rest_framework import routers
from django.urls import path, include

from .views import AuthViewSet, KorisnikList, KorisnikDetail

router = routers.DefaultRouter(trailing_slash=False)
router.register('api/auth', AuthViewSet, basename='auth')

urlpatterns = [
    path('', include(router.urls)),
    # path('api/auth/register', AuthViewSet),
    # path('api/auth/login', AuthViewSet),
    # path('api/auth/logout', AuthViewSet),
    path('api/auth/korisnici', KorisnikList.as_view()),
    path('api/auth/korisnici/<str:username>/', KorisnikDetail.as_view()),
]
