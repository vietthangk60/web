from django.shortcuts import render
from django.http import HttpRequest
# Create your views here.
def func_Mainview(request, *args, **kwargs): # *args, **kwargs
   # print(args, kwargs)
   # print(request.user)
    #return HttpResponse("<h1>Hello World</h1>") # string of HTML code
    return render(request, "index.html", {})