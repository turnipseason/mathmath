from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound


def my_page_not_found_view(request, exception):
    #return HttpResponseNotFound('<h1>Всё очень грустно, ничего не работает, страницы нет :(</h1>')
    # а ещё можно же было return redirect('home') прописать, хмм...
    return render(request, '404.html', status=404)


def my_server_error_view(request):
    #return HttpResponseNotFound('<h1>Всё прям совсем грустно :(</h1>')
    return render(request, '500.html', status=500)