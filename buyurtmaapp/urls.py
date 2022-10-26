from django.urls import path

from asosiyapp.views import *

from buyurtmaapp.views import *

from buyurtmaapp.views import *

urlpatterns = [
    path('tanlangan/',TanlanganView.as_view(),name="tanlangan"),
    path('savat/',SavatView.as_view(),name='savat'),
    path('savat_q/<int:pk>/',savat_qoshish),
    path('savat_k/<int:pk>/',savat_kamaytirish),
    path('savat_add/<int:pk>/',SavatAddView.as_view()),


]