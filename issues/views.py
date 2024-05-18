from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Issue, Status

class IssueBoardView(ListView):
    template_name = "issues/board.html"
    model = Issue

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        to_do = Status.objects.get(name="to do")
        in_progress = Status.objects.get(name="in progress")
        done = Status.objects.get(name="done")

        context["to_do_list"] = Issue.objects.filter(
            status=to_do
        ).order_by("created_on").reverse()
        context["in_progress_list"]= Issue.objects.filter(
            status=in_progress
        ).order_by("created_on").reverse()
        context["done_list"]= Issue.objects.filter(
            status=done
        ).order_by("created_on").reverse()
        context['user'] = self.request.user

        return context


class StatusUpdateView(UpdateView):
    template_name = "issues/edit.html"
    model = Issue
    fields = ["status"]
    success_url = reverse_lazy("board")


class IssueCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    template_name = "issues/new.html"
    model = Issue
    fields = ["name", "sumaaary", "description", "assigne"]
    success_url = reverse_lazy("board")

    def test_func(self):
        return self.request.user.role.name == "product owner"
    
    def form_valid(self, form):
        form.instance.reporter = self.request.user
        form.instance.Status = "to do"
        return super().form_valid(form)