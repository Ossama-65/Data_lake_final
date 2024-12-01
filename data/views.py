from django.http import JsonResponse

def home(request):
    return JsonResponse({"message": "Bienvenue dans votre API Data Lake"})
from django.shortcuts import render

# Create your views here.
