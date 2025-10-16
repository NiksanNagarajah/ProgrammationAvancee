from rest_framework import serializers
from monApp.models import Categorie, Produit, Statut, Rayon, Contenir
from datetime import datetime

class ProduitSerializer(serializers.ModelSerializer):
    """Serializer pour les produits avec tous les champs."""
    class Meta:
        model = Produit
        fields = '__all__'

class CategorieSerializerList(serializers.ModelSerializer):
    """
    Serializer pour la liste des catégories.
    Inclut tous les produits associés à chaque catégorie.
    """
    produits_categorie = ProduitSerializer(many=True)
    class Meta:
        model = Categorie
        fields = '__all__'
    
        
    def validate_nomCat(self, value):
        """Valide que le nom de catégorie soit unique."""
        if Categorie.objects.filter(nomCat=value).exists():
            raise serializers.ValidationError('La categorie existe déjà')
        return value
    
    def validate(self, data):
        """Valide que le nom ne dépasse pas 100 caractères."""
        if len(data['nomCat'])>100 :
            raise serializers.ValidationError('Pb question.')
        return data

class CategorieSerializer(serializers.ModelSerializer):
    """
    Serializer pour le détail d'une catégorie.
    Affiche les produits seulement s'il y en a au moins 2.
    """
    produits_categorie = serializers.SerializerMethodField()
    class Meta:
        model = Categorie
        # fields = '__all__'
        fields = ["idCat", "nomCat","produits_categorie"]
    
    def get_produits_categorie(self,instance):
        """Retourne les produits de la catégorie si elle en contient au moins 2."""
        queryset = instance.produits_categorie.all()
        # Ne renvoyer les produits que si la catégorie en a au moins 2
        if queryset.count() < 2:
            return [] # moins de 2 produits on renvoie une liste vide→
        serializer = ProduitSerializer(queryset, many=True)
        return serializer.data

class StatutSerializer(serializers.ModelSerializer):
    """Serializer pour les statuts de produits."""
    class Meta:
        model = Statut
        fields = '__all__'

class RayonSerializer(serializers.ModelSerializer):
    """Serializer pour les rayons de stockage."""
    class Meta:
        model = Rayon
        fields = '__all__'

class ContenirSerializer(serializers.ModelSerializer):
    """
    Serializer pour les stocks (relation produit-rayon).
    Représente la présence et la quantité d'un produit dans un rayon.
    """
    class Meta:
        model = Contenir
        fields = '__all__'

class MultipleSerializerMixin:
    """
    Mixin pour utiliser différents serializers selon l'action.
    Permet d'utiliser un serializer simplifié pour les listes et un plus détaillé pour le détail.
    """
    detail_serializer_class = None

    def get_serializer_class(self):
        """Retourne le serializer approprié selon l'action (retrieve vs autres)."""
        if self.action == 'retrieve' and self.detail_serializer_class is not None:
            return self.detail_serializer_class
        return super().get_serializer_class()