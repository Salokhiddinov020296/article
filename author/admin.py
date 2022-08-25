from django.contrib import admin

from author.models import AuthorModel, ArchiveModel


@admin.register(AuthorModel)
class AuthorModelAdmin(admin.ModelAdmin):
    list_display = ['name_uz', 'name_en', 'name_ru', 'content_uz', 'content_en', 'content_ru']


@admin.register(ArchiveModel)
class ArchiveModelAdmin(admin.ModelAdmin):
    list_display = ['volume', 'issue', 'date']