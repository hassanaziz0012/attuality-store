from django.shortcuts import render
from django.views import View

# Create your views here.
class HomeView(View):
    def get(self, request):
        return render(request, 'index.html')


# Footer views
class AttualityStoreView(View):
    def get(self, request):
        return render(request, 'footer/attuality_store.html')