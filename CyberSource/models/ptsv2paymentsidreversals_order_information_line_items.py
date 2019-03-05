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


class Ptsv2paymentsidreversalsOrderInformationLineItems(object):
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
        'quantity': 'float',
        'unit_price': 'str'
    }

    attribute_map = {
        'quantity': 'quantity',
        'unit_price': 'unitPrice'
    }

    def __init__(self, quantity=None, unit_price=None):
        """
        Ptsv2paymentsidreversalsOrderInformationLineItems - a model defined in Swagger
        """

        self._quantity = None
        self._unit_price = None

        if quantity is not None:
          self.quantity = quantity
        if unit_price is not None:
          self.unit_price = unit_price

    @property
    def quantity(self):
        """
        Gets the quantity of this Ptsv2paymentsidreversalsOrderInformationLineItems.
        For an authorization or capture transaction (`processingOptions.capture` is set to `true` or `false`), this field is required when _orderInformation.lineItems[].productCode_ is not set to **default** or one of the other values that are related to shipping and/or handling. 

        :return: The quantity of this Ptsv2paymentsidreversalsOrderInformationLineItems.
        :rtype: float
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """
        Sets the quantity of this Ptsv2paymentsidreversalsOrderInformationLineItems.
        For an authorization or capture transaction (`processingOptions.capture` is set to `true` or `false`), this field is required when _orderInformation.lineItems[].productCode_ is not set to **default** or one of the other values that are related to shipping and/or handling. 

        :param quantity: The quantity of this Ptsv2paymentsidreversalsOrderInformationLineItems.
        :type: float
        """
        if quantity is not None and quantity > 9999999999:
            raise ValueError("Invalid value for `quantity`, must be a value less than or equal to `9999999999`")
        if quantity is not None and quantity < 1:
            raise ValueError("Invalid value for `quantity`, must be a value greater than or equal to `1`")

        self._quantity = quantity

    @property
    def unit_price(self):
        """
        Gets the unit_price of this Ptsv2paymentsidreversalsOrderInformationLineItems.
        Per-item price of the product. This value cannot be negative. You can include a decimal point (.), but you cannot include any other special characters. CyberSource truncates the amount to the correct number of decimal places.  For processor-specific information, see the amount field in [Credit Card Services Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html)  **Important** Some processors have specific requirements and limitations, such as maximum amounts and maximum field lengths. This information is covered in: - Table 12, \"Authorization Information for Specific Processors,\" on page 36 - Table 16, \"Capture Information for Specific Processors,\" on page 51 - Table 20, \"Credit Information for Specific Processors,\" on page 65  **DCC for First Data**\\ This value is the original amount in your local currency. You must include this field. You cannot use grand_total_amount. See \"Dynamic Currency Conversion for First Data,\" page 113.  **FDMS South**\\ If you accept IDR or CLP currencies, see the entry for FDMS South in Table 12, \"Authorization Information for Specific Processors,\" on page 36.  **Zero Amount Authorizations**\\ If your processor supports zero amount authorizations, you can set this field to 0 for the authorization to check if the card is lost or stolen. See \"Zero Amount Authorizations,\" page 220. 

        :return: The unit_price of this Ptsv2paymentsidreversalsOrderInformationLineItems.
        :rtype: str
        """
        return self._unit_price

    @unit_price.setter
    def unit_price(self, unit_price):
        """
        Sets the unit_price of this Ptsv2paymentsidreversalsOrderInformationLineItems.
        Per-item price of the product. This value cannot be negative. You can include a decimal point (.), but you cannot include any other special characters. CyberSource truncates the amount to the correct number of decimal places.  For processor-specific information, see the amount field in [Credit Card Services Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html)  **Important** Some processors have specific requirements and limitations, such as maximum amounts and maximum field lengths. This information is covered in: - Table 12, \"Authorization Information for Specific Processors,\" on page 36 - Table 16, \"Capture Information for Specific Processors,\" on page 51 - Table 20, \"Credit Information for Specific Processors,\" on page 65  **DCC for First Data**\\ This value is the original amount in your local currency. You must include this field. You cannot use grand_total_amount. See \"Dynamic Currency Conversion for First Data,\" page 113.  **FDMS South**\\ If you accept IDR or CLP currencies, see the entry for FDMS South in Table 12, \"Authorization Information for Specific Processors,\" on page 36.  **Zero Amount Authorizations**\\ If your processor supports zero amount authorizations, you can set this field to 0 for the authorization to check if the card is lost or stolen. See \"Zero Amount Authorizations,\" page 220. 

        :param unit_price: The unit_price of this Ptsv2paymentsidreversalsOrderInformationLineItems.
        :type: str
        """
        if unit_price is not None and len(unit_price) > 15:
            raise ValueError("Invalid value for `unit_price`, length must be less than or equal to `15`")

        self._unit_price = unit_price

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
        if not isinstance(other, Ptsv2paymentsidreversalsOrderInformationLineItems):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
