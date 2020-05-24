from django.shortcuts import render
from .models import Project, Participant, Todo, Worker


def index(request):
    params = {
        'projects': Project.objects.all(),
        'participants': Participant.objects.all(),
        'todos': Todo.objects.all(),
        'workers': Worker.objects.all()
    }
    return render(request, 'todo/index.html', params)
