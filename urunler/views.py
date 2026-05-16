from django.shortcuts import render, get_object_or_404, redirect
from .models import Urun, Kategori, Siparis

def anasayfa(request):
    urunler = Urun.objects.all()
    kategoriler = Kategori.objects.all()
    return render(request, 'urunler/anasayfa.html', {
        'urunler': urunler,
        'kategoriler': kategoriler
    })

def urun_detay(request, pk):
    urun = get_object_or_404(Urun, pk=pk)
    return render(request, 'urunler/urun_detay.html', {'urun': urun})

def siparis_ver(request, pk):
    urun = get_object_or_404(Urun, pk=pk)
    if request.method == 'POST':
        ad = request.POST.get('ad')
        email = request.POST.get('email')
        miktar = int(request.POST.get('miktar', 1))
        toplam = urun.fiyat * miktar
        Siparis.objects.create(
            urun=urun,
            musteri_ad=ad,
            musteri_email=email,
            miktar=miktar,
            toplam_fiyat=toplam
        )
        return redirect('siparis_basarili')
    return render(request, 'urunler/siparis.html', {'urun': urun})

def siparis_basarili(request):
    return render(request, 'urunler/basarili.html')