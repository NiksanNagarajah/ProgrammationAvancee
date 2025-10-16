from django.test import TestCase
from django.urls import reverse, resolve
from monApp.models import Categorie, Rayon, Statut, Produit, Contenir
from django.contrib.auth.models import User

class RayonListViewTest(TestCase):
    def setUp(self):
        self.rayon1 = Rayon.objects.create(nomRayon='Rayon 1')
        self.rayon2 = Rayon.objects.create(nomRayon='Rayon 2')

    def test_rayon_list_view_get(self):
        response = self.client.get(reverse('lst_rayons'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'monApp/list_rayons.html')
        self.assertEqual(len(response.context['rayons']), 2)

    def test_rayon_list_view_search(self):
        response = self.client.get(reverse('lst_rayons') + '?search=Rayon 1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['rayons']), 1)


class RayonDetailViewTest(TestCase):
    def setUp(self):
        self.rayon = Rayon.objects.create(nomRayon='Rayon Test')
        self.cat = Categorie.objects.create(nomCat='Category')
        self.stat = Statut.objects.create(libelleStatus='Available')
        self.produit = Produit.objects.create(
            intituleProd='Product',
            prixUnitaireProd=10.00,
            categorie=self.cat,
            status=self.stat
        )
        self.contenir = Contenir.objects.create(
            produit=self.produit,
            rayon=self.rayon,
            Qte=5
        )

    def test_rayon_detail_view(self):
        response = self.client.get(reverse('dtl_rayon', args=[self.rayon.idRayon]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'monApp/detail_rayon.html')
        self.assertEqual(response.context['ray'], self.rayon)
        self.assertEqual(response.context['total_rayon'], 50.00)
        self.assertEqual(response.context['total_nb_produit'], 5)


class RayonCreateViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='secret')
        self.client.login(username='testuser', password='secret')

    def test_rayon_create_view_get(self):
        response = self.client.get(reverse('crt-rayon'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'monApp/create_rayon.html')

    def test_rayon_create_view_post_valid(self):
        data = {'nomRayon': 'New Rayon'}
        response = self.client.post(reverse('crt-rayon'), data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Rayon.objects.count(), 1)
        self.assertEqual(Rayon.objects.last().nomRayon, 'New Rayon')


class RayonUpdateViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='secret')
        self.rayon = Rayon.objects.create(nomRayon='Original Rayon')
        self.client.login(username='testuser', password='secret')

    def test_rayon_update_view_get(self):
        response = self.client.get(reverse('rayon-chng', args=[self.rayon.idRayon]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'monApp/update_rayon.html')

    def test_rayon_update_view_post_valid(self):
        data = {'nomRayon': 'Updated Rayon'}
        response = self.client.post(reverse('rayon-chng', args=[self.rayon.idRayon]), data)
        self.assertEqual(response.status_code, 302)
        self.rayon.refresh_from_db()
        self.assertEqual(self.rayon.nomRayon, 'Updated Rayon')


class RayonDeleteViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='secret')
        self.rayon = Rayon.objects.create(nomRayon='Rayon to Delete')
        self.client.login(username='testuser', password='secret')

    def test_rayon_delete_view_get(self):
        response = self.client.get(reverse('dlt-rayon', args=[self.rayon.idRayon]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'monApp/delete_rayon.html')

    def test_rayon_delete_view_post(self):
        response = self.client.post(reverse('dlt-rayon', args=[self.rayon.idRayon]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Rayon.objects.filter(idRayon=self.rayon.idRayon).exists())
        self.assertRedirects(response, reverse('lst_rayons'))

