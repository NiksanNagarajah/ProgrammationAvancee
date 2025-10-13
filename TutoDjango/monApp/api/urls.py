from monApp.api import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategorieViewSet, ProduitViewSet, StatutViewSet, RayonViewSet, ContenirViewSet

router = DefaultRouter()
router.register(r'categories', CategorieViewSet, basename='categorie')
router.register(r'produits', ProduitViewSet, basename='produits')
router.register(r'status', StatutViewSet, basename='status')
router.register(r'rayons', RayonViewSet, basename='rayons')
router.register(r'contenir', ContenirViewSet, basename='contenir')

urlpatterns = [
    path('', include(router.urls)),
]

