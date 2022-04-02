from django import forms
from django.forms import Textarea

from .models import Project

class AddProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields=('nom_projet',
                'duree_projet','temp_allouepar_createur',
                'besoin','description',
                'est_valide','createur')
        widgets={'besoin':Textarea(attrs={'cols':20,'rows':20})}