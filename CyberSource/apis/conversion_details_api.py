# coding: utf-8

"""
    CyberSource Flex API

    Simple PAN tokenization service

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class ConversionDetailsApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """
	
    def __init__(self, merchant_config, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client
        self.api_client.set_configuration(merchant_config) 


    def get_conversion_detail(self, start_time, end_time, **kwargs):
        """
        Get conversion detail transactions
        Get conversion detail of transactions for a merchant.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_conversion_detail(start_time, end_time, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param datetime start_time: Valid report Start Time in **ISO 8601 format** Please refer the following link to know more about ISO 8601 format. - https://xml2rfc.tools.ietf.org/public/rfc/html/rfc3339.html#anchor14   **Example date format:**   - yyyy-MM-dd'T'HH:mm:ssXXX  (required)
        :param datetime end_time: Valid report End Time in **ISO 8601 format** Please refer the following link to know more about ISO 8601 format. - https://xml2rfc.tools.ietf.org/public/rfc/html/rfc3339.html#anchor14   **Example date format:**   - yyyy-MM-dd'T'HH:mm:ssXXX  (required)
        :param str organization_id: Valid Cybersource Organization Id
        :return: ReportingV3ConversionDetailsGet200Response
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_conversion_detail_with_http_info(start_time, end_time, **kwargs)
        else:
            (data) = self.get_conversion_detail_with_http_info(start_time, end_time, **kwargs)
            return data

    def get_conversion_detail_with_http_info(self, start_time, end_time, **kwargs):
        """
        Get conversion detail transactions
        Get conversion detail of transactions for a merchant.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_conversion_detail_with_http_info(start_time, end_time, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param datetime start_time: Valid report Start Time in **ISO 8601 format** Please refer the following link to know more about ISO 8601 format. - https://xml2rfc.tools.ietf.org/public/rfc/html/rfc3339.html#anchor14   **Example date format:**   - yyyy-MM-dd'T'HH:mm:ssXXX  (required)
        :param datetime end_time: Valid report End Time in **ISO 8601 format** Please refer the following link to know more about ISO 8601 format. - https://xml2rfc.tools.ietf.org/public/rfc/html/rfc3339.html#anchor14   **Example date format:**   - yyyy-MM-dd'T'HH:mm:ssXXX  (required)
        :param str organization_id: Valid Cybersource Organization Id
        :return: ReportingV3ConversionDetailsGet200Response
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['start_time', 'end_time', 'organization_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_conversion_detail" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'start_time' is set
        if ('start_time' not in params) or (params['start_time'] is None):
            raise ValueError("Missing the required parameter `start_time` when calling `get_conversion_detail`")
        # verify the required parameter 'end_time' is set
        if ('end_time' not in params) or (params['end_time'] is None):
            raise ValueError("Missing the required parameter `end_time` when calling `get_conversion_detail`")

        if 'organization_id' in params and len(params['organization_id']) > 32:
            raise ValueError("Invalid value for parameter `organization_id` when calling `get_conversion_detail`, length must be less than or equal to `32`")
        if 'organization_id' in params and len(params['organization_id']) < 1:
            raise ValueError("Invalid value for parameter `organization_id` when calling `get_conversion_detail`, length must be greater than or equal to `1`")
        if 'organization_id' in params and not re.search('[a-zA-Z0-9-_]+', params['organization_id']):
            raise ValueError("Invalid value for parameter `organization_id` when calling `get_conversion_detail`, must conform to the pattern `/[a-zA-Z0-9-_]+/`")

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'start_time' in params:
            query_params.append(('startTime', params['start_time']))
        if 'end_time' in params:
            query_params.append(('endTime', params['end_time']))
        if 'organization_id' in params:
            query_params.append(('organizationId', params['organization_id']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/hal+json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json;charset=utf-8'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/reporting/v3/conversion-details', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='ReportingV3ConversionDetailsGet200Response',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
