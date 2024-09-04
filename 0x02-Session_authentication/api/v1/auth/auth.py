#!/usr/bin/env python3

"""This module implements base class for Authentication mechanisms."""

from typing import List, TypeVar, Union
from os import getenv

User = TypeVar("User")


class Auth:
    """Auth class to manage the API authentication."""

    @staticmethod
    def require_auth(path: str, excluded_paths: List[str]) -> bool:
        """Require authentication for API paths except for excluded paths."""
        if not path or not excluded_paths:
            return True

        path = path.rstrip("/") + "/"

        for exc_path in excluded_paths:
            # perform a simple a regex to accept paths matching the pattern
            if path.startswith(exc_path.rstrip("*")):
                return False

        return path not in excluded_paths

    @staticmethod
    def authorization_header(request=None) -> Union[str, None]:
        """Return the value of the Authorization header."""
        if not request:
            return None

        return request.headers.get("Authorization")

    def current_user(self, request=None) -> User:
        """Return the current user."""
        return None

    def session_cookie(self, request=None) -> Union[str, None]:
        """Return the value of the session cookie from the request."""
        if request is None:
            return None

        session_name = getenv("SESSION_NAME")
        if session_name is None:
            return None

        return request.cookies.get(session_name)
