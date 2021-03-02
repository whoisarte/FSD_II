from django.views.generic.base import TemplateView

class HomePageView(TemplateView):
    template_name = 'index.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

class ContentPageView(TemplateView):
    template_name = 'content.html'
