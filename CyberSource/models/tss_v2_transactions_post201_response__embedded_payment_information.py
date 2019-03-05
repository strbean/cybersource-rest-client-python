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


class TssV2TransactionsPost201ResponseEmbeddedPaymentInformation(object):
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
        'payment_method': 'TssV2TransactionsPost201ResponseEmbeddedPaymentInformationPaymentMethod',
        'customer': 'TssV2TransactionsGet200ResponsePaymentInformationCustomer',
        'card': 'TssV2TransactionsPost201ResponseEmbeddedPaymentInformationCard'
    }

    attribute_map = {
        'payment_method': 'paymentMethod',
        'customer': 'customer',
        'card': 'card'
    }

    def __init__(self, payment_method=None, customer=None, card=None):
        """
        TssV2TransactionsPost201ResponseEmbeddedPaymentInformation - a model defined in Swagger
        """

        self._payment_method = None
        self._customer = None
        self._card = None

        if payment_method is not None:
          self.payment_method = payment_method
        if customer is not None:
          self.customer = customer
        if card is not None:
          self.card = card

    @property
    def payment_method(self):
        """
        Gets the payment_method of this TssV2TransactionsPost201ResponseEmbeddedPaymentInformation.

        :return: The payment_method of this TssV2TransactionsPost201ResponseEmbeddedPaymentInformation.
        :rtype: TssV2TransactionsPost201ResponseEmbeddedPaymentInformationPaymentMethod
        """
        return self._payment_method

    @payment_method.setter
    def payment_method(self, payment_method):
        """
        Sets the payment_method of this TssV2TransactionsPost201ResponseEmbeddedPaymentInformation.

        :param payment_method: The payment_method of this TssV2TransactionsPost201ResponseEmbeddedPaymentInformation.
        :type: TssV2TransactionsPost201ResponseEmbeddedPaymentInformationPaymentMethod
        """

        self._payment_method = payment_method

    @property
    def customer(self):
        """
        Gets the customer of this TssV2TransactionsPost201ResponseEmbeddedPaymentInformation.

        :return: The customer of this TssV2TransactionsPost201ResponseEmbeddedPaymentInformation.
        :rtype: TssV2TransactionsGet200ResponsePaymentInformationCustomer
        """
        return self._customer

    @customer.setter
    def customer(self, customer):
        """
        Sets the customer of this TssV2TransactionsPost201ResponseEmbeddedPaymentInformation.

        :param customer: The customer of this TssV2TransactionsPost201ResponseEmbeddedPaymentInformation.
        :type: TssV2TransactionsGet200ResponsePaymentInformationCustomer
        """

        self._customer = customer

    @property
    def card(self):
        """
        Gets the card of this TssV2TransactionsPost201ResponseEmbeddedPaymentInformation.

        :return: The card of this TssV2TransactionsPost201ResponseEmbeddedPaymentInformation.
        :rtype: TssV2TransactionsPost201ResponseEmbeddedPaymentInformationCard
        """
        return self._card

    @card.setter
    def card(self, card):
        """
        Sets the card of this TssV2TransactionsPost201ResponseEmbeddedPaymentInformation.

        :param card: The card of this TssV2TransactionsPost201ResponseEmbeddedPaymentInformation.
        :type: TssV2TransactionsPost201ResponseEmbeddedPaymentInformationCard
        """

        self._card = card

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
        if not isinstance(other, TssV2TransactionsPost201ResponseEmbeddedPaymentInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
