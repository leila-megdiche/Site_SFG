from django.shortcuts import render

from django.http import HttpResponse

from django.template import loader


def Home(request):
    return render(request, 'index.html')

def AboutUs(request):
    return render(request, 'about.html')

def project(request):
    return render(request, 'project.html')

def quote(request):
    return render(request, 'quote.html')

def contact(request):
    return render(request, 'contact.html')

def service(request):
    return render(request, 'service.html')

def feature(request):
    return render(request, 'feature.html')

def testimonial(request):
    return render(request, 'testimonial.html')

def ereur(request):
    return render(request, '404.html')

def team(request):
    return render(request, 'team.html')
