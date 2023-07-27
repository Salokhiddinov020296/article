import os
from django.core.files.storage import default_storage
from django.db.models import FileField

def file_cleanup(sender, **kwargs):
    for field in sender._meta.get_fields():
        if isinstance(field, FileField):
            inst = kwargs["instance"]
            f = getattr(inst, field.name)
            m = inst.__class__._default_manager
            try:
                if hasattr(f, "path") and os.path.exists(f.path) and not m.filter(**{field.name: f}).exclude(pk=inst._get_pk_val()):
                    try:
                        default_storage.delete(f.path)
                    except:
                        pass
            except Exception as e:
                print(e)
                pass
