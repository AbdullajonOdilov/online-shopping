from django.shortcuts import render, redirect
from django.views import View

from userapp.models import *

from buyurtmaapp.models import *

from buyurtmaapp.models import Savat

from asosiyapp.models import Mahsulot
from userapp.models import Profil


class TanlanganView(View):
    def get(self,request):
        # if request.user.is_authenticated:
        data = {
            'tanlanganlar':Profil.objects.filter(user=request.user)
        }
        return render(request,'page-profile-wishlist.html',data)

class SavatView(View):
    def get(self,request):
        sv = Savat.objects.filter(profil__user=request.user)
        umumiy = 0
        for s in sv:
            umumiy += s.umumiy
        ch = 0
        for s in sv:
            ch += int(s.mahsulot.chegirma*s.mahsulot.narx%0.01*s.miqdor)
        context = {
            'savats':sv,
            'umumiy':umumiy,
            'chegirma':ch,
            'yakuniy':umumiy-ch

        }
        return render(request,'page-shopping-cart.html',context)
def savat_qoshish(request, pk):
    savat = Savat.objects.get(id = pk)
    if savat.miqdor != 10:
        savat.miqdor = savat.miqdor + 1
        savat.umumiy = int(savat.miqdor) * int(savat.mahsulot.narx)
    savat.save()
    return redirect('/profile/savat/')

def savat_kamaytirish(request,pk):
    savat = Savat.objects.get(id=pk)
    if savat.miqdor != 1:
        savat.miqdor = int(savat.miqdor) - 1
        savat.umumiy = int(savat.miqdor) * int(savat.mahsulot.narx)
    savat.save()
    return redirect('/profile/savat/')

class SavatAddView(View):
    def get(self, request, pk):
        pr = Profil.objects.get(user=request.user)
        m = Mahsulot.objects.get(id=pk)
        sv = Savat.objects.filter(mahsulot=m, profil=pr)
        if len(sv) > 0:
            return redirect('/profile/savat/')
        Savat.objects.create(
            mahsulot = m,
            profil = pr,
            umumiy = m.narx
        )
        return redirect('/profile/savat/')