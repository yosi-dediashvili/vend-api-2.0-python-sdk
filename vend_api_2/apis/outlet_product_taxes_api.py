# coding: utf-8

"""
    API 2.0

    Early release of version 2.0 of the Vend API.

    OpenAPI spec version: 2.0
    Contact: api@vendhq.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..api_client import ApiClient


class OutletProductTaxesApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def list_outlet_product_taxes(self, **kwargs):
        """
        List outlet product taxes
        Returns a paginated list of outlet-product-tax records.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_outlet_product_taxes(async=True)
        >>> result = thread.get()

        :param async bool
        :param str outlet_id: The ID of the outlet for which the results should be returned.
        :param float after: The lower limit for the version numbers to be included in the response.
        :param float before: The upper limit for the version numbers to be included in the response.
        :param float page_size: The maximum number of items to be returned in the response.
        :param bool deleted: Indicates whether deleted items should be included in the response.
        :return: OutletTaxCollection
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.list_outlet_product_taxes_with_http_info(**kwargs)
        else:
            (data) = self.list_outlet_product_taxes_with_http_info(**kwargs)
            return data

    def list_outlet_product_taxes_with_http_info(self, **kwargs):
        """
        List outlet product taxes
        Returns a paginated list of outlet-product-tax records.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_outlet_product_taxes_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param str outlet_id: The ID of the outlet for which the results should be returned.
        :param float after: The lower limit for the version numbers to be included in the response.
        :param float before: The upper limit for the version numbers to be included in the response.
        :param float page_size: The maximum number of items to be returned in the response.
        :param bool deleted: Indicates whether deleted items should be included in the response.
        :return: OutletTaxCollection
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['outlet_id', 'after', 'before', 'page_size', 'deleted']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_outlet_product_taxes" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'outlet_id' in params:
            query_params.append(('outlet_id', params['outlet_id']))
        if 'after' in params:
            query_params.append(('after', params['after']))
        if 'before' in params:
            query_params.append(('before', params['before']))
        if 'page_size' in params:
            query_params.append(('page_size', params['page_size']))
        if 'deleted' in params:
            query_params.append(('deleted', params['deleted']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/outlet_taxes', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='OutletTaxCollection',
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
