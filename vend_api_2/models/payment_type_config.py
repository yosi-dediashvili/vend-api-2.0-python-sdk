# coding: utf-8

"""
    API 2.0

    Early release of version 2.0 of the Vend API.

    OpenAPI spec version: 2.0
    Contact: api@vendhq.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class PaymentTypeConfig(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'url': 'str',
        '_print': 'bool'
    }

    attribute_map = {
        'url': 'url',
        '_print': 'print'
    }

    def __init__(self, url=None, _print=None):
        """
        PaymentTypeConfig - a model defined in Swagger
        """

        self._url = None
        self.__print = None

        if url is not None:
          self.url = url
        if _print is not None:
          self._print = _print

    @property
    def url(self):
        """
        Gets the url of this PaymentTypeConfig.
        The URL of  the gateway.

        :return: The url of this PaymentTypeConfig.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """
        Sets the url of this PaymentTypeConfig.
        The URL of  the gateway.

        :param url: The url of this PaymentTypeConfig.
        :type: str
        """

        self._url = url

    @property
    def _print(self):
        """
        Gets the _print of this PaymentTypeConfig.
        Indicates whether a receipt will be printed???

        :return: The _print of this PaymentTypeConfig.
        :rtype: bool
        """
        return self.__print

    @_print.setter
    def _print(self, _print):
        """
        Sets the _print of this PaymentTypeConfig.
        Indicates whether a receipt will be printed???

        :param _print: The _print of this PaymentTypeConfig.
        :type: bool
        """

        self.__print = _print

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, PaymentTypeConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
