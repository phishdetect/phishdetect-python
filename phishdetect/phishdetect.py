# This file is part of phishdetect-python:
# https://github.com/phishdetect/phishdetect-python
# See the file 'LICENSE' for copying permission.

import requests
from urllib.parse import urljoin

from . import models
from .endpoints import API_PATH
from .constants import USER_AGENT

class PhishDetect:

    def __init__(self, host, api_key=None):
        """Initialize a PhishDetect instance.

        :param host: Host to the PhishDetect Node.
        :param api_key: The API key to be used to authenticate requests.
        """
        self.host = host
        self.api_key = api_key
        self._session = requests.Session()
        self._session.headers = {'User-Agent': USER_AGENT}

        self.events = models.Events(self)
        self.indicators = models.Indicators(self)
        self.reports = models.Reports(self)
        self.users = models.Users(self)

    def request(self, method, path, data=None, json=None, files=None, params=None):
        """Return the json from the resource requested at ``path``.
        :param method: HTTP method (mainly GET or POST).
        :param path: The path to the resource. This will be combined to the host
            specified at creation.
        :param json: Any JSON encoded data to send with the request.
        :param data: Any data to send as body of the request.
        :param files: Files to upload.
        :param params: Query paramaters to send with the request.
        """
        url = urljoin(self.host, path)

        if not params:
            params = {}

        if self.api_key:
            params["key"] = self.api_key

        response = self._session.request(method=method, url=url, data=data,
            json=json, files=files, params=params)
        return response.json()

    def get(self, path, params=None):
        """Send a GET request and return the JSON response.
        :param path: Path to the resource to retrieve.
        """
        return self.request(method="GET", path=path, params=params)

    def post(self, path, data=None, json=None, files=None, params=None):
        """Send a POST request and return the JSON response.
        :param path: The path to the resource. This will be combined to the host
            specified at creation.
        :param json: Any JSON encoded data to send with the request.
        :param data: Any data to send as body of the request.
        :param files: Files to upload.
        :param params: Query paramaters to send with the request.
        """
        return self.request(method="POST", path=path, data=data,
            json=json, files=files, params=params)

    def get_config(self):
        """Retrieve the config of specified the PhishDetect Node.
        """
        return self.get(API_PATH["config"])
