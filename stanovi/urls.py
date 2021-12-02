from django.urls import path
from .views import (
    ProdavacStanList,
    ProdavacStanDetail,
    StanCreate,
    StanList,
    StanDetail,
    StanBy,
    StanPonudeList,
    StanIdPonude,
)

urlpatterns = [
    path('prodavac-stan/', ProdavacStanList.as_view()),
    path('prodavac-stan/<str:username>', ProdavacStanDetail.as_view()),
    path('stanovi/', StanCreate.as_view()),
    path('stanovi-list/', StanList.as_view()),
    path('stanovi/<int:pk>', StanDetail.as_view()),
    path('stanovi-by/', StanBy.as_view({'get': 'list'})),
    path('stanovi-ponude/', StanPonudeList.as_view()),
    path('stanovi-ponude/<int:id_stana>/', StanIdPonude.as_view()),
]
