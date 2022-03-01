from django.shortcuts import render

# Create your views here.
from django.http import HttpRequest

# Create your views here.
def func_VieccuatoiView(request, *args, **kwargs): # *args, **kwargs
   # print(args, kwargs)
   # print(request.user)
    #return HttpResponse("<h1>Hello World</h1>") # string of HTML code
    return render(request, "vieccuatoi.html", {})
def func_DuanView(request, *args, **kwargs): # *args, **kwargs
   # print(args, kwargs)
   # print(request.user)
    #return HttpResponse("<h1>Hello World</h1>") # string of HTML code
    return render(request, "duan.html", {})