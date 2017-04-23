from elasticsearch_api import PhotoSerializer, ElasticsearchAPI
from instagram_api import InstagramAPI


if __name__ == '__main__':
    instagram_api = InstagramAPI(
        credentials='credentials',
        secrets='client_secrets.json',
        scope='public_content',
        redirect="http://www.contman.pl/"
    )
    elasticsearch_api = ElasticsearchAPI(
        serializer=PhotoSerializer,
        hosts=['localhost']
    )
    instagram_api.authorize()
    media = instagram_api.get_recent_media()
    for photo in media:
        elasticsearch_api.serialize(photo)

    response = elasticsearch_api.search('quake')


