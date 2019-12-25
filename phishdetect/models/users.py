from ..endpoints import API_PATH
from .model import Model

class Users(Model):

    def get_pending_users(self):
        """Get list of users pending activation.
        """
        return self._phishdetect.get(API_PATH["users_pending"])

    def get_active_users(self):
        """Get list of active users.
        """
        return self._phishdetect.get(API_PATH["users_active"])

    def activate_user(self, api_key):
        """Activate pending user.
        :param api_key: API key used to identify the user to activate.
        """
        return self._phishdetect.get(API_PATH["users_activate"].format(api_key=api_key))

    def deactivate_user(self, api_key):
        """Deactivate existing user.
        :param api_key: API key used to identify the user to deactivate.
        """
        return self._phishdetect.get(API_PATH["users_deactivate"].format(api_key=api_key))
