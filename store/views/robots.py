from django.http import HttpResponse

def robots(request):
    content = "User-agent: *\nDisallow: /admin/ \n\nSitemap: http://127.0.0.1:8000/sitemap.xml"
    return HttpResponse(content, content_type="text/plain")