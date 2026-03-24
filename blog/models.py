from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    CATEGORY_CHOICES = [
        ('news', 'News'),
        ('diary', 'Diary'),
        ('dev', 'Dev Log'),
        ('music', 'Music'),
        ('art', 'Art'),
        ('world', 'World'),
    ]

    title = models.CharField(max_length=200)
    content = models.TextField()
    # slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(default=timezone.now)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.title