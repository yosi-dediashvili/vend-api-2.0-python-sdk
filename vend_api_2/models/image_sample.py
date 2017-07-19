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


class ImageSample(object):
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
        'url': 'str',
        'version': 'float'
    }

    attribute_map = {
        'id': 'id',
        'url': 'url',
        'version': 'version'
    }

    def __init__(self, id=None, url=None, version=None):
        """
        ImageSample - a model defined in Swagger
        """

        self._id = None
        self._url = None
        self._version = None

        if id is not None:
          self.id = id
        if url is not None:
          self.url = url
        if version is not None:
          self.version = version

    @property
    def id(self):
        """
        Gets the id of this ImageSample.
        Auto-generated object ID.

        :return: The id of this ImageSample.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ImageSample.
        Auto-generated object ID.

        :param id: The id of this ImageSample.
        :type: str
        """

        self._id = id

    @property
    def url(self):
        """
        Gets the url of this ImageSample.
        

        :return: The url of this ImageSample.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """
        Sets the url of this ImageSample.
        

        :param url: The url of this ImageSample.
        :type: str
        """

        self._url = url

    @property
    def version(self):
        """
        Gets the version of this ImageSample.
        Auto-incrementing object version number.

        :return: The version of this ImageSample.
        :rtype: float
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this ImageSample.
        Auto-incrementing object version number.

        :param version: The version of this ImageSample.
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
        if not isinstance(other, ImageSample):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
