from django.http import HttpResponse


def index(request):
    return HttpResponse("<h3>Hello, world. you're at the polls index.<h3>")
