# coding: utf-8

"""
    CyberSource Flex API

    Simple PAN tokenization service

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class PtsV1TransactionBatchesIdGet200Response(object):
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
        'upload_date': 'str',
        'completion_date': 'str',
        'transaction_count': 'int',
        'accepted_transaction_count': 'int',
        'rejected_transaction_count': 'str',
        'status': 'str',
        'links': 'PtsV1TransactionBatchesIdGet200ResponseLinks'
    }

    attribute_map = {
        'id': 'id',
        'upload_date': 'uploadDate',
        'completion_date': 'completionDate',
        'transaction_count': 'transactionCount',
        'accepted_transaction_count': 'acceptedTransactionCount',
        'rejected_transaction_count': 'rejectedTransactionCount',
        'status': 'status',
        'links': '_links'
    }

    def __init__(self, id=None, upload_date=None, completion_date=None, transaction_count=None, accepted_transaction_count=None, rejected_transaction_count=None, status=None, links=None):
        """
        PtsV1TransactionBatchesIdGet200Response - a model defined in Swagger
        """

        self._id = None
        self._upload_date = None
        self._completion_date = None
        self._transaction_count = None
        self._accepted_transaction_count = None
        self._rejected_transaction_count = None
        self._status = None
        self._links = None

        if id is not None:
          self.id = id
        if upload_date is not None:
          self.upload_date = upload_date
        if completion_date is not None:
          self.completion_date = completion_date
        if transaction_count is not None:
          self.transaction_count = transaction_count
        if accepted_transaction_count is not None:
          self.accepted_transaction_count = accepted_transaction_count
        if rejected_transaction_count is not None:
          self.rejected_transaction_count = rejected_transaction_count
        if status is not None:
          self.status = status
        if links is not None:
          self.links = links

    @property
    def id(self):
        """
        Gets the id of this PtsV1TransactionBatchesIdGet200Response.
        Unique identifier assigned to the batch file.

        :return: The id of this PtsV1TransactionBatchesIdGet200Response.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this PtsV1TransactionBatchesIdGet200Response.
        Unique identifier assigned to the batch file.

        :param id: The id of this PtsV1TransactionBatchesIdGet200Response.
        :type: str
        """
        if id is not None and len(id) > 8:
            raise ValueError("Invalid value for `id`, length must be less than or equal to `8`")
        if id is not None and len(id) < 1:
            raise ValueError("Invalid value for `id`, length must be greater than or equal to `1`")
        if id is not None and not re.search('^[a-zA-Z0-9_+-]*$', id):
            raise ValueError("Invalid value for `id`, must be a follow pattern or equal to `/^[a-zA-Z0-9_+-]*$/`")

        self._id = id

    @property
    def upload_date(self):
        """
        Gets the upload_date of this PtsV1TransactionBatchesIdGet200Response.
        Date when the batch template was update.

        :return: The upload_date of this PtsV1TransactionBatchesIdGet200Response.
        :rtype: str
        """
        return self._upload_date

    @upload_date.setter
    def upload_date(self, upload_date):
        """
        Sets the upload_date of this PtsV1TransactionBatchesIdGet200Response.
        Date when the batch template was update.

        :param upload_date: The upload_date of this PtsV1TransactionBatchesIdGet200Response.
        :type: str
        """

        self._upload_date = upload_date

    @property
    def completion_date(self):
        """
        Gets the completion_date of this PtsV1TransactionBatchesIdGet200Response.
        The date when the batch template processing completed.

        :return: The completion_date of this PtsV1TransactionBatchesIdGet200Response.
        :rtype: str
        """
        return self._completion_date

    @completion_date.setter
    def completion_date(self, completion_date):
        """
        Sets the completion_date of this PtsV1TransactionBatchesIdGet200Response.
        The date when the batch template processing completed.

        :param completion_date: The completion_date of this PtsV1TransactionBatchesIdGet200Response.
        :type: str
        """

        self._completion_date = completion_date

    @property
    def transaction_count(self):
        """
        Gets the transaction_count of this PtsV1TransactionBatchesIdGet200Response.
        Number of transactions in the transaction.

        :return: The transaction_count of this PtsV1TransactionBatchesIdGet200Response.
        :rtype: int
        """
        return self._transaction_count

    @transaction_count.setter
    def transaction_count(self, transaction_count):
        """
        Sets the transaction_count of this PtsV1TransactionBatchesIdGet200Response.
        Number of transactions in the transaction.

        :param transaction_count: The transaction_count of this PtsV1TransactionBatchesIdGet200Response.
        :type: int
        """

        self._transaction_count = transaction_count

    @property
    def accepted_transaction_count(self):
        """
        Gets the accepted_transaction_count of this PtsV1TransactionBatchesIdGet200Response.
        Number of transactions accepted.

        :return: The accepted_transaction_count of this PtsV1TransactionBatchesIdGet200Response.
        :rtype: int
        """
        return self._accepted_transaction_count

    @accepted_transaction_count.setter
    def accepted_transaction_count(self, accepted_transaction_count):
        """
        Sets the accepted_transaction_count of this PtsV1TransactionBatchesIdGet200Response.
        Number of transactions accepted.

        :param accepted_transaction_count: The accepted_transaction_count of this PtsV1TransactionBatchesIdGet200Response.
        :type: int
        """

        self._accepted_transaction_count = accepted_transaction_count

    @property
    def rejected_transaction_count(self):
        """
        Gets the rejected_transaction_count of this PtsV1TransactionBatchesIdGet200Response.
        Number of transactions rejected.

        :return: The rejected_transaction_count of this PtsV1TransactionBatchesIdGet200Response.
        :rtype: str
        """
        return self._rejected_transaction_count

    @rejected_transaction_count.setter
    def rejected_transaction_count(self, rejected_transaction_count):
        """
        Sets the rejected_transaction_count of this PtsV1TransactionBatchesIdGet200Response.
        Number of transactions rejected.

        :param rejected_transaction_count: The rejected_transaction_count of this PtsV1TransactionBatchesIdGet200Response.
        :type: str
        """

        self._rejected_transaction_count = rejected_transaction_count

    @property
    def status(self):
        """
        Gets the status of this PtsV1TransactionBatchesIdGet200Response.
        The status of you batch template processing.

        :return: The status of this PtsV1TransactionBatchesIdGet200Response.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this PtsV1TransactionBatchesIdGet200Response.
        The status of you batch template processing.

        :param status: The status of this PtsV1TransactionBatchesIdGet200Response.
        :type: str
        """

        self._status = status

    @property
    def links(self):
        """
        Gets the links of this PtsV1TransactionBatchesIdGet200Response.

        :return: The links of this PtsV1TransactionBatchesIdGet200Response.
        :rtype: PtsV1TransactionBatchesIdGet200ResponseLinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """
        Sets the links of this PtsV1TransactionBatchesIdGet200Response.

        :param links: The links of this PtsV1TransactionBatchesIdGet200Response.
        :type: PtsV1TransactionBatchesIdGet200ResponseLinks
        """

        self._links = links

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
        if not isinstance(other, PtsV1TransactionBatchesIdGet200Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
