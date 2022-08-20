from django.db import models
from django.utils.translation import get_language
from django.utils.translation import gettext_lazy as _


class AuthorModel(models.Model):
    name_uz = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255)
    name_ru = models.CharField(max_length=255)
    image = models.ImageField(upload_to='media/author/')
    content_uz = models.TextField(blank=True)
    content_en = models.TextField(blank=True)
    content_ru = models.TextField(blank=True)

    def __str__(self):
        return self.name_uz

    @property
    def name(self):
        return getattr(self, f"name_{get_language()}")

    @property
    def content(self):
        return getattr(self, f"content_{get_language()}")
