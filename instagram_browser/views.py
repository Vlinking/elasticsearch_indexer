from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import TemplateView

from utils.elasticsearch_api import ElasticsearchAPI, PhotoSerializer


class IndexView(TemplateView):
    """
    Index view for the main search app page.
    """
    template_name = 'instagram_browser/index.html'


class ElasticsearchView(TemplateView):
    """
    View for getting the search query from Elasticsearch.
    """
    template_name = 'instagram_browser/photo.html'

    def post(self, request):
        query = str(request.POST['query'])

        elasticsearch_api = ElasticsearchAPI(
            serializer=PhotoSerializer,
            hosts=['localhost']
        )

        response = elasticsearch_api.search(query)
        data = {
            'response': response,
            'error': ElasticsearchAPI.CONNECTION_ERROR,
            'error_message': ElasticsearchAPI.CONNECTION_ERROR_MESSAGE,
        }

        return render_to_response(self.template_name, data, context_instance=RequestContext(request))