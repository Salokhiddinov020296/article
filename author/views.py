from django.shortcuts import render
from django.views.generic import ListView

from author.models import AuthorModel, ArchiveModel


class AuthorListView(ListView):
    template_name = 'author/author.html'
    paginate_by = 10

    def get_queryset(self):
        qs = AuthorModel.objects.all()
        return qs


class ArchiveView(ListView):
    template_name = 'author/arxiv.html'

    def get_queryset(self):
        qs = ArchiveModel.objects.all()
        return qs
