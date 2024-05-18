from django.urls import path
from issues import views

urlpatterns = [
    path("", views.IssueBoardView.as_view(), name="board"),
    path("issue/<int:pk>/status/", views.StatusUpdateView.as_view(), name="update_status"),
    path("new/", views.IssueCreateView.as_view(), name="new"),

]
