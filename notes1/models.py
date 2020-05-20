from django.db import models
from django.utils import timezone
# Create your models here.
from django.contrib.auth.models import User
from django.urls import reverse

#USER = settings.AUTH_USER_MODEL


class Category(models.Model):
    title = models.CharField(max_length=120)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog-home')




class Post(models.Model):
    title = models.CharField(max_length=120)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    favourite = models.ManyToManyField(User,related_name='favs')
    category = models.CharField(max_length=120,default='заметка')
    #categories = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail',kwargs={'pk':self.pk})
