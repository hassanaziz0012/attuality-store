from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from main.models import Product


# Create your views here.
class HomeView(View):
    def get(self, request):
        products = Product.objects.all().order_by('order')[0:10]
        return render(request, 'index.html', context={'products': products})


class ProductView(View):
    def get(self, request, name):
        try:
            product = Product.objects.get(name=name)
            brand_products = Product.objects.filter(brand=product.brand)[0:10]
        except Product.DoesNotExist:
            return HttpResponse(status=404)

        return render(request, 'product.html', context={'product': product, 'brand_products': brand_products})


# Footer views
class FooterViews:
    class AttualityStoreView(View):
        def get(self, request):
            return render(request, 'footer/attuality_store.html')


    class PrivacyView(View):
        def get(self, request):
            return render(request, 'footer/privacy.html')


    class DomandeFrequentiView(View):
        def get(self, request):
            return render(request, 'footer/domande_frequenti.html')


    class ContattaciView(View):
        def get(self, request):
            return render(request, 'footer/contattaci.html')


    class SpedizioneResiGratuitiView(View):
        def get(self, request):
            return render(request, 'footer/spedizione_e_resi_gratuiti.html')


    class PagamentoView(View):
        def get(self, request):
            return render(request, 'footer/pagamento.html')


    class SpedizioneView(View):
        def get(self, request):
            return render(request, 'footer/spedizione.html')

        
    class ResiCambiView(View):
        def get(self, request):
            return render(request, 'footer/resi_cambi.html')


    class ServiziView(View):
        def get(self, request):
            return render(request, 'footer/servizi_online_esclusivi.html')

