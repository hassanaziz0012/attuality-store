from django.urls import path
from main import views

urlpatterns = [
    path('', views.HomeView.as_view(), name="home"),
    path('attuality-store', views.AttualityStoreView.as_view(), name="attuality-store"),
    path('privacy', views.PrivacyView.as_view(), name="privacy"),
    path('domande_frequenti', views.DomandeFrequentiView.as_view(), name="domande-frequenti"),
    path('contattaci', views.ContattaciView.as_view(), name="contattaci"),
    path('spedizione_resi_gratuiti', views.SpedizioneResiGratuitiView.as_view(), name="spedizione-resi-gratuiti"),
    path('pagamento', views.PagamentoView.as_view(), name="pagamento"),
    path('spedizione', views.SpedizioneView.as_view(), name="spedizione"),
    path('resi_cambi', views.ResiCambiView.as_view(), name="resi-cambi"),
    path('servizi', views.ServiziView.as_view(), name="servizi"),
]
