from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.core.paginator import Paginator
from django.shortcuts import redirect

from .forms import HelloForm, FindForm, MessageForm, FriendForm

from .models import Friend, Message


def check(request):
    params = {
        'title': 'Hello',
        'message':'check validation.',
        'form': FriendForm(),
    }
    if (request.method == 'POST'):
        obj = Friend()
        form = FriendForm(request.POST, instance=obj)
        params['form'] = form
        if (form.is_valid()):
            params['message'] = 'OK!'
        else:
            params['message'] = 'no good.'
    return render(request, 'hello/check.html', params)


class HelloView(TemplateView):

    def __init__(self):
        self.params = {
            'title': 'Hello',
            # 'message': 'your data:',
            'form': HelloForm(),
            'result': None
        }

    def get(self, request):
        return render(request, 'hello/index.html', self.params)

    def post(self, request):
        # msg = '名前：' + request.POST['name'] + \
        #     '<br>メール：' + request.POST['mail'] + \
        #     '<br>年齢：' + request.POST['age']
        # self.params['msg'] = msg
        chk = request.POST['check']
        self.params['result'] = 'you selected: "' + chk + '"'
        self.params['form'] = HelloForm(request.POST)
        return render(request, 'hello/index.html', self.params)


def index(request, num=1):
    data = Friend.objects.all()
    page = Paginator(data, 3)
    params = {
        'title': 'Hello',
        'message': '',
        'data': page.get_page(num),
    }
    return render(request, 'hello/index.html', params)


# create model
def create(request):
    params = {
        'title': 'Hello',
        'form': FriendForm(),
    }
    if (request.method == 'POST'):
        obj = Friend()
        friend = FriendForm(request.POST, instance=obj)
        friend.save()
        return redirect(to='/hello')
    return render(request, 'hello/create.html', params)


# edit model
def edit(request, num):
    obj = Friend.objects.get(id=num)
    if (request.method == 'POST'):
        friend = FriendForm(request.POST, instance=obj)
        friend.save()
        return redirect(to='/hello')
    params = {
        'title': 'Hello',
        'id': num,
        'form': FriendForm(instance=obj),
    }
    return render(request, 'hello/edit.html', params)


# delete model
def delete(request, num):
    friend = Friend.objects.get(id=num)
    if (request.method == 'POST'):
        friend.delete()
        return redirect(to='/hello')
    params = {
        'title': 'Hello',
        'id': num,
        'obj': friend,
    }
    return render(request, 'hello/delete.html', params)


# find model
def find(request):
    if (request.method == 'POST'):
        msg = request.POST['find']
        form = FindForm(request.POST)
        sql = 'select * from hello_friend'
        if (msg != ''):
            sql += ' where ' + msg
        data = Friend.objects.raw(sql)
        msg = sql
    else:
        msg = 'search words...'
        form = FindForm()
        data = Friend.objects.all()
    params = {
        'title': 'Hello',
        'message': msg,
        'form': form,
        'data': data,
    }
    return render(request, 'hello/find.html', params)


def message(request, page=1):
    if (request.method == 'POST'):
        obj = Message()
        form = MessageForm(request.POST, instance=obj)
        form.save()
    data = Message.objects.all().reverse()
    paginator = Paginator(data, 5)
    params = {
        'title': 'Message',
        'form': MessageForm(),
        'data': paginator.get_page(page),
    }
    return render(request, 'hello/message.html', params)


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
