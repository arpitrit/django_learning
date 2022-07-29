from django import http
from django.shortcuts import HttpResponse


def index(request):
    power = request.GET['number']
    power = int(power)**2
    print(power)
    # return HttpResponse(f'<h1>Hello {fname} {lname}</h1>')
    return HttpResponse(f'<h1>{power}</h1>')


# def common(request):
#     return HttpResponse('<h1>Welcome Everyone</h1>')