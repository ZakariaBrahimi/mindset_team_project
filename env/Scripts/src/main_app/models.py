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
    tags    = models.CharField(blank=True, max_length = 100)
    img     = models.ImageField(upload_to='notes_img', blank=True, null=True)
    
    def save(self, *arg, **kwarg):
        if not self.slug :
            self.slug = slugify(self.title)
        super(Post, self).save(*arg, **kwarg)

    
    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title
