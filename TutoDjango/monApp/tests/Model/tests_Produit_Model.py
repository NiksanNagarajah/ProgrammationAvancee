from django.test import TestCase
from monApp.models import Produit

# Create your tests here.

class ProduitModelTest(TestCase):
    def setUp(self):
        # Créer un attribut produit à utiliser dans les tests
        self.prdt = Produit.objects.create(intituleProd="ProduitPourTest", prixUnitaireProd=52.5)
    
    def test_produit_creation(self):
        self.assertEqual(self.prdt.intituleProd, "ProduitPourTest")
    
    def test_string_representation(self):
        self.assertEqual(str(self.prdt), "ProduitPourTest")
    
    def test_produit_updating(self):
        self.prdt.intituleProd = "ProduitPourTestChange"
        self.prdt.save()
        # Récupérer l'objet mis à jour
        updated_prdt = Produit.objects.get(refProd=self.prdt.refProd)
        self.assertEqual(updated_prdt.intituleProd, "ProduitPourTestChange")

    def test_produit_deletion(self):
        self.prdt.delete()
        self.assertEqual(Produit.objects.count(), 0)

