from calendar import EPOCH
from dataclasses import dataclass
from datetime import datetime ,timedelta,date
from dateutil.relativedelta import relativedelta
from email import message
from re import M
import time
import traceback
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import  render, redirect
from django.contrib.auth import login
from django.contrib import messages
from django.shortcuts import  render, redirect
from .models import ExtendUser, blog, destek, isplaniolusturmodel, isplaniornekmodel, lisanstip, nedir, odemetablo, onanalizmodel, video

from .forms import NewUserForm
from django.contrib.auth import login, authenticate,logout #add this
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm #add this
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render
from django.shortcuts import render
import iyzipay
import json
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
import requests
from django.contrib import messages
import pprint
# Create your views here.
mainurl = "http://194.87.17.120:80/"


def index(request):
    user=request.user
    yetki=request.user.is_authenticated
    if yetki == True:
        print (user.id) 
        return redirect(mainurl+"anasayfa/", {'url': mainurl})
    else :
        return redirect(mainurl+"giris/", {'url': mainurl})
def anasayfa(request):
    user=request.user
    yetki=request.user.is_authenticated
    blog1=blog.objects.all()
    if yetki == True:
        print (user.id) 
        user=request.user
        ex =ExtendUser.objects.get(user=user.id)
        if(ex.odemedurumu=="0"):
            return redirect(mainurl+"odemelerim/", {'url': mainurl})
        username=request.user.username
        items = isplaniolusturmodel.objects.filter(username = username) 
        return render(request, 'pages/anasayfa.html', {'user': user,'ex': ex,'items':items ,'blog':blog1, 'url': mainurl})    
    else :
        return redirect(mainurl+"giris/")
   
def isplanimnedir(request):
    b = nedir.objects.all()
    return render(request, 'pages/isplanimnedir.html',{'veri':b[0],'url': mainurl})
def isplanolustur(request):
    user=request.user
    yetki=request.user.is_authenticated
    if yetki == True:
        print (user.id) #the us
        ex =ExtendUser.objects.get(user=user.id)
        if(ex.odemedurumu=="0"):
            return redirect(mainurl+"odemelerim/")
        return render(request,'pages/isplaniolustur.html', {'url': mainurl})
    else :
        return redirect(mainurl+"giris/")

def isplanisil (request,id):
    user=request.user
    yetki=request.user.is_authenticated
    if yetki == True:
        print (user.id) #the us
        id2=id
        isplaniolusturmodel.objects.filter(id=id2).delete()
        #messages.success(request,"Silindi")
        return redirect(mainurl+"projeler/")
    else :
        return redirect(mainurl+"giris/")
      

def isplaniduzenle (request,id):
    user=request.user
    yetki=request.user.is_authenticated
    if yetki == True:
        ex =ExtendUser.objects.get(user=user.id)
        if(ex.odemedurumu=="0"):
            return redirect(mainurl+"odemelerim/")
        id2=id
        obj = isplaniolusturmodel.objects.get(id=id2)
        if(user.username!=obj.username):
            return redirect(mainurl+"anasayfa/")
        return render(request, 'pages/isplaniduzenle.html', {'obj': obj,'id':id2,'url': mainurl})
    else :
        return redirect(mainurl+"giris/")
    
   
    
   
def isplaniduzenlekaydet (request):
    user=request.user
    yetki=request.user.is_authenticated
    if yetki == True:
        print (user.id) #the us
        if request.method != "POST":
            return redirect(mainurl+"isplaniolustur/")
        else:
           
            urlid=request.POST.get("urlid")
            obj = isplaniolusturmodel.objects.get(id=urlid)
            obj.delete()
            username=request.user.username
            date= datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            isletmeyetkiliadsoyad=request.POST.get("isletmeyetkiliadsoyad")
            vergitcno=request.POST.get("vergitcno")
            isletmeadi=request.POST.get("isletmeadi")
            projeninadi=request.POST.get("projeninadi")
            projeninkisatanimi=request.POST.get("projeninkisatanimi")
            toplamprojesuresi=request.POST.get("toplamprojesuresi")
            toplamprojebutcesi=request.POST.get("toplamprojebutcesi")
            isletmeprojeyetkilisi=request.POST.get("isletmeprojeyetkilisi")
            eposta=request.POST.get("eposta")
            telfax=request.POST.get("telfax")
            #sayfa1 bitti
          
            isletmestatu=request.POST.get("radioInline")
            isletmeadlari=request.POST.get("isletmeadlari")
            ortaksayisi=request.POST.get("ortaksayisi")
            vergidairesi=request.POST.get("vergidairesi")
            verginumarasi=request.POST.get("verginumarasi")
            isletmeyetkilisi=request.POST.get("isletmeyetkilisi")
            isletmeprojeeyetkilisi=request.POST.get("isletmeprojeeyetkilisi")
            sgkisyerisicilno=request.POST.get("sgkisyerisicilno")
            
            ticaretisyerisicilno=request.POST.get("ticaretisyerisicilno")
            ticaretsicilgazetetarihno=request.POST.get("ticaretsicilgazetetarihno")
            kurulusyili=request.POST.get("kurulusyili")
            faaliyetebaslamayili=request.POST.get("faaliyetebaslamayili")
            toplampersonelsayisi=request.POST.get("toplampersonelsayisi")
            beyazyaka=request.POST.get("beyazyaka")
            maviyaka=request.POST.get("maviyaka")
            baglibulunduguoda=request.POST.get("baglibulunduguoda")   
            bulunduguyer=request.POST.get("bulunduguyer")
            adres=request.POST.get("adres")
            il=request.POST.get("il")
            ilce=request.POST.get("ilce")
            postakodu=request.POST.get("postakodu")
            telefon=request.POST.get("telefon")
            epostaadresi=request.POST.get("epostaadresi")
            webadresi=request.POST.get("webadresi")
            desteklerdenyararlanma=request.POST.get("desteklerdenyararlanma")
            checkbox0=request.POST.get("checkbox0")
            #id
            checkbox1=request.POST.get("checkbox1")
          
            checkbox2=request.POST.get("checkbox2")
            checkbox3=request.POST.get("checkbox3")
            checkbox4=request.POST.get("checkbox4")
            checkbox5=request.POST.get("checkbox5")
            checkbox6=request.POST.get("checkbox6")
            checkbox7=request.POST.get("checkbox7")
            checkbox8=request.POST.get("checkbox8")
            checkbox9=request.POST.get("checkbox9")
            customCheck1=request.POST.get("customCheck1")
            customCheck2=request.POST.get("customCheck2")
            customCheck3=request.POST.get("customCheck3")
            customCheck4=request.POST.get("customCheck4")
            customCheck5=request.POST.get("customCheck5")
            customCheck6=request.POST.get("customCheck6")
            customCheck7=request.POST.get("customCheck7")
            customCheck8=request.POST.get("customCheck8")
            nacekodu=request.POST.get("nacekodu")
            
            urungruplari=request.POST.get("urungruplari")
            isletmeortagiadisoyadi=request.POST.get("isletmeortagiadisoyadi")
            tckimlikvergino=request.POST.get("tckimlikvergino")
            isletmehissepayi=request.POST.get("isletmehissepayi")
            isletmetarihcesi=request.POST.get("isletmetarihcesi")
            projeninkonusu=request.POST.get("projeninkonusu")
            projeninamaci=request.POST.get("projeninamaci")
            projebenzerfaaliyet=request.POST.get("projebenzerfaaliyet")
            uzundonemhedef=request.POST.get("uzundonemhedef")
            projepazarnitelikleri=request.POST.get("projepazarnitelikleri")
            projebeklenenetkiler=request.POST.get("projebeklenenetkiler")
            rekabetedilebilirligi=request.POST.get("rekabetedilebilirligi")
            surdurulebilirlik=request.POST.get("surdurulebilirlik")
            hukikihusular=request.POST.get("hukikihusular")
            risklervarsayilan=request.POST.get("risklervarsayilan")
            digerhususlar=request.POST.get("digerhususlar")
            projeciktilari=request.POST.get("projeciktilari")
            projeninyonetimi=request.POST.get("projeninyonetimi")
            finansman=request.POST.get("finansman")
            print("buraya kadar tamam1")
            try:
                isplaniolusturmodel.objects.create(vergitcno=vergitcno,isletmeadi=isletmeadi,isletmeyetkiliadsoyad=isletmeyetkiliadsoyad,finansman=finansman,
                        projeninadi=projeninadi,projeninkisatanimi=projeninkisatanimi,toplamprojesuresi=toplamprojesuresi,toplamprojebutcesi=toplamprojebutcesi,
                          isletmeprojeyetkilisi=isletmeprojeyetkilisi,eposta=eposta,telfax=telfax,
                isletmestatu=isletmestatu,isletmeadlari=isletmeadlari,ortaksayisi=ortaksayisi,
                vergidairesi=vergidairesi,verginumarasi=verginumarasi,isletmeyetkilisi=isletmeyetkilisi,
                isletmeprojeeyetkilisi=isletmeprojeeyetkilisi,sgkisyerisicilno=sgkisyerisicilno,ticaretisyerisicilno=ticaretisyerisicilno,ticaretsicilgazetetarihno=ticaretsicilgazetetarihno,
                kurulusyili=kurulusyili,faaliyetebaslamayili=faaliyetebaslamayili,toplampersonelsayisi=toplampersonelsayisi,
                beyazyaka=beyazyaka,maviyaka=maviyaka,baglibulunduguoda=baglibulunduguoda,bulunduguyer=bulunduguyer,
                adres=adres,il=il,ilce=ilce,postakodu=postakodu,telefon=telefon,epostaadresi=epostaadresi,webadresi=webadresi,
                desteklerdenyararlanma=desteklerdenyararlanma,nacekodu=nacekodu,urungruplari=urungruplari,isletmeortagiadisoyadi=isletmeortagiadisoyadi,
                tckimlikvergino=tckimlikvergino,isletmehissepayi=isletmehissepayi,isletmetarihcesi=isletmetarihcesi,
                projeninkonusu=projeninkonusu,projeninamaci=projeninamaci,projebenzerfaaliyet=projebenzerfaaliyet,
                uzundonemhedef=uzundonemhedef,projepazarnitelikleri=projepazarnitelikleri,
                projebeklenenetkiler=projebeklenenetkiler,rekabetedilebilirligi=rekabetedilebilirligi,
                surdurulebilirlik=surdurulebilirlik,hukikihusular=hukikihusular,risklervarsayilan=risklervarsayilan,
                digerhususlar=digerhususlar,projeciktilari=projeciktilari,projeninyonetimi=projeninyonetimi,
                   checkbox0=checkbox0,checkbox1=checkbox1,
                checkbox3=checkbox3,checkbox2=checkbox2,
                checkbox5=checkbox5,checkbox4=checkbox4,
                checkbox7=checkbox7,checkbox6=checkbox6,
                checkbox9=checkbox9, checkbox8=checkbox8,
                customCheck1=customCheck1,customCheck2=customCheck2,
                customCheck6=customCheck6,customCheck3=customCheck3,
                customCheck7=customCheck7,customCheck4=customCheck4,
                customCheck8=customCheck8,customCheck5=customCheck5,username=username,date=date)  

                #messages.success(request,"Form Başarılı")
                return redirect(mainurl+"projeler/")
            
            except Exception as e:
      
                message = traceback.format_exc()
                print(message)
                #messages.error(request,"Form Başarısız")
                return redirect(mainurl+"isplaniolustur/")
          
            
            
    else :
        return redirect(mainurl+"giris/")
      
            

 


def isplaniolusturkaydet (request):
    user=request.user
    yetki=request.user.is_authenticated
    if yetki == True:
        print (user.id) #the us
        if request.method != "POST":
            return redirect(mainurl+"isplaniolustur/")
        else:
            username=request.user.username
            date= datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            isletmeyetkiliadsoyad=request.POST.get("isletmeyetkiliadsoyad")
            vergitcno=request.POST.get("vergitcno")
            isletmeadi=request.POST.get("isletmeadi")
            projeninadi=request.POST.get("projeninadi")
            projeninkisatanimi=request.POST.get("projeninkisatanimi")
            toplamprojesuresi=request.POST.get("toplamprojesuresi")
            toplamprojebutcesi=request.POST.get("toplamprojebutcesi")
            isletmeprojeyetkilisi=request.POST.get("isletmeprojeyetkilisi")
            eposta=request.POST.get("eposta")
            telfax=request.POST.get("telfax")
            #sayfa1 bitti
          
            isletmestatu=request.POST.get("radioInline")
            isletmeadlari=request.POST.get("isletmeadlari")
            ortaksayisi=request.POST.get("ortaksayisi")
            vergidairesi=request.POST.get("vergidairesi")
            verginumarasi=request.POST.get("verginumarasi")
            isletmeyetkilisi=request.POST.get("isletmeyetkilisi")
            isletmeprojeeyetkilisi=request.POST.get("isletmeprojeeyetkilisi")
            sgkisyerisicilno=request.POST.get("sgkisyerisicilno")
            
            ticaretisyerisicilno=request.POST.get("ticaretisyerisicilno")
            ticaretsicilgazetetarihno=request.POST.get("ticaretsicilgazetetarihno")
            kurulusyili=request.POST.get("kurulusyili")
            faaliyetebaslamayili=request.POST.get("faaliyetebaslamayili")
            toplampersonelsayisi=request.POST.get("toplampersonelsayisi")
            beyazyaka=request.POST.get("beyazyaka")
            maviyaka=request.POST.get("maviyaka")
            baglibulunduguoda=request.POST.get("baglibulunduguoda")   
            bulunduguyer=request.POST.get("bulunduguyer")
            adres=request.POST.get("adres")
            il=request.POST.get("il")
            ilce=request.POST.get("ilce")
            postakodu=request.POST.get("postakodu")
            telefon=request.POST.get("telefon")
            epostaadresi=request.POST.get("epostaadresi")
            webadresi=request.POST.get("webadresi")
            desteklerdenyararlanma=request.POST.get("desteklerdenyararlanma")
            checkbox0=request.POST.get("checkbox0")
            #id
            checkbox1=request.POST.get("checkbox1")
          
      
      
            checkbox2=request.POST.get("checkbox2")
            checkbox3=request.POST.get("checkbox3")
            checkbox4=request.POST.get("checkbox4")
            checkbox5=request.POST.get("checkbox5")
            checkbox6=request.POST.get("checkbox6")
            checkbox7=request.POST.get("checkbox7")
            checkbox8=request.POST.get("checkbox8")
            checkbox9=request.POST.get("checkbox9")
            customCheck1=request.POST.get("customCheck1")
            customCheck2=request.POST.get("customCheck2")
            customCheck3=request.POST.get("customCheck3")
            customCheck4=request.POST.get("customCheck4")
            customCheck5=request.POST.get("customCheck5")
            customCheck6=request.POST.get("customCheck6")
            customCheck7=request.POST.get("customCheck7")
            customCheck8=request.POST.get("customCheck8")
            nacekodu=request.POST.get("nacekodu")
            
            urungruplari=request.POST.get("urungruplari")
            isletmeortagiadisoyadi=request.POST.get("isletmeortagiadisoyadi")
            tckimlikvergino=request.POST.get("tckimlikvergino")
            isletmehissepayi=request.POST.get("isletmehissepayi")
            isletmetarihcesi=request.POST.get("isletmetarihcesi")
            projeninkonusu=request.POST.get("projeninkonusu")
            projeninamaci=request.POST.get("projeninamaci")
            projebenzerfaaliyet=request.POST.get("projebenzerfaaliyet")
            uzundonemhedef=request.POST.get("uzundonemhedef")
            projepazarnitelikleri=request.POST.get("projepazarnitelikleri")
            projebeklenenetkiler=request.POST.get("projebeklenenetkiler")
            rekabetedilebilirligi=request.POST.get("rekabetedilebilirligi")
            surdurulebilirlik=request.POST.get("surdurulebilirlik")
            hukikihusular=request.POST.get("hukikihusular")
            risklervarsayilan=request.POST.get("risklervarsayilan")
            digerhususlar=request.POST.get("digerhususlar")
            projeciktilari=request.POST.get("projeciktilari")
            projeninyonetimi=request.POST.get("projeninyonetimi")
            finansman=request.POST.get("finansman")
            print("buraya kadar tamam1")
            try:
                isplaniolusturmodel.objects.create(vergitcno=vergitcno,isletmeadi=isletmeadi,isletmeyetkiliadsoyad=isletmeyetkiliadsoyad,finansman=finansman,
                        projeninadi=projeninadi,projeninkisatanimi=projeninkisatanimi,toplamprojesuresi=toplamprojesuresi,toplamprojebutcesi=toplamprojebutcesi,
                          isletmeprojeyetkilisi=isletmeprojeyetkilisi,eposta=eposta,telfax=telfax,
                isletmestatu=isletmestatu,isletmeadlari=isletmeadlari,ortaksayisi=ortaksayisi,
                vergidairesi=vergidairesi,verginumarasi=verginumarasi,isletmeyetkilisi=isletmeyetkilisi,
                isletmeprojeeyetkilisi=isletmeprojeeyetkilisi,sgkisyerisicilno=sgkisyerisicilno,ticaretisyerisicilno=ticaretisyerisicilno,ticaretsicilgazetetarihno=ticaretsicilgazetetarihno,
                kurulusyili=kurulusyili,faaliyetebaslamayili=faaliyetebaslamayili,toplampersonelsayisi=toplampersonelsayisi,
                beyazyaka=beyazyaka,maviyaka=maviyaka,baglibulunduguoda=baglibulunduguoda,bulunduguyer=bulunduguyer,
                adres=adres,il=il,ilce=ilce,postakodu=postakodu,telefon=telefon,epostaadresi=epostaadresi,webadresi=webadresi,
                desteklerdenyararlanma=desteklerdenyararlanma,nacekodu=nacekodu,urungruplari=urungruplari,isletmeortagiadisoyadi=isletmeortagiadisoyadi,
                tckimlikvergino=tckimlikvergino,isletmehissepayi=isletmehissepayi,isletmetarihcesi=isletmetarihcesi,
                projeninkonusu=projeninkonusu,projeninamaci=projeninamaci,projebenzerfaaliyet=projebenzerfaaliyet,
                uzundonemhedef=uzundonemhedef,projepazarnitelikleri=projepazarnitelikleri,
                projebeklenenetkiler=projebeklenenetkiler,rekabetedilebilirligi=rekabetedilebilirligi,
                surdurulebilirlik=surdurulebilirlik,hukikihusular=hukikihusular,risklervarsayilan=risklervarsayilan,
                digerhususlar=digerhususlar,projeciktilari=projeciktilari,projeninyonetimi=projeninyonetimi,
                   checkbox0=checkbox0,checkbox1=checkbox1,
                checkbox3=checkbox3,checkbox2=checkbox2,
                checkbox5=checkbox5,checkbox4=checkbox4,
                checkbox7=checkbox7,checkbox6=checkbox6,
                checkbox9=checkbox9, checkbox8=checkbox8,
                customCheck1=customCheck1,customCheck2=customCheck2,
                customCheck6=customCheck6,customCheck3=customCheck3,
                customCheck7=customCheck7,customCheck4=customCheck4,
                customCheck8=customCheck8,customCheck5=customCheck5,username=username,date=date)  
      
                #messages.success(request,"Form Başarılı")
                return redirect(mainurl+"projeler/")
            
            except Exception as e:
      
                message = traceback.format_exc()
                print(message)
                #messages.error(request,"Form Başarısız")
                return redirect(mainurl+"isplaniolustur/")
          
            
            
    else :
        return redirect(mainurl+"giris/")
      
            
 
def register_request2(request):
    if request.method == "POST":
        user=request.user
        yetki=request.user.is_authenticated
        if yetki == True:
            print (user.id)
            username=request.user.username
            date= datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            if request.POST.get("form_type") == 'formOne':
                 adsoyad=request.POST.get("adsoyad")
                 telefon=request.POST.get("telefon")
                 meslek=request.POST.get("telefon")
          
      #  user2 = User.objects.get(id=user.id)
        a =ExtendUser.objects.get(user=user.id)
        print(a.id)
        a.adisoyad=adsoyad
        a.telefon=telefon
        a.meslek=meslek
        a.uyetarih=date
        print(a.user.username)
        print(a.user.id)
        a.save()
        return redirect(mainurl+"giris/")
        
        #messages.error(request, "Geçersiz bilgi girişi.")
    return render (request=request, template_name="pages/kayitol2.html",context={'url': mainurl})

def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            user=request.user
            ExtendUser.objects.create(user=user,odemedurumu="0",adisoyad=user.username)
            print("basarili")
            #messages.success(request, "Kayıt başarılı." )
            return redirect(mainurl+"")
        #messages.error(request, "Geçersiz bilgi girişi.")
    form = NewUserForm()
    return render (request=request, template_name="pages/kayitol.html", context={"register_form":form, 'url': mainurl})


 
def analizlerolustur(request):
    user=request.user
    yetki=request.user.is_authenticated
    if yetki == True:
        print (user.id) #the us
        ex =ExtendUser.objects.get(user=user.id)
        if(ex.odemedurumu=="0"):
            return redirect(mainurl+"odemelerim/")
        return render(request, 'pages/icanaliz.html', {'username': user.username,'url': mainurl})    
    else :
        return redirect(mainurl+"giris/")


 
def analizler(request):
    user=request.user
    yetki=request.user.is_authenticated
    if yetki == True:
        ex =ExtendUser.objects.get(user=user.id)
        if(ex.odemedurumu=="0"):
            return redirect(mainurl+"odemelerim/")
        print (user.id) 
        username=request.user.username
        items = onanalizmodel.objects.filter(username = username) 
        return render(request, 'pages/analizler.html', {'items': items,'url': mainurl})
        
    else :
        return redirect(mainurl+"giris/")
    



def projeler(request):
    user=request.user
    yetki=request.user.is_authenticated
    username=request.user.username
    if yetki == True:
        try:
            ex =ExtendUser.objects.get(user=user.id)
            if(ex.odemedurumu=="0"):
                return redirect(mainurl+"odemelerim/")
            items = isplaniolusturmodel.objects.filter(username = username) 
            return render(request, 'pages/projeler.html', {'items': items,'url': mainurl})
        except:
            ex=None
            print (user.id)
            logout(request)
            return redirect(mainurl+"giris/")
        
        
    else :  
        return redirect(mainurl+"giris/")
    


def ornekisplanlari(request):
    items = isplaniornekmodel.objects.all() 
    return render(request, 'pages/ornekisplanlari.html', {'items': items,'url': mainurl})
    
           
        
      


def ornekisplanidetay (request,id):
    id2=id
    obj = isplaniornekmodel.objects.get(id=id2)
    return render(request, 'pages/ornekisplanidetay.html', {'obj': obj,'id':id2,'url': mainurl})
 


def isvideo (request):
    user=request.user
    ex=video.objects.all()
    return render(request,'pages/isvideo.html',{'ex':ex,'url': mainurl})
def videodetay (request,id):
    id2=id
    ex=video.objects.get(id=id2)
    return render(request,'pages/videodetay.html',{'ex':ex,'url': mainurl})
def blogview (request):
    user=request.user
    yetki=request.user.is_authenticated
    ex=blog.objects.all()
    return render(request,'pages/blog.html', {'ex':ex,'url': mainurl})
def blogdetay (request,id):
    id2=id
    ex=blog.objects.get(id=id2)
    return render(request,'pages/blogdetay.html',{'ex':ex,'url': mainurl})
def uyedestekmerkezi (request):
    user=request.user
    yetki=request.user.is_authenticated
    destek1="boş";
    if yetki == True:
        ex =ExtendUser.objects.get(user=user.id)
        try:
           destek1 =destek.objects.get(userid=user.id)
        except:
            print(user.id)
        if(ex.odemedurumu=="0"):
            return redirect(mainurl+"odemelerim/")
        print (user.id) 
        username=request.user.username 
        return render(request, 'pages/uyedestekmerkezi.html', {'items': destek1,'url': mainurl})    
    else :
        return redirect(mainurl+"giris/")
def destekmesaji (request):
    user=request.user
    yetki=request.user.is_authenticated
    if yetki == True:
        ex =ExtendUser.objects.get(user=user.id)
        if(ex.odemedurumu=="0"):
            return redirect(mainurl+"odemelerim/")
        print (user.id) 
        username=request.user.username 
        return render(request, 'pages/destekmesaji.html', {'username': username,'url': mainurl})    
    else :
        return redirect(mainurl+"giris/")
  
def destekmesajiolustur (request):
    user=request.user
    yetki=request.user.is_authenticated
    if yetki == True:
        ex =ExtendUser.objects.get(user=user.id)
        if(ex.odemedurumu=="0"):
            return redirect(mainurl+"odemelerim/")
        print (user.id) 
        username=request.user.username 
        return render(request, 'pages/destekmesajiolustur.html', {'username': username,'url': mainurl})    
    else :
        return redirect(mainurl+"giris/")
def hesabim (request):
    user=request.user
    yetki=request.user.is_authenticated
    if yetki == True:
        if request.method == "POST":
            adisoyadi=request.POST.get("adisoyadi")
            telefon=request.POST.get("telefon")
            universite=request.POST.get("universite")
            meslek=request.POST.get("meslek")
            adres=request.POST.get("adres")
            ex = ExtendUser.objects.get(user=user.id)
            print(ex.adisoyad)
            print("aaaaa")
            ex.adisoyad=adisoyadi
            ex.telefon=telefon
            ex.meslek=meslek
            ex.adres=adres
            ex.universite=universite
            ex.save()
            return redirect(mainurl+"hesabim/")
        else:
            print (user.id) 
            user=request.user 
            ex =ExtendUser.objects.get(user=user.id)
            return render(request, 'pages/hesabim.html', {'username': user,'ex':ex,'url': mainurl})    
    else :
        return redirect(mainurl+"giris/")
        
def sifreyenile (request):
    user=request.user
    yetki=request.user.is_authenticated
    if yetki == True:
        print (user.id) 
        username=request.user.username 
        return render(request, 'pages/sifreyenile.html', {'username': username,'url': mainurl})    
    else :
        return redirect(mainurl+"giris/")

def odemelerim (request):
    user=request.user
    yetki=request.user.is_authenticated
    if yetki == True:
        print (user.id) 
        userid=request.user.id 
        ex =ExtendUser.objects.get(user=user.id)
        odemedurum=ex.odemedurumu
        items = odemetablo.objects.filter(userid = userid) 
        return render(request, 'pages/odemelerim.html', {'userid': userid, 'odemedurum': odemedurum, 'items': items,'url': mainurl})    
    else :
        return redirect(mainurl+"giris/")


def admin2(request):
    
    user=request.user
    if request.user.is_superuser:
        try:
            
            items = isplaniolusturmodel.objects.all() 
            return render(request, 'pages/admin/admin.html', {'items': items,'url': mainurl})
        except:
            return redirect(mainurl+"admin2/")
    else:
        return redirect(mainurl+"")

        
    


def admin2destek (request):
    user=request.user
    if request.user.is_superuser:

        return render(request, 'pages/admin/admindestek.html', {'url': mainurl})    
    else:
        return redirect(mainurl+"")

def admin2destekmesaj (request):
    if request.user.is_superuser:
        return render(request, 'pages/admin/admindestekmesaj.html', {'url': mainurl})    
    else:
        return redirect(mainurl+"")
    

def admin2blog (request):
        if request.user.is_superuser:
            ex=blog.objects.all()
            return render(request,'pages/admin/adminblog.html', {'ex':ex,'url': mainurl})
        else:
            return redirect(mainurl+"")
    

def admin2blogekleduzenle (request,id):
        if request.user.is_superuser:
            if request.method != "POST":
                if id == 00:
                    return render(request, 'pages/admin/adminblogekle.html', {'url': mainurl})   
                ex=blog.objects.get(id=id)
                return render(request, 'pages/admin/adminblogekle.html', {'url': mainurl,'ex':ex})   
            else:
                ex=blog.objects.get(id=id)
                ex.delete()
                baslik=request.POST.get("baslik")
                yazi=request.POST.get("yazi")
                img=request.FILES['resim']
                tarih=0
                aciklama=request.POST.get("aciklama")
                blogyazisi=blog.objects.create(baslik=baslik,yazi=yazi,img=img,tarih=tarih,aciklama=aciklama)
                blogyazisi.save()
                return redirect(mainurl+"admin2blog/")        
        else:
            return redirect(mainurl+"")



def admin2blogsil (request,id):
        if request.user.is_superuser:
            ex=blog.objects.get(id=id)
            ex.delete()
            return redirect(mainurl+"admin2blog/")
        else:
            return redirect(mainurl+"")



def admin2ayar (request):
    if request.user.is_superuser:
        if request.method != "POST":
             obj = lisanstip.objects.all()
             ex=obj[0]
             return render(request, 'pages/admin/adminayarlar.html', {'url': mainurl,'ex':ex})    
        else:
            fiyat=request.POST.get("fiyat")
            ad=request.POST.get("ad")
            gun=request.POST.get("gun")
            yonetici="admin"
            obj = lisanstip.objects.all()
            obj.delete()
            lisanstip.objects.create(gun=gun,ucret=fiyat,lisansadi=ad)
            return redirect(mainurl+"admin2ayar")

    else:
            return redirect(mainurl+"")


def admin2finansal (request):

    if request.user.is_superuser:
         return render(request, 'pages/admin/adminfinansalanalizler.html', {'url': mainurl})    
    else:
        return redirect(mainurl+"")



def admin2işplanımnedir (request):
    if request.method != "POST":
        if request.user.is_superuser:
            items = nedir.objects.all()
            title=items[0].title;
            description=items[0].description;
            img=items[0].img;
            return render(request, 'pages/admin/adminisplanimnedir.html', {'title': title , 'description': description , 'img': img,'url': mainurl})
        else:
            return redirect(mainurl+"")
    else:  
    
        if request.user.is_superuser:
            baslik=request.POST.get("baslik")
            aciklama=request.POST.get("aciklama")
            resim=request.FILES['resim']
            obj = nedir.objects.all()
            obj.delete()
            obj=nedir.objects.create(title=baslik,description=aciklama,img=resim)

            return redirect(mainurl+"admin2/")
        else:
            return redirect(mainurl+"")
            


def admin2işplanlari(request):
    if request.user.is_superuser:
        try:
            items = isplaniolusturmodel.objects.all() 
            return render(request, 'pages/admin/adminisplanlari.html', {'items': items,'url': mainurl})
        except:
            return redirect(mainurl+"admin2/")
    else:  
        return redirect(mainurl+"")


def admin2isplanigor(request,id):
     if request.user.is_superuser:
            id2=id
            obj = isplaniolusturmodel.objects.get(id=id2)
            return render(request, 'pages/admin/adminisplangor.html', {'obj': obj,'id':id2,'url': mainurl})
     else:
        return redirect(mainurl+"")



def admin2ornekplanekle (request):
    if request.user.is_superuser:
        return render(request, 'pages/admin/adminornekplanekle.html', {'url': mainurl})
    else:
        return redirect(mainurl+"")

def admin2ornekplanlar(request):
       if request.user.is_superuser:
            items = isplaniornekmodel.objects.all() 
            return render(request, 'pages/admin/adminornekplanlar.html', {'items': items,'url': mainurl})
       else:
          return redirect(mainurl+"")



def admin2isplaniolusturkaydet (request):
    user=request.user
    yetki=request.user.is_authenticated
    if yetki == True:
        print (user.id) #the us
        if request.method != "POST":
            return redirect(mainurl+"admin2ornekplanekle/")
        else:
            username=request.user.username
            date= datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            isletmeyetkiliadsoyad=request.POST.get("isletmeyetkiliadsoyad")
            vergitcno=request.POST.get("vergitcno")
            isletmeadi=request.POST.get("isletmeadi")
            projeninadi=request.POST.get("projeninadi")
            projeninkisatanimi=request.POST.get("projeninkisatanimi")
            toplamprojesuresi=request.POST.get("toplamprojesuresi")
            toplamprojebutcesi=request.POST.get("toplamprojebutcesi")
            isletmeprojeyetkilisi=request.POST.get("isletmeprojeyetkilisi")
            eposta=request.POST.get("eposta")
            telfax=request.POST.get("telfax")
            #sayfa1 bitti
          
            isletmestatu=request.POST.get("radioInline")
            isletmeadlari=request.POST.get("isletmeadlari")
            ortaksayisi=request.POST.get("ortaksayisi")
            vergidairesi=request.POST.get("vergidairesi")
            verginumarasi=request.POST.get("verginumarasi")
            isletmeyetkilisi=request.POST.get("isletmeyetkilisi")
            isletmeprojeeyetkilisi=request.POST.get("isletmeprojeeyetkilisi")
            sgkisyerisicilno=request.POST.get("sgkisyerisicilno")
            
            ticaretisyerisicilno=request.POST.get("ticaretisyerisicilno")
            ticaretsicilgazetetarihno=request.POST.get("ticaretsicilgazetetarihno")
            kurulusyili=request.POST.get("kurulusyili")
            faaliyetebaslamayili=request.POST.get("faaliyetebaslamayili")
            toplampersonelsayisi=request.POST.get("toplampersonelsayisi")
            beyazyaka=request.POST.get("beyazyaka")
            maviyaka=request.POST.get("maviyaka")
            baglibulunduguoda=request.POST.get("baglibulunduguoda")   
            bulunduguyer=request.POST.get("bulunduguyer")
            adres=request.POST.get("adres")
            il=request.POST.get("il")
            ilce=request.POST.get("ilce")
            postakodu=request.POST.get("postakodu")
            telefon=request.POST.get("telefon")
            epostaadresi=request.POST.get("epostaadresi")
            webadresi=request.POST.get("webadresi")
            desteklerdenyararlanma=request.POST.get("desteklerdenyararlanma")
            checkbox0=request.POST.get("checkbox0")
            #id
            checkbox1=request.POST.get("checkbox1")
          
      
      
            checkbox2=request.POST.get("checkbox2")
            checkbox3=request.POST.get("checkbox3")
            checkbox4=request.POST.get("checkbox4")
            checkbox5=request.POST.get("checkbox5")
            checkbox6=request.POST.get("checkbox6")
            checkbox7=request.POST.get("checkbox7")
            checkbox8=request.POST.get("checkbox8")
            checkbox9=request.POST.get("checkbox9")
            customCheck1=request.POST.get("customCheck1")
            customCheck2=request.POST.get("customCheck2")
            customCheck3=request.POST.get("customCheck3")
            customCheck4=request.POST.get("customCheck4")
            customCheck5=request.POST.get("customCheck5")
            customCheck6=request.POST.get("customCheck6")
            customCheck7=request.POST.get("customCheck7")
            customCheck8=request.POST.get("customCheck8")
            nacekodu=request.POST.get("nacekodu")
            
            urungruplari=request.POST.get("urungruplari")
            isletmeortagiadisoyadi=request.POST.get("isletmeortagiadisoyadi")
            tckimlikvergino=request.POST.get("tckimlikvergino")
            isletmehissepayi=request.POST.get("isletmehissepayi")
            isletmetarihcesi=request.POST.get("isletmetarihcesi")
            projeninkonusu=request.POST.get("projeninkonusu")
            projeninamaci=request.POST.get("projeninamaci")
            projebenzerfaaliyet=request.POST.get("projebenzerfaaliyet")
            uzundonemhedef=request.POST.get("uzundonemhedef")
            projepazarnitelikleri=request.POST.get("projepazarnitelikleri")
            projebeklenenetkiler=request.POST.get("projebeklenenetkiler")
            rekabetedilebilirligi=request.POST.get("rekabetedilebilirligi")
            surdurulebilirlik=request.POST.get("surdurulebilirlik")
            hukikihusular=request.POST.get("hukikihusular")
            risklervarsayilan=request.POST.get("risklervarsayilan")
            digerhususlar=request.POST.get("digerhususlar")
            projeciktilari=request.POST.get("projeciktilari")
            projeninyonetimi=request.POST.get("projeninyonetimi")
            finansman=request.POST.get("finansman")
            print("buraya kadar tamam1")
            try:
                isplaniornekmodel.objects.create(vergitcno=vergitcno,isletmeadi=isletmeadi,isletmeyetkiliadsoyad=isletmeyetkiliadsoyad,finansman=finansman,
                        projeninadi=projeninadi,projeninkisatanimi=projeninkisatanimi,toplamprojesuresi=toplamprojesuresi,toplamprojebutcesi=toplamprojebutcesi,
                          isletmeprojeyetkilisi=isletmeprojeyetkilisi,eposta=eposta,telfax=telfax,
                isletmestatu=isletmestatu,isletmeadlari=isletmeadlari,ortaksayisi=ortaksayisi,
                vergidairesi=vergidairesi,verginumarasi=verginumarasi,isletmeyetkilisi=isletmeyetkilisi,
                isletmeprojeeyetkilisi=isletmeprojeeyetkilisi,sgkisyerisicilno=sgkisyerisicilno,ticaretisyerisicilno=ticaretisyerisicilno,ticaretsicilgazetetarihno=ticaretsicilgazetetarihno,
                kurulusyili=kurulusyili,faaliyetebaslamayili=faaliyetebaslamayili,toplampersonelsayisi=toplampersonelsayisi,
                beyazyaka=beyazyaka,maviyaka=maviyaka,baglibulunduguoda=baglibulunduguoda,bulunduguyer=bulunduguyer,
                adres=adres,il=il,ilce=ilce,postakodu=postakodu,telefon=telefon,epostaadresi=epostaadresi,webadresi=webadresi,
                desteklerdenyararlanma=desteklerdenyararlanma,nacekodu=nacekodu,urungruplari=urungruplari,isletmeortagiadisoyadi=isletmeortagiadisoyadi,
                tckimlikvergino=tckimlikvergino,isletmehissepayi=isletmehissepayi,isletmetarihcesi=isletmetarihcesi,
                projeninkonusu=projeninkonusu,projeninamaci=projeninamaci,projebenzerfaaliyet=projebenzerfaaliyet,
                uzundonemhedef=uzundonemhedef,projepazarnitelikleri=projepazarnitelikleri,
                projebeklenenetkiler=projebeklenenetkiler,rekabetedilebilirligi=rekabetedilebilirligi,
                surdurulebilirlik=surdurulebilirlik,hukikihusular=hukikihusular,risklervarsayilan=risklervarsayilan,
                digerhususlar=digerhususlar,projeciktilari=projeciktilari,projeninyonetimi=projeninyonetimi,
                   checkbox0=checkbox0,checkbox1=checkbox1,
                checkbox3=checkbox3,checkbox2=checkbox2,
                checkbox5=checkbox5,checkbox4=checkbox4,
                checkbox7=checkbox7,checkbox6=checkbox6,
                checkbox9=checkbox9, checkbox8=checkbox8,
                customCheck1=customCheck1,customCheck2=customCheck2,
                customCheck6=customCheck6,customCheck3=customCheck3,
                customCheck7=customCheck7,customCheck4=customCheck4,
                customCheck8=customCheck8,customCheck5=customCheck5,username=username,date=date)  
      
                #messages.success(request,"Form Başarılı")
                return redirect(mainurl+"admin2ornekplanlar/")
            
            except Exception as e:
      
                message = traceback.format_exc()
                print(message)
                #messages.error(request,"Form Başarısız")
                return redirect(mainurl+"admin2ornekplanekle/")
          
            
            
    else :
        return redirect(mainurl+"giris/")
      
            



def admin2ornekplanlardetay(request,id):
     if request.user.is_superuser:
            
            id2=id
            obj = isplaniornekmodel.objects.get(id=id2)
            return render(request, 'pages/admin/adminornekisplandetay.html', {'obj': obj,'id':id2,'url': mainurl})
     else:
        return redirect(mainurl+"")
    





def admin2slider (request):
    if request.user.is_superuser:
        return render(request, 'pages/admin/adminslider.html', {'url': mainurl})
    else:
        return redirect(mainurl+"")

def admin2sliderekle (request):
    if request.user.is_superuser:
            return render(request, 'pages/admin/adminsliderekle.html', {'url': mainurl})
    else:
        return redirect(mainurl+"")

def admin2uyedetay (request):
    if request.user.is_superuser:
            return render(request, 'pages/admin/adminsuyedetay.html', {'url': mainurl})
    else:
        return redirect(mainurl+"")

def admin2uyeekle (request):
    if request.user.is_superuser:
            return render(request, 'pages/admin/adminuyeekle.html', {'url': mainurl})
    else:
        return redirect(mainurl+"")
def admin2uyeler (request):
    if request.user.is_superuser:
            return render(request, 'pages/admin/adminuyeler.html', {'url': mainurl})
    else:
        return redirect(mainurl+"")

def admin2video (request):
    if request.user.is_superuser:
         ex=video.objects.all()
         return render(request,'pages/admin/adminvideo.html',{'ex':ex,'url': mainurl})
    else:
        return redirect(mainurl+"")


def admin2videosil (request,id):
    if request.user.is_superuser:
         video.objects.filter(id=id).delete()
         return redirect(mainurl+"admin2video/")
    else:
        return redirect(mainurl+"")


def admin2videoekle (request):
    if request.user.is_superuser:
        if request.method == "POST":
            baslik=request.POST.get("baslik")
            aciklama=request.POST.get("aciklama")
            url=request.POST.get("url")
            video.objects.create(link=url,aciklama=aciklama,baslik=baslik,tarih=0)
            return redirect(mainurl+"admin2video/")


        else:
          return render(request, 'pages/admin/adminvideoekle.html', {'url': mainurl})
    else:
        return redirect(mainurl+"")



def sifremiunuttum (request):
    return render(request,'pages/sifremiunuttum.html', {'url': mainurl})

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request, user)
                #messages.info(request, f"Giriş yapıldı: {username}.")
                #lisans bitiş çdek
                if request.user.is_superuser:
                    return redirect(mainurl+"admin2/")
                else:
                    ex =ExtendUser.objects.get(user=user.id)
                    if(ex.odemedurumu!="1") :
                        return redirect(mainurl+"odemelerim/")
                    
                    epoch = time.time()
                    day = time.strftime('%d', time.localtime(epoch))
                    month = time.strftime('%m', time.localtime(epoch))
                    year = time.strftime('%Y', time.localtime(epoch))
                    lisansbitis=ex.lisansbitis
                    #30-10-2022
                    bitisgun=lisansbitis[0:2]
                    bitisay=lisansbitis[4:6]
                    bitisyil=lisansbitis[7:11]
                    if(bitisgun<day and bitisay<=month and bitisyil<=year):
                        ex.odemedurumu="0"
                        ex.save()
                        return redirect(mainurl+"odemelerim/")
                    else:
                        ex.odemedurumu="1"
                        ex.save()
                        return redirect(mainurl+"")
               
            #else:
                #messages.error(request,"Geçersiz kullanıcı adı yada şifre.")
        #else:
         #  messages.error(request,"Geçersiz kullanıcı adı yada şifre.")
    form = AuthenticationForm()
    return render(request=request, template_name="pages/giris.html", context={"login_form":form,'url': mainurl})


def logout_request(request):
    logout(request)
    #messages.info(request, "Çıkış yapıldı.") 
    return redirect(mainurl+"giris/")



api_key = 'sandbox-etkBOaBAec7Zh6jLDL59Gng0xJV2o1tV'
secret_key = 'sandbox-uC9ysXfBn2syo7ZMOW2ywhYoc9z9hTHh'
base_url = 'sandbox-api.iyzipay.com'


options = {
    'api_key': api_key,
    'secret_key': secret_key,
    'base_url': base_url
}
sozlukToken = list()


def odeme(request):
    user=request.user
    
    yetki=request.user.is_authenticated
    if yetki == True:
        print (user.id)  
        context = dict()
        context['message'] = 'o'
        return render(request,'pages/odeme/odeme.html',{'url': mainurl})
    else:
        return redirect(mainurl+"giris/")

     

def payment(request):
    user=request.user
    yetki=request.user.is_authenticated
    if yetki == False:
        redirect(mainurl+"giris/")
    context = dict()

    buyer={
        'id': 'BY789',
        'name': 'John',
        'surname': 'Doe',
        'gsmNumber': '+905350000000',
        'email': 'email@email.com',
        'identityNumber': '74300864791',
        'lastLoginDate': '2015-10-05 12:43:35',
        'registrationDate': '2013-04-21 15:12:09',
        'registrationAddress': 'Nidakule Göztepe, Merdivenköy Mah. Bora Sok. No:1',
        'ip': '85.34.78.112',
        'city': 'Istanbul',
        'country': 'Turkey',
        'zipCode': '34732'
    }

    address={
        'contactName': 'Jane Doe',
        'city': 'Istanbul',
        'country': 'Turkey',
        'address': 'Nidakule Göztepe, Merdivenköy Mah. Bora Sok. No:1',
        'zipCode': '34732'
    }

    basket_items=[
        {
            'id': 'BI101',
            'name': 'Binocular',
            'category1': 'Collectibles',
            'category2': 'Accessories',
            'itemType': 'PHYSICAL',
            'price': '0.3'
        },
        {
            'id': 'BI102',
            'name': 'Game code',
            'category1': 'Game',
            'category2': 'Online Game Items',
            'itemType': 'VIRTUAL',
            'price': '0.5'
        },
        {
            'id': 'BI103',
            'name': 'Usb',
            'category1': 'Electronics',
            'category2': 'Usb / Cable',
            'itemType': 'PHYSICAL',
            'price': '0.2'
        }
    ]

    request={
        'locale': 'tr',
        'conversationId': '123456789',
        'price': '1',
        'paidPrice': '1.2',
        'currency': 'TRY',
        'basketId': 'B67832',
        'paymentGroup': 'PRODUCT',
        "callbackUrl": "http://194.87.17.120/result/",
        "enabledInstallments": ['2', '3', '6', '9'],
        'buyer': buyer,
        'shippingAddress': address,
        'billingAddress': address,
        'basketItems': basket_items,
        # 'debitCardAllowed': True
    }

    checkout_form_initialize = iyzipay.CheckoutFormInitialize().create(request, options)

    #print(checkout_form_initialize.read().decode('utf-8'))
    page = checkout_form_initialize
    header = {'Content-Type': 'application/json'}
    content = checkout_form_initialize.read().decode('utf-8')
    json_content = json.loads(content)
    print(type(json_content))
    print(json_content["checkoutFormContent"])
    print("************************")
    print(json_content["token"])
    print("************************")
    sozlukToken.append(json_content["token"])
    return HttpResponse(json_content["checkoutFormContent"])

@require_http_methods(['POST'])
@csrf_exempt
def result(request):
    user=request.user
    print(user)
    print("usssser")
    context = dict()
    url = request.META.get('odeme')

    request = {
        'locale': 'tr',
        'conversationId': '123456789',
        'token': sozlukToken[0]
    }
    checkout_form_result = iyzipay.CheckoutForm().retrieve(request, options)
    print("************************")
    print(type(checkout_form_result))
    result = checkout_form_result.read().decode('utf-8')
    print("************************")
    print(sozlukToken[0])   # Form oluşturulduğunda 
    print("************************")
    print("************************")
    sonuc = json.loads(result, object_pairs_hook=list)
    #print(sonuc[0][1])  # İşlem sonuç Durumu dönüyor
    #print(sonuc[5][1])   # Test ödeme tutarı
    print("************************")
    for i in sonuc:
        print(i)
    print("************************")
    print(sozlukToken)
    print("************************")
    if sonuc[0][1] == 'success':
        context['success'] = 'Başarılı İŞLEMLER'
       
        return HttpResponseRedirect(reverse('success'), context)

    elif sonuc[0][1] == 'failure':
        context['failure'] = 'Başarısız'
        return HttpResponseRedirect(reverse('failure'), context)
    return HttpResponse(url)
def success(request):
    user=request.user
    context = dict()
    lisans =lisanstip.objects.get(id=1)
    ex =ExtendUser.objects.get(user=user.id)
    
   # now = datetime.now().timestamp()
   # orig = datetime.fromtimestamp(now)
   # datetime_object = datetime(0, 1, 0)
   # seconds_since_epoch = datetime_object.timestamp()

    delta = datetime.now()+ relativedelta(days=int(lisans.gun))

   # delta = date.today() + timedelta(days=)    
    ex.lisansbitis= delta.strftime("%d-%m-%Y")
    #(datetime.combine(date(1,1,1),t) + delta).time()
    odeme=lisans.ucret
    ex.odemedurumu="1"
    ex.save()   
    odemetablo.objects.create(userid=user.id,odemetarih=date.today(),odeme=odeme,lisansadi=lisans.lisansadi)
    print("başarılı")
    print(user.id)
    context['success'] = 'İşlem Başarılı'
    return redirect(mainurl+"odemelerim/",context)


def fail(request):
    context = dict()
    context['fail'] = 'İşlem Başarısız'
    return redirect(mainurl+"odeme/",context)


