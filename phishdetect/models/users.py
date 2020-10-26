# This file is part of phishdetect-python:
# https://github.com/phishdetect/phishdetect-python
# See the file 'LICENSE' for copying permission.

from .model import Model
from ..endpoints import API_PATH

class Users(Model):

    def get_pending(self):
        """Get list of users pending activation.
        """
        return self._phishdetect.get(API_PATH["users_pending"])

    def get_active(self):
        """Get list of active users.
        """
        return self._phishdetect.get(API_PATH["users_active"])

    def activate(self, uuid):
        """Activate pending user.
        :param uuid: UUID of the user to activate.
        """
        return self._phishdetect.get(API_PATH["users_activate"].format(uuid=uuid))

    def deactivate(self, uuid):
        """Deactivate existing user.
        :param uuid: UUID of the user to deactivate.
        """
        return self._phishdetect.get(API_PATH["users_deactivate"].format(uuid=uuid))
