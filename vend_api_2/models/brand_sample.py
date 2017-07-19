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


class BrandSample(object):
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
        'id': 'str',
        'name': 'str',
        'deleted_at': 'str',
        'version': 'float'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'deleted_at': 'deleted_at',
        'version': 'version'
    }

    def __init__(self, id=None, name=None, deleted_at=None, version=None):
        """
        BrandSample - a model defined in Swagger
        """

        self._id = None
        self._name = None
        self._deleted_at = None
        self._version = None

        if id is not None:
          self.id = id
        if name is not None:
          self.name = name
        if deleted_at is not None:
          self.deleted_at = deleted_at
        if version is not None:
          self.version = version

    @property
    def id(self):
        """
        Gets the id of this BrandSample.
        Auto-generated object ID.

        :return: The id of this BrandSample.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this BrandSample.
        Auto-generated object ID.

        :param id: The id of this BrandSample.
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this BrandSample.
        

        :return: The name of this BrandSample.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this BrandSample.
        

        :param name: The name of this BrandSample.
        :type: str
        """

        self._name = name

    @property
    def deleted_at(self):
        """
        Gets the deleted_at of this BrandSample.
        Deletion timestamp in UTC.

        :return: The deleted_at of this BrandSample.
        :rtype: str
        """
        return self._deleted_at

    @deleted_at.setter
    def deleted_at(self, deleted_at):
        """
        Sets the deleted_at of this BrandSample.
        Deletion timestamp in UTC.

        :param deleted_at: The deleted_at of this BrandSample.
        :type: str
        """

        self._deleted_at = deleted_at

    @property
    def version(self):
        """
        Gets the version of this BrandSample.
        Auto-incrementing object version number.

        :return: The version of this BrandSample.
        :rtype: float
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this BrandSample.
        Auto-incrementing object version number.

        :param version: The version of this BrandSample.
        :type: float
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
        if not isinstance(other, BrandSample):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
