# This file is part of phishdetect-python:
# https://github.com/phishdetect/phishdetect-python
# See the file 'LICENSE' for copying permission.

from .model import Model
from ..endpoints import API_PATH

class Indicators(Model):

    def add(self, indicators, tags=[], enabled=True, indicators_type=None):
        """Add new indicators to PhishDetect Node.
        :param indicators: List of indicators, e.g. ["domain1.com", "domain2.com"].
        :param tags: List of tags to assign to all these indicators.
        :param enabled: Boolean flag indicating if the indicators should be
                        marked as enabled.
        :param indicators_type: String value to explicitly specify the type of
                                indicators submitted. This is typically used
                                only if you are submitting indicators that are
                                already in hashed form, for which the Node can
                                not automatically detect a type.
        """
        json = {
            "indicators": indicators,
            "tags": tags,
            "enabled": enabled,
            "type": indicators_type,
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

    def get_pending(self):
        """Fetch all the indicators that are marked as pending.
        """
        return self._phishdetect.get(API_PATH["indicators_pending"])

    def get_disabled(self):
        """Fetch all the indicators that are marked as disabled.
        """
        return self._phishdetect.get(API_PATH["indicators_disabled"])

    def enable(self, indicators):
        """Set status of provided indicators to "enabled".
        :param indicators: List of hashed indicators in SHA256 format.
        """
        return self._phishdetect.post(API_PATH["indicators_enable"], json=indicators)

    def disable(self, indicators):
        """Set status of provided indicators to "disabled".
        :param indicators: List of hashed indicators in SHA256 format.
        """
        return self._phishdetect.post(API_PATH["indicators_disable"], json=indicators)
