from ..endpoints import API_PATH
from .model import Model

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
