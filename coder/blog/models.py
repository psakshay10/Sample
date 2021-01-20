from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from ckeditor.fields import RichTextField
from django.urls import reverse
class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    content = RichTextField(blank=True , null=True)
    author = models.CharField(max_length=20)
    slug = models.CharField(max_length=200)
    views = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
       return self.title+' by '+self.author
    
    def get_absolute_url(self):
        return reverse('addpost')
    

class BlogComment(models.Model):
    sno = models.AutoField(primary_key= True)
    comment = models.TextField()     
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
       return self.comment[0:13] + ' .... '+ "by " + self.user.username
    

   