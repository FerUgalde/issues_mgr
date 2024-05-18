from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


class Status(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=256)

    def __str__(self):
        return self.name
    

class Issue(models.Model):
    name = models.CharField(max_length=128)
    sumaaary = models.CharField(max_length=256)
    description = models.TextField()
    reporter = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name="reporter"
    )
    assigne = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name="assignee"
    )
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, default=1)
    is_done = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse("detail", args=[self.id])
    
    def __str__(self):
        return self.name
