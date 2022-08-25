from django.urls import path

from post.views import JournalView, MeetingsView, SendArticleView, ScienceView, InnovationView, GiftsView, \
    ContactUsView, VacancyView, ScienceBaseView, ImpactFactorView, PostDetailView, ArxivView

app_name = 'post'

urlpatterns = [
    path('journal/', JournalView.as_view(), name='journal'),
    path('articles/', MeetingsView.as_view(), name='meetings'),
    path('send/article/', SendArticleView.as_view(), name='send_article'),
    path('science/', ScienceView.as_view(), name='science'),
    path('innovation/', InnovationView.as_view(), name='innovation'),
    path('gift/', GiftsView.as_view(), name='gift'),
    path('contact/', ContactUsView.as_view(), name='contact'),
    path('vacancy/', VacancyView.as_view(), name='vacancy'),
    path('science/base/', ScienceBaseView.as_view(), name='science_base'),
    path('impact/factor/', ImpactFactorView.as_view(), name='impact_factor'),
    path('detail/<int:pk>/', PostDetailView.as_view(), name='detail'),
]
