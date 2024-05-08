from django.http import HttpResponse
from django.shortcuts import render



# Create your views here.

def biography(request):
    """this function displays the biography of malema """
    return render(request, 'biography.html')

def life_and_education(request):
    """this function displays the life and education of malema """
    return render(request, 'life_and_education.html')

def anc_youth(request):
    """this function displays the anc youth of malema that he was part of ."""
    return render(request, 'anc_youth.html')




