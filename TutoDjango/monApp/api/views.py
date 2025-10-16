from rest_framework import generics, viewsets
from rest_framework.pagination import PageNumberPagination
from monApp.models import Categorie, Produit, Statut, Rayon, Contenir
from .serializers import CategorieSerializer, ProduitSerializer, StatutSerializer, RayonSerializer, ContenirSerializer, CategorieSerializerList, MultipleSerializerMixin
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAdminAuthenticated
from rest_framework.schemas.openapi import AutoSchema
from datetime import datetime

class SmallResultsSetPagination(PageNumberPagination):
    page_size = 2 # minimum de résultats par page
    page_size_query_param = 'page_size'
    max_page_size = 4 # maximum de résultats par page

class CategorieViewSet(MultipleSerializerMixin, viewsets.ModelViewSet):
    """
    Gestion des catégories de produits.
    
    Permet de créer, lister, récupérer, mettre à jour et supprimer des catégories.
    """
    pagination_class = SmallResultsSetPagination
    # queryset = Categorie.objects.all().prefetch_related('produits_categorie')
    serializer_class = CategorieSerializerList
    detail_serializer_class = CategorieSerializer
    # permission_classes = [IsAuthenticated]
    permission_classes = [IsAdminAuthenticated]

    def get_queryset(self):
        """Retourne toutes les catégories avec leurs produits associés."""
        return Categorie.objects.all()

class ProduitViewSet(viewsets.ModelViewSet):
    """
    Gestion des produits.
    
    Permet de créer, lister, récupérer, mettre à jour et supprimer des produits.
    Supports filtering par date de fabrication avec le paramètre 'datefilter' (format: DD/MM/YYYY).
    """
    pagination_class = None
    queryset = Produit.objects.all()
    serializer_class = ProduitSerializer

    def get_queryset(self):
        """
        Filtre les produits selon la date de fabrication si le paramètre datefilter est fourni.
        """
        queryset = Produit.objects.all()
        datefilter = self.request.GET.get('datefilter')
        if datefilter is not None:
            datefilter=datetime.strptime(datefilter, "%d/%m/%Y")
            queryset = queryset.filter(dateFabProd__gt=datefilter)
        return queryset

class StatutViewSet(viewsets.ModelViewSet):
    """
    Gestion des statuts de produits (En ligne, Hors ligne, etc.).
    
    Permet de créer, lister, récupérer, mettre à jour et supprimer des statuts.
    """
    pagination_class = None
    queryset = Statut.objects.all()
    serializer_class = StatutSerializer

class RayonViewSet(viewsets.ModelViewSet):
    """
    Gestion des rayons (sections de stockage).
    
    Permet de créer, lister, récupérer, mettre à jour et supprimer des rayons.
    Chaque rayon peut contenir plusieurs produits avec différentes quantités.
    """
    pagination_class = None
    queryset = Rayon.objects.all()
    serializer_class = RayonSerializer

class ContenirViewSet(viewsets.ModelViewSet):
    """
    Gestion des stocks (relation produit-rayon).
    
    Permet de gérer la présence et la quantité des produits dans les rayons.
    Un produit ne peut être présent qu'une seule fois par rayon.
    """
    pagination_class = None
    queryset = Contenir.objects.all()
    serializer_class = ContenirSerializer

class CustomAutoSchema(AutoSchema):
    def get_tags(self):
        return super().get_tags()
