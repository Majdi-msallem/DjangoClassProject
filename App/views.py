from Tools.scripts.make_ctype import method
from django.contrib.auth import authenticate, login
from  django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView, DeleteView
from django.views.generic.list import ListView

from .forms import AddProjectForm
from .models import Project


def index (request):
    return HttpResponse("Bonjour 4twin6")
def index_id(request, classe):
    return HttpResponse('Boonjour %s' %classe)
def template(request):
    return render(request,'App/Affiche.html')
def Affiche(request):
    projet = Project.objects.all()#==>select *
   # resultat = '-'.join([p.nom_projet for p in projet])
   # return HttpResponse(resultat)
    return render(request,'App/Affiche.html',
                 {'pp': projet})
class Affiche_ListView(ListView):
    model =Project
    template_name = 'App/Affiche.html'
    context_object_name = 'pp'
    #ordering= ['-description']
    #fields="__all__"
def add_project(request):
    if request.method=="GET":
        form=AddProjectForm
        return render(request,'App/Ajout.html',
                      {'f':form})
    if request.method=="POST":
        form=AddProjectForm(request.POST)
        if form.is_valid():
            new_project=form.save(commit=False)
            new_project.save()
            return HttpResponseRedirect(reverse('LV'))
        else:
            return render(request,'App/Ajout.html',
                      {'f':form,'msg_erreur':"Erreur de l'ajout d'un projet"})
class CreateProject(CreateView):
    model = Project
    fields = [
        'nom_projet',
        'duree_projet', 'temp_allouepar_createur',
        'besoin', 'description',
        'est_valide', 'createur'
    ]
    success_url = reverse_lazy('LV')


def delete(request, id):
   projet=Project.objects.get(pk=id)
   projet.delete()
   return  HttpResponseRedirect(reverse('LV'))
class deleteGeneric (DeleteView):
    model = Project
    success_url = reverse_lazy('LV')
def Acceuil(request):
    return  render(request,'base.html')
def Login(request):
    if request.method=="POST":
        u=request.POST['username']
        p=request.POST['password']
        user=authenticate(request,username=u,password=p)
        if user is not None:
            login(request,user)
            return redirect('acceuil')
        else:
            messages.info(request,'User name or password incorrect')
            return redirect('login')
    else:
        return render(request,'App/login.html')

def register(request):
    if request.method=="POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('login')
        else:
         form=UserCreationForm()
    return  render(request,'App/signup.html',{'f':form})
