from django.shortcuts import render
from django.http import HttpResponse

def func1(request,q):
    d={"srit":[{"busno":q,"route":"ananthapur"},
               {"busno":q,"route":"Dharmavaram"},
               {"busno":"3","route":"Reddipalli"}]}
    return render(request,"link.html",d)


