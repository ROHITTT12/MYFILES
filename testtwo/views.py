from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def m1(request):
    return render(request,'i hate you.html')
def f(request):
    return render(request,'f.html')
def c(request):
    return render(request,'input.html')
def cal(request):
    v1=request.GET['display']
    print(v1)
    i=eval(v1)
    return render(request,'count.html', {'t1':i}  )

def m2(request):
    return render(request,'input1.html')
def ascii(request):
    y=request.GET['t1']
    z=request.GET['t2']
    r=request.GET['top']
    if r=="U":
        z=int(y)
        a=chr(z)
        return render(request,'count2.html',{'result':a})
    elif r=="C":
        h=ord(z)
        return render(request,'count2.html',{'result':h})