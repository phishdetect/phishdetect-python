# This file is part of phishdetect-python:
# https://github.com/phishdetect/phishdetect-python
# See the file 'LICENSE' for copying permission.

from base64 import b64encode

from .model import Model
from ..endpoints import API_PATH

class Analyze(Model):

    def domain(self, domain):
        """Request the PhishDetect Node to statically analyze a domain name.

        Args:
            domain (str): Domain to analyze.

        Returns:
            The parsed JSON response from the REST API request.

        Examples:
            ```python
            import phishdetect
            pd = phishdetect.PhishDetect(host="https://your-server.com",
                                         api_key="your-api-key")
            results = pd.analyze.domain("baddomain.com")
            ```
        """
        return self._phishdetect.post(API_PATH["analyze_domain"], json={"url": domain})

    def url(self, url):
        """Request the PhishDetect Node to statically analyze a URL.

        Args:
            url (str): URL to analyze.

        Returns:
            The parsed JSON response from the REST API request.

        Examples:
            ```python
            import phishdetect
            pd = phishdetect.PhishDetect(host="https://your-server.com",
                                         api_key="your-api-key")
            results = pd.analyze.url("http://www.badwebsite.com")
            ```
        """
        return self._phishdetect.post(API_PATH["analyze_url"], json={"url": url})

    def link(self, url):
        """Request the PhishDetect Node to dynamically analyze a URL.
        This is only available if the node supports dynamic analysis and
        if PhishDetect's Docker image is properly installed.

        Args:
            url (str): URL to analyze.

        Returns:
            The parsed JSON response from the REST API request.

        Examples:
            ```python
            import phishdetect
            pd = phishdetect.PhishDetect(host="https://your-server.com",
                                         api_key="your-api-key")
            results = pd.analyze.link("http://www.badwebsite.com")
            ```
        """
        return self._phishdetect.post(API_PATH["analyze_link"], json={"url": url})

    def html(self, url, html):
        """Request the PhishDetect Node to statically analyze an HTML page.

        Args:
            url (str): URL of the HTML page.
            html (str or bytes): HTML of the page to analyze.

        Returns:
            The parsed JSON response from the REST API request.

        Examples:
            ```python
            import phishdetect
            pd = phishdetect.PhishDetect(host="https://your-server.com",
                                         api_key="your-api-key")
            results = pd.analyze.html(url="http://www.badwebsite.com",
                                      html="<html><head></head><body>Bad website!</body></html>")
            ```
        """
        if html is str:
            html = html.encode()

        json = {
            "url": url,
            "html": b64encode(html).decode(),
        }
        return self._phishdetect.post(API_PATH["analyze_html"], json=json)
