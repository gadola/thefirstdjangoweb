from django.db import models
from django.conf import settings
# Create your models here.
class Post(models.Model):
    objects = models.Manager()
    title = models.CharField( max_length=150)
    body = models.TextField()
    date = models.DateTimeField( auto_now=True, auto_now_add=False)
    image = models.ImageField((""), upload_to=None, height_field=None, width_field=None, max_length=None, null=True)
    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE, related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    body = models.TextField()
    time = models.DateField( auto_now=False, auto_now_add=True)