from django.http import HttpResponse


def index(request):
    return HttpResponse('Hello Django!')


def test(request):
    return HttpResponse('Test')