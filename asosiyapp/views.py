from django.shortcuts import render,redirect
from django.views import View
from django.db.models import Count
from .models import *
# Create your views here.

class Home2View(View):
    def get(self, request):
        context = {
            'bolimlar': Bolim.objects.all()[:6]
        }
        return render(request, 'page-index-2.html', context)


class HomeView(View):
    def get(self, request):
        data = {
            'bolimlar': Bolim.objects.all()[:6],
            'davomlari': Bolim.objects.all()[6:]
        }
        return render(request, 'page-index.html', data)

class BolimlarView(View):
    def get(self,request):
        context = {
            'bolimlar': Bolim.objects.all()
        }
        return render(request, 'page-category.html', context)

class BolimIchkiView(View):
    def get(self, request, nom):
        context = {
            'ichki': Ichki.objects.filter(nom=nom),
        }
        return render(request, 'ichki.html', context)


class GridView(View):
    def get(self,request,pk):
        info = {
            'grids':Mahsulot.objects.filter(ichki__id = pk)
        }
        return render(request, 'page-listing-grid.html',info)

class PageDetailView(View):
    def get(self, request,pk):
        context = {
            'mahsulotlar':Mahsulot.objects.get(id=pk)
        }
        return render(request, 'page-detail-product.html',context)
class TanlanganView(View):
    def get(self,request):
        return render(request,'page-profile-wishlist.html')

class SavatView(View):
    def get(self,request):
        return render(request,'page-shopping-cart.html')
class BuyurmaView(View):
    def get(self,request):
        return render(request,'page-profile-orders.html')
