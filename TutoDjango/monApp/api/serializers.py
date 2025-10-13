from rest_framework import serializers
from monApp.models import Categorie, Produit, Statut, Rayon, Contenir
from datetime import datetime

class ProduitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produit
        fields = '__all__'

class CategorieSerializerList(serializers.ModelSerializer):
    produits_categorie = ProduitSerializer(many=True)
    class Meta:
        model = Categorie
        # fields = '__all__'
        fields = ["idCat", "nomCat","produits_categorie"]

class CategorieSerializer(serializers.ModelSerializer):
    produits_categorie = serializers.SerializerMethodField()
    class Meta:
        model = Categorie
        # fields = '__all__'
        fields = ["idCat", "nomCat","produits_categorie"]
    
    def get_produits_categorie(self,instance):
        queryset = instance.produits_categorie.all()
        # Ne renvoyer les produits que si la catégorie en a au moins 2
        if queryset.count() < 2:
            return [] # moins de 2 produits on renvoie une liste vide→
        serializer = ProduitSerializer(queryset, many=True)
        return serializer.data

class StatutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statut
        fields = '__all__'

class RayonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rayon
        fields = '__all__'

class ContenirSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contenir
        fields = '__all__'

