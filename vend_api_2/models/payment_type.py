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


class PaymentType(object):
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
        'type_id': 'int',
        'config': 'PaymentTypeConfig',
        'version': 'float'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'type_id': 'type_id',
        'config': 'config',
        'version': 'version'
    }

    def __init__(self, id=None, name=None, type_id=None, config=None, version=None):
        """
        PaymentType - a model defined in Swagger
        """

        self._id = None
        self._name = None
        self._type_id = None
        self._config = None
        self._version = None

        self.id = id
        self.name = name
        self.type_id = type_id
        if config is not None:
          self.config = config
        self.version = version

    @property
    def id(self):
        """
        Gets the id of this PaymentType.
        Auto-generated object ID.

        :return: The id of this PaymentType.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this PaymentType.
        Auto-generated object ID.

        :param id: The id of this PaymentType.
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this PaymentType.
        The name of the payment type.

        :return: The name of this PaymentType.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this PaymentType.
        The name of the payment type.

        :param name: The name of this PaymentType.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def type_id(self):
        """
        Gets the type_id of this PaymentType.
        The ID of the global Vend payment type. It shouldn't be used to identify the payment type - there may be multiple payment types with the same `type_id`.

        :return: The type_id of this PaymentType.
        :rtype: int
        """
        return self._type_id

    @type_id.setter
    def type_id(self, type_id):
        """
        Sets the type_id of this PaymentType.
        The ID of the global Vend payment type. It shouldn't be used to identify the payment type - there may be multiple payment types with the same `type_id`.

        :param type_id: The type_id of this PaymentType.
        :type: int
        """
        if type_id is None:
            raise ValueError("Invalid value for `type_id`, must not be `None`")

        self._type_id = type_id

    @property
    def config(self):
        """
        Gets the config of this PaymentType.

        :return: The config of this PaymentType.
        :rtype: PaymentTypeConfig
        """
        return self._config

    @config.setter
    def config(self, config):
        """
        Sets the config of this PaymentType.

        :param config: The config of this PaymentType.
        :type: PaymentTypeConfig
        """

        self._config = config

    @property
    def version(self):
        """
        Gets the version of this PaymentType.
        Auto

        :return: The version of this PaymentType.
        :rtype: float
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this PaymentType.
        Auto

        :param version: The version of this PaymentType.
        :type: float
        """
        if version is None:
            raise ValueError("Invalid value for `version`, must not be `None`")

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
        if not isinstance(other, PaymentType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
