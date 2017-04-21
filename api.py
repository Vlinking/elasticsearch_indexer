import webbrowser
import httplib2

from oauth2client import client
from oauth2client.file import Storage


class InstagramAPI(object):
    """
    Class for accessing Instagram API endpoints.
    """
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

    def _request(self, uri):
        """
        Wrap request to add auth_token
        """
        _http = httplib2.Http()
        return _http.request("{0}?access_token={1}".format(uri, self.credentials.access_token), method="GET")[1]