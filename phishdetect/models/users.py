# This file is part of phishdetect-python:
# https://github.com/phishdetect/phishdetect-python
# See the file 'LICENSE' for copying permission.

from .model import Model
from ..endpoints import API_PATH

class Users(Model):

    def get_pending(self):
        """Get list of users pending activation.

        Returns:
            The parsed JSON response from the REST API request.

        Examples:
            ```python
            import phishdetect
            pd = phishdetect.PhishDetect(host="https://your-server.com",
                                         api_key="your-api-key")
            pd.users.get_pending()
            ```
        """
        return self._phishdetect.get(API_PATH["users_pending"])

    def get_active(self):
        """Get list of active users.

        Returns:
            The parsed JSON response from the REST API request.

        Examples:
            ```python
            import phishdetect
            pd = phishdetect.PhishDetect(host="https://your-server.com",
                                         api_key="your-api-key")
            pd.users.get_active()
            ```
        """
        return self._phishdetect.get(API_PATH["users_active"])

    def activate(self, uuid):
        """Activate pending user.

        Args:
            uuid (str): UUID of the user to activate.

        Returns:
            The parsed JSON response from the REST API request.

        Examples:
            ```python
            import phishdetect
            pd = phishdetect.PhishDetect(host="https://your-server.com",
                                         api_key="your-api-key")
            for user in pd.users.get_pending():
                pd.users.activate(user["uuid"])
            ```
        """
        return self._phishdetect.get(API_PATH["users_activate"].format(uuid=uuid))

    def deactivate(self, uuid):
        """Deactivate existing user.

        Args:
            uuid (str): UUID of the user to deactivate.

        Returns:
            The parsed JSON response from the REST API request.

        Examples:
            ```python
            import phishdetect
            pd = phishdetect.PhishDetect(host="https://your-server.com",
                                         api_key="your-api-key")
            for user in pd.users.get_active():
                pd.users.deactivate(user["uuid"])
            ```
        """
        return self._phishdetect.get(API_PATH["users_deactivate"].format(uuid=uuid))
