# vend_api_2.OutletsApi

All URIs are relative to *https://domain_prefix.vendhq.com/api/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_outlet_by_id**](OutletsApi.md#get_outlet_by_id) | **GET** /outlets/{outlet_id} | Get a single outlet
[**list_outlets**](OutletsApi.md#list_outlets) | **GET** /outlets | List outlets


# **get_outlet_by_id**
> OutletResponse get_outlet_by_id(outlet_id)

Get a single outlet

Returns a single outlet with the requested ID.

### Example 
```python
from __future__ import print_function
import time
import vend_api_2
from vend_api_2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vend_api_2.OutletsApi()
outlet_id = 'outlet_id_example' # str | Valid Outlet ID.

try: 
    # Get a single outlet
    api_response = api_instance.get_outlet_by_id(outlet_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutletsApi->get_outlet_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **outlet_id** | **str**| Valid Outlet ID. | 

### Return type

[**OutletResponse**](OutletResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_outlets**
> OutletCollection list_outlets(after=after, before=before, page_size=page_size)

List outlets

Returns a collection of outlets.

### Example 
```python
from __future__ import print_function
import time
import vend_api_2
from vend_api_2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vend_api_2.OutletsApi()
after = 3.4 # float | The lower limit for the version numbers to be included in the response. (optional)
before = 3.4 # float | The upper limit for the version numbers to be included in the response. (optional)
page_size = 3.4 # float | The maximum number of items to be returned in the response. (optional)

try: 
    # List outlets
    api_response = api_instance.list_outlets(after=after, before=before, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutletsApi->list_outlets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **after** | **float**| The lower limit for the version numbers to be included in the response. | [optional] 
 **before** | **float**| The upper limit for the version numbers to be included in the response. | [optional] 
 **page_size** | **float**| The maximum number of items to be returned in the response. | [optional] 

### Return type

[**OutletCollection**](OutletCollection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

