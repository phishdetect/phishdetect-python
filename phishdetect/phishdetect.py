# This file is part of phishdetect-python:
# https://github.com/phishdetect/phishdetect-python
# See the file 'LICENSE' for copying permission.

import requests
from urllib.parse import urljoin

from . import models
from .endpoints import API_PATH

class PhishDetect:

    def __init__(self, host, api_key=None):
        """Initialize a PhishDetect instance.

        Args:
            host (str): Host to the PhishDetect Node.
            api_key (str): The API key to be used to authenticate requests.

        Returns:
            The parsed JSON response from the REST API request.

        Examples:
            ```python
            import phishdetect
            pd = phishdetect.PhishDetect(host="https://your-server.com",
                                         api_key="your-api-key")
            ```
        """
        self.host = host
        self.api_key = api_key
        self._session = requests.Session()
        self._session.headers = {"User-Agent": "phishdetect-python", "Connection": "close"}

        self.alerts = models.Alerts(self)
        self.indicators = models.Indicators(self)
        self.reports = models.Reports(self)
        self.users = models.Users(self)
        self.analyze = models.Analyze(self)

    def request(self, method, path, data=None, json=None, files=None, params=None):
        """Return the json from the resource requested at ``path``.

        Args:
            method (str): HTTP method (mainly GET or POST).
            path (str): The path to the resource. This will be combined to the host
                specified at creation.
            json (str): Any JSON encoded data to send with the request.
            data: Any data to send as body of the request.
            files: Files to upload.
            params: Query paramaters to send with the request.

        Returns:
            The parsed JSON response from the REST API request.
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

        Args:
            path (str): Path to the resource to retrieve.

        Returns:
            The parsed JSON response from the REST API request.
        """
        return self.request(method="GET", path=path, params=params)

    def post(self, path, data=None, json=None, files=None, params=None):
        """Send a POST request and return the JSON response.

        Args:
            path (str): The path to the resource. This will be combined to the host
                specified at creation.
            json: Any JSON encoded data to send with the request.
            data: Any data to send as body of the request.
            files: Files to upload.
            params: Query paramaters to send with the request.

        Returns:
            The parsed JSON response from the REST API request.
        """
        return self.request(method="POST", path=path, data=data,
            json=json, files=files, params=params)

    def get_config(self):
        """Retrieve the config of specified the PhishDetect Node.

        Returns:
            The parsed JSON response from the REST API request.
        """
        return self.get(API_PATH["config"])
