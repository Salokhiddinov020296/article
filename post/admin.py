from django.contrib import admin

from .forms import ClassModelAdmin
from .models import WhichLanguageWriteModel, AclassModel, FieldModel, PropagandistModel



@admin.register(FieldModel)
class FieldModel(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']
    search_fields = ['name']


@admin.register(PropagandistModel)
class PropagandistModelAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_link = ['name']
    search_fields = ['name']


@admin.register(WhichLanguageWriteModel)
class WhichLanguageWriteModelAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']
    search_fields = ['name']


@admin.register(AclassModel)
class AclassModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'article_pdf', 'certificate','volume', 'issue', 'pages', 'article_name_uz','article_name_en',
                    'article_name_ru', 'field', 'language',
                    'date', 'promoter']
    list_display_links = ['id', 'article_pdf', 'certificate','volume', 'issue', 'pages','field',
                          'language', 'date', 'promoter']
    list_filter = ['date']
    search_fields = ['author1',]
