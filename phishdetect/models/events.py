from ..endpoints import API_PATH
from .model import Model

class Events(Model):

    def fetch(self, limit=0, offset=0):
        params = {
            "limit": limit,
            "offset": offset,
        }
        return self._phishdetect.get(API_PATH["events_fetch"], params=params)
