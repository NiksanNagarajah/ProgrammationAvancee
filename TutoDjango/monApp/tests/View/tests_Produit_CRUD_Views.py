from django.test import TestCase
from django.urls import reverse, resolve
from monApp.models import Categorie, Statut, Produit
from django.contrib.auth.models import User

class ProduitListViewTest(TestCase):
    def setUp(self):
        self.cat = Categorie.objects.create(nomCat='Category Test')
        self.stat = Statut.objects.create(libelleStatus='Available')
        self.produit1 = Produit.objects.create(
            intituleProd='Product 1',
            prixUnitaireProd=10.00,
            categorie=self.cat,
            status=self.stat
        )
        self.produit2 = Produit.objects.create(
            intituleProd='Product 2',
            prixUnitaireProd=20.00,
            categorie=self.cat,
            status=self.stat
        )

    def test_produit_list_view_get(self):
        response = self.client.get(reverse('lst_prdts'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'monApp/list_produits.html')
        self.assertEqual(len(response.context['prdts']), 2)

    def test_produit_list_view_search(self):
        response = self.client.get(reverse('lst_prdts') + '?search=Product 1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['prdts']), 1)
        self.assertEqual(response.context['prdts'][0].intituleProd, 'Product 1')


class ProduitDetailViewTest(TestCase):
    def setUp(self):
        self.cat = Categorie.objects.create(nomCat='Category Test')
        self.stat = Statut.objects.create(libelleStatus='Available')
        self.produit = Produit.objects.create(
            intituleProd='Product Test',
            prixUnitaireProd=15.00,
            categorie=self.cat,
            status=self.stat
        )

    def test_produit_detail_view(self):
        response = self.client.get(reverse('dtl_prdt', args=[self.produit.refProd]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'monApp/detail_produit.html')
        self.assertEqual(response.context['prdt'], self.produit)


class ProduitCreateViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='secret')
        self.cat = Categorie.objects.create(nomCat='Category Test')
        self.stat = Statut.objects.create(libelleStatus='Available')
        self.client.login(username='testuser', password='secret')

    def test_produit_create_view_get(self):
        response = self.client.get(reverse('crt-prdt'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'monApp/create_produit.html')

    # def test_produit_create_view_post_valid(self):
    #     data = {
    #         'intituleProd': 'New Product',
    #         'prixUnitaireProd': 25.00,
    #         'categorie': self.cat.idCat,
    #         'status': self.stat.idStatus
    #     }
    #     response = self.client.post(reverse('crt-prdt'), data)
    #     self.assertEqual(response.status_code, 302)
    #     self.assertEqual(Produit.objects.count(), 1)
    #     self.assertEqual(Produit.objects.last().intituleProd, 'New Product')

    def test_produit_create_view_redirect_unauthenticated(self):
        self.client.logout()
        response = self.client.get(reverse('crt-prdt'))
        self.assertEqual(response.status_code, 302)


class ProduitUpdateViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='secret')
        self.cat = Categorie.objects.create(nomCat='Category Test')
        self.stat = Statut.objects.create(libelleStatus='Available')
        self.produit = Produit.objects.create(
            intituleProd='Product Test',
            prixUnitaireProd=10.00,
            categorie=self.cat,
            status=self.stat
        )
        self.client.login(username='testuser', password='secret')

    def test_produit_update_view_get(self):
        response = self.client.get(reverse('prdt-chng', args=[self.produit.refProd]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'monApp/update_produit.html')

    # def test_produit_update_view_post_valid(self):
    #     data = {
    #         'intituleProd': 'Product Updated',
    #         'prixUnitaireProd': 15.00,
    #         'categorie': self.cat.idCat,
    #         'status': self.stat.idStatus
    #     }
    #     response = self.client.post(reverse('prdt-chng', args=[self.produit.refProd]), data)
    #     self.assertEqual(response.status_code, 302)
    #     self.produit.refresh_from_db()
    #     self.assertEqual(self.produit.intituleProd, 'Product Updated')
    #     self.assertEqual(self.produit.prixUnitaireProd, 15.00)


class ProduitDeleteViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='secret')
        self.cat = Categorie.objects.create(nomCat='Category Test')
        self.stat = Statut.objects.create(libelleStatus='Available')
        self.produit = Produit.objects.create(
            intituleProd='Product Test',
            prixUnitaireProd=10.00,
            categorie=self.cat,
            status=self.stat
        )
        self.client.login(username='testuser', password='secret')

    def test_produit_delete_view_get(self):
        response = self.client.get(reverse('dlt-prdt', args=[self.produit.refProd]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'monApp/delete_produit.html')

    def test_produit_delete_view_post(self):
        response = self.client.post(reverse('dlt-prdt', args=[self.produit.refProd]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Produit.objects.filter(refProd=self.produit.refProd).exists())
        self.assertRedirects(response, reverse('lst_prdts'))

