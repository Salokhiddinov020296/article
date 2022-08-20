from django.shortcuts import render
from django.views.generic import ListView

from author.models import AuthorModel


class AuthorListView(ListView):
    template_name = 'author/author.html'
    paginate_by = 10

    def get_queryset(self):
        qs = AuthorModel.objects.all()
        return qs
