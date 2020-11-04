# This file is part of phishdetect-python:
# https://github.com/phishdetect/phishdetect-python
# See the file 'LICENSE' for copying permission.

from .model import Model
from ..endpoints import API_PATH

class Indicators(Model):

    def add(self, indicators, tags=[], enabled=True, indicators_type=None):
        """Add new indicators to PhishDetect Node.

        Args:
            indicators (list): List of indicators, e.g. ["domain1.com", "domain2.com"].
                This list can also contain indicators hashed in SHA256 form,
                but in that case the `indicators_type` argument is required
                in order to specify if they are domains or emails.
            tags (list)): List of tags to assign to all these indicators.
            enabled (list): Boolean flag indicating if the indicators should be
                marked as enabled.
            indicators_type (str): String value to explicitly specify the type
                of indicators submitted. This is typically used only if you are
                submitting indicators that are already in hashed form, for
                which the Node can not automatically detect a type.

        Returns:
            The parsed JSON response from the REST API request.

        Examples:
            ```python
            import phishdetect
            pd = phishdetect.PhishDetect(host="https://your-server.com",
                                         api_key="your-api-key")
            # Add new indicators.
            pd.indicators.add(indicators=["baddomain1.com", "baddomain2.com"],
                              tags=["tag1", "tag2"])
            # Add new indicators in "pending" state.
            pd.indicators.add(indicators=["baddomain1.com", "baddomain2.com"],
                              tags=["tag1", "tag2"],
                              enabled=False)
            # Add new hashed indicators.
            pd.indicators.add(indicators=["3a2868d359962f226187048c8f7cbf42a5df3dddcd33746f6eb874a660a84bb6"],
                              indicators_type="domain")
            ```
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

        Returns:
            The parsed JSON response from the REST API request.

        Examples:
            ```python
            import phishdetect
            pd = phishdetect.PhishDetect(host="https://your-server.com",
                                         api_key="your-api-key")
            iocs = pd.indicators.fetch()
            ```
        """
        return self._phishdetect.get(API_PATH["indicators_fetch"])

    def fetch_recent(self):
        """Fetch only the indicators from the last 24 hours.

        Returns:
            The parsed JSON response from the REST API request.

        Examples:
            ```python
            import phishdetect
            pd = phishdetect.PhishDetect(host="https://your-server.com",
                                         api_key="your-api-key")
            iocs = pd.indicators.fetch_recent()
            ```
        """
        return self._phishdetect.get(API_PATH["indicators_fetch_recent"])

    def fetch_all(self):
        """Fetch all the indicators stored in the Node.
        This API should be avoided unless strictly necessary.

        Returns:
            The parsed JSON response from the REST API request.

        Examples:
            ```python
            import phishdetect
            pd = phishdetect.PhishDetect(host="https://your-server.com",
                                         api_key="your-api-key")
            iocs = pd.indicators.fetch_all()
            ```
        """
        return self._phishdetect.get(API_PATH["indicators_fetch_all"])        

    def details(self, sha256):
        """Retrieve details on a given indicator (by hash).

        Args:
            sha256 (str): SHA256 hash of the indicator.

        Returns:
            The parsed JSON response from the REST API request.

        Examples:
            ```python
            import phishdetect
            pd = phishdetect.PhishDetect(host="https://your-server.com",
                                         api_key="your-api-key")
            # Get details of a hashed indicator.
            details = pd.indicators.details(sha256="3a2868d359962f226187048c8f7cbf42a5df3dddcd33746f6eb874a660a84bb6")
            ```
        """
        return self._phishdetect.get(API_PATH["indicators_details"].format(sha256=sha256))

    def get_pending(self):
        """Fetch all the indicators that are marked as pending.

        Returns:
            The parsed JSON response from the REST API request.

        Examples:
            ```python
            import phishdetect
            pd = phishdetect.PhishDetect(host="https://your-server.com",
                                         api_key="your-api-key")
            pending_iocs = pd.indicators.get_pending()
            ```
        """
        return self._phishdetect.get(API_PATH["indicators_pending"])

    def get_disabled(self):
        """Fetch all the indicators that are marked as disabled.

        Returns:
            The parsed JSON response from the REST API request.

        Examples:
            ```python
            import phishdetect
            pd = phishdetect.PhishDetect(host="https://your-server.com",
                                         api_key="your-api-key")
            disabled_iocs = pd.indicators.get_disabled()
            ```
        """
        return self._phishdetect.get(API_PATH["indicators_disabled"])

    def enable(self, indicators):
        """Set status of provided indicators to "enabled".
        Args:
            indicators (list): List of hashed indicators in SHA256 format.

        Returns:
            The parsed JSON response from the REST API request.

        Examples:
            ```python
            import phishdetect
            pd = phishdetect.PhishDetect(host="https://your-server.com",
                                         api_key="your-api-key")
            pd.indicators.enable(indicators=["3a2868d359962f226187048c8f7cbf42a5df3dddcd33746f6eb874a660a84bb6"])
            ```
        """
        return self._phishdetect.post(API_PATH["indicators_enable"], json=indicators)

    def disable(self, indicators):
        """Set status of provided indicators to "disabled".

        Args:
            indicators (list): List of hashed indicators in SHA256 format.

        Returns:
            The parsed JSON response from the REST API request.

        Examples:
            ```python
            import phishdetect
            pd = phishdetect.PhishDetect(host="https://your-server.com",
                                         api_key="your-api-key")
            pd.indicators.disable(indicators=["3a2868d359962f226187048c8f7cbf42a5df3dddcd33746f6eb874a660a84bb6"])
            ```
        """
        return self._phishdetect.post(API_PATH["indicators_disable"], json=indicators)
