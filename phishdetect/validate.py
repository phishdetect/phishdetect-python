# This file is part of phishdetect-python:
# https://github.com/phishdetect/phishdetect-python
# See the file 'LICENSE' for copying permission.

import re

class InvalidParameter(Exception):
    pass

def validate_uuid(uuid):
    uuid_regex = re.compile("^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-4[a-fA-F0-9]{3}-[4|5|6|7|8|9|aA|bB][a-fA-F0-9]{3}-[a-fA-F0-9]{12}$")
    if not uuid_regex.match(uuid):
        raise InvalidParameter

def validate_sha256(sha256):
    sha256_regex = re.compile("^[a-fA-F0-9]{64}$")
    if not sha256_regex.match(sha256):
        raise InvalidParameter
