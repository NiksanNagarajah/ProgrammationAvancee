from django.test import TestCase
from monApp.models import Rayon
from monApp.forms import RayonForm

# Create your tests here.

class RayonFormTest(TestCase):
    def test_form_valid_data(self):
        form = RayonForm(data = {'nomRayon': 'RayonPourTest'})
        self.assertTrue(form.is_valid()) # Le formulaire doit être valide

    def test_form_valid_data_too_long(self):
        form = RayonForm(data = {'nomRayon': 
        'RayonPourTestRayonPourTestRayonPourTestRayonPourTestRayonPourTestRayonPourTestRayonPourTestRayonPourTestRayonPourTestRayonPourTest'})
        self.assertFalse(form.is_valid()) # Le formulaire doit être invalide
        self.assertIn('nomRayon', form.errors) # Le champ 'nomRayon' doit contenir une erreur
        self.assertEqual(form.errors['nomRayon'], ['Assurez-vous que cette valeur comporte au plus 100 caractères (actuellement 130).'])

    def test_form_valid_data_missed(self):
        form = RayonForm(data = {'nomRayon': ''})
        self.assertFalse(form.is_valid()) # Le formulaire doit être invalide
        self.assertIn('nomRayon', form.errors) # Le champ 'nomRayon' doit contenir une erreur
        self.assertEqual(form.errors['nomRayon'], ['Ce champ est obligatoire.'])

    def test_form_save(self):
        form = RayonForm(data = {'nomRayon': 'RayonPourTest'})
        self.assertTrue(form.is_valid())
        ryn = form.save()
        self.assertEqual(ryn.nomRayon, 'RayonPourTest')
        self.assertEqual(ryn.idRayon, 1)

