from elasticsearch_api import PhotoSerializer
from elasticsearch_doctype import Photo
from instagram_api import InstagramAPI
from elasticsearch_dsl.connections import connections


if __name__ == '__main__':
    api = InstagramAPI(
        credentials='credentials',
        secrets='client_secrets.json',
        scope='public_content',
        redirect="http://www.contman.pl/"
    )

    connections.create_connection(hosts=['localhost'])

    Photo.init()
    api.authorize()
    media = api.get_recent_media()
    for photo in media:
        PhotoSerializer.serialize(photo)

    # media2 = api.get_tag_media('vidya')
    # for photo in media2:
    #     print(photo)

    print(connections.get_connection().cluster.health())

