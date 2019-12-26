from .model import Model
from ..endpoints import API_PATH

class Raw(Model):

    def fetch(self, limit=0, offset=0):
        """Fetch all raw messages stored by PhishDetect Node.
        :param limit: Set an integer to use as limit of records to retrieve.
        :param offset: Set an integer to use as offset of records to retrieve.
        """
        params = {
            "limit": limit,
            "offset": offset,
        }
        return self._phishdetect.get(API_PATH["raw_fetch"], params=params)

    def details(self, uuid):
        """Get details of a raw message, including content.
        :param uuid: Identifier of the message to fetch.
        """
        return self._phishdetect.get(API_PATH["raw_details"].format(uuid=uuid))
