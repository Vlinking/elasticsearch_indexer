from django.views.generic import TemplateView


class IndexView(TemplateView):
    """
    Index view for the main search app page.
    """
    template_name = 'instagram_browser/index.html'