from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='project_owner')
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)


class Participant(models.Model):
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='participant_project')
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='participant_user')


class Todo(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=500)
    status = models.IntegerField(default=0)
    creator = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='creator')
    create_date = models.DateTimeField(auto_now_add=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()


class Worker(models.Model):
    todo = models.ForeignKey(
        Todo,
        on_delete=models.CASCADE,
        related_name='worker_todo')
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='worker_user')