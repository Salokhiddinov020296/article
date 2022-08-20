from django.urls import path

from author.views import AuthorListView

app_name = 'author'

urlpatterns = [
    path('', AuthorListView.as_view(), name='author')
]