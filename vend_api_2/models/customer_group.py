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


class CustomerGroup(object):
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
        'name': 'str',
        'id': 'str',
        'group_id': 'str',
        'created_at': 'str',
        'updated_at': 'str',
        'deleted_at': 'str',
        'version': 'float'
    }

    attribute_map = {
        'name': 'name',
        'id': 'id',
        'group_id': 'group_id',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'deleted_at': 'deleted_at',
        'version': 'version'
    }

    def __init__(self, name=None, id=None, group_id=None, created_at=None, updated_at=None, deleted_at=None, version=None):
        """
        CustomerGroup - a model defined in Swagger
        """

        self._name = None
        self._id = None
        self._group_id = None
        self._created_at = None
        self._updated_at = None
        self._deleted_at = None
        self._version = None

        self.name = name
        if id is not None:
          self.id = id
        if group_id is not None:
          self.group_id = group_id
        if created_at is not None:
          self.created_at = created_at
        if updated_at is not None:
          self.updated_at = updated_at
        if deleted_at is not None:
          self.deleted_at = deleted_at
        if version is not None:
          self.version = version

    @property
    def name(self):
        """
        Gets the name of this CustomerGroup.
        The customer group name.

        :return: The name of this CustomerGroup.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CustomerGroup.
        The customer group name.

        :param name: The name of this CustomerGroup.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def id(self):
        """
        Gets the id of this CustomerGroup.
        Auto-generated object ID.

        :return: The id of this CustomerGroup.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this CustomerGroup.
        Auto-generated object ID.

        :param id: The id of this CustomerGroup.
        :type: str
        """

        self._id = id

    @property
    def group_id(self):
        """
        Gets the group_id of this CustomerGroup.
        The customer group identifier.

        :return: The group_id of this CustomerGroup.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """
        Sets the group_id of this CustomerGroup.
        The customer group identifier.

        :param group_id: The group_id of this CustomerGroup.
        :type: str
        """

        self._group_id = group_id

    @property
    def created_at(self):
        """
        Gets the created_at of this CustomerGroup.
        Creation timestamp in UTC.

        :return: The created_at of this CustomerGroup.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """
        Sets the created_at of this CustomerGroup.
        Creation timestamp in UTC.

        :param created_at: The created_at of this CustomerGroup.
        :type: str
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """
        Gets the updated_at of this CustomerGroup.
        Last update timestamp in UTC.

        :return: The updated_at of this CustomerGroup.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """
        Sets the updated_at of this CustomerGroup.
        Last update timestamp in UTC.

        :param updated_at: The updated_at of this CustomerGroup.
        :type: str
        """

        self._updated_at = updated_at

    @property
    def deleted_at(self):
        """
        Gets the deleted_at of this CustomerGroup.
        Deletion timestamp in UTC.

        :return: The deleted_at of this CustomerGroup.
        :rtype: str
        """
        return self._deleted_at

    @deleted_at.setter
    def deleted_at(self, deleted_at):
        """
        Sets the deleted_at of this CustomerGroup.
        Deletion timestamp in UTC.

        :param deleted_at: The deleted_at of this CustomerGroup.
        :type: str
        """

        self._deleted_at = deleted_at

    @property
    def version(self):
        """
        Gets the version of this CustomerGroup.
        Auto-incrementing object version number.

        :return: The version of this CustomerGroup.
        :rtype: float
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this CustomerGroup.
        Auto-incrementing object version number.

        :param version: The version of this CustomerGroup.
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
        if not isinstance(other, CustomerGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
