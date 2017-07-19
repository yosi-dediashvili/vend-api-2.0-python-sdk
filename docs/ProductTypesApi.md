# vend_api_2.ProductTypesApi

All URIs are relative to *https://domain_prefix.vendhq.com/api/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_product_type_by_id**](ProductTypesApi.md#get_product_type_by_id) | **GET** /product_types/{product_type_id} | Get a single product type
[**list_product_types**](ProductTypesApi.md#list_product_types) | **GET** /product_types | ListProductTypes


# **get_product_type_by_id**
> ProductTypeResponse get_product_type_by_id(product_type_id)

Get a single product type

Returns a single product type with a given ID.

### Example 
```python
from __future__ import print_function
import time
import vend_api_2
from vend_api_2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vend_api_2.ProductTypesApi()
product_type_id = 'product_type_id_example' # str | Valid product type ID.

try: 
    # Get a single product type
    api_response = api_instance.get_product_type_by_id(product_type_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductTypesApi->get_product_type_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_type_id** | **str**| Valid product type ID. | 

### Return type

[**ProductTypeResponse**](ProductTypeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_product_types**
> ProductTypeCollection list_product_types(after=after, before=before, page_size=page_size)

ListProductTypes

Returns a paginated list of product types.

### Example 
```python
from __future__ import print_function
import time
import vend_api_2
from vend_api_2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vend_api_2.ProductTypesApi()
after = 3.4 # float | The lower limit for the version numbers to be included in the response. (optional)
before = 3.4 # float | The upper limit for the version numbers to be included in the response. (optional)
page_size = 3.4 # float | The maximum number of items to be returned in the response. (optional)

try: 
    # ListProductTypes
    api_response = api_instance.list_product_types(after=after, before=before, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductTypesApi->list_product_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **after** | **float**| The lower limit for the version numbers to be included in the response. | [optional] 
 **before** | **float**| The upper limit for the version numbers to be included in the response. | [optional] 
 **page_size** | **float**| The maximum number of items to be returned in the response. | [optional] 

### Return type

[**ProductTypeCollection**](ProductTypeCollection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

