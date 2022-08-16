from django.http import HttpResponse
from django.utils.translation import gettext_lazy


def hello(request):

    return HttpResponse(gettext_lazy("who is your dad ？"))



