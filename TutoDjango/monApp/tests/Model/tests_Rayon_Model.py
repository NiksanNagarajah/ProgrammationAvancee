from django.test import TestCase
from monApp.models import Rayon

# Create your tests here.

class RayonModelTest(TestCase):
    def setUp(self):
        # Créer un attribut produit à utiliser dans les tests
        self.ryn = Rayon.objects.create(nomRayon="RayonPourTest")
    
    def test_rayon_creation(self):
        self.assertEqual(self.ryn.nomRayon, "RayonPourTest")
    
    def test_string_representation(self):
        self.assertEqual(str(self.ryn), "RayonPourTest")
    
    def test_rayon_updating(self):
        self.ryn.nomRayon = "RayonPourTestChange"
        self.ryn.save()
        # Récupérer l'objet mis à jour
        updated_ryn = Rayon.objects.get(idRayon=self.ryn.idRayon)
        self.assertEqual(updated_ryn.nomRayon, "RayonPourTestChange")

    def test_rayon_deletion(self):
        self.ryn.delete()
        self.assertEqual(Rayon.objects.count(), 0)

