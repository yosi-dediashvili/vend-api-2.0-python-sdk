# vend_api_2.RegistersApi

All URIs are relative to *https://domain_prefix.vendhq.com/api/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_register_by_id**](RegistersApi.md#get_register_by_id) | **GET** /registers/{register_id} | Get a single register
[**list_registers**](RegistersApi.md#list_registers) | **GET** /registers | List registers


# **get_register_by_id**
> RegisterResponse get_register_by_id(register_id)

Get a single register

Returns a single register with the requested ID.

### Example 
```python
from __future__ import print_function
import time
import vend_api_2
from vend_api_2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vend_api_2.RegistersApi()
register_id = 'register_id_example' # str | Valid register ID.

try: 
    # Get a single register
    api_response = api_instance.get_register_by_id(register_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegistersApi->get_register_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **register_id** | **str**| Valid register ID. | 

### Return type

[**RegisterResponse**](RegisterResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_registers**
> RegisterCollection list_registers(after=after, before=before, deleted=deleted, page_size=page_size)

List registers

Returns a paginated list of registers.

### Example 
```python
from __future__ import print_function
import time
import vend_api_2
from vend_api_2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vend_api_2.RegistersApi()
after = 3.4 # float | The lower limit for the version numbers to be included in the response. (optional)
before = 3.4 # float | The upper limit for the version numbers to be included in the response. (optional)
deleted = true # bool | Indicates whether deleted items should be included in the response. (optional)
page_size = 3.4 # float | The maximum number of items to be returned in the response. (optional)

try: 
    # List registers
    api_response = api_instance.list_registers(after=after, before=before, deleted=deleted, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegistersApi->list_registers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **after** | **float**| The lower limit for the version numbers to be included in the response. | [optional] 
 **before** | **float**| The upper limit for the version numbers to be included in the response. | [optional] 
 **deleted** | **bool**| Indicates whether deleted items should be included in the response. | [optional] 
 **page_size** | **float**| The maximum number of items to be returned in the response. | [optional] 

### Return type

[**RegisterCollection**](RegisterCollection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

