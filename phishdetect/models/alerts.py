# This file is part of phishdetect-python:
# https://github.com/phishdetect/phishdetect-python
# See the file 'LICENSE' for copying permission.

from .model import Model
from ..endpoints import API_PATH

class Alerts(Model):

    def fetch(self, limit=0, offset=0):
        """Fetch all alerts stored by PhishDetect Node.

        Args:
            limit (int): Set an integer to use as limit of records to retrieve.
            offset (int): Set an integer to use as offset of records to retrieve.

        Returns:
            The parsed JSON response from the REST API request.

        Examples:
            ```python
            import phishdetect
            pd = phishdetect.PhishDetect(host="https://your-server.com",
                                         api_key="your-api-key")
            for alert in pd.alerts.fetch(limit=10):
                print(alert)
            ```
        """
        params = {
            "limit": limit,
            "offset": offset,
        }
        return self._phishdetect.get(API_PATH["alerts_fetch"], params=params)
