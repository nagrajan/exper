# Create your views here.
from django.shortcuts import HttpResponse, render_to_response


def index(request):
    return render_to_response("index.html")
    #return HttpResponse("hello world")
