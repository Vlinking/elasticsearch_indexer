from datetime import datetime
from elasticsearch_dsl import Search
from elasticsearch_dsl.connections import connections

from elasticsearch_doctype import Photo


class PhotoSerializer(object):
    """
    A class to translate photo data from Instagram's JSON into Elasticsearch's JSON.
    """
    def serialize(self, data):
        """
        Fill in all the necessary fields.
        """
        photo = Photo(
            text=data['caption']['text'],
            from_user=data['caption']['from']['username'],
            thumbnail=data['images']['thumbnail']['url'],
            image=data['images']['standard_resolution']['url'],
            created_time=datetime.fromtimestamp(float(data['created_time'])).strftime('%Y-%m-%d %H:%M:%S')
        )

        # add tags similarly to related fields in Django ORM
        for tag in data['tags']:
            photo.add_tag(tag)

        photo.meta.id = data['id']
        photo.save()


class ElasticsearchAPI(object):
    """
    Class that wraps all communication to Elasticsearch via a given serializer.
    """
    def __init__(self, serializer=None, hosts=None):
        """
        Set serializer that will allow us to store data.
        """
        self.serializer = serializer()
        connections.create_connection(hosts=hosts)

    def serialize(self, data):
        """
        Composition wrapper for serialize.
        """
        self.serializer.serialize(data)

    def search(self, keyword):
        """
        Wrapper for search.
        """
        _query = Search().query("match", text=keyword)
        return _query.execute()