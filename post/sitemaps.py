from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from .models import AclassModel

class ArticleSitemap(Sitemap):
    limit = AclassModel.objects.all().count()
    def items(self):
        return AclassModel.objects.all()

    def location(self, obj):
        return reverse('detail', args=[str(obj.id)])
