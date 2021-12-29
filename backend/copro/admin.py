from django.contrib import admin
from .models import Echeance,Paiement,Resident,Periode


class EcheanceAdmin(admin.ModelAdmin):
    list_display = ('id_echeance', 'id_resident', 'id_paiement', 'code_periode', 'status', 'echu', 'montant', 'reste', 'date_delai')

class PaiementAdmin(admin.ModelAdmin):
    list_display = ('id_paiement', 'id_resident', 'code_paiement', 'type_paiement', 'date_paiement', 'date_creation', 'date_maj', 'validation', 'verification', 'montant', 'montant_ht', 'montant_ttc')
 
class PeriodeAdmin(admin.ModelAdmin):
    list_display = ('id_periode', 'code_periode', 'date_debut', 'date_fin', 'montant_defaut')

class ResidentAdmin(admin.ModelAdmin):
    list_display = ('id_resident', 'nom', 'prenom', 'nom_complet', 'tel', 'adresse', 'email', 'num_appartement', 'num_meuble', 'ntranche', 'date_creation', 'date_maj')

# Register your models here.

admin.site.register(Echeance, EcheanceAdmin)
admin.site.register(Paiement, PaiementAdmin)
admin.site.register(Periode, PeriodeAdmin)
admin.site.register(Resident, ResidentAdmin)

