```py
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    name = 'Your-Name'
    respString = "Hello, %s. You're at the polls index."%(name)
    resp = HttpResponse(respString)
    return resp
```
