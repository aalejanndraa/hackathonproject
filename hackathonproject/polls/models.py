from django.db import models
import datetime

# Create your models here.
class User(models.Model):
  username = models.CharField(max_length = 20)
  password = models.CharField(max_length = 20)


class Post(models.Model): 
  title_text = models.CharField(max_length=200)
  body_text = models.CharField(max_length=500)
  pub_date = models.DateTimeField('date published')
  votes = models.IntegerField(default=0)
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Comment(models.Model):
  body_text = models.CharField(max_length=500)
  post = models.ForeignKey(Post, on_delete=models.CASCADE)
  parentcomment = models.ForeignKey('Comment', on_delete=models.CASCADE)
  votes = models.IntegerField(default=0)
  author = models.ForeignKey(User, on_delete=models.CASCADE)

from django.db import models
from django.utils import timezone

