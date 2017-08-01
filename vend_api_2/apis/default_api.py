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


class DefaultApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def search_get(self, type, **kwargs):
        """
        This endpoint enables seaching for a few types of entities (currently sales, products and customers) by a number of different attributes associated with them. The description for every query parameter indicates which type of object the parameter can be used to search for.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.search_get(type, async=True)
        >>> result = thread.get()

        :param async bool
        :param str type: The enity type to search for. One of: `sales`, `products`, `customers`. (required)
        :param str order_by: The attribute used to sort items returned in the response.
        :param str order_direction: Sorting direction. One of: `asc`, `desc`.
        :param int page_size: The maximum number of objects to be included in the response, currently limited to 10000.
        :param int offset: The number of objects to be \"skipped\" for the response. Used for pagination.
        :param str id: The `id` of the object to be included in the response.
        :param str id2: The `id` of the object to be excluded from the response.
        :param bool deleted: Indicated whether deleted objects should be included in the response.
        :param str status: **SALES** Status of the sale to find. Can be used multiple times to search for objects with different values of this parameter.
        :param str invoice_number: **SALES** Invoice number of the sale.
        :param str customer_id: **SALES** The `ID` of the customer associated with the sales.
        :param str user_id: **SALES** The `ID` of the user associated with the sales.
        :param str outlet_id: **SALES** The `ID` of the outlet associated with the sales.
        :param str date_from: **SALES** Lower limit for the sale date.
        :param str date_to: **SALES** The `ID` Upper limit for the sale date.
        :param str sku: __PRODUCTS__ The SKU of products to include in the search. Can be used multiple times to search for objects with different values of this parameter.
        :param str sku2: __PRODUCTS__ The SKU of products to exclude from the search. Can be used multiple times to search for objects with different values of this parameter.
        :param str supplier_id: __PRODUCTS__ The ID of the supplier associated with the product to include in the search. Can be used multiple times to search for objects with different values of this parameter.
        :param str supplier_id2: __PRODUCTS__ The ID of the supplier associated with the product to exclude from the search. Can be used multiple times to search for objects with different values of this parameter.
        :param str brand_id: __PRODUCTS__ The ID of the brand associated with the product to include in the search. Can be used multiple times to search for objects with different values of this parameter.
        :param str brand_id2: __PRODUCTS__ The ID of the brand associated with the product to exclude from the search. Can be used multiple times to search for objects with different values of this parameter.
        :param str tag_id: __PRODUCTS__ The ID of the tag associated with the product to include in the search. Can be used multiple times to search for objects with different values of this parameter.
        :param str tag_id2: __PRODUCTS__ The ID of the brand associated with the product to exclude from the search. Can be used multiple times to search for objects with different values of this parameter.
        :param str product_type_id: __PRODUCTS__ The ID of the product type associated with the product to include in the search. Can be used multiple times to search for objects with different values of this parameter.
        :param str product_type_id2: __PRODUCTS__ The ID of the product type associated with the product to exclude from the search. Can be used multiple times to search for objects with different values of this parameter.
        :param str variant_parent_id: __PRODUCTS__ The ID of the variant parent product associated with the product to include in the search. Can be used multiple times to search for objects with different values of this parameter.
        :param str variant_parent_id2: __PRODUCTS__ The ID of the variant parent product associated with the product to exclude from the search. Can be used multiple times to search for objects with different values of this parameter.
        :param str customer_code: **CUSTOMERS** The `customer_code` associated with the customer to find.
        :param str first_name: **CUSTOMERS** The `first_name` for the customers to find.
        :param str last_name: **CUSTOMERS** The `last_name` for the customers to find.
        :param str company_name: **CUSTOMERS** The `company_name` for the customers to find.
        :param str phone: **CUSTOMERS** The `phone_number` for the customer(s) to find.
        :param str mobile: **CUSTOMERS** The `mobile` phone number for the customer(s) to find.
        :param str email: **CUSTOMERS** The `email` for the customer(s) to find.
        :return: SearchResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.search_get_with_http_info(type, **kwargs)
        else:
            (data) = self.search_get_with_http_info(type, **kwargs)
            return data

    def search_get_with_http_info(self, type, **kwargs):
        """
        This endpoint enables seaching for a few types of entities (currently sales, products and customers) by a number of different attributes associated with them. The description for every query parameter indicates which type of object the parameter can be used to search for.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.search_get_with_http_info(type, async=True)
        >>> result = thread.get()

        :param async bool
        :param str type: The enity type to search for. One of: `sales`, `products`, `customers`. (required)
        :param str order_by: The attribute used to sort items returned in the response.
        :param str order_direction: Sorting direction. One of: `asc`, `desc`.
        :param int page_size: The maximum number of objects to be included in the response, currently limited to 10000.
        :param int offset: The number of objects to be \"skipped\" for the response. Used for pagination.
        :param str id: The `id` of the object to be included in the response.
        :param str id2: The `id` of the object to be excluded from the response.
        :param bool deleted: Indicated whether deleted objects should be included in the response.
        :param str status: **SALES** Status of the sale to find. Can be used multiple times to search for objects with different values of this parameter.
        :param str invoice_number: **SALES** Invoice number of the sale.
        :param str customer_id: **SALES** The `ID` of the customer associated with the sales.
        :param str user_id: **SALES** The `ID` of the user associated with the sales.
        :param str outlet_id: **SALES** The `ID` of the outlet associated with the sales.
        :param str date_from: **SALES** Lower limit for the sale date.
        :param str date_to: **SALES** The `ID` Upper limit for the sale date.
        :param str sku: __PRODUCTS__ The SKU of products to include in the search. Can be used multiple times to search for objects with different values of this parameter.
        :param str sku2: __PRODUCTS__ The SKU of products to exclude from the search. Can be used multiple times to search for objects with different values of this parameter.
        :param str supplier_id: __PRODUCTS__ The ID of the supplier associated with the product to include in the search. Can be used multiple times to search for objects with different values of this parameter.
        :param str supplier_id2: __PRODUCTS__ The ID of the supplier associated with the product to exclude from the search. Can be used multiple times to search for objects with different values of this parameter.
        :param str brand_id: __PRODUCTS__ The ID of the brand associated with the product to include in the search. Can be used multiple times to search for objects with different values of this parameter.
        :param str brand_id2: __PRODUCTS__ The ID of the brand associated with the product to exclude from the search. Can be used multiple times to search for objects with different values of this parameter.
        :param str tag_id: __PRODUCTS__ The ID of the tag associated with the product to include in the search. Can be used multiple times to search for objects with different values of this parameter.
        :param str tag_id2: __PRODUCTS__ The ID of the brand associated with the product to exclude from the search. Can be used multiple times to search for objects with different values of this parameter.
        :param str product_type_id: __PRODUCTS__ The ID of the product type associated with the product to include in the search. Can be used multiple times to search for objects with different values of this parameter.
        :param str product_type_id2: __PRODUCTS__ The ID of the product type associated with the product to exclude from the search. Can be used multiple times to search for objects with different values of this parameter.
        :param str variant_parent_id: __PRODUCTS__ The ID of the variant parent product associated with the product to include in the search. Can be used multiple times to search for objects with different values of this parameter.
        :param str variant_parent_id2: __PRODUCTS__ The ID of the variant parent product associated with the product to exclude from the search. Can be used multiple times to search for objects with different values of this parameter.
        :param str customer_code: **CUSTOMERS** The `customer_code` associated with the customer to find.
        :param str first_name: **CUSTOMERS** The `first_name` for the customers to find.
        :param str last_name: **CUSTOMERS** The `last_name` for the customers to find.
        :param str company_name: **CUSTOMERS** The `company_name` for the customers to find.
        :param str phone: **CUSTOMERS** The `phone_number` for the customer(s) to find.
        :param str mobile: **CUSTOMERS** The `mobile` phone number for the customer(s) to find.
        :param str email: **CUSTOMERS** The `email` for the customer(s) to find.
        :return: SearchResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['type', 'order_by', 'order_direction', 'page_size', 'offset', 'id', 'id2', 'deleted', 'status', 'invoice_number', 'customer_id', 'user_id', 'outlet_id', 'date_from', 'date_to', 'sku', 'sku2', 'supplier_id', 'supplier_id2', 'brand_id', 'brand_id2', 'tag_id', 'tag_id2', 'product_type_id', 'product_type_id2', 'variant_parent_id', 'variant_parent_id2', 'customer_code', 'first_name', 'last_name', 'company_name', 'phone', 'mobile', 'email']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'type' is set
        if ('type' not in params) or (params['type'] is None):
            raise ValueError("Missing the required parameter `type` when calling `search_get`")


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'type' in params:
            query_params.append(('type', params['type']))
        if 'order_by' in params:
            query_params.append(('order_by', params['order_by']))
        if 'order_direction' in params:
            query_params.append(('order_direction', params['order_direction']))
        if 'page_size' in params:
            query_params.append(('page_size', params['page_size']))
        if 'offset' in params:
            query_params.append(('offset', params['offset']))
        if 'id' in params:
            query_params.append(('_id', params['id']))
        if 'id2' in params:
            query_params.append(('-_id', params['id2']))
        if 'deleted' in params:
            query_params.append(('deleted', params['deleted']))
        if 'status' in params:
            query_params.append(('status', params['status']))
        if 'invoice_number' in params:
            query_params.append(('invoice_number', params['invoice_number']))
        if 'customer_id' in params:
            query_params.append(('customer_id', params['customer_id']))
        if 'user_id' in params:
            query_params.append(('user_id', params['user_id']))
        if 'outlet_id' in params:
            query_params.append(('outlet_id', params['outlet_id']))
        if 'date_from' in params:
            query_params.append(('date_from', params['date_from']))
        if 'date_to' in params:
            query_params.append(('date_to', params['date_to']))
        if 'sku' in params:
            query_params.append(('sku', params['sku']))
        if 'sku2' in params:
            query_params.append(('-sku', params['sku2']))
        if 'supplier_id' in params:
            query_params.append(('supplier_id', params['supplier_id']))
        if 'supplier_id2' in params:
            query_params.append(('-supplier_id', params['supplier_id2']))
        if 'brand_id' in params:
            query_params.append(('brand_id', params['brand_id']))
        if 'brand_id2' in params:
            query_params.append(('-brand_id', params['brand_id2']))
        if 'tag_id' in params:
            query_params.append(('tag_id', params['tag_id']))
        if 'tag_id2' in params:
            query_params.append(('-tag_id', params['tag_id2']))
        if 'product_type_id' in params:
            query_params.append(('product_type_id', params['product_type_id']))
        if 'product_type_id2' in params:
            query_params.append(('-product_type_id', params['product_type_id2']))
        if 'variant_parent_id' in params:
            query_params.append(('variant_parent_id', params['variant_parent_id']))
        if 'variant_parent_id2' in params:
            query_params.append(('-variant_parent_id', params['variant_parent_id2']))
        if 'customer_code' in params:
            query_params.append(('customer_code', params['customer_code']))
        if 'first_name' in params:
            query_params.append(('first_name', params['first_name']))
        if 'last_name' in params:
            query_params.append(('last_name', params['last_name']))
        if 'company_name' in params:
            query_params.append(('company_name', params['company_name']))
        if 'phone' in params:
            query_params.append(('phone', params['phone']))
        if 'mobile' in params:
            query_params.append(('mobile', params['mobile']))
        if 'email' in params:
            query_params.append(('email', params['email']))

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

        return self.api_client.call_api('/search', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='SearchResponse',
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
