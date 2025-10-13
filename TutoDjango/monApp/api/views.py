from rest_framework import generics, viewsets
from rest_framework.pagination import PageNumberPagination
from monApp.models import Categorie, Produit, Statut, Rayon, Contenir
from .serializers import CategorieSerializer, ProduitSerializer, StatutSerializer, RayonSerializer, ContenirSerializer, CategorieSerializerList
from datetime import datetime

class SmallResultsSetPagination(PageNumberPagination):
    page_size = 2 # minimum de résultats par page
    page_size_query_param = 'page_size'
    max_page_size = 4 # maximum de résultats par page

class CategorieViewSet(viewsets.ModelViewSet):
    pagination_class = SmallResultsSetPagination
    # queryset = Categorie.objects.all().prefetch_related('produits_categorie')
    serializer_class = CategorieSerializerList
    detail_serializer_class = CategorieSerializer

    def get_queryset(self):
        return Categorie.objects.all()
    
    def get_serializer_class(self):
        if self.action == 'retrieve':
            #on utilise le serializer qui donne tous les détails : catégorie + produits
            return self.detail_serializer_class
        #on utilise le serializer qui donne les catégorie sans les produits
        return super().get_serializer_class()

class ProduitViewSet(viewsets.ModelViewSet):
    pagination_class = None
    queryset = Produit.objects.all()
    serializer_class = ProduitSerializer

    def get_queryset(self):
        queryset = Produit.objects.all()
        datefilter = self.request.GET.get('datefilter')
        if datefilter is not None:
            datefilter=datetime.strptime(datefilter, "%d/%m/%Y")
            queryset = queryset.filter(dateFabProd__gt=datefilter)
        return queryset

class StatutViewSet(viewsets.ModelViewSet):
    pagination_class = None
    queryset = Statut.objects.all()
    serializer_class = StatutSerializer

class RayonViewSet(viewsets.ModelViewSet):
    pagination_class = None
    queryset = Rayon.objects.all()
    serializer_class = RayonSerializer

class ContenirViewSet(viewsets.ModelViewSet):
    pagination_class = None
    queryset = Contenir.objects.all()
    serializer_class = ContenirSerializer

