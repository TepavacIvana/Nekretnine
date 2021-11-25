from django.urls import path
from .views import *


urlpatterns = [
    path('kupci', KupacList.as_view()),
    path('kupci/<str:full_or_company_name>/', KupacByName.as_view()),
    path('kupci-stan/', KupacStanList.as_view()),
    path('kupci-stan/<str:full_or_company_name>/', KupacStanDetail.as_view()),
]
