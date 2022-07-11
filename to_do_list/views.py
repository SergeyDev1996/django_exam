from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

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
    # tag1 = Tag.objects.create(name="Coding")
    # tag1.save()
    # tag2 = Tag.objects.create(name="Workout")
    # tag2.save()
    # a = Task.objects.create(content="Buy 3 carrots and 1 pineapple", is_done=False)
    # a.save()
    # a.tags.add(tag1)
    # a.tags.add(tag2)
    # a.save()
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
    success_url = reverse_lazy("to_do_list:tags-list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = "__all__"
    template_name = "to_do_list/task_update.html"
    success_url = reverse_lazy("to_do_list:tags-list")

class TaskCreateView(generic.CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("to_do_list:index")
    template_name = "to_do_list/task_create.html"

def task_status_update(request, pk, operation):

    task = Task.objects.get(id=pk)
    if operation == "Complete":
        task.is_done = 1
    elif operation == "Undo":
        task.is_done = 0
    task.save()
    return HttpResponseRedirect(reverse_lazy("to_do_list:index"))