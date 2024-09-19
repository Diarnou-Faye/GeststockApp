from django.shortcuts import render, HttpResponseRedirect
from .forms import ProductRegistration
from .models import Product


# Create your views here.
# Fonction d'ajout et d'affichage des infos d'un étudiant
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
