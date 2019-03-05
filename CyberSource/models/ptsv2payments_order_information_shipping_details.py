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


class Ptsv2paymentsOrderInformationShippingDetails(object):
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
        'gift_wrap': 'bool',
        'shipping_method': 'str',
        'ship_from_postal_code': 'str'
    }

    attribute_map = {
        'gift_wrap': 'giftWrap',
        'shipping_method': 'shippingMethod',
        'ship_from_postal_code': 'shipFromPostalCode'
    }

    def __init__(self, gift_wrap=None, shipping_method=None, ship_from_postal_code=None):
        """
        Ptsv2paymentsOrderInformationShippingDetails - a model defined in Swagger
        """

        self._gift_wrap = None
        self._shipping_method = None
        self._ship_from_postal_code = None

        if gift_wrap is not None:
          self.gift_wrap = gift_wrap
        if shipping_method is not None:
          self.shipping_method = shipping_method
        if ship_from_postal_code is not None:
          self.ship_from_postal_code = ship_from_postal_code

    @property
    def gift_wrap(self):
        """
        Gets the gift_wrap of this Ptsv2paymentsOrderInformationShippingDetails.
        The description for this field is not available.

        :return: The gift_wrap of this Ptsv2paymentsOrderInformationShippingDetails.
        :rtype: bool
        """
        return self._gift_wrap

    @gift_wrap.setter
    def gift_wrap(self, gift_wrap):
        """
        Sets the gift_wrap of this Ptsv2paymentsOrderInformationShippingDetails.
        The description for this field is not available.

        :param gift_wrap: The gift_wrap of this Ptsv2paymentsOrderInformationShippingDetails.
        :type: bool
        """

        self._gift_wrap = gift_wrap

    @property
    def shipping_method(self):
        """
        Gets the shipping_method of this Ptsv2paymentsOrderInformationShippingDetails.
        Shipping method for the product. Possible values:   - `lowcost`: Lowest-cost service  - `sameday`: Courier or same-day service  - `oneday`: Next-day or overnight service  - `twoday`: Two-day service  - `threeday`: Three-day service  - `pickup`: Store pick-up  - `other`: Other shipping method  - `none`: No shipping method because product is a service or subscription 

        :return: The shipping_method of this Ptsv2paymentsOrderInformationShippingDetails.
        :rtype: str
        """
        return self._shipping_method

    @shipping_method.setter
    def shipping_method(self, shipping_method):
        """
        Sets the shipping_method of this Ptsv2paymentsOrderInformationShippingDetails.
        Shipping method for the product. Possible values:   - `lowcost`: Lowest-cost service  - `sameday`: Courier or same-day service  - `oneday`: Next-day or overnight service  - `twoday`: Two-day service  - `threeday`: Three-day service  - `pickup`: Store pick-up  - `other`: Other shipping method  - `none`: No shipping method because product is a service or subscription 

        :param shipping_method: The shipping_method of this Ptsv2paymentsOrderInformationShippingDetails.
        :type: str
        """
        if shipping_method is not None and len(shipping_method) > 10:
            raise ValueError("Invalid value for `shipping_method`, length must be less than or equal to `10`")

        self._shipping_method = shipping_method

    @property
    def ship_from_postal_code(self):
        """
        Gets the ship_from_postal_code of this Ptsv2paymentsOrderInformationShippingDetails.
        Postal code for the address from which the goods are shipped, which is used to establish nexus. The default is the postal code associated with your CyberSource account.  The postal code must consist of 5 to 9 digits. When the billing country is the U.S., the 9-digit postal code must follow this format:  `[5 digits][dash][4 digits]`  Example 12345-6789  When the billing country is Canada, the 6-digit postal code must follow this format:  `[alpha][numeric][alpha][space] [numeric][alpha][numeric]`  Example A1B 2C3  This field is frequently used for Level II and Level III transactions. 

        :return: The ship_from_postal_code of this Ptsv2paymentsOrderInformationShippingDetails.
        :rtype: str
        """
        return self._ship_from_postal_code

    @ship_from_postal_code.setter
    def ship_from_postal_code(self, ship_from_postal_code):
        """
        Sets the ship_from_postal_code of this Ptsv2paymentsOrderInformationShippingDetails.
        Postal code for the address from which the goods are shipped, which is used to establish nexus. The default is the postal code associated with your CyberSource account.  The postal code must consist of 5 to 9 digits. When the billing country is the U.S., the 9-digit postal code must follow this format:  `[5 digits][dash][4 digits]`  Example 12345-6789  When the billing country is Canada, the 6-digit postal code must follow this format:  `[alpha][numeric][alpha][space] [numeric][alpha][numeric]`  Example A1B 2C3  This field is frequently used for Level II and Level III transactions. 

        :param ship_from_postal_code: The ship_from_postal_code of this Ptsv2paymentsOrderInformationShippingDetails.
        :type: str
        """
        if ship_from_postal_code is not None and len(ship_from_postal_code) > 10:
            raise ValueError("Invalid value for `ship_from_postal_code`, length must be less than or equal to `10`")

        self._ship_from_postal_code = ship_from_postal_code

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
        if not isinstance(other, Ptsv2paymentsOrderInformationShippingDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
