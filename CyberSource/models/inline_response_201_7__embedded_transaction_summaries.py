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


class InlineResponse2017EmbeddedTransactionSummaries(object):
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
        'submit_time_utc': 'str',
        'merchant_id': 'str',
        'application_information': 'InlineResponse20012ApplicationInformation',
        'buyer_information': 'InlineResponse2017EmbeddedBuyerInformation',
        'client_reference_information': 'InlineResponse2017EmbeddedClientReferenceInformation',
        'consumer_authentication_information': 'InlineResponse2017EmbeddedConsumerAuthenticationInformation',
        'device_information': 'InlineResponse2017EmbeddedDeviceInformation',
        'fraud_marking_information': 'InlineResponse20012FraudMarkingInformation',
        'merchant_defined_information': 'list[InlineResponse20012MerchantDefinedInformation]',
        'merchant_information': 'InlineResponse2017EmbeddedMerchantInformation',
        'order_information': 'InlineResponse2017EmbeddedOrderInformation',
        'payment_information': 'InlineResponse2017EmbeddedPaymentInformation',
        'processing_information': 'InlineResponse2017EmbeddedProcessingInformation',
        'processor_information': 'InlineResponse2017EmbeddedProcessorInformation',
        'point_of_sale_information': 'InlineResponse2017EmbeddedPointOfSaleInformation',
        'risk_information': 'InlineResponse2017EmbeddedRiskInformation',
        'links': 'InlineResponse2017EmbeddedLinks'
    }

    attribute_map = {
        'id': 'id',
        'submit_time_utc': 'submitTimeUtc',
        'merchant_id': 'merchantId',
        'application_information': 'applicationInformation',
        'buyer_information': 'buyerInformation',
        'client_reference_information': 'clientReferenceInformation',
        'consumer_authentication_information': 'consumerAuthenticationInformation',
        'device_information': 'deviceInformation',
        'fraud_marking_information': 'fraudMarkingInformation',
        'merchant_defined_information': 'merchantDefinedInformation',
        'merchant_information': 'merchantInformation',
        'order_information': 'orderInformation',
        'payment_information': 'paymentInformation',
        'processing_information': 'processingInformation',
        'processor_information': 'processorInformation',
        'point_of_sale_information': 'pointOfSaleInformation',
        'risk_information': 'riskInformation',
        'links': '_links'
    }

    def __init__(self, id=None, submit_time_utc=None, merchant_id=None, application_information=None, buyer_information=None, client_reference_information=None, consumer_authentication_information=None, device_information=None, fraud_marking_information=None, merchant_defined_information=None, merchant_information=None, order_information=None, payment_information=None, processing_information=None, processor_information=None, point_of_sale_information=None, risk_information=None, links=None):
        """
        InlineResponse2017EmbeddedTransactionSummaries - a model defined in Swagger
        """

        self._id = None
        self._submit_time_utc = None
        self._merchant_id = None
        self._application_information = None
        self._buyer_information = None
        self._client_reference_information = None
        self._consumer_authentication_information = None
        self._device_information = None
        self._fraud_marking_information = None
        self._merchant_defined_information = None
        self._merchant_information = None
        self._order_information = None
        self._payment_information = None
        self._processing_information = None
        self._processor_information = None
        self._point_of_sale_information = None
        self._risk_information = None
        self._links = None

        if id is not None:
          self.id = id
        if submit_time_utc is not None:
          self.submit_time_utc = submit_time_utc
        if merchant_id is not None:
          self.merchant_id = merchant_id
        if application_information is not None:
          self.application_information = application_information
        if buyer_information is not None:
          self.buyer_information = buyer_information
        if client_reference_information is not None:
          self.client_reference_information = client_reference_information
        if consumer_authentication_information is not None:
          self.consumer_authentication_information = consumer_authentication_information
        if device_information is not None:
          self.device_information = device_information
        if fraud_marking_information is not None:
          self.fraud_marking_information = fraud_marking_information
        if merchant_defined_information is not None:
          self.merchant_defined_information = merchant_defined_information
        if merchant_information is not None:
          self.merchant_information = merchant_information
        if order_information is not None:
          self.order_information = order_information
        if payment_information is not None:
          self.payment_information = payment_information
        if processing_information is not None:
          self.processing_information = processing_information
        if processor_information is not None:
          self.processor_information = processor_information
        if point_of_sale_information is not None:
          self.point_of_sale_information = point_of_sale_information
        if risk_information is not None:
          self.risk_information = risk_information
        if links is not None:
          self.links = links

    @property
    def id(self):
        """
        Gets the id of this InlineResponse2017EmbeddedTransactionSummaries.
        An unique identification number assigned by CyberSource to identify the submitted request.

        :return: The id of this InlineResponse2017EmbeddedTransactionSummaries.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this InlineResponse2017EmbeddedTransactionSummaries.
        An unique identification number assigned by CyberSource to identify the submitted request.

        :param id: The id of this InlineResponse2017EmbeddedTransactionSummaries.
        :type: str
        """
        if id is not None and len(id) > 26:
            raise ValueError("Invalid value for `id`, length must be less than or equal to `26`")

        self._id = id

    @property
    def submit_time_utc(self):
        """
        Gets the submit_time_utc of this InlineResponse2017EmbeddedTransactionSummaries.
        Time of request in UTC. `Format: YYYY-MM-DDThh:mm:ssZ`  Example 2016-08-11T22:47:57Z equals August 11, 2016, at 22:47:57 (10:47:57 p.m.). The T separates the date and the time. The Z indicates UTC. 

        :return: The submit_time_utc of this InlineResponse2017EmbeddedTransactionSummaries.
        :rtype: str
        """
        return self._submit_time_utc

    @submit_time_utc.setter
    def submit_time_utc(self, submit_time_utc):
        """
        Sets the submit_time_utc of this InlineResponse2017EmbeddedTransactionSummaries.
        Time of request in UTC. `Format: YYYY-MM-DDThh:mm:ssZ`  Example 2016-08-11T22:47:57Z equals August 11, 2016, at 22:47:57 (10:47:57 p.m.). The T separates the date and the time. The Z indicates UTC. 

        :param submit_time_utc: The submit_time_utc of this InlineResponse2017EmbeddedTransactionSummaries.
        :type: str
        """

        self._submit_time_utc = submit_time_utc

    @property
    def merchant_id(self):
        """
        Gets the merchant_id of this InlineResponse2017EmbeddedTransactionSummaries.
        The description for this field is not available.

        :return: The merchant_id of this InlineResponse2017EmbeddedTransactionSummaries.
        :rtype: str
        """
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, merchant_id):
        """
        Sets the merchant_id of this InlineResponse2017EmbeddedTransactionSummaries.
        The description for this field is not available.

        :param merchant_id: The merchant_id of this InlineResponse2017EmbeddedTransactionSummaries.
        :type: str
        """

        self._merchant_id = merchant_id

    @property
    def application_information(self):
        """
        Gets the application_information of this InlineResponse2017EmbeddedTransactionSummaries.

        :return: The application_information of this InlineResponse2017EmbeddedTransactionSummaries.
        :rtype: InlineResponse20012ApplicationInformation
        """
        return self._application_information

    @application_information.setter
    def application_information(self, application_information):
        """
        Sets the application_information of this InlineResponse2017EmbeddedTransactionSummaries.

        :param application_information: The application_information of this InlineResponse2017EmbeddedTransactionSummaries.
        :type: InlineResponse20012ApplicationInformation
        """

        self._application_information = application_information

    @property
    def buyer_information(self):
        """
        Gets the buyer_information of this InlineResponse2017EmbeddedTransactionSummaries.

        :return: The buyer_information of this InlineResponse2017EmbeddedTransactionSummaries.
        :rtype: InlineResponse2017EmbeddedBuyerInformation
        """
        return self._buyer_information

    @buyer_information.setter
    def buyer_information(self, buyer_information):
        """
        Sets the buyer_information of this InlineResponse2017EmbeddedTransactionSummaries.

        :param buyer_information: The buyer_information of this InlineResponse2017EmbeddedTransactionSummaries.
        :type: InlineResponse2017EmbeddedBuyerInformation
        """

        self._buyer_information = buyer_information

    @property
    def client_reference_information(self):
        """
        Gets the client_reference_information of this InlineResponse2017EmbeddedTransactionSummaries.

        :return: The client_reference_information of this InlineResponse2017EmbeddedTransactionSummaries.
        :rtype: InlineResponse2017EmbeddedClientReferenceInformation
        """
        return self._client_reference_information

    @client_reference_information.setter
    def client_reference_information(self, client_reference_information):
        """
        Sets the client_reference_information of this InlineResponse2017EmbeddedTransactionSummaries.

        :param client_reference_information: The client_reference_information of this InlineResponse2017EmbeddedTransactionSummaries.
        :type: InlineResponse2017EmbeddedClientReferenceInformation
        """

        self._client_reference_information = client_reference_information

    @property
    def consumer_authentication_information(self):
        """
        Gets the consumer_authentication_information of this InlineResponse2017EmbeddedTransactionSummaries.

        :return: The consumer_authentication_information of this InlineResponse2017EmbeddedTransactionSummaries.
        :rtype: InlineResponse2017EmbeddedConsumerAuthenticationInformation
        """
        return self._consumer_authentication_information

    @consumer_authentication_information.setter
    def consumer_authentication_information(self, consumer_authentication_information):
        """
        Sets the consumer_authentication_information of this InlineResponse2017EmbeddedTransactionSummaries.

        :param consumer_authentication_information: The consumer_authentication_information of this InlineResponse2017EmbeddedTransactionSummaries.
        :type: InlineResponse2017EmbeddedConsumerAuthenticationInformation
        """

        self._consumer_authentication_information = consumer_authentication_information

    @property
    def device_information(self):
        """
        Gets the device_information of this InlineResponse2017EmbeddedTransactionSummaries.

        :return: The device_information of this InlineResponse2017EmbeddedTransactionSummaries.
        :rtype: InlineResponse2017EmbeddedDeviceInformation
        """
        return self._device_information

    @device_information.setter
    def device_information(self, device_information):
        """
        Sets the device_information of this InlineResponse2017EmbeddedTransactionSummaries.

        :param device_information: The device_information of this InlineResponse2017EmbeddedTransactionSummaries.
        :type: InlineResponse2017EmbeddedDeviceInformation
        """

        self._device_information = device_information

    @property
    def fraud_marking_information(self):
        """
        Gets the fraud_marking_information of this InlineResponse2017EmbeddedTransactionSummaries.

        :return: The fraud_marking_information of this InlineResponse2017EmbeddedTransactionSummaries.
        :rtype: InlineResponse20012FraudMarkingInformation
        """
        return self._fraud_marking_information

    @fraud_marking_information.setter
    def fraud_marking_information(self, fraud_marking_information):
        """
        Sets the fraud_marking_information of this InlineResponse2017EmbeddedTransactionSummaries.

        :param fraud_marking_information: The fraud_marking_information of this InlineResponse2017EmbeddedTransactionSummaries.
        :type: InlineResponse20012FraudMarkingInformation
        """

        self._fraud_marking_information = fraud_marking_information

    @property
    def merchant_defined_information(self):
        """
        Gets the merchant_defined_information of this InlineResponse2017EmbeddedTransactionSummaries.
        The description for this field is not available.

        :return: The merchant_defined_information of this InlineResponse2017EmbeddedTransactionSummaries.
        :rtype: list[InlineResponse20012MerchantDefinedInformation]
        """
        return self._merchant_defined_information

    @merchant_defined_information.setter
    def merchant_defined_information(self, merchant_defined_information):
        """
        Sets the merchant_defined_information of this InlineResponse2017EmbeddedTransactionSummaries.
        The description for this field is not available.

        :param merchant_defined_information: The merchant_defined_information of this InlineResponse2017EmbeddedTransactionSummaries.
        :type: list[InlineResponse20012MerchantDefinedInformation]
        """

        self._merchant_defined_information = merchant_defined_information

    @property
    def merchant_information(self):
        """
        Gets the merchant_information of this InlineResponse2017EmbeddedTransactionSummaries.

        :return: The merchant_information of this InlineResponse2017EmbeddedTransactionSummaries.
        :rtype: InlineResponse2017EmbeddedMerchantInformation
        """
        return self._merchant_information

    @merchant_information.setter
    def merchant_information(self, merchant_information):
        """
        Sets the merchant_information of this InlineResponse2017EmbeddedTransactionSummaries.

        :param merchant_information: The merchant_information of this InlineResponse2017EmbeddedTransactionSummaries.
        :type: InlineResponse2017EmbeddedMerchantInformation
        """

        self._merchant_information = merchant_information

    @property
    def order_information(self):
        """
        Gets the order_information of this InlineResponse2017EmbeddedTransactionSummaries.

        :return: The order_information of this InlineResponse2017EmbeddedTransactionSummaries.
        :rtype: InlineResponse2017EmbeddedOrderInformation
        """
        return self._order_information

    @order_information.setter
    def order_information(self, order_information):
        """
        Sets the order_information of this InlineResponse2017EmbeddedTransactionSummaries.

        :param order_information: The order_information of this InlineResponse2017EmbeddedTransactionSummaries.
        :type: InlineResponse2017EmbeddedOrderInformation
        """

        self._order_information = order_information

    @property
    def payment_information(self):
        """
        Gets the payment_information of this InlineResponse2017EmbeddedTransactionSummaries.

        :return: The payment_information of this InlineResponse2017EmbeddedTransactionSummaries.
        :rtype: InlineResponse2017EmbeddedPaymentInformation
        """
        return self._payment_information

    @payment_information.setter
    def payment_information(self, payment_information):
        """
        Sets the payment_information of this InlineResponse2017EmbeddedTransactionSummaries.

        :param payment_information: The payment_information of this InlineResponse2017EmbeddedTransactionSummaries.
        :type: InlineResponse2017EmbeddedPaymentInformation
        """

        self._payment_information = payment_information

    @property
    def processing_information(self):
        """
        Gets the processing_information of this InlineResponse2017EmbeddedTransactionSummaries.

        :return: The processing_information of this InlineResponse2017EmbeddedTransactionSummaries.
        :rtype: InlineResponse2017EmbeddedProcessingInformation
        """
        return self._processing_information

    @processing_information.setter
    def processing_information(self, processing_information):
        """
        Sets the processing_information of this InlineResponse2017EmbeddedTransactionSummaries.

        :param processing_information: The processing_information of this InlineResponse2017EmbeddedTransactionSummaries.
        :type: InlineResponse2017EmbeddedProcessingInformation
        """

        self._processing_information = processing_information

    @property
    def processor_information(self):
        """
        Gets the processor_information of this InlineResponse2017EmbeddedTransactionSummaries.

        :return: The processor_information of this InlineResponse2017EmbeddedTransactionSummaries.
        :rtype: InlineResponse2017EmbeddedProcessorInformation
        """
        return self._processor_information

    @processor_information.setter
    def processor_information(self, processor_information):
        """
        Sets the processor_information of this InlineResponse2017EmbeddedTransactionSummaries.

        :param processor_information: The processor_information of this InlineResponse2017EmbeddedTransactionSummaries.
        :type: InlineResponse2017EmbeddedProcessorInformation
        """

        self._processor_information = processor_information

    @property
    def point_of_sale_information(self):
        """
        Gets the point_of_sale_information of this InlineResponse2017EmbeddedTransactionSummaries.

        :return: The point_of_sale_information of this InlineResponse2017EmbeddedTransactionSummaries.
        :rtype: InlineResponse2017EmbeddedPointOfSaleInformation
        """
        return self._point_of_sale_information

    @point_of_sale_information.setter
    def point_of_sale_information(self, point_of_sale_information):
        """
        Sets the point_of_sale_information of this InlineResponse2017EmbeddedTransactionSummaries.

        :param point_of_sale_information: The point_of_sale_information of this InlineResponse2017EmbeddedTransactionSummaries.
        :type: InlineResponse2017EmbeddedPointOfSaleInformation
        """

        self._point_of_sale_information = point_of_sale_information

    @property
    def risk_information(self):
        """
        Gets the risk_information of this InlineResponse2017EmbeddedTransactionSummaries.

        :return: The risk_information of this InlineResponse2017EmbeddedTransactionSummaries.
        :rtype: InlineResponse2017EmbeddedRiskInformation
        """
        return self._risk_information

    @risk_information.setter
    def risk_information(self, risk_information):
        """
        Sets the risk_information of this InlineResponse2017EmbeddedTransactionSummaries.

        :param risk_information: The risk_information of this InlineResponse2017EmbeddedTransactionSummaries.
        :type: InlineResponse2017EmbeddedRiskInformation
        """

        self._risk_information = risk_information

    @property
    def links(self):
        """
        Gets the links of this InlineResponse2017EmbeddedTransactionSummaries.

        :return: The links of this InlineResponse2017EmbeddedTransactionSummaries.
        :rtype: InlineResponse2017EmbeddedLinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """
        Sets the links of this InlineResponse2017EmbeddedTransactionSummaries.

        :param links: The links of this InlineResponse2017EmbeddedTransactionSummaries.
        :type: InlineResponse2017EmbeddedLinks
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
        if not isinstance(other, InlineResponse2017EmbeddedTransactionSummaries):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other