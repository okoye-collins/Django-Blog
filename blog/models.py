from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200, null=True, blank=True)
    profile_pic = models.ImageField(null=True, blank=True, upload_to = "Profile")
    bio = models.TextField(null=True, blank=True)
    facebk_link = models.URLField(max_length=250, null=True, blank=True)

    def __str__(self):
        name = str(self.first_name)
        if self.last_name:
            name = " " + str(self.last_name )
        return name

class ArticleManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status = "published")

class Tag(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

class Article(models.Model):
    article_status = (
        ('published', 'published'),
        ('draft', 'draft')
    )

    author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name= 'author')
    headline = models.CharField(max_length=200, null=True, blank=True)
    sub_headline = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField( null=True, blank=True ,upload_to = "article_pic", default="placeholder.png")
    body = RichTextUploadingField(null=True, blank=True)
    tag = models.ManyToManyField(Tag, blank=True)
    featured = models.BooleanField(default=False)
    #unique_for_date ensures that there will be only one post with a slug for a given date, thus we can retrieve single posts using date and slug
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    publish = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=150, choices=article_status, default='draft')

    objects = models.Manager() # default manager
    articlemanager = ArticleManager() #custom manager

    def get_absolute_url(self):
        return reverse('blog:article', args=[self.slug])

    class Meta:
        ordering = ['-publish']

    def __str__(self):
        return self.headline