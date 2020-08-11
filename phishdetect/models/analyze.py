# This file is part of phishdetect-python:
# https://github.com/phishdetect/phishdetect-python
# See the file 'LICENSE' for copying permission.

from base64 import b64encode

from .model import Model
from ..endpoints import API_PATH

class Analyze(Model):

    def domain(self, domain):
        """Request the PhishDetect Node to statically analyze a domain name.
        :param domain: Domain to analyze.
        """
        return self._phishdetect.post(API_PATH["analyze_domain"], json={"url": domain})

    def url(self, url):
        """Request the PhishDetect Node to statically analyze a URL.
        :param url: URL to analyze.
        """
        return self._phishdetect.post(API_PATH["analyze_url"], json={"url": url})

    def link(self, url):
        """Request the PhishDetect Node to dynamically analyze a URL.
        :param url: URL to analyze.
        """
        return self._phishdetect.post(API_PATH["analyze_link"], json={"url": url})

    def html(self, url, html):
        """Request the PhishDetect Node to statically analyze an HTML page.
        :param url: URL of the HTML page.
        :param html: HTML of the page to analyze.
        """
        json = {
            "url": url,
            "html": b64encode(html.encode()).decode(),
        }
        return self._phishdetect.post(API_PATH["analyze_html"], json=json)
