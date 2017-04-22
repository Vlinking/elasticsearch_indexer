import json
from instagram_api import InstagramAPI


if __name__ == '__main__':

    api = InstagramAPI(
        credentials='credentials',
        secrets='client_secrets.json',
        scope='public_content',
        redirect="http://www.contman.pl/"
    )

    api.authorize()
    media = api.get_recent_media()
    for photo in media:
        print(photo)

    media2 = api.get_tag_media('vidya')
    for photo in media2:
        print(photo)




