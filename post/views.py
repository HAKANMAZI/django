from django.shortcuts import render, HttpResponse


def post_index(request):
    return HttpResponse('<b>index sayfası</b>')

def post_detail(request):
    return HttpResponse('<b>detail sayfası</b>')

def post_create(request):
    return HttpResponse('<b>create sayfası</b>')
def post_delete(request):
    return HttpResponse('<b>post_delete sayfası</b>')
def post_update(request):
    return HttpResponse('<b>post_update sayfası</b>')