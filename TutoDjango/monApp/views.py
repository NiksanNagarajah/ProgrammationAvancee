from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import *
from django.views.generic import *

# Create your views here.

class HomeView(TemplateView):
    template_name = "monApp/home.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['titreh1'] = "Hello DJANGO"
        return context

    def post(self, request, **kwargs):
        return render(request, self.template_name)
    
class AboutView(TemplateView):
    template_name = "monApp/home.html"

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        print(context)
        context['titreh1'] = "About us..."
        print(context)
        return context
    
    def post(self, request, **kwargs):
        return render(request, self.template_name)

def contact(request):
    return render(request, 'monApp/contact.html')

def about(request):
    return render(request, 'monApp/about.html')

def listProduits(request):
    prdts = Produit.objects.all()
    return render(request, 'monApp/list_produits.html',{'prdts': prdts})

def listCategries(request):
    cats = Categorie.objects.all()
    return render(request, 'monApp/list_categories.html',{'cats': cats})

def listStatuts(request):
    stats = Statut.objects.all()
    return render(request, 'monApp/list_statuts.html',{'stats': stats})

def listRayons(request):
    rayons = Rayon.objects.all()
    return render(request, 'monApp/list_rayons.html',{'rayons': rayons})

