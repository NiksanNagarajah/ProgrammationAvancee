from rest_framework import generics, viewsets
from monApp.models import Categorie, Produit, Statut, Rayon, Contenir
from .serializers import CategorieSerializer, ProduitSerializer, StatutSerializer, RayonSerializer, ContenirSerializer
from datetime import datetime

class CategorieViewSet(viewsets.ModelViewSet):
    queryset = Categorie.objects.all()
    serializer_class = CategorieSerializer

class ProduitViewSet(viewsets.ModelViewSet):
    queryset = Produit.objects.all()
    serializer_class = ProduitSerializer

    # def get_queryset(self):
    #     queryset = Produit.objects.all()
    #     datefilter = self.request.GET.get('datefilter')
    #     if datefilter is not None:
    #         datefilter=datetime.strptime(datefilter, "%d/%m/%Y")
    #         queryset = queryset.filter(dateFabProd__gt=datefilter)
    #     return queryset

class StatutViewSet(viewsets.ModelViewSet):
    queryset = Statut.objects.all()
    serializer_class = StatutSerializer

class RayonViewSet(viewsets.ModelViewSet):
    queryset = Rayon.objects.all()
    serializer_class = RayonSerializer

class ContenirViewSet(viewsets.ModelViewSet):
    queryset = Contenir.objects.all()
    serializer_class = ContenirSerializer

