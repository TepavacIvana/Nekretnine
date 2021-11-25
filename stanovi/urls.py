from django.urls import path
from .views import *


urlpatterns = [
    path('korisnik-stan/', KorisnikStanList.as_view()),
    path('korisnik-stan/<str:username>', KorisnikStanDetail.as_view()),
    path('stanovi/', StanList.as_view()),
    path('stanovi/<int:pk>', StanDetail.as_view()),
    path('stan-by/', StanBy.as_view({'get': 'list'})),
]
