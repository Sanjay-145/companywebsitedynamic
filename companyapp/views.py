from django.shortcuts import render
from .models import people
from .models import products
# Create your views here.
def home(request):
    context = {}
    return render(request, 'companyapp/home.html', context)

def productslist(request):
    context = {}
    context['productss'] = products.objects.all()
    return render(request, 'companyapp/products.html', context)    

def peoplelist(request):
    context = {}
    context['peoples'] = people.objects.all()
    return render(request, 'companyapp/people.html', context)

def contact(request):
    context = {}
    return render(request, 'companyapp/contactus.html', context)    