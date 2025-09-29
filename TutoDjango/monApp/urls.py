"""
URL configuration for TutoDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("home/",  views.HomeView.as_view(), name="home"),
    path("home/<param>",  views.HomeView.as_view(), name="home"),
    path("contact/", views.ContactView, name="contact"),
    path("email-sent/", views.ConfirmationView, name="email-sent"),
    path("about/", views.AboutView.as_view(), name="about"),
    path("produits/", views.ProduitListView.as_view(), name="lst_prdts"),
    path("produit/<pk>/",views.ProduitDetailView.as_view(), name="dtl_prdt"),
    path("categories/", views.CategorieListView.as_view(), name="lst_cats"),
    path("categorie/<pk>", views.CategorieDetailView.as_view(), name="dtl_cat"),
    path("statuts/", views.StatutListView.as_view(), name="lst_stats"),
    path("statut/<pk>", views.StatutDetailView.as_view(), name="dtl_stat"),
    path("rayons/", views.RayonListView.as_view(), name="lst_rayons"),
    path("rayon/<pk>", views.RayonDetailView.as_view(), name="dtl_rayon"),
    path('login/', views.ConnectView.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('logout/', views.DisconnectView.as_view(), name='logout'),
    path("produit/",views.ProduitCreateView.as_view(), name="crt-prdt"),
    path("produit/<pk>/update/",views.ProduitUpdateView.as_view(), name="prdt-chng"),
    path("produit/<pk>/delete/",views.ProduitDeleteView.as_view(), name="dlt-prdt"),
    path("categorie/",views.CategorieCreateView.as_view(), name="crt-cat"),
    path("statut/",views.StatutCreateView.as_view(), name="crt-stat"),
    path("rayon/",views.RayonCreateView.as_view(), name="crt-rayon"),
    path("categorie/<pk>/update/",views.CategorieUpdateView.as_view(), name="cat-chng"),
    path("statut/<pk>/update/",views.StatutUpdateView.as_view(), name="stat-chng"),
    path("rayon/<pk>/update/",views.RayonUpdateView.as_view(), name="rayon-chng"),
    path("categorie/<pk>/delete/",views.CategorieDeleteView.as_view(), name="dlt-cat"),
    path("statut/<pk>/delete/",views.StatutDeleteView.as_view(), name="dlt-stat"),
    path("rayon/<pk>/delete/",views.RayonDeleteView.as_view(), name="dlt-rayon"),
    path('rayon/<pk>/cntnr', views.ContenirCreateView.as_view(), name='cntnr-crt'),
]
