# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Echeance(models.Model):
    id_echeance = models.AutoField(primary_key=True)
    id_resident = models.IntegerField()
    id_paiement = models.IntegerField(blank=True, null=True)
    code_periode = models.CharField(max_length=45)
    status = models.CharField(max_length=45, blank=True, null=True)
    echu = models.CharField(max_length=45, blank=True, null=True)
    montant = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    reste = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    date_delai = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'echeance'


class Paiement(models.Model):
    id_paiement = models.AutoField(primary_key=True)
    id_resident = models.ForeignKey('Resident', models.DO_NOTHING, db_column='id_resident')
    code_paiement = models.CharField(max_length=16)
    type_paiement = models.CharField(max_length=45)
    date_paiement = models.DateTimeField()
    date_creation = models.DateTimeField(blank=True, null=True)
    date_maj = models.DateTimeField(blank=True, null=True)
    validation = models.BooleanField(default=False)
    verification = models.BooleanField(default=False)
    montant = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    montant_ht = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    montant_ttc = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'paiement'


class Periode(models.Model):
    id_periode = models.AutoField(primary_key=True)
    code_periode = models.CharField(max_length=45)
    date_debut = models.DateField()
    date_fin = models.DateField()
    montant_defaut = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'periode'
        unique_together = (('id_periode', 'code_periode'),)


class Resident(models.Model):
    id_resident = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=45, blank=True, null=True)
    prenom = models.CharField(max_length=45, blank=True, null=True)
    nom_complet = models.CharField(max_length=255)
    tel = models.IntegerField(blank=True, null=True)
    adresse = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    num_appartement = models.IntegerField(db_column='Num_appartement', blank=True, null=True)  # Field name made lowercase.
    num_meuble = models.IntegerField(db_column='Num_meuble', blank=True, null=True)  # Field name made lowercase.
    ntranche = models.IntegerField(db_column='Ntranche', blank=True, null=True)  # Field name made lowercase.
    date_creation = models.DateTimeField(blank=True, null=True)
    date_maj = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'resident'


class User(models.Model):
    username = models.CharField(max_length=16)
    email = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=32)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'
