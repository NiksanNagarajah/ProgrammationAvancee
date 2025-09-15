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
        context['title'] = "Accueil"
        context['message'] = "Bienvenue sur la page d'accueil de notre site !"
        return context

    def post(self, request, **kwargs):
        return render(request, self.template_name)
    
class AboutView(TemplateView):
    template_name = "monApp/home.html"

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        context['titreh1'] = "About us..."
        context['title'] = "About"
        context['message'] = "Bienvenue sur la page À propos de notre site !"
        return context
    
    def post(self, request, **kwargs):
        return render(request, self.template_name)

class ContactView(TemplateView):
    template_name = "monApp/home.html"

    def get_context_data(self, **kwargs):
        context = super(ContactView, self).get_context_data(**kwargs)
        context['titreh1'] = "Contact us..."
        context['title'] = "Contact"
        context['message'] = "Bienvenue sur la page Contact de notre site !"
        return context
    
    def post(self, request, **kwargs):
        return render(request, self.template_name)

class ProduitListView(ListView):
    model = Produit
    template_name = "monApp/list_produits.html"
    context_object_name = "prdts"

    def get_context_data(self, **kwargs):
        context = super(ProduitListView, self).get_context_data(**kwargs)
        context['titremenu'] = "Liste de mes produits"
        return context

class ProduitDetailView(DetailView):
    model = Produit
    template_name = "monApp/detail_produit.html"
    context_object_name = "prdt"
    
    def get_context_data(self, **kwargs):
        context = super(ProduitDetailView, self).get_context_data(**kwargs)
        context['titremenu'] = "Détail du produit"
        return context
    
def listCategries(request):
    cats = Categorie.objects.all()
    return render(request, 'monApp/list_categories.html',{'cats': cats})

def listStatuts(request):
    stats = Statut.objects.all()
    return render(request, 'monApp/list_statuts.html',{'stats': stats})

def listRayons(request):
    rayons = Rayon.objects.all()
    return render(request, 'monApp/list_rayons.html',{'rayons': rayons})

