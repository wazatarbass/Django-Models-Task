from time import timezone
from django.db import models

# Create your models here.
class Post(models.Model):
    Title = models.CharField(max_length=200)
    Text =  models.TextField(max_length=300)
    Author = models.ForeignKey('auth.User', on_delete=models.CASCADE,)
    Created_date = models.DateTimeField(auto_now_add=True)
    Published_date =models.DateTimeField(default=timezone.now)
    
    def __str__(self):
     return self.Title
    