# This file is part of phishdetect-python:
# https://github.com/phishdetect/phishdetect-python
# See the file 'LICENSE' for copying permission.

from .model import Model
from ..endpoints import API_PATH

class Reports(Model):

    def fetch(self, limit=0, offset=0, report_type=""):
        """Fetch all reports stored by PhishDetect Node.

        Args:
            limit (int): Set an integer to use as limit of records to retrieve.
            offset (int): Set an integer to use as offset of records to retrieve.
            report_type (str): Type of report ("email" or "url").

        Returns:
            The parsed JSON response from the REST API request.

        Examples:
            ```python
            import phishdetect
            pd = phishdetect.PhishDetect(host="https://your-server.com",
                                         api_key="your-api-key")
            for report in pd.reports.fetch(limit=10):
                print(report)
            ```
        """
        params = {
            "limit": limit,
            "offset": offset,
            "type": report_type,
        }
        return self._phishdetect.get(API_PATH["reports_fetch"], params=params)

    def details(self, uuid):
        """Get details of a report, including content.

        Args:
            uuid (str): Identifier of the message to fetch.

        Returns:
            The parsed JSON response from the REST API request.

        Examples:
            ```python
            import phishdetect
            pd = phishdetect.PhishDetect(host="https://your-server.com",
                                         api_key="your-api-key")
            for report in pd.reports.fetch():
                details = pd.reports.details(report["uuid"])
            ```
        """
        return self._phishdetect.get(API_PATH["reports_details"].format(uuid=uuid))
