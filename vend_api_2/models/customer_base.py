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


class CustomerBase(object):
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
        'first_name': 'str',
        'last_name': 'str',
        'customer_code': 'str',
        'customer_group_id': 'str',
        'enable_loyalty': 'bool',
        'email': 'str',
        'note': 'str',
        'gender': 'str',
        'date_of_birth': 'str',
        'company_name': 'str',
        'do_not_email': 'bool',
        'phone': 'str',
        'mobile': 'str',
        'fax': 'str',
        'twitter': 'str',
        'website': 'str',
        'physical_address_1': 'str',
        'physical_address_2': 'str',
        'physical_suburb': 'str',
        'physical_city': 'str',
        'physical_postcode': 'str',
        'physical_state': 'str',
        'physical_country_id': 'str',
        'postal_address_1': 'str',
        'postal_address_2': 'str',
        'postal_suburb': 'str',
        'postal_city': 'str',
        'postal_postcode': 'str',
        'postal_state': 'str',
        'postal_country_id': 'str',
        'custom_field_1': 'str',
        'custom_field_2': 'str',
        'custom_field_3': 'str',
        'custom_field_4': 'str'
    }

    attribute_map = {
        'first_name': 'first_name',
        'last_name': 'last_name',
        'customer_code': 'customer_code',
        'customer_group_id': 'customer_group_id',
        'enable_loyalty': 'enable_loyalty',
        'email': 'email',
        'note': 'note',
        'gender': 'gender',
        'date_of_birth': 'date_of_birth',
        'company_name': 'company_name',
        'do_not_email': 'do_not_email',
        'phone': 'phone',
        'mobile': 'mobile',
        'fax': 'fax',
        'twitter': 'twitter',
        'website': 'website',
        'physical_address_1': 'physical_address_1',
        'physical_address_2': 'physical_address_2',
        'physical_suburb': 'physical_suburb',
        'physical_city': 'physical_city',
        'physical_postcode': 'physical_postcode',
        'physical_state': 'physical_state',
        'physical_country_id': 'physical_country_id',
        'postal_address_1': 'postal_address_1',
        'postal_address_2': 'postal_address_2',
        'postal_suburb': 'postal_suburb',
        'postal_city': 'postal_city',
        'postal_postcode': 'postal_postcode',
        'postal_state': 'postal_state',
        'postal_country_id': 'postal_country_id',
        'custom_field_1': 'custom_field_1',
        'custom_field_2': 'custom_field_2',
        'custom_field_3': 'custom_field_3',
        'custom_field_4': 'custom_field_4'
    }

    def __init__(self, first_name=None, last_name=None, customer_code=None, customer_group_id=None, enable_loyalty=None, email=None, note=None, gender=None, date_of_birth=None, company_name=None, do_not_email=False, phone=None, mobile=None, fax=None, twitter=None, website=None, physical_address_1=None, physical_address_2=None, physical_suburb=None, physical_city=None, physical_postcode=None, physical_state=None, physical_country_id=None, postal_address_1=None, postal_address_2=None, postal_suburb=None, postal_city=None, postal_postcode=None, postal_state=None, postal_country_id=None, custom_field_1=None, custom_field_2=None, custom_field_3=None, custom_field_4=None):
        """
        CustomerBase - a model defined in Swagger
        """

        self._first_name = None
        self._last_name = None
        self._customer_code = None
        self._customer_group_id = None
        self._enable_loyalty = None
        self._email = None
        self._note = None
        self._gender = None
        self._date_of_birth = None
        self._company_name = None
        self._do_not_email = None
        self._phone = None
        self._mobile = None
        self._fax = None
        self._twitter = None
        self._website = None
        self._physical_address_1 = None
        self._physical_address_2 = None
        self._physical_suburb = None
        self._physical_city = None
        self._physical_postcode = None
        self._physical_state = None
        self._physical_country_id = None
        self._postal_address_1 = None
        self._postal_address_2 = None
        self._postal_suburb = None
        self._postal_city = None
        self._postal_postcode = None
        self._postal_state = None
        self._postal_country_id = None
        self._custom_field_1 = None
        self._custom_field_2 = None
        self._custom_field_3 = None
        self._custom_field_4 = None
        self.discriminator = None

        self.first_name = first_name
        self.last_name = last_name
        if customer_code is not None:
          self.customer_code = customer_code
        if customer_group_id is not None:
          self.customer_group_id = customer_group_id
        if enable_loyalty is not None:
          self.enable_loyalty = enable_loyalty
        if email is not None:
          self.email = email
        if note is not None:
          self.note = note
        if gender is not None:
          self.gender = gender
        if date_of_birth is not None:
          self.date_of_birth = date_of_birth
        if company_name is not None:
          self.company_name = company_name
        if do_not_email is not None:
          self.do_not_email = do_not_email
        if phone is not None:
          self.phone = phone
        if mobile is not None:
          self.mobile = mobile
        if fax is not None:
          self.fax = fax
        if twitter is not None:
          self.twitter = twitter
        if website is not None:
          self.website = website
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
        if postal_address_1 is not None:
          self.postal_address_1 = postal_address_1
        if postal_address_2 is not None:
          self.postal_address_2 = postal_address_2
        if postal_suburb is not None:
          self.postal_suburb = postal_suburb
        if postal_city is not None:
          self.postal_city = postal_city
        if postal_postcode is not None:
          self.postal_postcode = postal_postcode
        if postal_state is not None:
          self.postal_state = postal_state
        if postal_country_id is not None:
          self.postal_country_id = postal_country_id
        if custom_field_1 is not None:
          self.custom_field_1 = custom_field_1
        if custom_field_2 is not None:
          self.custom_field_2 = custom_field_2
        if custom_field_3 is not None:
          self.custom_field_3 = custom_field_3
        if custom_field_4 is not None:
          self.custom_field_4 = custom_field_4

    @property
    def first_name(self):
        """
        Gets the first_name of this CustomerBase.
        Customer's first name.

        :return: The first_name of this CustomerBase.
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """
        Sets the first_name of this CustomerBase.
        Customer's first name.

        :param first_name: The first_name of this CustomerBase.
        :type: str
        """
        if first_name is None:
            raise ValueError("Invalid value for `first_name`, must not be `None`")

        self._first_name = first_name

    @property
    def last_name(self):
        """
        Gets the last_name of this CustomerBase.
        Customer 's last name.

        :return: The last_name of this CustomerBase.
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """
        Sets the last_name of this CustomerBase.
        Customer 's last name.

        :param last_name: The last_name of this CustomerBase.
        :type: str
        """
        if last_name is None:
            raise ValueError("Invalid value for `last_name`, must not be `None`")

        self._last_name = last_name

    @property
    def customer_code(self):
        """
        Gets the customer_code of this CustomerBase.
        Customer code used for claiming loyalty.

        :return: The customer_code of this CustomerBase.
        :rtype: str
        """
        return self._customer_code

    @customer_code.setter
    def customer_code(self, customer_code):
        """
        Sets the customer_code of this CustomerBase.
        Customer code used for claiming loyalty.

        :param customer_code: The customer_code of this CustomerBase.
        :type: str
        """

        self._customer_code = customer_code

    @property
    def customer_group_id(self):
        """
        Gets the customer_group_id of this CustomerBase.
        Customer group ID.

        :return: The customer_group_id of this CustomerBase.
        :rtype: str
        """
        return self._customer_group_id

    @customer_group_id.setter
    def customer_group_id(self, customer_group_id):
        """
        Sets the customer_group_id of this CustomerBase.
        Customer group ID.

        :param customer_group_id: The customer_group_id of this CustomerBase.
        :type: str
        """

        self._customer_group_id = customer_group_id

    @property
    def enable_loyalty(self):
        """
        Gets the enable_loyalty of this CustomerBase.
        

        :return: The enable_loyalty of this CustomerBase.
        :rtype: bool
        """
        return self._enable_loyalty

    @enable_loyalty.setter
    def enable_loyalty(self, enable_loyalty):
        """
        Sets the enable_loyalty of this CustomerBase.
        

        :param enable_loyalty: The enable_loyalty of this CustomerBase.
        :type: bool
        """

        self._enable_loyalty = enable_loyalty

    @property
    def email(self):
        """
        Gets the email of this CustomerBase.
        Customer's email address.

        :return: The email of this CustomerBase.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this CustomerBase.
        Customer's email address.

        :param email: The email of this CustomerBase.
        :type: str
        """

        self._email = email

    @property
    def note(self):
        """
        Gets the note of this CustomerBase.
        Customer note.

        :return: The note of this CustomerBase.
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note):
        """
        Sets the note of this CustomerBase.
        Customer note.

        :param note: The note of this CustomerBase.
        :type: str
        """

        self._note = note

    @property
    def gender(self):
        """
        Gets the gender of this CustomerBase.
        Customer's gender. Can be `M`, `F` or null.

        :return: The gender of this CustomerBase.
        :rtype: str
        """
        return self._gender

    @gender.setter
    def gender(self, gender):
        """
        Sets the gender of this CustomerBase.
        Customer's gender. Can be `M`, `F` or null.

        :param gender: The gender of this CustomerBase.
        :type: str
        """

        self._gender = gender

    @property
    def date_of_birth(self):
        """
        Gets the date_of_birth of this CustomerBase.
        Birthday.

        :return: The date_of_birth of this CustomerBase.
        :rtype: str
        """
        return self._date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, date_of_birth):
        """
        Sets the date_of_birth of this CustomerBase.
        Birthday.

        :param date_of_birth: The date_of_birth of this CustomerBase.
        :type: str
        """

        self._date_of_birth = date_of_birth

    @property
    def company_name(self):
        """
        Gets the company_name of this CustomerBase.
        Company name.

        :return: The company_name of this CustomerBase.
        :rtype: str
        """
        return self._company_name

    @company_name.setter
    def company_name(self, company_name):
        """
        Sets the company_name of this CustomerBase.
        Company name.

        :param company_name: The company_name of this CustomerBase.
        :type: str
        """

        self._company_name = company_name

    @property
    def do_not_email(self):
        """
        Gets the do_not_email of this CustomerBase.
        Indicates whether the customer opted out of email communications.

        :return: The do_not_email of this CustomerBase.
        :rtype: bool
        """
        return self._do_not_email

    @do_not_email.setter
    def do_not_email(self, do_not_email):
        """
        Sets the do_not_email of this CustomerBase.
        Indicates whether the customer opted out of email communications.

        :param do_not_email: The do_not_email of this CustomerBase.
        :type: bool
        """

        self._do_not_email = do_not_email

    @property
    def phone(self):
        """
        Gets the phone of this CustomerBase.
        Phone no.

        :return: The phone of this CustomerBase.
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """
        Sets the phone of this CustomerBase.
        Phone no.

        :param phone: The phone of this CustomerBase.
        :type: str
        """

        self._phone = phone

    @property
    def mobile(self):
        """
        Gets the mobile of this CustomerBase.
        Mobile phone no.

        :return: The mobile of this CustomerBase.
        :rtype: str
        """
        return self._mobile

    @mobile.setter
    def mobile(self, mobile):
        """
        Sets the mobile of this CustomerBase.
        Mobile phone no.

        :param mobile: The mobile of this CustomerBase.
        :type: str
        """

        self._mobile = mobile

    @property
    def fax(self):
        """
        Gets the fax of this CustomerBase.
        Fax no.

        :return: The fax of this CustomerBase.
        :rtype: str
        """
        return self._fax

    @fax.setter
    def fax(self, fax):
        """
        Sets the fax of this CustomerBase.
        Fax no.

        :param fax: The fax of this CustomerBase.
        :type: str
        """

        self._fax = fax

    @property
    def twitter(self):
        """
        Gets the twitter of this CustomerBase.
        Twitter handle.

        :return: The twitter of this CustomerBase.
        :rtype: str
        """
        return self._twitter

    @twitter.setter
    def twitter(self, twitter):
        """
        Sets the twitter of this CustomerBase.
        Twitter handle.

        :param twitter: The twitter of this CustomerBase.
        :type: str
        """

        self._twitter = twitter

    @property
    def website(self):
        """
        Gets the website of this CustomerBase.
        Website URL.

        :return: The website of this CustomerBase.
        :rtype: str
        """
        return self._website

    @website.setter
    def website(self, website):
        """
        Sets the website of this CustomerBase.
        Website URL.

        :param website: The website of this CustomerBase.
        :type: str
        """

        self._website = website

    @property
    def physical_address_1(self):
        """
        Gets the physical_address_1 of this CustomerBase.
        Physical address, line 1.

        :return: The physical_address_1 of this CustomerBase.
        :rtype: str
        """
        return self._physical_address_1

    @physical_address_1.setter
    def physical_address_1(self, physical_address_1):
        """
        Sets the physical_address_1 of this CustomerBase.
        Physical address, line 1.

        :param physical_address_1: The physical_address_1 of this CustomerBase.
        :type: str
        """

        self._physical_address_1 = physical_address_1

    @property
    def physical_address_2(self):
        """
        Gets the physical_address_2 of this CustomerBase.
        Physical address, line 2.

        :return: The physical_address_2 of this CustomerBase.
        :rtype: str
        """
        return self._physical_address_2

    @physical_address_2.setter
    def physical_address_2(self, physical_address_2):
        """
        Sets the physical_address_2 of this CustomerBase.
        Physical address, line 2.

        :param physical_address_2: The physical_address_2 of this CustomerBase.
        :type: str
        """

        self._physical_address_2 = physical_address_2

    @property
    def physical_suburb(self):
        """
        Gets the physical_suburb of this CustomerBase.
        Physical address, suburb.

        :return: The physical_suburb of this CustomerBase.
        :rtype: str
        """
        return self._physical_suburb

    @physical_suburb.setter
    def physical_suburb(self, physical_suburb):
        """
        Sets the physical_suburb of this CustomerBase.
        Physical address, suburb.

        :param physical_suburb: The physical_suburb of this CustomerBase.
        :type: str
        """

        self._physical_suburb = physical_suburb

    @property
    def physical_city(self):
        """
        Gets the physical_city of this CustomerBase.
        Physical address, city.

        :return: The physical_city of this CustomerBase.
        :rtype: str
        """
        return self._physical_city

    @physical_city.setter
    def physical_city(self, physical_city):
        """
        Sets the physical_city of this CustomerBase.
        Physical address, city.

        :param physical_city: The physical_city of this CustomerBase.
        :type: str
        """

        self._physical_city = physical_city

    @property
    def physical_postcode(self):
        """
        Gets the physical_postcode of this CustomerBase.
        Physical address, post code.

        :return: The physical_postcode of this CustomerBase.
        :rtype: str
        """
        return self._physical_postcode

    @physical_postcode.setter
    def physical_postcode(self, physical_postcode):
        """
        Sets the physical_postcode of this CustomerBase.
        Physical address, post code.

        :param physical_postcode: The physical_postcode of this CustomerBase.
        :type: str
        """

        self._physical_postcode = physical_postcode

    @property
    def physical_state(self):
        """
        Gets the physical_state of this CustomerBase.
        Physical address, state.

        :return: The physical_state of this CustomerBase.
        :rtype: str
        """
        return self._physical_state

    @physical_state.setter
    def physical_state(self, physical_state):
        """
        Sets the physical_state of this CustomerBase.
        Physical address, state.

        :param physical_state: The physical_state of this CustomerBase.
        :type: str
        """

        self._physical_state = physical_state

    @property
    def physical_country_id(self):
        """
        Gets the physical_country_id of this CustomerBase.
        Physical address, country code.

        :return: The physical_country_id of this CustomerBase.
        :rtype: str
        """
        return self._physical_country_id

    @physical_country_id.setter
    def physical_country_id(self, physical_country_id):
        """
        Sets the physical_country_id of this CustomerBase.
        Physical address, country code.

        :param physical_country_id: The physical_country_id of this CustomerBase.
        :type: str
        """

        self._physical_country_id = physical_country_id

    @property
    def postal_address_1(self):
        """
        Gets the postal_address_1 of this CustomerBase.
        Postal address, line 1.

        :return: The postal_address_1 of this CustomerBase.
        :rtype: str
        """
        return self._postal_address_1

    @postal_address_1.setter
    def postal_address_1(self, postal_address_1):
        """
        Sets the postal_address_1 of this CustomerBase.
        Postal address, line 1.

        :param postal_address_1: The postal_address_1 of this CustomerBase.
        :type: str
        """

        self._postal_address_1 = postal_address_1

    @property
    def postal_address_2(self):
        """
        Gets the postal_address_2 of this CustomerBase.
        Postal address, line 2.

        :return: The postal_address_2 of this CustomerBase.
        :rtype: str
        """
        return self._postal_address_2

    @postal_address_2.setter
    def postal_address_2(self, postal_address_2):
        """
        Sets the postal_address_2 of this CustomerBase.
        Postal address, line 2.

        :param postal_address_2: The postal_address_2 of this CustomerBase.
        :type: str
        """

        self._postal_address_2 = postal_address_2

    @property
    def postal_suburb(self):
        """
        Gets the postal_suburb of this CustomerBase.
        Postal address, suburb.

        :return: The postal_suburb of this CustomerBase.
        :rtype: str
        """
        return self._postal_suburb

    @postal_suburb.setter
    def postal_suburb(self, postal_suburb):
        """
        Sets the postal_suburb of this CustomerBase.
        Postal address, suburb.

        :param postal_suburb: The postal_suburb of this CustomerBase.
        :type: str
        """

        self._postal_suburb = postal_suburb

    @property
    def postal_city(self):
        """
        Gets the postal_city of this CustomerBase.
        Postal address, city.

        :return: The postal_city of this CustomerBase.
        :rtype: str
        """
        return self._postal_city

    @postal_city.setter
    def postal_city(self, postal_city):
        """
        Sets the postal_city of this CustomerBase.
        Postal address, city.

        :param postal_city: The postal_city of this CustomerBase.
        :type: str
        """

        self._postal_city = postal_city

    @property
    def postal_postcode(self):
        """
        Gets the postal_postcode of this CustomerBase.
        Postal address, post code.

        :return: The postal_postcode of this CustomerBase.
        :rtype: str
        """
        return self._postal_postcode

    @postal_postcode.setter
    def postal_postcode(self, postal_postcode):
        """
        Sets the postal_postcode of this CustomerBase.
        Postal address, post code.

        :param postal_postcode: The postal_postcode of this CustomerBase.
        :type: str
        """

        self._postal_postcode = postal_postcode

    @property
    def postal_state(self):
        """
        Gets the postal_state of this CustomerBase.
        Postal address, state.

        :return: The postal_state of this CustomerBase.
        :rtype: str
        """
        return self._postal_state

    @postal_state.setter
    def postal_state(self, postal_state):
        """
        Sets the postal_state of this CustomerBase.
        Postal address, state.

        :param postal_state: The postal_state of this CustomerBase.
        :type: str
        """

        self._postal_state = postal_state

    @property
    def postal_country_id(self):
        """
        Gets the postal_country_id of this CustomerBase.
        Postal address, country code.

        :return: The postal_country_id of this CustomerBase.
        :rtype: str
        """
        return self._postal_country_id

    @postal_country_id.setter
    def postal_country_id(self, postal_country_id):
        """
        Sets the postal_country_id of this CustomerBase.
        Postal address, country code.

        :param postal_country_id: The postal_country_id of this CustomerBase.
        :type: str
        """

        self._postal_country_id = postal_country_id

    @property
    def custom_field_1(self):
        """
        Gets the custom_field_1 of this CustomerBase.
        Custom field 1. Can be used to store random data.

        :return: The custom_field_1 of this CustomerBase.
        :rtype: str
        """
        return self._custom_field_1

    @custom_field_1.setter
    def custom_field_1(self, custom_field_1):
        """
        Sets the custom_field_1 of this CustomerBase.
        Custom field 1. Can be used to store random data.

        :param custom_field_1: The custom_field_1 of this CustomerBase.
        :type: str
        """

        self._custom_field_1 = custom_field_1

    @property
    def custom_field_2(self):
        """
        Gets the custom_field_2 of this CustomerBase.
        Custom field 2.

        :return: The custom_field_2 of this CustomerBase.
        :rtype: str
        """
        return self._custom_field_2

    @custom_field_2.setter
    def custom_field_2(self, custom_field_2):
        """
        Sets the custom_field_2 of this CustomerBase.
        Custom field 2.

        :param custom_field_2: The custom_field_2 of this CustomerBase.
        :type: str
        """

        self._custom_field_2 = custom_field_2

    @property
    def custom_field_3(self):
        """
        Gets the custom_field_3 of this CustomerBase.
        Custom field 3.

        :return: The custom_field_3 of this CustomerBase.
        :rtype: str
        """
        return self._custom_field_3

    @custom_field_3.setter
    def custom_field_3(self, custom_field_3):
        """
        Sets the custom_field_3 of this CustomerBase.
        Custom field 3.

        :param custom_field_3: The custom_field_3 of this CustomerBase.
        :type: str
        """

        self._custom_field_3 = custom_field_3

    @property
    def custom_field_4(self):
        """
        Gets the custom_field_4 of this CustomerBase.
        Custom field 4.

        :return: The custom_field_4 of this CustomerBase.
        :rtype: str
        """
        return self._custom_field_4

    @custom_field_4.setter
    def custom_field_4(self, custom_field_4):
        """
        Sets the custom_field_4 of this CustomerBase.
        Custom field 4.

        :param custom_field_4: The custom_field_4 of this CustomerBase.
        :type: str
        """

        self._custom_field_4 = custom_field_4

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
        if not isinstance(other, CustomerBase):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
