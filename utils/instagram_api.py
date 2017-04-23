import json
import webbrowser
import httplib2
from urllib import urlencode
from urlparse import urlsplit, parse_qs
from oauth2client import client
from oauth2client.file import Storage


class InstagramAPI(object):
    """
    Class for accessing Instagram API endpoints.
    Due to the constraints with Sandbox mode, we can't really do much with data or users.
    """
    CORE_URL = 'https://api.instagram.com/v1/'
    SELF_RECENT_MEDIA_URL = 'users/self/media/recent'
    TAG_MEDIA_URL = 'tags/{0}/media/recent'

    def __init__(self, credentials='', secrets='', scope='', redirect=''):
        """
        Sets inital data
        """
        self.credentials = credentials
        self.secrets = secrets
        self.scope = scope
        self.redirect = redirect
        self.storage = Storage(self.credentials)

    def authorize(self):
        """
        Handler for establishing connection and getting credentials.
        """
        _flow = client.flow_from_clientsecrets(self.secrets, self.scope, self.redirect)
        _credentials = self.storage.get()

        # If there are no credentials, the library gives us a warning instead of error
        if not _credentials:
            _auth_uri = _flow.step1_get_authorize_url()
            webbrowser.open(_auth_uri)
            _auth_code = raw_input("Enter the authorization code from the url")
            _credentials = _flow.step2_exchange(_auth_code)
            self.storage.put(_credentials)

        self.credentials = _credentials

    def _add_parameter(self, uri, parameter, value):
        """
        Add parameter to the url.
        """
        url_data = urlsplit(uri)
        qs_data = parse_qs(url_data.query)

        if not parameter in qs_data:
            qs_data[parameter] = value

        return url_data._replace(query=urlencode(qs_data, True)).geturl()

    def _request(self, uri):
        """
        Wrap request to add auth_token, I found oauth2client library has problems with it.
        """
        _http = httplib2.Http()
        uri = self.CORE_URL + uri
        uri = self._add_parameter(uri, 'access_token', self.credentials.access_token)
        return json.loads(_http.request(uri, method="GET")[1])['data']

    def get_recent_media(self):
        """
        Make a request for recent media of our user.
        """
        return self._request(self.SELF_RECENT_MEDIA_URL)

    def get_tag_media(self, tag):
        """
        Make a request for current user's media.
        """
        return self._request(self.TAG_MEDIA_URL.format(tag))