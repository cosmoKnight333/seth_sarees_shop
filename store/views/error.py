from django.shortcuts import render

def error_400(request, exception):
    return render(request, 'error404.html', status=400)

def error_404(request, exception):
    return render(request, 'error404.html', status=404)

def error_500(request):
    return render(request, 'error404.html', status=500)