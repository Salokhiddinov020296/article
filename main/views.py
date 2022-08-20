from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from post.models import AclassModel


class MainIndexView(ListView):
    template_name = 'index.html'
    paginate_by = 5

    def get_queryset(self):
        qs = AclassModel.objects.all()
        name = self.request.GET.get('name')
        if name:
            qs = qs.filter(writer__icontains=name)
        return qs
