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


class Ptsv2paymentsidcapturesAggregatorInformation(object):
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
        'aggregator_id': 'str',
        'name': 'str',
        'sub_merchant': 'Ptsv2paymentsidcapturesAggregatorInformationSubMerchant'
    }

    attribute_map = {
        'aggregator_id': 'aggregatorId',
        'name': 'name',
        'sub_merchant': 'subMerchant'
    }

    def __init__(self, aggregator_id=None, name=None, sub_merchant=None):
        """
        Ptsv2paymentsidcapturesAggregatorInformation - a model defined in Swagger
        """

        self._aggregator_id = None
        self._name = None
        self._sub_merchant = None

        if aggregator_id is not None:
          self.aggregator_id = aggregator_id
        if name is not None:
          self.name = name
        if sub_merchant is not None:
          self.sub_merchant = sub_merchant

    @property
    def aggregator_id(self):
        """
        Gets the aggregator_id of this Ptsv2paymentsidcapturesAggregatorInformation.
        Value that identifies you as a payment aggregator. Get this value from the processor.  For processor-specific information, see the aggregator_id field in [Credit Card Services Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html) 

        :return: The aggregator_id of this Ptsv2paymentsidcapturesAggregatorInformation.
        :rtype: str
        """
        return self._aggregator_id

    @aggregator_id.setter
    def aggregator_id(self, aggregator_id):
        """
        Sets the aggregator_id of this Ptsv2paymentsidcapturesAggregatorInformation.
        Value that identifies you as a payment aggregator. Get this value from the processor.  For processor-specific information, see the aggregator_id field in [Credit Card Services Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html) 

        :param aggregator_id: The aggregator_id of this Ptsv2paymentsidcapturesAggregatorInformation.
        :type: str
        """
        if aggregator_id is not None and len(aggregator_id) > 20:
            raise ValueError("Invalid value for `aggregator_id`, length must be less than or equal to `20`")

        self._aggregator_id = aggregator_id

    @property
    def name(self):
        """
        Gets the name of this Ptsv2paymentsidcapturesAggregatorInformation.
        Your payment aggregator business name.  For processor-specific information, see the aggregator_name field in [Credit Card Services Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html) 

        :return: The name of this Ptsv2paymentsidcapturesAggregatorInformation.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Ptsv2paymentsidcapturesAggregatorInformation.
        Your payment aggregator business name.  For processor-specific information, see the aggregator_name field in [Credit Card Services Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html) 

        :param name: The name of this Ptsv2paymentsidcapturesAggregatorInformation.
        :type: str
        """
        if name is not None and len(name) > 37:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `37`")

        self._name = name

    @property
    def sub_merchant(self):
        """
        Gets the sub_merchant of this Ptsv2paymentsidcapturesAggregatorInformation.

        :return: The sub_merchant of this Ptsv2paymentsidcapturesAggregatorInformation.
        :rtype: Ptsv2paymentsidcapturesAggregatorInformationSubMerchant
        """
        return self._sub_merchant

    @sub_merchant.setter
    def sub_merchant(self, sub_merchant):
        """
        Sets the sub_merchant of this Ptsv2paymentsidcapturesAggregatorInformation.

        :param sub_merchant: The sub_merchant of this Ptsv2paymentsidcapturesAggregatorInformation.
        :type: Ptsv2paymentsidcapturesAggregatorInformationSubMerchant
        """

        self._sub_merchant = sub_merchant

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
        if not isinstance(other, Ptsv2paymentsidcapturesAggregatorInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other