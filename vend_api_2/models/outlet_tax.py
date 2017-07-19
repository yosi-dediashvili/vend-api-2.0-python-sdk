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


class OutletTax(object):
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
        'outlet_id': 'str',
        'product_id': 'str',
        'tax_id': 'str',
        'deleted_at': 'str',
        'version': 'int'
    }

    attribute_map = {
        'outlet_id': 'outlet_id',
        'product_id': 'product_id',
        'tax_id': 'tax_id',
        'deleted_at': 'deleted_at',
        'version': 'version'
    }

    def __init__(self, outlet_id=None, product_id=None, tax_id=None, deleted_at=None, version=None):
        """
        OutletTax - a model defined in Swagger
        """

        self._outlet_id = None
        self._product_id = None
        self._tax_id = None
        self._deleted_at = None
        self._version = None

        self.outlet_id = outlet_id
        self.product_id = product_id
        self.tax_id = tax_id
        if deleted_at is not None:
          self.deleted_at = deleted_at
        self.version = version

    @property
    def outlet_id(self):
        """
        Gets the outlet_id of this OutletTax.
        The ID of the outlet this record is associated with.

        :return: The outlet_id of this OutletTax.
        :rtype: str
        """
        return self._outlet_id

    @outlet_id.setter
    def outlet_id(self, outlet_id):
        """
        Sets the outlet_id of this OutletTax.
        The ID of the outlet this record is associated with.

        :param outlet_id: The outlet_id of this OutletTax.
        :type: str
        """
        if outlet_id is None:
            raise ValueError("Invalid value for `outlet_id`, must not be `None`")

        self._outlet_id = outlet_id

    @property
    def product_id(self):
        """
        Gets the product_id of this OutletTax.
        The ID of the product this record is associated with.

        :return: The product_id of this OutletTax.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """
        Sets the product_id of this OutletTax.
        The ID of the product this record is associated with.

        :param product_id: The product_id of this OutletTax.
        :type: str
        """
        if product_id is None:
            raise ValueError("Invalid value for `product_id`, must not be `None`")

        self._product_id = product_id

    @property
    def tax_id(self):
        """
        Gets the tax_id of this OutletTax.
        The ID of the tax this record is associated with.

        :return: The tax_id of this OutletTax.
        :rtype: str
        """
        return self._tax_id

    @tax_id.setter
    def tax_id(self, tax_id):
        """
        Sets the tax_id of this OutletTax.
        The ID of the tax this record is associated with.

        :param tax_id: The tax_id of this OutletTax.
        :type: str
        """
        if tax_id is None:
            raise ValueError("Invalid value for `tax_id`, must not be `None`")

        self._tax_id = tax_id

    @property
    def deleted_at(self):
        """
        Gets the deleted_at of this OutletTax.
        Deletion timestamp in UTC.

        :return: The deleted_at of this OutletTax.
        :rtype: str
        """
        return self._deleted_at

    @deleted_at.setter
    def deleted_at(self, deleted_at):
        """
        Sets the deleted_at of this OutletTax.
        Deletion timestamp in UTC.

        :param deleted_at: The deleted_at of this OutletTax.
        :type: str
        """

        self._deleted_at = deleted_at

    @property
    def version(self):
        """
        Gets the version of this OutletTax.
        Auto-incrementing object version number.

        :return: The version of this OutletTax.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this OutletTax.
        Auto-incrementing object version number.

        :param version: The version of this OutletTax.
        :type: int
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
        if not isinstance(other, OutletTax):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
