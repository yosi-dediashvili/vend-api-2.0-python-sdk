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


class BrandsApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_brand_by_id(self, brand_id, **kwargs):
        """
        Get a single brand
        Returns a single brand with a requested ID
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_brand_by_id(brand_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str brand_id: Valid brand ID. (required)
        :return: BrandResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_brand_by_id_with_http_info(brand_id, **kwargs)
        else:
            (data) = self.get_brand_by_id_with_http_info(brand_id, **kwargs)
            return data

    def get_brand_by_id_with_http_info(self, brand_id, **kwargs):
        """
        Get a single brand
        Returns a single brand with a requested ID
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_brand_by_id_with_http_info(brand_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str brand_id: Valid brand ID. (required)
        :return: BrandResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['brand_id']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_brand_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'brand_id' is set
        if ('brand_id' not in params) or (params['brand_id'] is None):
            raise ValueError("Missing the required parameter `brand_id` when calling `get_brand_by_id`")


        collection_formats = {}

        path_params = {}
        if 'brand_id' in params:
            path_params['brand_id'] = params['brand_id']

        query_params = []

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

        return self.api_client.call_api('/brands/{brand_id}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='BrandResponse',
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def list_brands(self, **kwargs):
        """
        List brands
        Returns a paginated list of brands.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_brands(async=True)
        >>> result = thread.get()

        :param async bool
        :param float after: The lower limit for the version numbers to be included in the response.
        :param float before: The upper limit for the version numbers to be included in the response.
        :param float page_size: The maximum number of items to be returned in the response.
        :return: BrandCollection
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.list_brands_with_http_info(**kwargs)
        else:
            (data) = self.list_brands_with_http_info(**kwargs)
            return data

    def list_brands_with_http_info(self, **kwargs):
        """
        List brands
        Returns a paginated list of brands.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_brands_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param float after: The lower limit for the version numbers to be included in the response.
        :param float before: The upper limit for the version numbers to be included in the response.
        :param float page_size: The maximum number of items to be returned in the response.
        :return: BrandCollection
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['after', 'before', 'page_size']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_brands" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'after' in params:
            query_params.append(('after', params['after']))
        if 'before' in params:
            query_params.append(('before', params['before']))
        if 'page_size' in params:
            query_params.append(('page_size', params['page_size']))

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

        return self.api_client.call_api('/brands', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='BrandCollection',
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
