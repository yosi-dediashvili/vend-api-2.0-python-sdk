# vend_api_2.OutletProductTaxesApi

All URIs are relative to *https://domain_prefix.vendhq.com/api/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_outlet_product_taxes**](OutletProductTaxesApi.md#list_outlet_product_taxes) | **GET** /outlet_taxes | List outlet product taxes


# **list_outlet_product_taxes**
> OutletTaxCollection list_outlet_product_taxes(outlet_id=outlet_id, after=after, before=before, page_size=page_size, deleted=deleted)

List outlet product taxes

Returns a paginated list of outlet-product-tax records.

### Example 
```python
from __future__ import print_function
import time
import vend_api_2
from vend_api_2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vend_api_2.OutletProductTaxesApi()
outlet_id = 'outlet_id_example' # str | The ID of the outlet for which the results should be returned. (optional)
after = 3.4 # float | The lower limit for the version numbers to be included in the response. (optional)
before = 3.4 # float | The upper limit for the version numbers to be included in the response. (optional)
page_size = 3.4 # float | The maximum number of items to be returned in the response. (optional)
deleted = true # bool | Indicates whether deleted items should be included in the response. (optional)

try: 
    # List outlet product taxes
    api_response = api_instance.list_outlet_product_taxes(outlet_id=outlet_id, after=after, before=before, page_size=page_size, deleted=deleted)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutletProductTaxesApi->list_outlet_product_taxes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **outlet_id** | **str**| The ID of the outlet for which the results should be returned. | [optional] 
 **after** | **float**| The lower limit for the version numbers to be included in the response. | [optional] 
 **before** | **float**| The upper limit for the version numbers to be included in the response. | [optional] 
 **page_size** | **float**| The maximum number of items to be returned in the response. | [optional] 
 **deleted** | **bool**| Indicates whether deleted items should be included in the response. | [optional] 

### Return type

[**OutletTaxCollection**](OutletTaxCollection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

