from django.contrib import admin
from django.urls import path
from django.urls import include
from django.urls import path
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static



#now import the views.py file into this code
from . import views
urlpatterns=[
  
  path('icanaliz/',views.analizlerolustur,name='analiz'),
  path('cikis/',views.logout_request,name='cıkıs'),
  path('admin/', admin.site.urls),
  path('anasayfa/',views.anasayfa),
  path('',views.index),
  path('index2/',views.index),
  path('isplanimnedir/',views.isplanimnedir),
  path('projeler/',views.projeler),
  path('analizler/',views.analizler),

  path('projesil/<int:id>',views.isplanisil),
  path('projeduzenle/<int:id>',views.isplaniduzenle),
  path('isplaniolustur/',views.isplanolustur),
  path('isplaniolusturkaydet/',views.isplaniolusturkaydet,name='isplaniolusturkaydet'),
  path('isplaniduzenlekaydet/',views.isplaniduzenlekaydet,name='isplaniduzenlekaydet'),
path('admin2/',views.admin2,name='admin2'),
path('admin2destek/',views.admin2destek,name='admin2destek'),
path('admin2destekmesaj/',views.admin2destekmesaj,name='admin2'),
path('admin2blog/',views.admin2blog,name='admin2'),
path('admin2blogekle/',views.admin2blogekle,name='admin2blogekle'),
path('admin2ayar/',views.admin2ayar,name='admin2ayar'),
path('admin2finansal/',views.admin2finansal,name='admin2'),
path('admin2işplanımnedir/',views.admin2işplanımnedir,name='admin2işplanımnedir'),
path('admin2işplanlari/',views.admin2işplanlari,name='admin2işplanlari'),
path('admin2ornekplanlar/',views.admin2ornekplanlar,name='admin2ornekplanlar'),
path('admin2ornekplanlardetay/<int:id>',views.admin2ornekplanlardetay,name='admin2ornekplanlar'),

path('admin2ornekplanekle/',views.admin2ornekplanekle,name='admin2ornekplanekle'),
path('admin2slider/',views.admin2slider,name='admin2slider'),
path('admin2sliderekle/',views.admin2sliderekle,name='admin2sliderekle'),
path('admin2uyedetay/',views.admin2uyedetay,name='admin2uyedetay'),
path('admin2uyeekle/',views.admin2uyeekle,name='admin2uyeekle'),
path('admin2uyeler/',views.admin2uyeler,name='admin2uyeler'),
path('admin2video/',views.admin2video,name='admin2video'),
path('admin2videoekle/',views.admin2videoekle,name='admin2videoekle'),


  path('ornekisplanidetay/<int:id>',views.ornekisplanidetay),
  path('ornekisplanlari/',views.ornekisplanlari),
  path('isvideo/',views.isvideo),
  path('videodetay/<int:id>',views.videodetay),
  path('blog/',views.blogview),
  path('blogdetay/<int:id>',views.blogdetay),
  path('uyedestekmerkezi/',views.uyedestekmerkezi),
  path('destekmesaji/',views.destekmesaji),
  path('destekmesajiolustur/',views.destekmesajiolustur),
  path('hesabim/',views.hesabim),
  path('sifreyenile/',views.sifreyenile),
  path('odemelerim/',views.odemelerim),
  path('admin2/',views.admin2),
  path("giris/", views.login_request, name="login"),
  path("kayitol/", views.register_request, name="register"),
  path("kayitol2/", views.register_request2, name="register"),

  path('sifremiunuttum/',views.sifremiunuttum),
  path('odeme/', views.odeme, name='index'),
  path('payment/', views.payment, name='payment'),
  path('result/', views.result, name='result'),
  path('success/', views.success, name='success'),
  path('failure/', views.fail, name='failure')
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)