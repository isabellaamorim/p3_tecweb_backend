from django.http import HttpResponse


def index(request):
    return HttpResponse("Olá mundo! Este é o projeto 3 de Tecnologias Web do Insper.")