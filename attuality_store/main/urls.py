from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from main import views


urlpatterns = [
    path('', views.HomeView.as_view(), name="home"),
    path('product/<str:name>', views.ProductView.as_view(), name="product"),

    path('attuality-store', views.FooterViews.AttualityStoreView.as_view(), name="attuality-store"),
    path('privacy', views.FooterViews.PrivacyView.as_view(), name="privacy"),
    path('domande_frequenti', views.FooterViews.DomandeFrequentiView.as_view(), name="domande-frequenti"),
    path('contattaci', views.FooterViews.ContattaciView.as_view(), name="contattaci"),
    path('spedizione_resi_gratuiti', views.FooterViews.SpedizioneResiGratuitiView.as_view(), name="spedizione-resi-gratuiti"),
    path('pagamento', views.FooterViews.PagamentoView.as_view(), name="pagamento"),
    path('spedizione', views.FooterViews.SpedizioneView.as_view(), name="spedizione"),
    path('resi_cambi', views.FooterViews.ResiCambiView.as_view(), name="resi-cambi"),
    path('servizi', views.FooterViews.ServiziView.as_view(), name="servizi"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)