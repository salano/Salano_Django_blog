from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE) # delete all posts when user is deleted

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        # pk (default primay key) is the parameter of the post-detail route
        return reverse('post-detail', kwargs={'pk': self.pk})
    
