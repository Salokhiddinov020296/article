from django.contrib import admin

from author.models import AuthorModel


@admin.register(AuthorModel)
class AuthorModelAdmin(admin.ModelAdmin):
    list_display = ['name_uz', 'name_en', 'name_ru', 'content_uz', 'content_en', 'content_ru']
