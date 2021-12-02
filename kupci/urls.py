from django.urls import path
from .views import KupacPonudeList, KupacByName, KupacCreate, KupacList, KupacIdPonude


urlpatterns = [
    path('kupci-ponude/', KupacPonudeList.as_view()),
    path('kupci-ponude/<int:id_kupca>/', KupacIdPonude.as_view()),
    path('kupci/', KupacCreate.as_view()),
    path('kupci-list/', KupacList.as_view()),
    path('kupci/<str:full_or_company_name>/', KupacByName.as_view()),
]
