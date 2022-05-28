from django.shortcuts import render
from django.http import HttpResponse

def first(request):
    return render(request, 'web/index1.html')

def second(request):
    return render(request, 'web/indexNEWS.html')

def third(request):
    return render(request, 'web/indexDISCO.html')

def fourth(request):
    return render(request, 'web/indexBIO.html')

def fifth(request):
    return render(request, 'web/indexSCHEDULE.html')

def sixth(request):
    return render(request, 'web/indexMEDIA.html')

def seventh(request):
    return render(request, 'web/indexBLOG.html')

def eighth(request):
    return render(request, 'web/indexGOODS.html')


