from rest_framework import serializers
from monApp.models import Categorie, Produit, Statut, Rayon, Contenir

class CategorieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorie
        fields = '__all__'

class ProduitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produit
        fields = '__all__'

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

