from django.urls import path

from main.views import MainIndexView

app_name = 'main'
urlpatterns = [
    path('', MainIndexView.as_view(), name='home')
]