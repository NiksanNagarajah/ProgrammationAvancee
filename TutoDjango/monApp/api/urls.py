from monApp.api import views
from django.urls import path

urlpatterns = [
    path('categories/',views.CategorieAPIView.as_view(),name="api-lst-ctgrs"),
    path('produits/',views.ProduitAPIView.as_view(),name="api-lst-prdts"),
    path('status/',views.StatutAPIView.as_view(),name="api-lst-stats"),
    path('rayons/',views.RayonAPIView.as_view(),name="api-lst-ryns"),
    path('contenir/',views.ContenirAPIView.as_view(),name="api-lst-cntrs"),

    path('categorie/<pk>/',views.CategorieDetailAPIView.as_view(),name="api-dtl-ctgr"),
    path('produit/<pk>/',views.ProduitDetailAPIView.as_view(),name="api-dtl-prdt"),
    path('statut/<pk>/',views.StatutDetailAPIView.as_view(),name="api-dtl-stat"),
    path('rayon/<pk>/',views.RayonDetailAPIView.as_view(),name="api-dtl-ryn"),
]