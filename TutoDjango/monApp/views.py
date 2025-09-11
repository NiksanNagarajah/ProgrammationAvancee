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
    message =   """
                    <h1>Bienvenue dans notre magasin !!</h1>
                    <p>Voici les catégories de produits que nous proposons : </p>
                """
    if len(cats) != 0:
        message += "<ul>"
        for i in range(len(cats)):
            message += f"<li>{cats[i].nomCat}</li>"
        message += "</ul>"
    else:
        message += "<p> rien pour l'instant. Désolé</p>"
    return HttpResponse(message)

def listStatuts(request):
    stats = Statut.objects.all()
    message =   """
                    <h1>Bienvenue dans notre magasin !!</h1>
                    <p>Voici les statuts des produits que nous proposons : </p>
                """
    if len(stats) != 0:
        message += "<ul>"
        for i in range(len(stats)):
            message += f"<li>{stats[i].libelleStatus}</li>"
        message += "</ul>"
    else:
        message += "<p> rien pour l'instant. Désolé</p>"
    return HttpResponse(message)

def listRayons(request):
    rayons = Rayon.objects.all()
    message =   """
                    <h1>Bienvenue dans notre magasin !!</h1>
                    <p>Voici les rayons que vous pouvez trouver dans notre magasins : </p>
                """
    if len(rayons) != 0:
        message += "<ul>"
        for i in range(len(rayons)):
            message += f"<li>{rayons[i].nomRayon}</li>"
        message += "</ul>"
    else:
        message += "<p> rien pour l'instant. Désolé</p>"
    return HttpResponse(message)