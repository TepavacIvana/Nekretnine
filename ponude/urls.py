from django.urls import path
from .views import (
    PonudaCreate,
    PonudaList,
    PonudaDetail,
    PonudaBy,
)

urlpatterns = [
    path('ponude/', PonudaCreate.as_view()),
    path('ponude-list/', PonudaList.as_view()),
    path('ponude/<int:pk>', PonudaDetail.as_view()),
    path('ponude-by/', PonudaBy.as_view({'get': 'list'})),
]
