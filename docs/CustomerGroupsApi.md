# vend_api_2.CustomerGroupsApi

All URIs are relative to *https://domain_prefix.vendhq.com/api/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_customer_groups**](CustomerGroupsApi.md#list_customer_groups) | **GET** /customer_groups | List customer groups


# **list_customer_groups**
> CustomerGroupCollection list_customer_groups(after=after, before=before, page_size=page_size)

List customer groups

Returns a paginated list of customer groups.

### Example 
```python
from __future__ import print_function
import time
import vend_api_2
from vend_api_2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vend_api_2.CustomerGroupsApi()
after = 3.4 # float | The lower limit for the version numbers to be included in the response. (optional)
before = 3.4 # float | The upper limit for the version numbers to be included in the response. (optional)
page_size = 3.4 # float | The maximum number of items to be returned in the response. (optional)

try: 
    # List customer groups
    api_response = api_instance.list_customer_groups(after=after, before=before, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerGroupsApi->list_customer_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **after** | **float**| The lower limit for the version numbers to be included in the response. | [optional] 
 **before** | **float**| The upper limit for the version numbers to be included in the response. | [optional] 
 **page_size** | **float**| The maximum number of items to be returned in the response. | [optional] 

### Return type

[**CustomerGroupCollection**](CustomerGroupCollection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

