from django.shortcuts import render, redirect, HttpResponseRedirect
from .forms import ProductRegistration, UserRegistration
from .models import Product, User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


# Create your views here.
# Affichage de la page d'accueil
# @login_required(login_url="home")


def homepage(request):
    fm = UserRegistration(request.POST or None)

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        # Authentification de l'utilisateur
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("addandshow")  # Rediriger après une connexion réussie
        else:
            # Ajoute une erreur en cas de connexion échouée
            fm.add_error(None, "Nom d'utilisateur ou mot de passe incorrect.")

    return render(request, "produit/login.html", {"form": fm})


# Fonction d'ajout et d'affichage des infos des produits
def add_show(request):
    if request.method == "POST":
        fm = ProductRegistration(request.POST)
        if fm.is_valid():
            ttr = fm.cleaned_data["titre"]
            desc = fm.cleaned_data["description"]
            p = fm.cleaned_data["prix"]
            nb = fm.cleaned_data["nombre"]
            reg = Product(titre=ttr, description=desc, prix=p, nombre=nb)
            reg.save()
            fm = ProductRegistration()
    else:
        fm = ProductRegistration()
    stud = Product.objects.all()
    return render(request, "produit/addandshow.html", {"form": fm, "stu": stud})


# Fonction de modification des données
def update_data(request, id):
    if request.method == "POST":
        pi = Product.objects.get(pk=id)
        fm = ProductRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = Product.objects.get(pk=id)
        fm = ProductRegistration(instance=pi)
    return render(request, "produit/updateproduct.html", {"form": fm})


# Fonction de supression des données
def delete_data(request, id):
    if request.method == "POST":
        pi = Product.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect("/")


# Fonction Afficher un produit
def show_data(request, id):
    if request.method == "POST":
        pi = Product.objects.get(pk=id)
        fm = ProductRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = Product.objects.get(pk=id)
        fm = ProductRegistration(instance=pi)
    stud = Product.objects.get(pk=id)
    return render(request, "produit/showproduct.html", {"form": fm, "stu": stud})
