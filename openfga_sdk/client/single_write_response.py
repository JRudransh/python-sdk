# coding: utf-8
"""
   Python SDK for OpenFGA

   API version: 0.1
   Website: https://openfga.dev
   Documentation: https://openfga.dev/docs
   Support: https://discord.gg/8naAwJfWN6
   License: [Apache-2.0](https://github.com/openfga/python-sdk/blob/main/LICENSE)

   NOTE: This file was auto generated by OpenAPI Generator (https://openapi-generator.tech). DO NOT EDIT.
"""

from openfga_sdk.client.client_tuple import ClientTuple


def construct_single_write_response(tuple_key: ClientTuple, success: bool, error: Exception = None):
    """
    Helper function to return a single write response
    """
    return SingleWriteResponse(tuple_key, success, error)


class SingleWriteResponse():
    """
    SingleWriteResponse encapsulates the response of a single write
    """

    def __init__(self, tuple_key: ClientTuple, success: bool, error: Exception = None):
        self._tuple_key = tuple_key
        self._success = success
        self._error = error

    def __eq__(self, other):
        return self.tuple_key == other.tuple_key and self.success == other.success and self.error == other.error

    @property
    def tuple_key(self):
        """
        Return tuple_key
        """
        return self._tuple_key

    @property
    def success(self):
        """
        Return success
        """
        return self._success

    @property
    def error(self):
        """
        Return error
        """
        return self._error
