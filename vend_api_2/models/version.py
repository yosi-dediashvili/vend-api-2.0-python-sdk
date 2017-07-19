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


class Version(object):
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
        'min': 'int',
        'max': 'int'
    }

    attribute_map = {
        'min': 'min',
        'max': 'max'
    }

    def __init__(self, min=None, max=None):
        """
        Version - a model defined in Swagger
        """

        self._min = None
        self._max = None

        self.min = min
        self.max = max

    @property
    def min(self):
        """
        Gets the min of this Version.
        Lowest version number of the payload.

        :return: The min of this Version.
        :rtype: int
        """
        return self._min

    @min.setter
    def min(self, min):
        """
        Sets the min of this Version.
        Lowest version number of the payload.

        :param min: The min of this Version.
        :type: int
        """
        if min is None:
            raise ValueError("Invalid value for `min`, must not be `None`")

        self._min = min

    @property
    def max(self):
        """
        Gets the max of this Version.
        Highest version number of the payload.

        :return: The max of this Version.
        :rtype: int
        """
        return self._max

    @max.setter
    def max(self, max):
        """
        Sets the max of this Version.
        Highest version number of the payload.

        :param max: The max of this Version.
        :type: int
        """
        if max is None:
            raise ValueError("Invalid value for `max`, must not be `None`")

        self._max = max

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
        if not isinstance(other, Version):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
