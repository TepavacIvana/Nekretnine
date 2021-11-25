from django.urls import path
from .views import *


urlpatterns = [
    path('ponude/', PonudaList.as_view()),
    path('ponude/<int:pk>', PonudaDetail.as_view()),
    path('ponude-by/', PonudaBy.as_view({'get': 'list'})),
]
