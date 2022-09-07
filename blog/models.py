from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=255)
    article_img = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100,default="")
    field = models.CharField(max_length=50,default="")
    slug = models.SlugField()
    intro = models.TextField()
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added']

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date_added']

class subscriber(models.Model):
    date_added = models.DateTimeField(auto_now_add=True)
    email = models.EmailField()

class feedback(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)


class students(models.Model):
    firstname= models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)