from django.urls import path

from author.views import AuthorListView, ArchiveView

app_name = 'author'

urlpatterns = [
    path('', AuthorListView.as_view(), name='author'),
    path('archive/', ArchiveView.as_view(), name='arxiv')
]