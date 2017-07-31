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


class ConsignmentsApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def adjust_inventory_item_count(self, consignment_id, body, **kwargs):
        """
        Adjust the inventory item count
        Increases or decreases the count for a specific product within the inventory count.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.adjust_inventory_item_count(consignment_id, body, async=True)
        >>> result = thread.get()

        :param async bool
        :param str consignment_id: Valid consignment ID. (required)
        :param InventoryCountItemRequest body:  (required)
        :return: InventoryCountItemResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.adjust_inventory_item_count_with_http_info(consignment_id, body, **kwargs)
        else:
            (data) = self.adjust_inventory_item_count_with_http_info(consignment_id, body, **kwargs)
            return data

    def adjust_inventory_item_count_with_http_info(self, consignment_id, body, **kwargs):
        """
        Adjust the inventory item count
        Increases or decreases the count for a specific product within the inventory count.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.adjust_inventory_item_count_with_http_info(consignment_id, body, async=True)
        >>> result = thread.get()

        :param async bool
        :param str consignment_id: Valid consignment ID. (required)
        :param InventoryCountItemRequest body:  (required)
        :return: InventoryCountItemResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['consignment_id', 'body']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method adjust_inventory_item_count" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'consignment_id' is set
        if ('consignment_id' not in params) or (params['consignment_id'] is None):
            raise ValueError("Missing the required parameter `consignment_id` when calling `adjust_inventory_item_count`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `adjust_inventory_item_count`")


        collection_formats = {}

        path_params = {}
        if 'consignment_id' in params:
            path_params['consignment_id'] = params['consignment_id']

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
        auth_settings = ['oauth', 'personal_token']

        return self.api_client.call_api('/consignments/{consignment_id}/products', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='InventoryCountItemResponse',
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def create_inventory_count(self, body, **kwargs):
        """
        Create an inventory count
        Creates a new consignment of type `STOCKTAKE`. Currently, this endpoint only supports creation of inventory counts (stock takes).
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_inventory_count(body, async=True)
        >>> result = thread.get()

        :param async bool
        :param InventoryCount body:  (required)
        :return: ConsignmentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.create_inventory_count_with_http_info(body, **kwargs)
        else:
            (data) = self.create_inventory_count_with_http_info(body, **kwargs)
            return data

    def create_inventory_count_with_http_info(self, body, **kwargs):
        """
        Create an inventory count
        Creates a new consignment of type `STOCKTAKE`. Currently, this endpoint only supports creation of inventory counts (stock takes).
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_inventory_count_with_http_info(body, async=True)
        >>> result = thread.get()

        :param async bool
        :param InventoryCount body:  (required)
        :return: ConsignmentResponse
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
                    " to method create_inventory_count" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_inventory_count`")


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
        auth_settings = ['oauth', 'personal_token']

        return self.api_client.call_api('/consignments', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='ConsignmentResponse',
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def delete_consignment_by_id(self, consignment_id, **kwargs):
        """
        Delete a consignment
        Deletes the consignment with the given ID.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_consignment_by_id(consignment_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str consignment_id:  (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.delete_consignment_by_id_with_http_info(consignment_id, **kwargs)
        else:
            (data) = self.delete_consignment_by_id_with_http_info(consignment_id, **kwargs)
            return data

    def delete_consignment_by_id_with_http_info(self, consignment_id, **kwargs):
        """
        Delete a consignment
        Deletes the consignment with the given ID.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_consignment_by_id_with_http_info(consignment_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str consignment_id:  (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['consignment_id']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_consignment_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'consignment_id' is set
        if ('consignment_id' not in params) or (params['consignment_id'] is None):
            raise ValueError("Missing the required parameter `consignment_id` when calling `delete_consignment_by_id`")


        collection_formats = {}

        path_params = {}
        if 'consignment_id' in params:
            path_params['consignment_id'] = params['consignment_id']

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
        auth_settings = ['oauth', 'personal_token']

        return self.api_client.call_api('/consignments/{consignment_id}', 'DELETE',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type=None,
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def delete_item_from_inventory_count(self, consignment_id, product_id, **kwargs):
        """
        Delete an item from an inventory count
        Removes the count for a specific product from the inventory count.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_item_from_inventory_count(consignment_id, product_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str consignment_id: Valid consignment (inventory count) ID. (required)
        :param str product_id: The ID of a product included in the inventory count (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.delete_item_from_inventory_count_with_http_info(consignment_id, product_id, **kwargs)
        else:
            (data) = self.delete_item_from_inventory_count_with_http_info(consignment_id, product_id, **kwargs)
            return data

    def delete_item_from_inventory_count_with_http_info(self, consignment_id, product_id, **kwargs):
        """
        Delete an item from an inventory count
        Removes the count for a specific product from the inventory count.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_item_from_inventory_count_with_http_info(consignment_id, product_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str consignment_id: Valid consignment (inventory count) ID. (required)
        :param str product_id: The ID of a product included in the inventory count (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['consignment_id', 'product_id']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_item_from_inventory_count" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'consignment_id' is set
        if ('consignment_id' not in params) or (params['consignment_id'] is None):
            raise ValueError("Missing the required parameter `consignment_id` when calling `delete_item_from_inventory_count`")
        # verify the required parameter 'product_id' is set
        if ('product_id' not in params) or (params['product_id'] is None):
            raise ValueError("Missing the required parameter `product_id` when calling `delete_item_from_inventory_count`")


        collection_formats = {}

        path_params = {}
        if 'consignment_id' in params:
            path_params['consignment_id'] = params['consignment_id']
        if 'product_id' in params:
            path_params['product_id'] = params['product_id']

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
        auth_settings = ['oauth', 'personal_token']

        return self.api_client.call_api('/consignments/{consignment_id}/products/{product_id}', 'DELETE',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type=None,
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_consignment_by_id(self, consignment_id, **kwargs):
        """
        Get a single consignment
        Returns a single consignment with the requested ID.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_consignment_by_id(consignment_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str consignment_id: Valid consignment ID. (required)
        :return: ConsignmentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_consignment_by_id_with_http_info(consignment_id, **kwargs)
        else:
            (data) = self.get_consignment_by_id_with_http_info(consignment_id, **kwargs)
            return data

    def get_consignment_by_id_with_http_info(self, consignment_id, **kwargs):
        """
        Get a single consignment
        Returns a single consignment with the requested ID.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_consignment_by_id_with_http_info(consignment_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str consignment_id: Valid consignment ID. (required)
        :return: ConsignmentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['consignment_id']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_consignment_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'consignment_id' is set
        if ('consignment_id' not in params) or (params['consignment_id'] is None):
            raise ValueError("Missing the required parameter `consignment_id` when calling `get_consignment_by_id`")


        collection_formats = {}

        path_params = {}
        if 'consignment_id' in params:
            path_params['consignment_id'] = params['consignment_id']

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
        auth_settings = ['oauth', 'personal_token']

        return self.api_client.call_api('/consignments/{consignment_id}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='ConsignmentResponse',
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def list_consignments(self, **kwargs):
        """
        List consignments
        Returns a paginated list of consignments.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_consignments(async=True)
        >>> result = thread.get()

        :param async bool
        :param float after: The lower limit for the version numbers to be included in the response.
        :param float before: The upper limit for the version numbers to be included in the response.
        :param float page_size: The maximum number of items to be returned in the response.
        :return: ConsignmentCollection
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.list_consignments_with_http_info(**kwargs)
        else:
            (data) = self.list_consignments_with_http_info(**kwargs)
            return data

    def list_consignments_with_http_info(self, **kwargs):
        """
        List consignments
        Returns a paginated list of consignments.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_consignments_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param float after: The lower limit for the version numbers to be included in the response.
        :param float before: The upper limit for the version numbers to be included in the response.
        :param float page_size: The maximum number of items to be returned in the response.
        :return: ConsignmentCollection
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
                    " to method list_consignments" % key
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
        auth_settings = ['oauth', 'personal_token']

        return self.api_client.call_api('/consignments', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='ConsignmentCollection',
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def list_products_by_consignment_id(self, consignment_id, **kwargs):
        """
        List all products for a specific consignment
        Returns a collection of consignment products associated with the specified consignment.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_products_by_consignment_id(consignment_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str consignment_id: The ID of the consignment for which products should be listed. (required)
        :param float after: The lower limit for the version numbers to be included in the response.
        :param float before: The upper limit for the version numbers to be included in the response.
        :param float page_size: The maximum number of items to be returned in the response.
        :return: ConsignmentProductCollection
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.list_products_by_consignment_id_with_http_info(consignment_id, **kwargs)
        else:
            (data) = self.list_products_by_consignment_id_with_http_info(consignment_id, **kwargs)
            return data

    def list_products_by_consignment_id_with_http_info(self, consignment_id, **kwargs):
        """
        List all products for a specific consignment
        Returns a collection of consignment products associated with the specified consignment.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_products_by_consignment_id_with_http_info(consignment_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str consignment_id: The ID of the consignment for which products should be listed. (required)
        :param float after: The lower limit for the version numbers to be included in the response.
        :param float before: The upper limit for the version numbers to be included in the response.
        :param float page_size: The maximum number of items to be returned in the response.
        :return: ConsignmentProductCollection
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['consignment_id', 'after', 'before', 'page_size']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_products_by_consignment_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'consignment_id' is set
        if ('consignment_id' not in params) or (params['consignment_id'] is None):
            raise ValueError("Missing the required parameter `consignment_id` when calling `list_products_by_consignment_id`")


        collection_formats = {}

        path_params = {}
        if 'consignment_id' in params:
            path_params['consignment_id'] = params['consignment_id']

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
        auth_settings = ['oauth', 'personal_token']

        return self.api_client.call_api('/consignments/{consignment_id}/products', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='ConsignmentProductCollection',
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def update_inventory_count_by_id(self, consignment_id, body, **kwargs):
        """
        Update an inventory count
        Updates the inventory count with requested ID.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_inventory_count_by_id(consignment_id, body, async=True)
        >>> result = thread.get()

        :param async bool
        :param str consignment_id: Valid consignment ID. (required)
        :param InventoryCount body:  (required)
        :return: ConsignmentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.update_inventory_count_by_id_with_http_info(consignment_id, body, **kwargs)
        else:
            (data) = self.update_inventory_count_by_id_with_http_info(consignment_id, body, **kwargs)
            return data

    def update_inventory_count_by_id_with_http_info(self, consignment_id, body, **kwargs):
        """
        Update an inventory count
        Updates the inventory count with requested ID.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_inventory_count_by_id_with_http_info(consignment_id, body, async=True)
        >>> result = thread.get()

        :param async bool
        :param str consignment_id: Valid consignment ID. (required)
        :param InventoryCount body:  (required)
        :return: ConsignmentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['consignment_id', 'body']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_inventory_count_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'consignment_id' is set
        if ('consignment_id' not in params) or (params['consignment_id'] is None):
            raise ValueError("Missing the required parameter `consignment_id` when calling `update_inventory_count_by_id`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_inventory_count_by_id`")


        collection_formats = {}

        path_params = {}
        if 'consignment_id' in params:
            path_params['consignment_id'] = params['consignment_id']

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
        auth_settings = ['oauth', 'personal_token']

        return self.api_client.call_api('/consignments/{consignment_id}', 'PUT',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='ConsignmentResponse',
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
