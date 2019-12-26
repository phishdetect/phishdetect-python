# This file is part of phishdetect-python:
# https://github.com/phishdetect/phishdetect-python
# See the file 'LICENSE' for copying permission.

from .model import Model
from ..endpoints import API_PATH

class Reports(Model):

    def fetch(self, limit=0, offset=0, report_type=""):
        """Fetch all reports stored by PhishDetect Node.
        :param limit: Set an integer to use as limit of records to retrieve.
        :param offset: Set an integer to use as offset of records to retrieve.
        """
        params = {
            "limit": limit,
            "offset": offset,
            "type": report_type,
        }
        return self._phishdetect.get(API_PATH["reports_fetch"], params=params)

    def details(self, uuid):
        """Get details of a report, including content.
        :param uuid: Identifier of the message to fetch.
        """
        return self._phishdetect.get(API_PATH["reports_details"].format(uuid=uuid))
