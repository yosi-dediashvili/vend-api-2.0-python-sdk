# vend_api_2.BrandsApi

All URIs are relative to *https://domain_prefix.vendhq.com/api/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_brand_by_id**](BrandsApi.md#get_brand_by_id) | **GET** /brands/{brand_id} | Get a single brand
[**list_brands**](BrandsApi.md#list_brands) | **GET** /brands | List brands


# **get_brand_by_id**
> BrandResponse get_brand_by_id(brand_id)

Get a single brand

Returns a single brand with a requested ID

### Example 
```python
from __future__ import print_function
import time
import vend_api_2
from vend_api_2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth
configuration = vend_api_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure API key authorization: personal_token
configuration = vend_api_2.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = vend_api_2.BrandsApi(vend_api_2.ApiClient(configuration))
brand_id = 'brand_id_example' # str | Valid brand ID.

try: 
    # Get a single brand
    api_response = api_instance.get_brand_by_id(brand_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BrandsApi->get_brand_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **brand_id** | **str**| Valid brand ID. | 

### Return type

[**BrandResponse**](BrandResponse.md)

### Authorization

[oauth](../README.md#oauth), [personal_token](../README.md#personal_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_brands**
> BrandCollection list_brands(after=after, before=before, page_size=page_size)

List brands

Returns a paginated list of brands.

### Example 
```python
from __future__ import print_function
import time
import vend_api_2
from vend_api_2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth
configuration = vend_api_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure API key authorization: personal_token
configuration = vend_api_2.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = vend_api_2.BrandsApi(vend_api_2.ApiClient(configuration))
after = 3.4 # float | The lower limit for the version numbers to be included in the response. (optional)
before = 3.4 # float | The upper limit for the version numbers to be included in the response. (optional)
page_size = 3.4 # float | The maximum number of items to be returned in the response. (optional)

try: 
    # List brands
    api_response = api_instance.list_brands(after=after, before=before, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BrandsApi->list_brands: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **after** | **float**| The lower limit for the version numbers to be included in the response. | [optional] 
 **before** | **float**| The upper limit for the version numbers to be included in the response. | [optional] 
 **page_size** | **float**| The maximum number of items to be returned in the response. | [optional] 

### Return type

[**BrandCollection**](BrandCollection.md)

### Authorization

[oauth](../README.md#oauth), [personal_token](../README.md#personal_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

