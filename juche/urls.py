from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'juche'

urlpatterns = [
    path('',views.home,name='home'),
    path('historia/',views.historia,name='historia'),
    path('zuche/',views.zuche,name='zuche'),
    path('songun/',views.songun,name='songun'),
    path('byungjin/',views.byungjin,name='byungjin'),
    path('mais/',views.mais,name='mais'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
