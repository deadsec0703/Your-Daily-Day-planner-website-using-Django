from django.db import models
from django.contrib.auth.models import User

class TodoModel(models.Model):
    task = models.TextField(primary_key=True)
    deadline = models.CharField(max_length=50)
    Note = models.TextField(max_length=50) # btw, make this attribute lowercase
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.task