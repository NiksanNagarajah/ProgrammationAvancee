from django.test import TestCase
from monApp.forms import ContactUsForm

# Create your tests here.

class ContactUsFormTest(TestCase):
    def test_form_valid_data(self):
        form = ContactUsForm(data = {'email': 'email@test.com', 'message': 'TestMessage'})
        self.assertTrue(form.is_valid()) # Le formulaire doit être valide

    def test_form_valid_data_too_long(self):
        form = ContactUsForm(data = {'email': 'email@test.com', 'message': 
            'TestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessageTestMessage'})
        self.assertFalse(form.is_valid()) # Le formulaire doit être invalide
        self.assertIn('message', form.errors) # Le champ 'email' doit contenir une erreur
        self.assertEqual(form.errors['message'], ['Assurez-vous que cette valeur comporte au plus 1000 caractères (actuellement 1837).'])

    def test_form_valid_data_missed(self):
        form = ContactUsForm(data = {'email': ''})
        self.assertFalse(form.is_valid()) # Le formulaire doit être invalide
        self.assertIn('email', form.errors) # Le champ 'email' doit contenir une erreur
        self.assertEqual(form.errors['email'], ['Ce champ est obligatoire.'])


