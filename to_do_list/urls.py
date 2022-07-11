from django.urls import path, include
from .views import TagsListView, TagsDeleteView, TagsUpdateView, TagsCreateView, TaskListView, TaskDeleteView, TaskUpdateView, task_status_update

urlpatterns = [
    path("", TaskListView.as_view(), name="index"),
    path("tags/", TagsListView.as_view(), name="tags-list"),
    path("tags/<int:pk>/delete", TagsDeleteView.as_view(), name="tags_delete"),
    path("tags/<int:pk>/update", TagsUpdateView.as_view(), name="tags-update"),
    path("tags/create", TagsCreateView.as_view(), name="tags-create"),
    path("task/<int:pk>/delete", TaskDeleteView.as_view(), name="task-delete"),
    path("task/<int:pk>/update", TaskUpdateView.as_view(), name="task-update"),
    path("task/<int:pk>/<operation>/", task_status_update, name="status-update"),
]

app_name = "to_do_list"