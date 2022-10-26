
from django.urls import path
from .views import *
from userapp.views import *
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('bolimlar/', BolimlarView.as_view(), name='bolimlar'),
    path('bolim/<str:nom>/', BolimIchkiView.as_view(), name='bolim_ichki'),
    path('listing/<int:pk>/',GridView.as_view(),name = 'grid'),



    path('detail/<int:pk>/',PageDetailView.as_view(),name = 'detail'),

]
