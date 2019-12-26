# This file is part of phishdetect-python:
# https://github.com/phishdetect/phishdetect-python
# See the file 'LICENSE' for copying permission.

from .model import Model
from ..endpoints import API_PATH

class Indicators(Model):

    def add(self, indicators, indicators_type, tags=[]):
        """Add new indicators to PhishDetect Node.
        :param indicators: list of indicators, e.g. ["domain1.com", "domain2.com"].
        :param indicators_type: the indicator format, e.g.: "domain" or "email".
        :param tags: List of tags to assign to all these indicators.
        """
        json = {
            "indicators": indicators,
            "type": indicators_type,
            "tags": tags,
        }
        return self._phishdetect.post(API_PATH["indicators_add"], json=json)

    def fetch(self):
        """Fetch the default set of indicators (should be, from last 6 months.)
        """
        return self._phishdetect.get(API_PATH["indicators_fetch"])

    def fetch_recent(self):
        """Fetch only the indicators from the last 24 hours.
        """
        return self._phishdetect.get(API_PATH["indicators_fetch_recent"])

    def fetch_all(self):
        """Fetch all the indicators stored in the Node.
        This API should be avoided unless strictly necessary.
        """
        return self._phishdetect.get(API_PATH["indicators_fetch_all"])        

    def details(self, sha256):
        """Retrieve details on a given indicator (by hash).
        :param sha256: SHA256 hash of the indicator.
        """
        return self._phishdetect.get(API_PATH["indicators_details"].format(sha256=sha256))
