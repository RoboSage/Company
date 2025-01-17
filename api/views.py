from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.object.all()
    serializer_class = CompanySerializer