from django.shortcuts import render
from rest_framework import viewsets
from .serializers import EcheanceSerializer,PaiementSerializer,ResidentSerializer,PeriodeSerializer
from .models import Echeance,Paiement,Resident,Periode

# Create your views here.

class EcheanceView(viewsets.ModelViewSet):
    serializer_class = EcheanceSerializer
    queryset = Echeance.objects.all()

class PaiementView(viewsets.ModelViewSet):
    serializer_class = PaiementSerializer
    queryset = Paiement.objects.all()

class PeriodeView(viewsets.ModelViewSet):
    serializer_class = PeriodeSerializer
    queryset = Periode.objects.all()

class ResidentView(viewsets.ModelViewSet):
    serializer_class = ResidentSerializer
    queryset = Resident.objects.all()
