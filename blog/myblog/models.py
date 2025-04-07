from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from django.db import models
from django.utils.text import slugify
from unidecode import unidecode
class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)  # Nazwa kategorii (z polskimi znakami)
    slug = models.SlugField(max_length=255, unique=True, blank=True)  # URL-friendly wersja

    def save(self, *args, **kwargs):
        if not self.slug:  # Tworzenie sluga tylko jeśli nie został ustawiony
            self.slug = slugify(unidecode(self.name))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cats': self.slug})

class Post(models.Model):
    title = models.CharField(max_length=100)
    title_tag = models.CharField(max_length=100, default='test')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    post_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=255, default = 'test')
    category_slug = models.SlugField(max_length=255, default = 'test')

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        #return reverse('article-detail', args=(str(self.id)))
        return reverse('home')