from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def fun1(request):
    B = {'buses':[
    {'name': 'bus1', 'area':'Dharmavaram'},
    {'name': 'bus13', 'area':'Rudrampeta Bypass'},
    {'name': 'bus10', 'area':'Kalyandurgam Bypass'}
]}
    return render(request,'info.html',B)
