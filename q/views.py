from django.shortcuts import render

def index_page(reguest):
    return render(reguest, 'index.html')

def about_page(reguest):
    return render(reguest, 'about.html')


# Create your views here.
