from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    # return HttpResponse("Hello Django!!")
    params = {
        'title': 'hello/index',
        'msg': 'お名前は？',
    }
    return render(request, 'hello/index.html', params)


def form(request):
    msg = request.POST['msg']
    params = {
        'title': 'hello/next',
        'msg': 'こんにちは、' + msg + 'さん。',
    }
    return render(request, 'hello/index.html', params)


def query(request):
    if 'msg' in request.GET:
        msg = request.GET['msg']
        return HttpResponse('you typed: ' + msg + '.')
    else:
        result = 'please send msg parameter!'
    return HttpResponse(result)


def query_smart(request, id, nickname):
    result = 'you id: ' + str(id) + ', name: ' + nickname + '.'
    return HttpResponse(result)


def me(request, name, age):
    result = 'your account: ' + name + '(' + str(age) + ').'
    return HttpResponse(result)
