import json
import webbrowser
from urllib import urlencode
from urlparse import urlsplit, parse_qs

import httplib2

from oauth2client import client
from oauth2client.file import Storage


class InstagramAPI(object):
    """
    Class for accessing Instagram API endpoints.
    """
    SELF_RECENT_URL = 'https://api.instagram.com/v1/users/self/media/recent'


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
        Wrap request to add auth_token.
        """
        _http = httplib2.Http()
        uri = self._add_parameter(uri, 'access_token', self.credentials.access_token)
        return _http.request(uri, method="GET")

    def get_recent_media(self):
        """
        Make a request for recent media.
        """
        return self._request(self.SELF_RECENT_URL)


