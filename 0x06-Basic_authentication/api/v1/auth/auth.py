#!/usr/bin/env python3
""" Module of auth
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """Auth Class"""

    def __init__(self):
        """
        Constructor

        Args:
            path: path to authenticate
            excluded_paths: list of excluded path to authenticate
        """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Require the auth

        Args:
            path: path to authenticate
            excluded_paths: list of excluded path to authenticate

        Return:
            True if is authenticated
        """
        if not path or not excluded_paths:
            return True

        if path[-1] != "/":
            path += "/"

        if path not in excluded_paths:
            return True

        return False

    def authorization_header(self, request=None) -> str:
        """
        Look the headers

        Args:
            request: Look the autthorization

        Return:
            The request found
        """
        print(request)
        if not request or "Authorization" not in request:
            return None

        return request["Authorization"]

    def current_user(self, request=None) -> TypeVar("User"):
        """
        Look current user

        Args:
            request: Look the reques user

        Return:
            The user
        """
        return request
