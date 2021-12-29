from rest_framework import serializers
from .models import Echeance,Paiement,Resident,Periode

class EcheanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Echeance
        fields = ('id_echeance', 'id_resident', 'id_paiement', 'code_periode', 'status', 'echu', 'montant', 'reste', 'date_delai')

class PaiementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paiement
        fields = ('id_paiement', 'id_resident', 'code_paiement', 'type_paiement', 'date_paiement', 'date_creation', 'date_maj', 'validation', 'verification', 'montant', 'montant_ht', 'montant_ttc')
 
class PeriodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Periode
        fields =('id_periode', 'code_periode', 'date_debut', 'date_fin', 'montant_defaut')
   
class ResidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resident
        fields = ('id_resident', 'nom', 'prenom', 'nom_complet', 'tel', 'adresse', 'email', 'num_appartement', 'num_meuble', 'ntranche', 'date_creation', 'date_maj')

