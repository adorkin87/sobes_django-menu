from django.shortcuts import render

def index(request):
    template = 'mainsite/index.html'
    return render(request, template)

def pages(request, url_pages):
    template = 'mainsite/pages.html'
    context = {'slug': url_pages}
    return render(request, template, context)
