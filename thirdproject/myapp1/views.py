from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def my_view(request):
    msg="Response from myapp1"
    return HttpResponse(msg)