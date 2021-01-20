from django.db import models
from django.urls import reverse
class Contact(models.Model):
   sno = models.AutoField(primary_key=True)
   name = models.CharField(max_length=255)
   phone = models.CharField(max_length=255)
   email = models.CharField(max_length=20)
   content = models.TextField()
   timestamp = models.DateTimeField(auto_now_add=True, blank=True)

   def __str__(self):
       return 'Message from '+self.name+'-'+self.email


    
    