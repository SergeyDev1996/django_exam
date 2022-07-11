from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from templates.to_do_list.forms import TaskForm
from to_do_list.models import Tag, Task


class TaskListView(generic.ListView):
    model = Task
    template_name = "to_do_list/task_list.html"
    context_object_name = "task_list"


class TagsListView(generic.ListView):
    model = Tag
    context_object_name = "tag_list"
    template_name = "to_do_list/tag_list.html"


class TagsDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("to_do_list:tags-list")


class TagsUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    template_name = "to_do_list/tag_update_form.html"
    success_url = reverse_lazy("to_do_list:tags-list")


class TagsCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("to_do_list:tags-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("to_do_list:index")


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = "__all__"
    template_name = "to_do_list/task_update.html"
    success_url = reverse_lazy("to_do_list:index")

class TaskCreateView(generic.CreateView):
    model = Task
    fields = "__all__"
    template_name = "to_do_list/task_create.html"
    success_url = reverse_lazy("to_do_list:index")

def task_status_update(request, pk, operation):

    task = Task.objects.get(id=pk)
    if operation == "Complete":
        task.is_done = 1
    elif operation == "Undo":
        task.is_done = 0
    task.save()
    return HttpResponseRedirect(reverse_lazy("to_do_list:index"))