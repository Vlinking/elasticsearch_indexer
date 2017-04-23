from datetime import datetime
from elasticsearch_doctype import Photo


class PhotoSerializer(object):
    """
    A class to translate photo data from Instagram's JSON into Elasticsearch's JSON.
    """
    @classmethod
    def serialize(cls, data):
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

        photo.save()

