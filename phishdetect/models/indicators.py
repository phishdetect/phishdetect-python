from ..endpoints import API_PATH
from .model import Model

class Indicators(Model):

    def add(self, indicators, indicators_type, tags=[]):
        json = {
            "indicators": indicators,
            "type": indicators_type,
            "tags": tags,
        }
        return self._phishdetect.post(API_PATH["indicators_add"], json=json)

    def fetch(self):
        return self._phishdetect.get(API_PATH["indicators_fetch"])

    def fetch_recent(self):
        return self._phishdetect.get(API_PATH["indicators_fetch_recent"])

    def fetch_all(self):
        return self._phishdetect.get(API_PATH["indicators_fetch_all"])        
