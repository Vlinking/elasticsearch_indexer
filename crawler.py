from api import InstagramAPI


if __name__ == '__main__':

    api = InstagramAPI(
        credentials='credentials',
        secrets='client_secrets.json',
        scope='public_content',
        redirect="http://www.contman.pl/"
    )

    api.authorize()
    request = api._request('https://api.instagram.com/v1/tags/search?q=snowy')

    # need first to install BlueStacks to emulate Android and upload to Instagram, my tablet
    # is TOAST...
    request2 = api._request('https://api.instagram.com/v1/tags/nofilter/media/recent')


