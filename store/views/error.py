from django.shortcuts import render
from .data import initial_data

def error_400(request, exception):
    data= initial_data
    return render(request, 'error404.html', data,status=400)


def error_500(request):
    data=initial_data
    return render(request, 'error500.html', data,status=500)