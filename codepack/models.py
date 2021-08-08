from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=130)
    excert = models.CharField(max_length=300)
    content = models.TextField()
    timeStamp = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=130)
    publish = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title

class Category(models.Model):
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.category

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rate=models.IntegerField(default=0)
    def __str__(self):
        return f'{self.user}'

class HomeModel(models.Model):
    title = models.CharField(max_length=255)
    overview = models.TextField()
    time_uploade = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    thumbnail=models.ImageField(upload_to = 'thumbnails')
    publish = models.BooleanField()
    Categories = models.ManyToManyField(Category)
    read=models.IntegerField(default=0)

    class Meta:
        ordering=['-pk']
    def __str__(self):
        return self.title