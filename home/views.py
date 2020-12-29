from django.shortcuts import render, HttpResponse

def home_view(request):
    context = {
        'isim':'hakan', 
        'soyisim':'Mazi',
    }

    return render(request, 'home.html', context)
