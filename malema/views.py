from django.http import HttpResponse
from django.shortcuts import render



# Create your views here.

def biography(request):
    """displays biography page"""
    return render(request, 'biography.html')

def life_and_education(request):
    """displays life and education page"""
    return render(request, 'life_and_education.html')

def anc_youth(request):
    """displays anc youth page"""
    return render(request, 'anc_youth.html')




