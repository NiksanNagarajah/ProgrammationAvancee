from django.test import TestCase
from monApp.models import Contenir, Produit, Rayon

# Create your tests here.

class ContenirModelTest(TestCase):
    def setUp(self):
        # Créer un attribut produit à utiliser dans les tests
        self.prdt = Produit.objects.create(intituleProd="ProduitPourTest", prixUnitaireProd=52.5)
        self.ryn = Rayon.objects.create(nomRayon="RayonPourTest")
        self.cntnr = Contenir.objects.create(produit=self.prdt, rayon=self.ryn)
    
    def test_contenir_creation(self):
        self.assertEqual(self.cntnr.produit.intituleProd, "ProduitPourTest")
        self.assertEqual(self.cntnr.rayon.nomRayon, "RayonPourTest")
    
    def test_string_representation(self):
        self.assertEqual(str(self.cntnr), "ProduitPourTest dans RayonPourTest (Qte: 0)")
    
    def test_contenir_updating(self):
        prdt2 = Produit.objects.create(intituleProd="TestPrdt", prixUnitaireProd=12.5)
        self.cntnr.produit = prdt2
        self.cntnr.save()
        # Récupérer l'objet mis à jour
        updated_cntnr = Contenir.objects.get(produit=prdt2)
        self.assertEqual(updated_cntnr.produit.intituleProd, "TestPrdt")

    def test_contenir_deletion(self):
        self.cntnr.delete()
        self.assertEqual(Contenir.objects.count(), 0)

