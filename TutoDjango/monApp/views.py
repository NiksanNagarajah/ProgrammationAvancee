from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import *

# Create your views here.

def home(request, param=None):
    if request.GET and request.GET["test"]:
        raise Http404
    return HttpResponse("Bonjour Monde!")
    # if param:
    #     return HttpResponse(
    #         f"""
    #         <h1>Hello Django!</h1>
    #         <p>Bonjour, {param}</p>
    #         """
    #     )
    # else:
    #     return HttpResponse("<h1>Hello Django!</h1>")

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

