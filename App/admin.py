from django.contrib import admin, messages

# Register your models here.
from .models import *
class members(admin.StackedInline):
    model = MemberShipInProject
    extra = 0
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):

    def set_to_valid(self,request,queryset):
        queryset.update(est_valide=True)
    actions = ['set_to_valid', 'set_to_no_valid']
    set_to_valid.short_description="Valider"
    def set_to_no_valid(self,request,queryset):
        rows=queryset.filter(est_valide=False)
        a=rows.count()
        if a>0:
            messages.error(request, "%s projets non valide" % a)
        else:
            rows_update=queryset.update(est_valide=False)
            if rows_update==1:
                message="1 project was updates"
            else:
                message="%s projects where updates " % rows_update
            self.message_user(request,message)

    set_to_no_valid.short_description = "refuser"

    list_display = ('nom_projet','duree_projet',
                    'temp_allouepar_createur',
                    'description','besoin','est_valide')
    list_per_page = 5
    inlines = (members,)
    list_filter = ('est_valide' , 'createur__prenom')
    actions_on_top = False
   # actions_on_bottom = True
    #Barre de recherche
    search_fields = ('nom_projet','duree_projet')
admin.site.register(Etudiant)
admin.site.register(Coach)
#admin.site.register(Project,ProjectAdmin)