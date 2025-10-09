from django.test import TestCase
from monApp.models import Contenir, Rayon, Produit
from monApp.forms import ContenirForm

# Create your tests here.

class ContenirFormTest(TestCase):
    def setUp(self):
        # Créer un attribut produit à utiliser dans les tests
        self.prdt = Produit.objects.create(intituleProd="ProduitPourTest", prixUnitaireProd=52.5)
        self.ryn = Rayon.objects.create(nomRayon="RayonPourTest")

    def test_form_valid_data(self):
        form = ContenirForm(data = {'produit': self.prdt, 'rayon': self.ryn, 'Qte': 5})
        self.assertTrue(form.is_valid()) # Le formulaire doit être valide

    def test_form_valid_data_missed(self):
        form = ContenirForm(data = {'produit': '', 'rayon': self.ryn, 'Qte': 5})
        self.assertFalse(form.is_valid()) # Le formulaire doit être invalide
        self.assertIn('produit', form.errors) # Le champ 'produit' doit contenir une erreur
        self.assertEqual(form.errors['produit'], ['Ce champ est obligatoire.'])

    # def test_form_save(self):
    #     form = ContenirForm(data={'produit': self.prdt.refProd, 'rayon': self.ryn.idRayon, 'Qte': 5})
    #     self.assertTrue(form.is_valid())
    #     cntn = form.save()
    #     self.assertEqual(cntn.produit, self.prdt)
    #     self.assertEqual(cntn.rayon, self.ryn)

