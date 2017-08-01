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


class SaleTax(object):
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
        'rate': 'float',
        'amount': 'float'
    }

    attribute_map = {
        'name': 'name',
        'rate': 'rate',
        'amount': 'amount'
    }

    def __init__(self, name=None, rate=None, amount=None):
        """
        SaleTax - a model defined in Swagger
        """

        self._name = None
        self._rate = None
        self._amount = None
        self.discriminator = None

        if name is not None:
          self.name = name
        if rate is not None:
          self.rate = rate
        if amount is not None:
          self.amount = amount

    @property
    def name(self):
        """
        Gets the name of this SaleTax.
        Tax name.

        :return: The name of this SaleTax.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this SaleTax.
        Tax name.

        :param name: The name of this SaleTax.
        :type: str
        """

        self._name = name

    @property
    def rate(self):
        """
        Gets the rate of this SaleTax.
        Tax rate.

        :return: The rate of this SaleTax.
        :rtype: float
        """
        return self._rate

    @rate.setter
    def rate(self, rate):
        """
        Sets the rate of this SaleTax.
        Tax rate.

        :param rate: The rate of this SaleTax.
        :type: float
        """

        self._rate = rate

    @property
    def amount(self):
        """
        Gets the amount of this SaleTax.
        Tax amount.

        :return: The amount of this SaleTax.
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """
        Sets the amount of this SaleTax.
        Tax amount.

        :param amount: The amount of this SaleTax.
        :type: float
        """

        self._amount = amount

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
        if not isinstance(other, SaleTax):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
