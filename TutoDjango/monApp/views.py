from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import *
from .forms import *
from django.views.generic import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.views import *
from django.shortcuts import redirect
from django.core.mail import send_mail
from django.forms.models import BaseModelForm
from django.urls import reverse_lazy 
from django.db.models import Count, Prefetch


# Create your views here.

class HomeView(TemplateView):
    template_name = "monApp/page_home.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            print(self.request.user)
            context['param'] = self.request.user
        context['titreh1'] = "Hello DJANGO"
        context['title'] = "Accueil"
        context['message'] = "Bienvenue sur la page d'accueil de notre site !"
        return context

    def post(self, request, **kwargs):
        return render(request, self.template_name)
    
class AboutView(TemplateView):
    template_name = "monApp/page_home.html"

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        context['titreh1'] = "About us..."
        context['title'] = "About"
        context['message'] = "Bienvenue sur la page À propos de notre site !"
        return context
    
    def post(self, request, **kwargs):
        return render(request, self.template_name)

def ContactView(request):
    titreh1 = "Contact us !"
    if request.method=='POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            send_mail(
            subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via TutoDjango Contact form',
            message=form.cleaned_data['message'],
            from_email=form.cleaned_data['email'],
            recipient_list=['admin@monApp.com'],
            )
            return redirect('email-sent')
    else:
        form = ContactUsForm()
    print('La méthode de requête est : ', request.method)
    print('Les données POST sont : ', request.POST)
    return render(request, "monApp/page_home.html",{'titreh1':titreh1, 'form':form, 'title':titreh1})

def ConfirmationView(request):
    return render(request, "monApp/page_confirmation.html")

class ProduitListView(ListView):
    model = Produit
    template_name = "monApp/list_produits.html"
    context_object_name = "prdts"

    def get_queryset(self):
        # Charge les catégories et les statuts en même temps
        return Produit.objects.select_related('categorie').select_related('status')

    def get_context_data(self, **kwargs):
        context = super(ProduitListView, self).get_context_data(**kwargs)
        context['titremenu'] = "Liste de mes produits"
        return context

class ProduitDetailView(DetailView):
    model = Produit
    template_name = "monApp/detail_produit.html"
    context_object_name = "prdt"

    def get_context_data(self, **kwargs):
        context = super(ProduitDetailView, self).get_context_data(**kwargs)
        context['titremenu'] = "Détail du produit"
        return context

class CategorieListView(ListView):
    model = Categorie
    template_name = "monApp/list_categories.html"
    context_object_name = "cats"

    def get_queryset(self):
        # Annoter chaque catégorie avec le nombre de produits liés
        return Categorie.objects.annotate(nb_produits=Count('produits_categorie'))

    def get_context_data(self, **kwargs):
        context = super(CategorieListView, self).get_context_data(**kwargs)
        context['titremenu'] = "Liste de mes catégories"
        return context

class CategorieDetailView(DetailView):
    model = Categorie
    template_name = "monApp/detail_categorie.html"
    context_object_name = "cat"

    def get_queryset(self):
        # Annoter chaque catégorie avec le nombre de produits liés
        return Categorie.objects.annotate(nb_produits=Count('produits_categorie'))

    def get_context_data(self, **kwargs):
        context = super(CategorieDetailView, self).get_context_data(**kwargs)
        context['titremenu'] = "Détail de la catégorie"
        context['prdts'] = self.object.produits_categorie.all()
        return context
    
class StatutListView(ListView):
    model = Statut
    template_name = "monApp/list_statuts.html"
    context_object_name = "stats"

    def get_queryset(self):
        # Annoter chaque catégorie avec le nombre de produits liés
        return Statut.objects.annotate(nb_produits=Count('produits_status'))

    def get_context_data(self, **kwargs):
        context = super(StatutListView, self).get_context_data(**kwargs)
        context['titremenu'] = "Liste de mes statuts"
        return context

class StatutDetailView(DetailView):
    model = Statut
    template_name = "monApp/detail_statut.html"
    context_object_name = "stat"

    def get_queryset(self):
        # Annoter chaque catégorie avec le nombre de produits liés
        return Statut.objects.annotate(nb_produits=Count('produits_status'))

    def get_context_data(self, **kwargs):
        context = super(StatutDetailView, self).get_context_data(**kwargs)
        context['titremenu'] = "Détail du statut"
        context['prdts'] = self.object.produits_status.all()
        return context

class RayonListView(ListView):
    model = Rayon
    template_name = "monApp/list_rayons.html"
    context_object_name = "rayons"

    def get_queryset(self):
        # Précharge tous les "contenir" de chaque rayon,
        # et en même temps le produit de chaque contenir
        return Rayon.objects.prefetch_related(
        Prefetch("contenir_rayon", queryset=Contenir.objects.select_related("produit")))

    def get_context_data(self, **kwargs):
        context = super(RayonListView, self).get_context_data(**kwargs)
        context['titremenu'] = "Liste de mes rayons"
        ryns_dt = []
        for rayon in context['object_list']:
            total = 0
            for contenir in rayon.contenir_rayon.all():
                total += contenir.produit.prixUnitaireProd * contenir.Qte
            ryns_dt.append({'rayon': rayon,'total_stock': total})
        context['ryns_dt'] = ryns_dt
        return context

class RayonDetailView(DetailView):
    model = Rayon
    template_name = "monApp/detail_rayon.html"
    context_object_name = "ray"

    def get_context_data(self, **kwargs):
        context = super(RayonDetailView, self).get_context_data(**kwargs)
        context['titremenu'] = "Détail du rayon"

        prdts_dt = []
        total_rayon = 0
        total_nb_produit = 0
        for contenir in self.object.contenir_rayon.all():
            total_produit = contenir.produit.prixUnitaireProd * contenir.Qte
            prdts_dt.append({ 'produit': contenir.produit,
                'qte': contenir.Qte,
                'prix_unitaire': contenir.produit.prixUnitaireProd,
                'total_produit': total_produit})
            total_rayon += total_produit
            total_nb_produit += contenir.Qte
        context['prdts_dt'] = prdts_dt
        context['total_rayon'] = total_rayon
        context['total_nb_produit'] = total_nb_produit

        return context

class ConnectView(LoginView):
    template_name = 'monApp/page_login.html'

    def post(self, request, **kwargs):
        lgn = request.POST.get('username', False)
        pswrd = request.POST.get('password', False)
        user = authenticate(username=lgn, password=pswrd)
        if user is not None and user.is_active:
            login(request, user)
            return redirect('home') 
        else:
            return render(request, 'monApp/page_register.html')

class RegisterView(TemplateView):
    template_name = 'monApp/page_register.html'

    def post(self, request, **kwargs):
        username = request.POST.get('username', False)
        mail = request.POST.get('mail', False)
        password = request.POST.get('password', False)
        user = User.objects.create_user(username, mail, password)
        user.save()
        if user is not None and user.is_active:
            return render(request, 'monApp/page_login.html')
        else:
            return render(request, 'monApp/page_register.html')
        
class DisconnectView(TemplateView):
    template_name = 'monApp/page_logout.html'

    def get(self, request, **kwargs):
        logout(request)
        return render(request, self.template_name)

class ProduitCreateView(CreateView):
    model = Produit
    form_class=ProduitForm
    template_name = "monApp/create_produit.html"

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        prdt = form.save()
        return redirect('dtl_prdt', prdt.refProd)

class ProduitUpdateView(UpdateView):
    model = Produit
    form_class=ProduitForm
    template_name = "monApp/update_produit.html"
    
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        prdt = form.save()
        return redirect('dtl_prdt', prdt.refProd)

class ProduitDeleteView(DeleteView):
    model = Produit
    template_name = "monApp/delete_produit.html"
    success_url = reverse_lazy('lst_prdts')


class CategorieCreateView(CreateView):
    model = Categorie
    form_class=CategorieForm
    template_name = "monApp/create_categorie.html"

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        cat = form.save()
        return redirect('dtl_cat', cat.idCat)

class CategorieUpdateView(UpdateView):
    model = Categorie
    form_class=CategorieForm
    template_name = "monApp/update_categorie.html"
    
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        cat = form.save()
        return redirect('dtl_cat', cat.idCat)

class CategorieDeleteView(DeleteView):
    model = Categorie
    template_name = "monApp/delete_categorie.html"
    success_url = reverse_lazy('lst_cats')    

class StatutCreateView(CreateView):
    model = Statut
    form_class=StatutForm
    template_name = "monApp/create_statut.html"

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        stat = form.save()
        return redirect('dtl_stat', stat.idStatus)

class StatutUpdateView(UpdateView):
    model = Statut
    form_class=StatutForm
    template_name = "monApp/update_statut.html"
    
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        stat = form.save()
        return redirect('dtl_stat', stat.idStatus)

class StatutDeleteView(DeleteView):
    model = Statut
    template_name = "monApp/delete_statut.html"
    success_url = reverse_lazy('lst_stats')  


class RayonCreateView(CreateView):
    model = Rayon
    form_class=RayonForm
    template_name = "monApp/create_rayon.html"

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        ray = form.save()
        return redirect('dtl_rayon', ray.idRayon)

class RayonUpdateView(UpdateView):
    model = Rayon
    form_class=RayonForm
    template_name = "monApp/update_rayon.html"
    
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        rayon = form.save()
        return redirect('dtl_rayon', rayon.idRayon)

class RayonDeleteView(DeleteView):
    model = Rayon
    template_name = "monApp/delete_rayon.html"
    success_url = reverse_lazy('lst_rayons')  


