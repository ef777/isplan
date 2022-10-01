from datetime import datetime
from django.db import models


from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
# Create your models here.
class ExtendUser(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,related_name="extenduser")
    dogum=models.CharField(max_length=30,blank=True, null=True)
    bilgigirisi=models.CharField(max_length=30,blank=True, null=True)
    odemedurumu=models.CharField(max_length=30,blank=True, null=True)
    sehir = models.CharField(max_length=30,blank=True, null=True)
    telefon = models.CharField(max_length=30,blank=True, null=True)
    adisoyad = models.CharField(max_length=30,blank=True, null=True)
    uyetarih=models.CharField(max_length=30,blank=True, null=True)
    lisansbitis=models.CharField(max_length=30,blank=True, null=True)
    lisansbaslangic=models.CharField(max_length=30,blank=True, null=True)
    universite = models.CharField(max_length=30,blank=True, null=True)
    meslek = models.CharField(max_length=30,blank=True, null=True)
    adres = models.CharField(max_length=30,blank=True, null=True)
    sehir = models.CharField(max_length=30,blank=True, null=True)
    ulke = models.CharField(max_length=30,blank=True, null=True)
    #resim = models.ImageField(upload_to='root/myprojectdir/isplan-main/is/static/images/',blank=True,null=True)
    def  __str__(self):
        return self.user.username
   



class lisanstip(models.Model):
    yonetici=models.CharField(max_length=30,blank=True, null=True)
    lisansadi=models.CharField(max_length=30,blank=True, null=True)
    ucret=models.CharField(max_length=30,blank=True, null=True)
    gun=models.CharField(max_length=30,blank=True, null=True)
    def  __int__(self):
        return self.id


class odemetablo(models.Model):
    lisansadi=models.CharField(max_length=30,blank=True, null=True)
    userid=models.CharField(max_length=30,blank=True, null=True)
    odeme=models.CharField(max_length=30,blank=True, null=True)
    odemetarih=models.CharField(max_length=30,blank=True, null=True)
    def  __str__(self):
        return self.userid

class video(models.Model):
        # fields of the model
    tarih = models.CharField(max_length = 30, blank=True, null=True)
    baslik = models.CharField(max_length = 100, blank=True, null=True)
    aciklama =  models.CharField(max_length=200, blank=True, null=True)
    link=models.TextField(max_length=400, blank=True, null=True)

        # renames the instances of the mode        # with their title name
    def __str__(self):
        return self.baslik

class blog(models.Model):
        # fields of the model
    tarih = models.CharField(max_length = 30, blank=True, null=True)
    baslik = models.CharField(max_length = 100, blank=True, null=True)
    aciklama =  models.CharField(max_length=200, blank=True, null=True)
    yazi=models.TextField(max_length=400, blank=True, null=True)
    img = models.ImageField(upload_to = "root/myprojectdir/isplan-main/is/static/images/",blank=True, null=True)

        # renames the instances of the model
        # with their title name
    def __str__(self):
        return self.baslik


class anasayfamodel(models.Model):
        # fields of the model
    img1 = models.ImageField(upload_to = "root/myprojectdir/isplan-main/is/static/images/",blank=True, null=True)
    img2 = models.ImageField(upload_to = "root/myprojectdir/isplan-main/is/static/images/",blank=True, null=True)
    img3 = models.ImageField(upload_to = "root/myprojectdir/isplan-main/is/static/images/",blank=True, null=True)
    img4 = models.ImageField(upload_to = "root/myprojectdir/isplan-main/is/static/images/",blank=True, null=True)
    img5 = models.ImageField(upload_to = "root/myprojectdir/isplan-main/is/static/images/",blank=True, null=True)
 
        # renames the instances of the model
        # with their title name
    def __str__(self):
        return self.title

class nedir(models.Model):# fields of the model
    
    title = models.CharField(max_length = 200,blank=True, null=True)
    description =  models.TextField(max_length=290, blank=True, null=True)
    img = models.ImageField(upload_to = "root/myprojectdir/isplan-main/is/static/images/",blank=True, null=True)
        # renames the instances of the model
        # with their title name
    def __int__(self):
        return self.id

class onanalizmodel(models.Model):
    analizid = models.CharField(max_length=30, blank=True, null=True)
    userid=models.CharField(max_length=30, blank=True, null=True)
    username = models.CharField(max_length=30, blank=True, null=True)
    date = models.CharField(max_length=30, blank=True, null=True)
    title = models.CharField(max_length = 200, blank=True, null=True)
    def __str__(self):
        return self.analizid

class icanalizmodel(models.Model):
    analizid = models.CharField(max_length=30, blank=True, null=True)
    userid=models.CharField(max_length=30, blank=True, null=True)
    username = models.CharField(max_length=30, blank=True, null=True)
    date = models.CharField(max_length=30, blank=True, null=True)
    title = models.CharField(max_length = 200, blank=True, null=True)
    def __str__(self):
        return self.analizid


    
class destek(models.Model):
    baslik=models.CharField(max_length=30, blank=True, null=True)
    userid=models.CharField(max_length=30, blank=True, null=True)
    username = models.CharField(max_length=30, blank=True, null=True)
    mail = models.CharField(max_length = 200, blank=True, null=True)
    telefon = models.CharField(max_length = 200, blank=True, null=True)
    date = models.CharField(max_length=30, blank=True, null=True)
    soru = models.CharField(max_length = 200, blank=True, null=True)
    cevap = models.CharField(max_length = 200, blank=True, null=True)
    def __str__(self):
        return self.analizid
    




class isplaniornekmodel(models.Model):
    username = models.CharField(max_length=30, blank=True, null=True)
    date = models.CharField(max_length=30, blank=True, null=True)
    uyeid = models.CharField(max_length=30, blank=True, null=True)
    isletmeadi =  models.CharField(max_length=30, blank=True, null=True)
    isletmeyetkiliadsoyad =  models.CharField(max_length=30, blank=True, null=True)
    vergitcno =   models.CharField(max_length=30, blank=True, null=True)
    projeninadi =   models.CharField(max_length=30, blank=True, null=True)
    projeninkisatanimi =   models.CharField(max_length=30, blank=True, null=True)
    toplamprojesuresi =   models.CharField(max_length=30, blank=True, null=True)
    toplamprojebutcesi =   models.CharField(max_length=30, blank=True, null=True)
    isletmeprojeyetkilisi =   models.CharField(max_length=30, blank=True, null=True)
    eposta =   models.CharField(max_length=30, blank=True, null=True)
    telfax =   models.CharField(max_length=30, blank=True, null=True)
    isletmestatu =   models.CharField(max_length=30, blank=True, null=True)
    isletmeadlari =   models.CharField(max_length=30, blank=True, null=True)
    ortaksayisi =   models.CharField(max_length=30, blank=True, null=True)
    vergidairesi =   models.CharField(max_length=30, blank=True, null=True)
    verginumarasi =   models.CharField(max_length=30, blank=True, null=True)
    isletmeyetkilisi =   models.CharField(max_length=30, blank=True, null=True)
    isletmeprojeeyetkilisi =   models.CharField(max_length=30, blank=True, null=True)
    sgkisyerisicilno =   models.CharField(max_length=30, blank=True, null=True)
    ticaretisyerisicilno =   models.CharField(max_length=30, blank=True, null=True)
    ticaretsicilgazetetarihno =   models.CharField(max_length=30, blank=True, null=True)
    kurulusyili =   models.CharField(max_length=30, blank=True, null=True)
    faaliyetebaslamayili =   models.CharField(max_length=30, blank=True, null=True)
    toplampersonelsayisi =   models.CharField(max_length=30, blank=True, null=True)
    beyazyaka =   models.CharField(max_length=30, blank=True, null=True)
    maviyaka =   models.CharField(max_length=30, blank=True, null=True)
    baglibulunduguoda =   models.CharField(max_length=30, blank=True, null=True)
    bulunduguyer =   models.CharField(max_length=30, blank=True, null=True)
    adres =   models.CharField(max_length=30, blank=True, null=True)
    il =   models.CharField(max_length=30, blank=True, null=True)
    ilce =   models.CharField(max_length=30, blank=True, null=True)
    postakodu =   models.CharField(max_length=30, blank=True, null=True)
    telefon =   models.CharField(max_length=30, blank=True, null=True)
    epostaadresi =   models.CharField(max_length=30, blank=True, null=True)
    webadresi =   models.CharField(max_length=30, blank=True, null=True)
    desteklerdenyararlanma =   models.CharField(max_length=30, blank=True, null=True)
    checkbox0 =   models.CharField(max_length=30, blank=True, null=True)
    checkbox1 =   models.CharField(max_length=30, blank=True, null=True)
    checkbox2 =   models.CharField(max_length=30, blank=True, null=True)
    checkbox3 =   models.CharField(max_length=30, blank=True, null=True)
    checkbox4 =   models.CharField(max_length=30, blank=True, null=True)
    checkbox5 =   models.CharField(max_length=30, blank=True, null=True)
    checkbox6 =   models.CharField(max_length=30, blank=True, null=True)
    checkbox7 =   models.CharField(max_length=30, blank=True, null=True)
    checkbox8 =   models.CharField(max_length=30, blank=True, null=True)
    checkbox9 =   models.CharField(max_length=30, blank=True, null=True)
    customCheck1 =   models.CharField(max_length=30, blank=True, null=True)
    customCheck2 =   models.CharField(max_length=30, blank=True, null=True)
    customCheck3 =   models.CharField(max_length=30, blank=True, null=True)
    customCheck4 =   models.CharField(max_length=30, blank=True, null=True)
    customCheck5 =   models.CharField(max_length=30, blank=True, null=True)
    customCheck6 =   models.CharField(max_length=30, blank=True, null=True)
    customCheck7 =   models.CharField(max_length=30, blank=True, null=True)
    customCheck8 =   models.CharField(max_length=30, blank=True, null=True)
    nacekodu=   models.CharField(max_length=30, blank=True, null=True)
    urungruplari =   models.CharField(max_length=30, blank=True, null=True)
    isletmeortagiadisoyadi =   models.CharField(max_length=30, blank=True, null=True)
    tckimlikvergino =   models.CharField(max_length=30, blank=True, null=True)
    isletmehissepayi =   models.CharField(max_length=30, blank=True, null=True)
    isletmetarihcesi =   models.CharField(max_length=30, blank=True, null=True)
    projeninkonusu =   models.CharField(max_length=30, blank=True, null=True)
    projeninamaci =   models.CharField(max_length=30, blank=True, null=True)
    projebenzerfaaliyet =   models.CharField(max_length=30, blank=True, null=True)
    uzundonemhedef =   models.CharField(max_length=30, blank=True, null=True)
    projepazarnitelikleri =   models.CharField(max_length=30, blank=True, null=True)
    projebeklenenetkiler =   models.CharField(max_length=30, blank=True, null=True)
    rekabetedilebilirligi =   models.CharField(max_length=30, blank=True, null=True)
    surdurulebilirlik =   models.CharField(max_length=30, blank=True, null=True)
    hukikihusular =   models.CharField(max_length=30, blank=True, null=True)
    risklervarsayilan =   models.CharField(max_length=30, blank=True, null=True)
    digerhususlar =   models.CharField(max_length=30, blank=True, null=True)
    projeciktilari =   models.CharField(max_length=30, blank=True, null=True)
    projeninyonetimi =   models.CharField(max_length=30, blank=True, null=True)
    finansman =   models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):

        return self.username
   
   



class isplaniolusturmodel(models.Model):
    tarih = models.CharField(max_length=30, blank=True, null=True)
    username = models.CharField(max_length=30, blank=True, null=True)
    date = models.CharField(max_length=30, blank=True, null=True)
    id = models.AutoField(primary_key=True)
    uyeid = models.CharField(max_length=30, blank=True, null=True)
    isletmeadi =  models.CharField(max_length=30, blank=True, null=True)
    isletmeyetkiliadsoyad =  models.CharField(max_length=30, blank=True, null=True)
    vergitcno =   models.CharField(max_length=30, blank=True, null=True)
    projeninadi =   models.CharField(max_length=30, blank=True, null=True)
    projeninkisatanimi =   models.CharField(max_length=30, blank=True, null=True)
    toplamprojesuresi =   models.CharField(max_length=30, blank=True, null=True)
    toplamprojebutcesi =   models.CharField(max_length=30, blank=True, null=True)
    isletmeprojeyetkilisi =   models.CharField(max_length=30, blank=True, null=True)
    eposta =   models.CharField(max_length=30, blank=True, null=True)
    telfax =   models.CharField(max_length=30, blank=True, null=True)
    isletmestatu =   models.CharField(max_length=30, blank=True, null=True)
    isletmeadlari =   models.CharField(max_length=30, blank=True, null=True)
    ortaksayisi =   models.CharField(max_length=30, blank=True, null=True)
    vergidairesi =   models.CharField(max_length=30, blank=True, null=True)
    verginumarasi =   models.CharField(max_length=30, blank=True, null=True)
    isletmeyetkilisi =   models.CharField(max_length=30, blank=True, null=True)
    isletmeprojeeyetkilisi =   models.CharField(max_length=30, blank=True, null=True)
    sgkisyerisicilno =   models.CharField(max_length=30, blank=True, null=True)
    ticaretisyerisicilno =   models.CharField(max_length=30, blank=True, null=True)
    ticaretsicilgazetetarihno =   models.CharField(max_length=30, blank=True, null=True)
    kurulusyili =   models.CharField(max_length=30, blank=True, null=True)
    faaliyetebaslamayili =   models.CharField(max_length=30, blank=True, null=True)
    toplampersonelsayisi =   models.CharField(max_length=30, blank=True, null=True)
    beyazyaka =   models.CharField(max_length=30, blank=True, null=True)
    maviyaka =   models.CharField(max_length=30, blank=True, null=True)
    baglibulunduguoda =   models.CharField(max_length=30, blank=True, null=True)
    bulunduguyer =   models.CharField(max_length=30, blank=True, null=True)
    adres =   models.CharField(max_length=30, blank=True, null=True)
    il =   models.CharField(max_length=30, blank=True, null=True)
    ilce =   models.CharField(max_length=30, blank=True, null=True)
    postakodu =   models.CharField(max_length=30, blank=True, null=True)
    telefon =   models.CharField(max_length=30, blank=True, null=True)
    epostaadresi =   models.CharField(max_length=30, blank=True, null=True)
    webadresi =   models.CharField(max_length=30, blank=True, null=True)
    desteklerdenyararlanma =   models.CharField(max_length=30, blank=True, null=True)
    checkbox0 =   models.CharField(max_length=30, blank=True, null=True)
    checkbox1 =   models.CharField(max_length=30, blank=True, null=True)
    checkbox2 =   models.CharField(max_length=30, blank=True, null=True)
    checkbox3 =   models.CharField(max_length=30, blank=True, null=True)
    checkbox4 =   models.CharField(max_length=30, blank=True, null=True)
    checkbox5 =   models.CharField(max_length=30, blank=True, null=True)
    checkbox6 =   models.CharField(max_length=30, blank=True, null=True)
    checkbox7 =   models.CharField(max_length=30, blank=True, null=True)
    checkbox8 =   models.CharField(max_length=30, blank=True, null=True)
    checkbox9 =   models.CharField(max_length=30, blank=True, null=True)
    customCheck1 =   models.CharField(max_length=30, blank=True, null=True)
    customCheck2 =   models.CharField(max_length=30, blank=True, null=True)
    customCheck3 =   models.CharField(max_length=30, blank=True, null=True)
    customCheck4 =   models.CharField(max_length=30, blank=True, null=True)
    customCheck5 =   models.CharField(max_length=30, blank=True, null=True)
    customCheck6 =   models.CharField(max_length=30, blank=True, null=True)
    customCheck7 =   models.CharField(max_length=30, blank=True, null=True)
    customCheck8 =   models.CharField(max_length=30, blank=True, null=True)
    nacekodu=   models.CharField(max_length=30, blank=True, null=True)
    urungruplari =   models.CharField(max_length=30, blank=True, null=True)
    isletmeortagiadisoyadi =   models.CharField(max_length=30, blank=True, null=True)
    tckimlikvergino =   models.CharField(max_length=30, blank=True, null=True)
    isletmehissepayi =   models.CharField(max_length=30, blank=True, null=True)
    isletmetarihcesi =   models.CharField(max_length=30, blank=True, null=True)
    projeninkonusu =   models.CharField(max_length=30, blank=True, null=True)
    projeninamaci =   models.CharField(max_length=30, blank=True, null=True)
    projebenzerfaaliyet =   models.CharField(max_length=30, blank=True, null=True)
    uzundonemhedef =   models.CharField(max_length=30, blank=True, null=True)
    projepazarnitelikleri =   models.CharField(max_length=30, blank=True, null=True)
    projebeklenenetkiler =   models.CharField(max_length=30, blank=True, null=True)
    rekabetedilebilirligi =   models.CharField(max_length=30, blank=True, null=True)
    surdurulebilirlik =   models.CharField(max_length=30, blank=True, null=True)
    hukikihusular =   models.CharField(max_length=30, blank=True, null=True)
    risklervarsayilan =   models.CharField(max_length=30, blank=True, null=True)
    digerhususlar =   models.CharField(max_length=30, blank=True, null=True)
    projeciktilari =   models.CharField(max_length=30, blank=True, null=True)
    projeninyonetimi =   models.CharField(max_length=30, blank=True, null=True)
    finansman =   models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):

        return self.id
   
   
