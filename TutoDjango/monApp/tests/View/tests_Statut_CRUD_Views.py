from django.test import TestCase
from django.urls import reverse, resolve
from monApp.models import Statut, Categorie, Produit
from django.contrib.auth.models import User

class StatutListViewTest(TestCase):
    def setUp(self):
        self.stat1 = Statut.objects.create(libelleStatus='Available')
        self.stat2 = Statut.objects.create(libelleStatus='Out of Stock')

    def test_statut_list_view_get(self):
        response = self.client.get(reverse('lst_stats'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'monApp/list_statuts.html')
        self.assertEqual(len(response.context['stats']), 2)

    def test_statut_list_view_search(self):
        response = self.client.get(reverse('lst_stats') + '?search=Available')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['stats']), 1)


class StatutDetailViewTest(TestCase):
    def setUp(self):
        self.stat = Statut.objects.create(libelleStatus='Available')
        self.cat = Categorie.objects.create(nomCat='Category Test')
        self.produit = Produit.objects.create(
            intituleProd='Product Test',
            prixUnitaireProd=10.00,
            categorie=self.cat,
            status=self.stat
        )

    def test_statut_detail_view(self):
        response = self.client.get(reverse('dtl_stat', args=[self.stat.idStatus]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'monApp/detail_statut.html')
        self.assertEqual(response.context['stat'], self.stat)
        self.assertIn(self.produit, response.context['prdts'])


class StatutCreateViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='secret')
        self.client.login(username='testuser', password='secret')

    def test_statut_create_view_get(self):
        response = self.client.get(reverse('crt-stat'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'monApp/create_statut.html')

    def test_statut_create_view_post_valid(self):
        data = {'libelleStatus': 'New Status'}
        response = self.client.post(reverse('crt-stat'), data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Statut.objects.count(), 1)
        self.assertEqual(Statut.objects.last().libelleStatus, 'New Status')


class StatutUpdateViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='secret')
        self.stat = Statut.objects.create(libelleStatus='Original Status')
        self.client.login(username='testuser', password='secret')

    def test_statut_update_view_get(self):
        response = self.client.get(reverse('stat-chng', args=[self.stat.idStatus]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'monApp/update_statut.html')

    def test_statut_update_view_post_valid(self):
        data = {'libelleStatus': 'Updated Status'}
        response = self.client.post(reverse('stat-chng', args=[self.stat.idStatus]), data)
        self.assertEqual(response.status_code, 302)
        self.stat.refresh_from_db()
        self.assertEqual(self.stat.libelleStatus, 'Updated Status')


class StatutDeleteViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='secret')
        self.stat = Statut.objects.create(libelleStatus='Status to Delete')
        self.client.login(username='testuser', password='secret')

    def test_statut_delete_view_get(self):
        response = self.client.get(reverse('dlt-stat', args=[self.stat.idStatus]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'monApp/delete_statut.html')

    def test_statut_delete_view_post(self):
        response = self.client.post(reverse('dlt-stat', args=[self.stat.idStatus]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Statut.objects.filter(idStatus=self.stat.idStatus).exists())
        self.assertRedirects(response, reverse('lst_stats'))

