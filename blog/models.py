from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    #if user is deleted, delete all their posts
    #research ForeignKey

    #special method in OOP python
    def __str__(self):
        return self.title

    #use reverse function to return the full url to a route as a string
    #let view handle url for us
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
