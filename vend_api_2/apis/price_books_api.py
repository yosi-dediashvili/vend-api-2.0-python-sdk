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


class PriceBooksApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_price_book(self, body, **kwargs):
        """
        Create a price book
        Creates a new price book.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_price_book(body, async=True)
        >>> result = thread.get()

        :param async bool
        :param PriceBookBase body:  (required)
        :return: PriceBookResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.create_price_book_with_http_info(body, **kwargs)
        else:
            (data) = self.create_price_book_with_http_info(body, **kwargs)
            return data

    def create_price_book_with_http_info(self, body, **kwargs):
        """
        Create a price book
        Creates a new price book.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_price_book_with_http_info(body, async=True)
        >>> result = thread.get()

        :param async bool
        :param PriceBookBase body:  (required)
        :return: PriceBookResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_price_book" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_price_book`")


        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/price_books', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='PriceBookResponse',
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_price_bookby_id(self, price_book_id, **kwargs):
        """
        Get a single price book
        Returns a single price book with a requested ID
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_price_bookby_id(price_book_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str price_book_id: Valid price book ID. (required)
        :return: PriceBookResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_price_bookby_id_with_http_info(price_book_id, **kwargs)
        else:
            (data) = self.get_price_bookby_id_with_http_info(price_book_id, **kwargs)
            return data

    def get_price_bookby_id_with_http_info(self, price_book_id, **kwargs):
        """
        Get a single price book
        Returns a single price book with a requested ID
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_price_bookby_id_with_http_info(price_book_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str price_book_id: Valid price book ID. (required)
        :return: PriceBookResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['price_book_id']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_price_bookby_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'price_book_id' is set
        if ('price_book_id' not in params) or (params['price_book_id'] is None):
            raise ValueError("Missing the required parameter `price_book_id` when calling `get_price_bookby_id`")


        collection_formats = {}

        path_params = {}
        if 'price_book_id' in params:
            path_params['price_book_id'] = params['price_book_id']

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

        return self.api_client.call_api('/price_books/{price_book_id}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='PriceBookResponse',
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def list_price_books(self, **kwargs):
        """
        List price books
        Returns a paginated list of price books
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_price_books(async=True)
        >>> result = thread.get()

        :param async bool
        :param float after: The lower limit for the version numbers to be included in the response.
        :param float before: The upper limit for the version numbers to be included in the response.
        :param float page_size: The maximum number of items to be returned in the response.
        :return: PriceBookCollection
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.list_price_books_with_http_info(**kwargs)
        else:
            (data) = self.list_price_books_with_http_info(**kwargs)
            return data

    def list_price_books_with_http_info(self, **kwargs):
        """
        List price books
        Returns a paginated list of price books
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_price_books_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param float after: The lower limit for the version numbers to be included in the response.
        :param float before: The upper limit for the version numbers to be included in the response.
        :param float page_size: The maximum number of items to be returned in the response.
        :return: PriceBookCollection
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
                    " to method list_price_books" % key
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

        return self.api_client.call_api('/price_books', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='PriceBookCollection',
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
