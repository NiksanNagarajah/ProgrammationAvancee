from django.test import TestCase
from monApp.models import Statut

# Create your tests here.

class StatutModelTest(TestCase):
    def setUp(self):
        # Créer un attribut produit à utiliser dans les tests
        self.stat = Statut.objects.create(libelleStatus="StatutPourTest")
    
    def test_statut_creation(self):
        self.assertEqual(self.stat.libelleStatus, "StatutPourTest")
    
    def test_string_representation(self):
        self.assertEqual(str(self.stat), "StatutPourTest")
    
    def test_statut_updating(self):
        self.stat.libelleStatus = "StatutPourTestChange"
        self.stat.save()
        # Récupérer l'objet mis à jour
        updated_stat = Statut.objects.get(idStatus=self.stat.idStatus)
        self.assertEqual(updated_stat.libelleStatus, "StatutPourTestChange")

    def test_statut_deletion(self):
        self.stat.delete()
        self.assertEqual(Statut.objects.count(), 0)

