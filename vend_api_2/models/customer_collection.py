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


class CustomerCollection(object):
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
        'data': 'list[Customer]',
        'version': 'Version'
    }

    attribute_map = {
        'data': 'data',
        'version': 'version'
    }

    def __init__(self, data=None, version=None):
        """
        CustomerCollection - a model defined in Swagger
        """

        self._data = None
        self._version = None
        self.discriminator = None

        if data is not None:
          self.data = data
        if version is not None:
          self.version = version

    @property
    def data(self):
        """
        Gets the data of this CustomerCollection.
        An array of Customer objects.

        :return: The data of this CustomerCollection.
        :rtype: list[Customer]
        """
        return self._data

    @data.setter
    def data(self, data):
        """
        Sets the data of this CustomerCollection.
        An array of Customer objects.

        :param data: The data of this CustomerCollection.
        :type: list[Customer]
        """

        self._data = data

    @property
    def version(self):
        """
        Gets the version of this CustomerCollection.

        :return: The version of this CustomerCollection.
        :rtype: Version
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this CustomerCollection.

        :param version: The version of this CustomerCollection.
        :type: Version
        """

        self._version = version

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
        if not isinstance(other, CustomerCollection):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
