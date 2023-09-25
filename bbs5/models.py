from django.db import models

# Create your models here.
class Bbs(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    author=models.CharField(max_length=50)
    created=models.DateTimeField(auto_now_add=True)