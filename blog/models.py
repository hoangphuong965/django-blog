from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title

    # noi cho django biet sau khi post-new duoc tao se reverse url post-detail
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

class About(models.Model):
    content = models.TextField()

    def __str__(self) -> str:
        return "about_content"