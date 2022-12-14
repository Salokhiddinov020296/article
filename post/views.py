from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from post.models import AclassModel

def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)

class PostDetailView(DetailView):
    template_name = 'post/detail.html'

    def get_queryset(self):
        qs = AclassModel.objects.all().order_by('-date')
        return qs


class JournalView(TemplateView):
    template_name = 'post/journal.html'


class MeetingsView(ListView):
    template_name = 'post/meetings.html'
    paginate_by = 5

    def get_queryset(self):
        qs = AclassModel.objects.all().order_by('-date')
        name = self.request.GET.get('name')
        if name:
            qs = qs.filter(writer__icontains=name).order_by('-date')
        return qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get('name')
        if name:
            context['name'] = name
        return context


class ArxivView(ListView):
    template_name = 'post/../templates/author/arxiv.html'

    def get_queryset(self):
        qs = AclassModel.objects.all().order_by('-date')
        return qs


class SendArticleView(TemplateView):
    template_name = 'post/send_article.html'


class ScienceView(TemplateView):
    template_name = 'post/science.html'


class InnovationView(TemplateView):
    template_name = 'post/innovation.html'


class GiftsView(TemplateView):
    template_name = 'post/gift.html'


class ContactUsView(TemplateView):
    template_name = 'post/contact.html'


class VacancyView(TemplateView):
    template_name = 'post/vacancy.html'


class ScienceBaseView(TemplateView):
    template_name = 'post/science_base.html'


class ImpactFactorView(TemplateView):
    template_name = 'post/impact_factor.html'
