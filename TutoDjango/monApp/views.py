from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.

def home(request, param=None):
    if param:
        return HttpResponse(
            f"""
            <h1>Hello Django!</h1>
            <p>Bonjour, {param}</p>
            """
        )
    else:
        return HttpResponse("<h1>Hello Django!</h1>")

def contact(request):
    return HttpResponse(
        """
        <h1>Page Contact</h1>
        <p>Ceci est une page de contact !!</p>
        """
    )

def about(request):
    return HttpResponse(
        """
        <h1>Page A propos</h1>
        <p>Ceci est une page A propos !!</p>
        """
    )

def listProduits(request):
    prdts = Produit.objects.all()
    message =   """
                    <h1>Bienvenue dans notre magasin !!</h1>
                    <p>Voici la liste de produits que nous proposons : </p>
                """
    if len(prdts) != 0:
        message += "<ul>"
        for i in range(len(prdts)):
            message += f"<li>{prdts[i].intituleProd} {prdts[i].prixUnitaireProd}€</li>"
        message += "</ul>"
    else:
        message += "<p> rien pour l'instant. Désolé</p>"
    return HttpResponse(message)

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
            message += f"<li>{stats[i].libelleStat}</li>"
        message += "</ul>"
    else:
        message += "<p> rien pour l'instant. Désolé</p>"
    return HttpResponse(message)

