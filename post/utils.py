import os
from django.conf import settings
from django.core.files.storage import default_storage
from django.db.models import FileField, ImageField

def file_cleanup(sender, **kwargs):
    for field in sender._meta.get_fields():
        if isinstance(field, FileField) or isinstance(field, ImageField):
            inst = kwargs["instance"]
            f = getattr(inst, field.name)
            try:
                default_storage.delete(f.path)
                print(f.path,"fpath")
            except Exception as e:
                try:
                    filepath = settings.MEDIA_ROOT+"/"+str(f)
                    default_storage.delete(filepath)
                    print(str(filepath), "f")
                except Exception as e:
                    print(e, " e")
