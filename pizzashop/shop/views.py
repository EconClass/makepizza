from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


def home(request):
    return render(request, 'shop/home.html', {})