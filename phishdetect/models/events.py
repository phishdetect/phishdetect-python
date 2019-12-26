# This file is part of phishdetect-python:
# https://github.com/phishdetect/phishdetect-python
# See the file 'LICENSE' for copying permission.

from .model import Model
from ..endpoints import API_PATH

class Events(Model):

    def fetch(self, limit=0, offset=0):
        """Fetch all events stored by PhishDetect Node.
        :param limit: Set an integer to use as limit of records to retrieve.
        :param offset: Set an integer to use as offset of records to retrieve.
        """
        params = {
            "limit": limit,
            "offset": offset,
        }
        return self._phishdetect.get(API_PATH["events_fetch"], params=params)
