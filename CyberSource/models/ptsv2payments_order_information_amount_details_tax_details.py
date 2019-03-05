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


class Ptsv2paymentsOrderInformationAmountDetailsTaxDetails(object):
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
        'type': 'str',
        'amount': 'str',
        'rate': 'str',
        'code': 'str',
        'tax_id': 'str',
        'applied': 'bool',
        'exemption_code': 'str'
    }

    attribute_map = {
        'type': 'type',
        'amount': 'amount',
        'rate': 'rate',
        'code': 'code',
        'tax_id': 'taxId',
        'applied': 'applied',
        'exemption_code': 'exemptionCode'
    }

    def __init__(self, type=None, amount=None, rate=None, code=None, tax_id=None, applied=None, exemption_code=None):
        """
        Ptsv2paymentsOrderInformationAmountDetailsTaxDetails - a model defined in Swagger
        """

        self._type = None
        self._amount = None
        self._rate = None
        self._code = None
        self._tax_id = None
        self._applied = None
        self._exemption_code = None

        if type is not None:
          self.type = type
        if amount is not None:
          self.amount = amount
        if rate is not None:
          self.rate = rate
        if code is not None:
          self.code = code
        if tax_id is not None:
          self.tax_id = tax_id
        if applied is not None:
          self.applied = applied
        if exemption_code is not None:
          self.exemption_code = exemption_code

    @property
    def type(self):
        """
        Gets the type of this Ptsv2paymentsOrderInformationAmountDetailsTaxDetails.
        This is used to determine what type of tax related data should be inclued under _taxDetails_ object.  Possible values:  - alternate  - local  - national  - vat 

        :return: The type of this Ptsv2paymentsOrderInformationAmountDetailsTaxDetails.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this Ptsv2paymentsOrderInformationAmountDetailsTaxDetails.
        This is used to determine what type of tax related data should be inclued under _taxDetails_ object.  Possible values:  - alternate  - local  - national  - vat 

        :param type: The type of this Ptsv2paymentsOrderInformationAmountDetailsTaxDetails.
        :type: str
        """
        allowed_values = ["alternate", "local", "national", "vat"]
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def amount(self):
        """
        Gets the amount of this Ptsv2paymentsOrderInformationAmountDetailsTaxDetails.
        Please see below table for related decription based on above _type_ field.  | type      | type description | |-----------|--------------------| | alternate | Total amount of alternate tax for the order. | | local     | Sales tax for the order. | | national  | National tax for the order. | | vat       | Total amount of VAT or other tax included in the order. | | other     | Other tax. | 

        :return: The amount of this Ptsv2paymentsOrderInformationAmountDetailsTaxDetails.
        :rtype: str
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """
        Sets the amount of this Ptsv2paymentsOrderInformationAmountDetailsTaxDetails.
        Please see below table for related decription based on above _type_ field.  | type      | type description | |-----------|--------------------| | alternate | Total amount of alternate tax for the order. | | local     | Sales tax for the order. | | national  | National tax for the order. | | vat       | Total amount of VAT or other tax included in the order. | | other     | Other tax. | 

        :param amount: The amount of this Ptsv2paymentsOrderInformationAmountDetailsTaxDetails.
        :type: str
        """
        if amount is not None and len(amount) > 13:
            raise ValueError("Invalid value for `amount`, length must be less than or equal to `13`")

        self._amount = amount

    @property
    def rate(self):
        """
        Gets the rate of this Ptsv2paymentsOrderInformationAmountDetailsTaxDetails.
        Rate of VAT or other tax for the order.  Example 0.040 (=4%)  Valid range: 0.01 to 0.99 (1% to 99%, with only whole percentage values accepted; values with additional decimal places will be truncated) 

        :return: The rate of this Ptsv2paymentsOrderInformationAmountDetailsTaxDetails.
        :rtype: str
        """
        return self._rate

    @rate.setter
    def rate(self, rate):
        """
        Sets the rate of this Ptsv2paymentsOrderInformationAmountDetailsTaxDetails.
        Rate of VAT or other tax for the order.  Example 0.040 (=4%)  Valid range: 0.01 to 0.99 (1% to 99%, with only whole percentage values accepted; values with additional decimal places will be truncated) 

        :param rate: The rate of this Ptsv2paymentsOrderInformationAmountDetailsTaxDetails.
        :type: str
        """
        if rate is not None and len(rate) > 6:
            raise ValueError("Invalid value for `rate`, length must be less than or equal to `6`")

        self._rate = rate

    @property
    def code(self):
        """
        Gets the code of this Ptsv2paymentsOrderInformationAmountDetailsTaxDetails.
        Type of tax being applied to the item. Possible values:  Below values are used by **RBS WorldPay Atlanta**, **FDC Nashville Global**, **Litle**   - 0000: unknown tax type  - 0001: federal/national sales tax  - 0002: state sales tax  - 0003: city sales tax  - 0004: local sales tax  - 0005: municipal sales tax  - 0006: other tax  - 0010: value-added tax (VAT)  - 0011: goods and services tax (GST)  - 0012: provincial sales tax  - 0013: harmonized sales tax  - 0014: Quebec sales tax (QST)  - 0020: room tax  - 0021: occupancy tax  - 0022: energy tax  - 0023: city tax  - 0024: county or parish sales tax  - 0025: county tax  - 0026: environment tax  - 0027: state and local sales tax (combined)  - Blank: Tax not supported on line item. 

        :return: The code of this Ptsv2paymentsOrderInformationAmountDetailsTaxDetails.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """
        Sets the code of this Ptsv2paymentsOrderInformationAmountDetailsTaxDetails.
        Type of tax being applied to the item. Possible values:  Below values are used by **RBS WorldPay Atlanta**, **FDC Nashville Global**, **Litle**   - 0000: unknown tax type  - 0001: federal/national sales tax  - 0002: state sales tax  - 0003: city sales tax  - 0004: local sales tax  - 0005: municipal sales tax  - 0006: other tax  - 0010: value-added tax (VAT)  - 0011: goods and services tax (GST)  - 0012: provincial sales tax  - 0013: harmonized sales tax  - 0014: Quebec sales tax (QST)  - 0020: room tax  - 0021: occupancy tax  - 0022: energy tax  - 0023: city tax  - 0024: county or parish sales tax  - 0025: county tax  - 0026: environment tax  - 0027: state and local sales tax (combined)  - Blank: Tax not supported on line item. 

        :param code: The code of this Ptsv2paymentsOrderInformationAmountDetailsTaxDetails.
        :type: str
        """
        if code is not None and len(code) > 4:
            raise ValueError("Invalid value for `code`, length must be less than or equal to `4`")

        self._code = code

    @property
    def tax_id(self):
        """
        Gets the tax_id of this Ptsv2paymentsOrderInformationAmountDetailsTaxDetails.
        Your tax ID number to use for the alternate tax amount. Required if you set alternate tax amount to any value, including zero. You may send this field without sending alternate tax amount. 

        :return: The tax_id of this Ptsv2paymentsOrderInformationAmountDetailsTaxDetails.
        :rtype: str
        """
        return self._tax_id

    @tax_id.setter
    def tax_id(self, tax_id):
        """
        Sets the tax_id of this Ptsv2paymentsOrderInformationAmountDetailsTaxDetails.
        Your tax ID number to use for the alternate tax amount. Required if you set alternate tax amount to any value, including zero. You may send this field without sending alternate tax amount. 

        :param tax_id: The tax_id of this Ptsv2paymentsOrderInformationAmountDetailsTaxDetails.
        :type: str
        """
        if tax_id is not None and len(tax_id) > 15:
            raise ValueError("Invalid value for `tax_id`, length must be less than or equal to `15`")

        self._tax_id = tax_id

    @property
    def applied(self):
        """
        Gets the applied of this Ptsv2paymentsOrderInformationAmountDetailsTaxDetails.
        The tax is applied. Valid value is `true` or `false`.

        :return: The applied of this Ptsv2paymentsOrderInformationAmountDetailsTaxDetails.
        :rtype: bool
        """
        return self._applied

    @applied.setter
    def applied(self, applied):
        """
        Sets the applied of this Ptsv2paymentsOrderInformationAmountDetailsTaxDetails.
        The tax is applied. Valid value is `true` or `false`.

        :param applied: The applied of this Ptsv2paymentsOrderInformationAmountDetailsTaxDetails.
        :type: bool
        """

        self._applied = applied

    @property
    def exemption_code(self):
        """
        Gets the exemption_code of this Ptsv2paymentsOrderInformationAmountDetailsTaxDetails.
        Code for exemption from sales and use tax. This field is a pass-through, which means that CyberSource does not verify the value or modify it in any way before sending it to the processor.  For possible values, see Exemption Status Values. See Numbered Elements.  Important For information about using this field, see Item-Level Tax Fields. 

        :return: The exemption_code of this Ptsv2paymentsOrderInformationAmountDetailsTaxDetails.
        :rtype: str
        """
        return self._exemption_code

    @exemption_code.setter
    def exemption_code(self, exemption_code):
        """
        Sets the exemption_code of this Ptsv2paymentsOrderInformationAmountDetailsTaxDetails.
        Code for exemption from sales and use tax. This field is a pass-through, which means that CyberSource does not verify the value or modify it in any way before sending it to the processor.  For possible values, see Exemption Status Values. See Numbered Elements.  Important For information about using this field, see Item-Level Tax Fields. 

        :param exemption_code: The exemption_code of this Ptsv2paymentsOrderInformationAmountDetailsTaxDetails.
        :type: str
        """
        if exemption_code is not None and len(exemption_code) > 1:
            raise ValueError("Invalid value for `exemption_code`, length must be less than or equal to `1`")

        self._exemption_code = exemption_code

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
        if not isinstance(other, Ptsv2paymentsOrderInformationAmountDetailsTaxDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
