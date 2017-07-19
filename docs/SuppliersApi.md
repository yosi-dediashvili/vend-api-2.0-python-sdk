# vend_api_2.SuppliersApi

All URIs are relative to *https://domain_prefix.vendhq.com/api/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_supplier_by_id**](SuppliersApi.md#get_supplier_by_id) | **GET** /suppliers/{supplier_id} | Get a single supplier
[**list_suppliers**](SuppliersApi.md#list_suppliers) | **GET** /suppliers | List suppliers


# **get_supplier_by_id**
> SupplierResponse get_supplier_by_id(supplier_id)

Get a single supplier

Returns a single supplier with a given ID.

### Example 
```python
from __future__ import print_function
import time
import vend_api_2
from vend_api_2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vend_api_2.SuppliersApi()
supplier_id = 'supplier_id_example' # str | 

try: 
    # Get a single supplier
    api_response = api_instance.get_supplier_by_id(supplier_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SuppliersApi->get_supplier_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **supplier_id** | **str**|  | 

### Return type

[**SupplierResponse**](SupplierResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_suppliers**
> SupplierCollection list_suppliers(after=after, before=before, page_size=page_size)

List suppliers

Returns a paginated list of suppliers.

### Example 
```python
from __future__ import print_function
import time
import vend_api_2
from vend_api_2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vend_api_2.SuppliersApi()
after = 3.4 # float | The lower limit for the version numbers to be included in the response. (optional)
before = 3.4 # float | The upper limit for the version numbers to be included in the response. (optional)
page_size = 3.4 # float | The maximum number of items to be returned in the response. (optional)

try: 
    # List suppliers
    api_response = api_instance.list_suppliers(after=after, before=before, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SuppliersApi->list_suppliers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **after** | **float**| The lower limit for the version numbers to be included in the response. | [optional] 
 **before** | **float**| The upper limit for the version numbers to be included in the response. | [optional] 
 **page_size** | **float**| The maximum number of items to be returned in the response. | [optional] 

### Return type

[**SupplierCollection**](SupplierCollection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

