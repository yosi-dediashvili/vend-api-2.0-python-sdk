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


class Consignment(object):
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
        'outlet_id': 'str',
        'name': 'str',
        'consignment_date': 'str',
        'due_at': 'str',
        'received_at': 'str',
        'type': 'str',
        'status': 'str',
        'supplier_id': 'str',
        'source_outlet_id': 'str',
        'supplier_invoice': 'str',
        'reference': 'str',
        'total_cost_gain': 'float',
        'total_count_loss': 'float',
        'total_cost_loss': 'float',
        'created_at': 'str',
        'updated_at': 'str',
        'deleted_at': 'str',
        'version': 'float',
        'total_count_gain': 'float'
    }

    attribute_map = {
        'id': 'id',
        'outlet_id': 'outlet_id',
        'name': 'name',
        'consignment_date': 'consignment_date',
        'due_at': 'due_at',
        'received_at': 'received_at',
        'type': 'type',
        'status': 'status',
        'supplier_id': 'supplier_id',
        'source_outlet_id': 'source_outlet_id',
        'supplier_invoice': 'supplier_invoice',
        'reference': 'reference',
        'total_cost_gain': 'total_cost_gain',
        'total_count_loss': 'total_count_loss',
        'total_cost_loss': 'total_cost_loss',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'deleted_at': 'deleted_at',
        'version': 'version',
        'total_count_gain': 'total_count_gain'
    }

    def __init__(self, id=None, outlet_id=None, name=None, consignment_date=None, due_at=None, received_at=None, type=None, status=None, supplier_id=None, source_outlet_id=None, supplier_invoice=None, reference=None, total_cost_gain=None, total_count_loss=None, total_cost_loss=None, created_at=None, updated_at=None, deleted_at=None, version=None, total_count_gain=None):
        """
        Consignment - a model defined in Swagger
        """

        self._id = None
        self._outlet_id = None
        self._name = None
        self._consignment_date = None
        self._due_at = None
        self._received_at = None
        self._type = None
        self._status = None
        self._supplier_id = None
        self._source_outlet_id = None
        self._supplier_invoice = None
        self._reference = None
        self._total_cost_gain = None
        self._total_count_loss = None
        self._total_cost_loss = None
        self._created_at = None
        self._updated_at = None
        self._deleted_at = None
        self._version = None
        self._total_count_gain = None
        self.discriminator = None

        if id is not None:
          self.id = id
        if outlet_id is not None:
          self.outlet_id = outlet_id
        if name is not None:
          self.name = name
        if consignment_date is not None:
          self.consignment_date = consignment_date
        if due_at is not None:
          self.due_at = due_at
        if received_at is not None:
          self.received_at = received_at
        if type is not None:
          self.type = type
        if status is not None:
          self.status = status
        if supplier_id is not None:
          self.supplier_id = supplier_id
        if source_outlet_id is not None:
          self.source_outlet_id = source_outlet_id
        if supplier_invoice is not None:
          self.supplier_invoice = supplier_invoice
        if reference is not None:
          self.reference = reference
        if total_cost_gain is not None:
          self.total_cost_gain = total_cost_gain
        if total_count_loss is not None:
          self.total_count_loss = total_count_loss
        if total_cost_loss is not None:
          self.total_cost_loss = total_cost_loss
        if created_at is not None:
          self.created_at = created_at
        if updated_at is not None:
          self.updated_at = updated_at
        if deleted_at is not None:
          self.deleted_at = deleted_at
        if version is not None:
          self.version = version
        if total_count_gain is not None:
          self.total_count_gain = total_count_gain

    @property
    def id(self):
        """
        Gets the id of this Consignment.
        Auto-generated object ID.

        :return: The id of this Consignment.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Consignment.
        Auto-generated object ID.

        :param id: The id of this Consignment.
        :type: str
        """

        self._id = id

    @property
    def outlet_id(self):
        """
        Gets the outlet_id of this Consignment.
        A valid ID of an outlet where stock will be received.

        :return: The outlet_id of this Consignment.
        :rtype: str
        """
        return self._outlet_id

    @outlet_id.setter
    def outlet_id(self, outlet_id):
        """
        Sets the outlet_id of this Consignment.
        A valid ID of an outlet where stock will be received.

        :param outlet_id: The outlet_id of this Consignment.
        :type: str
        """

        self._outlet_id = outlet_id

    @property
    def name(self):
        """
        Gets the name of this Consignment.
        Tue 29 Nov 2016 (string) - Consignment name.

        :return: The name of this Consignment.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Consignment.
        Tue 29 Nov 2016 (string) - Consignment name.

        :param name: The name of this Consignment.
        :type: str
        """

        self._name = name

    @property
    def consignment_date(self):
        """
        Gets the consignment_date of this Consignment.
        11-28T19:02:15+00:00 (timestamp) - Consignment creation date.

        :return: The consignment_date of this Consignment.
        :rtype: str
        """
        return self._consignment_date

    @consignment_date.setter
    def consignment_date(self, consignment_date):
        """
        Sets the consignment_date of this Consignment.
        11-28T19:02:15+00:00 (timestamp) - Consignment creation date.

        :param consignment_date: The consignment_date of this Consignment.
        :type: str
        """

        self._consignment_date = consignment_date

    @property
    def due_at(self):
        """
        Gets the due_at of this Consignment.
        11-30T19:08:541+00:00 (timestamp) - Due date.

        :return: The due_at of this Consignment.
        :rtype: str
        """
        return self._due_at

    @due_at.setter
    def due_at(self, due_at):
        """
        Sets the due_at of this Consignment.
        11-30T19:08:541+00:00 (timestamp) - Due date.

        :param due_at: The due_at of this Consignment.
        :type: str
        """

        self._due_at = due_at

    @property
    def received_at(self):
        """
        Gets the received_at of this Consignment.
        11-30T19:08:541+00:00 (timestamp) - The date when consignment was received.

        :return: The received_at of this Consignment.
        :rtype: str
        """
        return self._received_at

    @received_at.setter
    def received_at(self, received_at):
        """
        Sets the received_at of this Consignment.
        11-30T19:08:541+00:00 (timestamp) - The date when consignment was received.

        :param received_at: The received_at of this Consignment.
        :type: str
        """

        self._received_at = received_at

    @property
    def type(self):
        """
        Gets the type of this Consignment.
        One of `SUPPLIER`, `OUTLET`, `STOCKTAKE`, `RETURN`.

        :return: The type of this Consignment.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this Consignment.
        One of `SUPPLIER`, `OUTLET`, `STOCKTAKE`, `RETURN`.

        :param type: The type of this Consignment.
        :type: str
        """

        self._type = type

    @property
    def status(self):
        """
        Gets the status of this Consignment.
        One of `OPEN`, `RECEIVED`, `SENT`, `STOCKTAKE`, `STOCKTAKE_SCHEDULED`, `STOCKTAKE_IN_PROGRESS`, `STOCKTAKE_IN_PROGRESS_PROCESSED`, `STOCKTAKE_COMPLETE`, `CLOSED`, `CANCELLED`

        :return: The status of this Consignment.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this Consignment.
        One of `OPEN`, `RECEIVED`, `SENT`, `STOCKTAKE`, `STOCKTAKE_SCHEDULED`, `STOCKTAKE_IN_PROGRESS`, `STOCKTAKE_IN_PROGRESS_PROCESSED`, `STOCKTAKE_COMPLETE`, `CLOSED`, `CANCELLED`

        :param status: The status of this Consignment.
        :type: str
        """

        self._status = status

    @property
    def supplier_id(self):
        """
        Gets the supplier_id of this Consignment.
        a valid supplier ID.

        :return: The supplier_id of this Consignment.
        :rtype: str
        """
        return self._supplier_id

    @supplier_id.setter
    def supplier_id(self, supplier_id):
        """
        Sets the supplier_id of this Consignment.
        a valid supplier ID.

        :param supplier_id: The supplier_id of this Consignment.
        :type: str
        """

        self._supplier_id = supplier_id

    @property
    def source_outlet_id(self):
        """
        Gets the source_outlet_id of this Consignment.
        A valid ID of an outlet where stock will come from. **Stock transfers only**.

        :return: The source_outlet_id of this Consignment.
        :rtype: str
        """
        return self._source_outlet_id

    @source_outlet_id.setter
    def source_outlet_id(self, source_outlet_id):
        """
        Sets the source_outlet_id of this Consignment.
        A valid ID of an outlet where stock will come from. **Stock transfers only**.

        :param source_outlet_id: The source_outlet_id of this Consignment.
        :type: str
        """

        self._source_outlet_id = source_outlet_id

    @property
    def supplier_invoice(self):
        """
        Gets the supplier_invoice of this Consignment.
        Supplier invoice number.

        :return: The supplier_invoice of this Consignment.
        :rtype: str
        """
        return self._supplier_invoice

    @supplier_invoice.setter
    def supplier_invoice(self, supplier_invoice):
        """
        Sets the supplier_invoice of this Consignment.
        Supplier invoice number.

        :param supplier_invoice: The supplier_invoice of this Consignment.
        :type: str
        """

        self._supplier_invoice = supplier_invoice

    @property
    def reference(self):
        """
        Gets the reference of this Consignment.
        Order number.+ `total_count_gain` (number)

        :return: The reference of this Consignment.
        :rtype: str
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        """
        Sets the reference of this Consignment.
        Order number.+ `total_count_gain` (number)

        :param reference: The reference of this Consignment.
        :type: str
        """

        self._reference = reference

    @property
    def total_cost_gain(self):
        """
        Gets the total_cost_gain of this Consignment.
        The cost of items over the expected level.

        :return: The total_cost_gain of this Consignment.
        :rtype: float
        """
        return self._total_cost_gain

    @total_cost_gain.setter
    def total_cost_gain(self, total_cost_gain):
        """
        Sets the total_cost_gain of this Consignment.
        The cost of items over the expected level.

        :param total_cost_gain: The total_cost_gain of this Consignment.
        :type: float
        """

        self._total_cost_gain = total_cost_gain

    @property
    def total_count_loss(self):
        """
        Gets the total_count_loss of this Consignment.
        The number of items below the expected level.

        :return: The total_count_loss of this Consignment.
        :rtype: float
        """
        return self._total_count_loss

    @total_count_loss.setter
    def total_count_loss(self, total_count_loss):
        """
        Sets the total_count_loss of this Consignment.
        The number of items below the expected level.

        :param total_count_loss: The total_count_loss of this Consignment.
        :type: float
        """

        self._total_count_loss = total_count_loss

    @property
    def total_cost_loss(self):
        """
        Gets the total_cost_loss of this Consignment.
        The cost of items below the expected level.

        :return: The total_cost_loss of this Consignment.
        :rtype: float
        """
        return self._total_cost_loss

    @total_cost_loss.setter
    def total_cost_loss(self, total_cost_loss):
        """
        Sets the total_cost_loss of this Consignment.
        The cost of items below the expected level.

        :param total_cost_loss: The total_cost_loss of this Consignment.
        :type: float
        """

        self._total_cost_loss = total_cost_loss

    @property
    def created_at(self):
        """
        Gets the created_at of this Consignment.
        Creation timestamp in UTC.

        :return: The created_at of this Consignment.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """
        Sets the created_at of this Consignment.
        Creation timestamp in UTC.

        :param created_at: The created_at of this Consignment.
        :type: str
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """
        Gets the updated_at of this Consignment.
        Last update timestamp in UTC.

        :return: The updated_at of this Consignment.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """
        Sets the updated_at of this Consignment.
        Last update timestamp in UTC.

        :param updated_at: The updated_at of this Consignment.
        :type: str
        """

        self._updated_at = updated_at

    @property
    def deleted_at(self):
        """
        Gets the deleted_at of this Consignment.
        Deletion timestamp in UTC.

        :return: The deleted_at of this Consignment.
        :rtype: str
        """
        return self._deleted_at

    @deleted_at.setter
    def deleted_at(self, deleted_at):
        """
        Sets the deleted_at of this Consignment.
        Deletion timestamp in UTC.

        :param deleted_at: The deleted_at of this Consignment.
        :type: str
        """

        self._deleted_at = deleted_at

    @property
    def version(self):
        """
        Gets the version of this Consignment.
        Auto-incrementing object version number.

        :return: The version of this Consignment.
        :rtype: float
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this Consignment.
        Auto-incrementing object version number.

        :param version: The version of this Consignment.
        :type: float
        """

        self._version = version

    @property
    def total_count_gain(self):
        """
        Gets the total_count_gain of this Consignment.
        The number of items over the expected level.

        :return: The total_count_gain of this Consignment.
        :rtype: float
        """
        return self._total_count_gain

    @total_count_gain.setter
    def total_count_gain(self, total_count_gain):
        """
        Sets the total_count_gain of this Consignment.
        The number of items over the expected level.

        :param total_count_gain: The total_count_gain of this Consignment.
        :type: float
        """

        self._total_count_gain = total_count_gain

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
        if not isinstance(other, Consignment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
