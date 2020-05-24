from django.contrib import admin
from .models import Project, Participant, Todo, Worker

admin.site.register(Project)
admin.site.register(Participant)
admin.site.register(Todo)
admin.site.register(Worker)
