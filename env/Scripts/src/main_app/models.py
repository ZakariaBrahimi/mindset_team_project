from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.utils.text import slugify
import datetime
# Create your models here.

class Post(models.Model):
    user    = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    slug    = models.SlugField(blank=True, null=True)
    title   = models.CharField(max_length=50)
    content = models.TextField()
    created = models.DateTimeField(blank = True, default= datetime.datetime.now)
    # tags    = models.CharField(blank=True, max_length = 100)
    img     = models.ImageField(upload_to='notes_img', blank=True, null=True)
    active = models.BooleanField(default=False)

    def save(self, *arg, **kwarg):
        if not self.slug :
            self.slug = slugify(self.title)
        super(Post, self).save(*arg, **kwarg)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title

class Contact(models.Model):
    msg = models.TextField()
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50,blank=True, null=True)
    subject = models.CharField(max_length=50)
    def __str__(self):
        return self.email

class Comment(models.Model):
    comment = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.comment

class Story(models.Model):
    user    = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    slug    = models.SlugField(blank=True, null=True)
    title   = models.CharField(max_length=50)
    content = models.TextField()
    created = models.DateTimeField(blank = True, auto_now_add=True, auto_now=False)
    # tags    = models.CharField(blank=True, max_length = 100)
    Image     = models.ImageField(upload_to='stories_img', blank=True, null=True)
    Video = models.FileField(upload_to='stories_videos', blank=True, null=True)
    # comments = models.ForeignKey(Comment, on_delete=models.SET_NULL, blank=True, null=True)
    active = models.BooleanField(default=False)

    def save(self, *arg, **kwarg):
        if not self.slug :
            self.slug = slugify(self.title)
        super(Story, self).save(*arg, **kwarg)
    
    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title


class Appointment(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    typee = models.CharField(max_length=50, blank=True, null=True)
    time = models.CharField(max_length=50, blank=True, null=True)
    text = models.CharField(max_length=1000, blank=True, null=True)
    def __str__(self):
        return self.name