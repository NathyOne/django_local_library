from django.db import models

# Create your models here.

from django.http import HttpResponse

def index(request):
    return HttpResponse("Catalog app is working! 🎉")