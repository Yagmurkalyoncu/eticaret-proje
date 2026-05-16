from django.db import models

class Kategori(models.Model):
    ad = models.CharField(max_length=100)
    
    def __str__(self):
        return self.ad

class Urun(models.Model):
    ad = models.CharField(max_length=200)
    aciklama = models.TextField()
    fiyat = models.DecimalField(max_digits=10, decimal_places=2)
    stok = models.IntegerField(default=0)
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE)
    resim = models.ImageField(upload_to='urunler/', blank=True, null=True)
    tarih = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.ad

class Siparis(models.Model):
    urun = models.ForeignKey(Urun, on_delete=models.CASCADE)
    musteri_ad = models.CharField(max_length=100)
    musteri_email = models.EmailField()
    miktar = models.IntegerField(default=1)
    toplam_fiyat = models.DecimalField(max_digits=10, decimal_places=2)
    tarih = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.musteri_ad} - {self.urun.ad}"