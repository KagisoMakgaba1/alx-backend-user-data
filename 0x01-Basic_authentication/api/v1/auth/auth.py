# api/v1/auth/auth.py

"""This module implements base class for Authentication mechanisms."""

from flask import request
from typing import List, TypeVar


class Auth:
    """Template for managing API authentication"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Determines if authentication is required"""
        return False

    def authorization_header(self, request=None) -> str:
        """Returns the value of the Authorization header"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Returns the current user - currently returns None"""
        return None
