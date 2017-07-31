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


class Outlet(object):
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
        'time_zone': 'str',
        'default_tax_id': 'str',
        'currency': 'str',
        'currency_symbol': 'str',
        'display_prices': 'str',
        'physical_address_1': 'str',
        'physical_address_2': 'str',
        'physical_suburb': 'str',
        'physical_city': 'str',
        'physical_postcode': 'str',
        'physical_state': 'str',
        'physical_country_id': 'str',
        'deleted_at': 'str',
        'version': 'float'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'time_zone': 'time_zone',
        'default_tax_id': 'default_tax_id',
        'currency': 'currency',
        'currency_symbol': 'currency_symbol',
        'display_prices': 'display_prices',
        'physical_address_1': 'physical_address_1',
        'physical_address_2': 'physical_address_2',
        'physical_suburb': 'physical_suburb',
        'physical_city': 'physical_city',
        'physical_postcode': 'physical_postcode',
        'physical_state': 'physical_state',
        'physical_country_id': 'physical_country_id',
        'deleted_at': 'deleted_at',
        'version': 'version'
    }

    def __init__(self, id=None, name=None, time_zone=None, default_tax_id=None, currency=None, currency_symbol=None, display_prices=None, physical_address_1=None, physical_address_2=None, physical_suburb=None, physical_city=None, physical_postcode=None, physical_state=None, physical_country_id=None, deleted_at=None, version=None):
        """
        Outlet - a model defined in Swagger
        """

        self._id = None
        self._name = None
        self._time_zone = None
        self._default_tax_id = None
        self._currency = None
        self._currency_symbol = None
        self._display_prices = None
        self._physical_address_1 = None
        self._physical_address_2 = None
        self._physical_suburb = None
        self._physical_city = None
        self._physical_postcode = None
        self._physical_state = None
        self._physical_country_id = None
        self._deleted_at = None
        self._version = None
        self.discriminator = None

        if id is not None:
          self.id = id
        if name is not None:
          self.name = name
        if time_zone is not None:
          self.time_zone = time_zone
        if default_tax_id is not None:
          self.default_tax_id = default_tax_id
        if currency is not None:
          self.currency = currency
        if currency_symbol is not None:
          self.currency_symbol = currency_symbol
        if display_prices is not None:
          self.display_prices = display_prices
        if physical_address_1 is not None:
          self.physical_address_1 = physical_address_1
        if physical_address_2 is not None:
          self.physical_address_2 = physical_address_2
        if physical_suburb is not None:
          self.physical_suburb = physical_suburb
        if physical_city is not None:
          self.physical_city = physical_city
        if physical_postcode is not None:
          self.physical_postcode = physical_postcode
        if physical_state is not None:
          self.physical_state = physical_state
        if physical_country_id is not None:
          self.physical_country_id = physical_country_id
        if deleted_at is not None:
          self.deleted_at = deleted_at
        if version is not None:
          self.version = version

    @property
    def id(self):
        """
        Gets the id of this Outlet.
        Auto-generated object ID.

        :return: The id of this Outlet.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Outlet.
        Auto-generated object ID.

        :param id: The id of this Outlet.
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this Outlet.
        The outlet name.

        :return: The name of this Outlet.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Outlet.
        The outlet name.

        :param name: The name of this Outlet.
        :type: str
        """

        self._name = name

    @property
    def time_zone(self):
        """
        Gets the time_zone of this Outlet.
        Outlet timezone. **read only**

        :return: The time_zone of this Outlet.
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        """
        Sets the time_zone of this Outlet.
        Outlet timezone. **read only**

        :param time_zone: The time_zone of this Outlet.
        :type: str
        """

        self._time_zone = time_zone

    @property
    def default_tax_id(self):
        """
        Gets the default_tax_id of this Outlet.
        Default tax id used for sales in this outlet. **deprecated**

        :return: The default_tax_id of this Outlet.
        :rtype: str
        """
        return self._default_tax_id

    @default_tax_id.setter
    def default_tax_id(self, default_tax_id):
        """
        Sets the default_tax_id of this Outlet.
        Default tax id used for sales in this outlet. **deprecated**

        :param default_tax_id: The default_tax_id of this Outlet.
        :type: str
        """

        self._default_tax_id = default_tax_id

    @property
    def currency(self):
        """
        Gets the currency of this Outlet.
        Currency name.

        :return: The currency of this Outlet.
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """
        Sets the currency of this Outlet.
        Currency name.

        :param currency: The currency of this Outlet.
        :type: str
        """

        self._currency = currency

    @property
    def currency_symbol(self):
        """
        Gets the currency_symbol of this Outlet.
        Currency symbol.

        :return: The currency_symbol of this Outlet.
        :rtype: str
        """
        return self._currency_symbol

    @currency_symbol.setter
    def currency_symbol(self, currency_symbol):
        """
        Sets the currency_symbol of this Outlet.
        Currency symbol.

        :param currency_symbol: The currency_symbol of this Outlet.
        :type: str
        """

        self._currency_symbol = currency_symbol

    @property
    def display_prices(self):
        """
        Gets the display_prices of this Outlet.
        Indicates whether prices in this outlet should be displayed as tax-inclusive.

        :return: The display_prices of this Outlet.
        :rtype: str
        """
        return self._display_prices

    @display_prices.setter
    def display_prices(self, display_prices):
        """
        Sets the display_prices of this Outlet.
        Indicates whether prices in this outlet should be displayed as tax-inclusive.

        :param display_prices: The display_prices of this Outlet.
        :type: str
        """

        self._display_prices = display_prices

    @property
    def physical_address_1(self):
        """
        Gets the physical_address_1 of this Outlet.
        Physical address, line 1.

        :return: The physical_address_1 of this Outlet.
        :rtype: str
        """
        return self._physical_address_1

    @physical_address_1.setter
    def physical_address_1(self, physical_address_1):
        """
        Sets the physical_address_1 of this Outlet.
        Physical address, line 1.

        :param physical_address_1: The physical_address_1 of this Outlet.
        :type: str
        """

        self._physical_address_1 = physical_address_1

    @property
    def physical_address_2(self):
        """
        Gets the physical_address_2 of this Outlet.
        Physical address, line 2.

        :return: The physical_address_2 of this Outlet.
        :rtype: str
        """
        return self._physical_address_2

    @physical_address_2.setter
    def physical_address_2(self, physical_address_2):
        """
        Sets the physical_address_2 of this Outlet.
        Physical address, line 2.

        :param physical_address_2: The physical_address_2 of this Outlet.
        :type: str
        """

        self._physical_address_2 = physical_address_2

    @property
    def physical_suburb(self):
        """
        Gets the physical_suburb of this Outlet.
        Physical address, suburb.

        :return: The physical_suburb of this Outlet.
        :rtype: str
        """
        return self._physical_suburb

    @physical_suburb.setter
    def physical_suburb(self, physical_suburb):
        """
        Sets the physical_suburb of this Outlet.
        Physical address, suburb.

        :param physical_suburb: The physical_suburb of this Outlet.
        :type: str
        """

        self._physical_suburb = physical_suburb

    @property
    def physical_city(self):
        """
        Gets the physical_city of this Outlet.
        Physical address, city.

        :return: The physical_city of this Outlet.
        :rtype: str
        """
        return self._physical_city

    @physical_city.setter
    def physical_city(self, physical_city):
        """
        Sets the physical_city of this Outlet.
        Physical address, city.

        :param physical_city: The physical_city of this Outlet.
        :type: str
        """

        self._physical_city = physical_city

    @property
    def physical_postcode(self):
        """
        Gets the physical_postcode of this Outlet.
        Physical address, post code.

        :return: The physical_postcode of this Outlet.
        :rtype: str
        """
        return self._physical_postcode

    @physical_postcode.setter
    def physical_postcode(self, physical_postcode):
        """
        Sets the physical_postcode of this Outlet.
        Physical address, post code.

        :param physical_postcode: The physical_postcode of this Outlet.
        :type: str
        """

        self._physical_postcode = physical_postcode

    @property
    def physical_state(self):
        """
        Gets the physical_state of this Outlet.
        Physical address, state.

        :return: The physical_state of this Outlet.
        :rtype: str
        """
        return self._physical_state

    @physical_state.setter
    def physical_state(self, physical_state):
        """
        Sets the physical_state of this Outlet.
        Physical address, state.

        :param physical_state: The physical_state of this Outlet.
        :type: str
        """

        self._physical_state = physical_state

    @property
    def physical_country_id(self):
        """
        Gets the physical_country_id of this Outlet.
        Physical address, country code.

        :return: The physical_country_id of this Outlet.
        :rtype: str
        """
        return self._physical_country_id

    @physical_country_id.setter
    def physical_country_id(self, physical_country_id):
        """
        Sets the physical_country_id of this Outlet.
        Physical address, country code.

        :param physical_country_id: The physical_country_id of this Outlet.
        :type: str
        """

        self._physical_country_id = physical_country_id

    @property
    def deleted_at(self):
        """
        Gets the deleted_at of this Outlet.
        Deletion timestamp in UTC.

        :return: The deleted_at of this Outlet.
        :rtype: str
        """
        return self._deleted_at

    @deleted_at.setter
    def deleted_at(self, deleted_at):
        """
        Sets the deleted_at of this Outlet.
        Deletion timestamp in UTC.

        :param deleted_at: The deleted_at of this Outlet.
        :type: str
        """

        self._deleted_at = deleted_at

    @property
    def version(self):
        """
        Gets the version of this Outlet.
        Auto-incrementing object version number.

        :return: The version of this Outlet.
        :rtype: float
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this Outlet.
        Auto-incrementing object version number.

        :param version: The version of this Outlet.
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
        if not isinstance(other, Outlet):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
