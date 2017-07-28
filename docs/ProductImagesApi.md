# vend_api_2.ProductImagesApi

All URIs are relative to *https://domain_prefix.vendhq.com/api/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_product_image_by_id**](ProductImagesApi.md#delete_product_image_by_id) | **DELETE** /product_images/{product_image_id} | Delete a product_image
[**get_product_image_data_by_id**](ProductImagesApi.md#get_product_image_data_by_id) | **GET** /product_images/{product_image_id} | Get a single product_image data
[**set_image_position**](ProductImagesApi.md#set_image_position) | **PUT** /product_images/{product_image_id} | Set image position


# **delete_product_image_by_id**
> delete_product_image_by_id(product_image_id)

Delete a product_image

Deletes the product_image with the requested ID.

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
api_instance = vend_api_2.ProductImagesApi(vend_api_2.ApiClient(configuration))
product_image_id = 'product_image_id_example' # str | 

try: 
    # Delete a product_image
    api_instance.delete_product_image_by_id(product_image_id)
except ApiException as e:
    print("Exception when calling ProductImagesApi->delete_product_image_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_image_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[oauth](../README.md#oauth), [personal_token](../README.md#personal_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_product_image_data_by_id**
> ImageResponse get_product_image_data_by_id(product_image_id)

Get a single product_image data

Returns the metadata for a single product image with a given ID. This method is useful for checking the status of an image after it was uploaded.

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
api_instance = vend_api_2.ProductImagesApi(vend_api_2.ApiClient(configuration))
product_image_id = 'product_image_id_example' # str | Valid product ID.

try: 
    # Get a single product_image data
    api_response = api_instance.get_product_image_data_by_id(product_image_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductImagesApi->get_product_image_data_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_image_id** | **str**| Valid product ID. | 

### Return type

[**ImageResponse**](ImageResponse.md)

### Authorization

[oauth](../README.md#oauth), [personal_token](../README.md#personal_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_image_position**
> ImageResponse set_image_position(body, product_image_id)

Set image position

Allows for changing the image position in the list

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
api_instance = vend_api_2.ProductImagesApi(vend_api_2.ApiClient(configuration))
body = vend_api_2.ImagePosition() # ImagePosition | 
product_image_id = 'product_image_id_example' # str | 

try: 
    # Set image position
    api_response = api_instance.set_image_position(body, product_image_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductImagesApi->set_image_position: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ImagePosition**](ImagePosition.md)|  | 
 **product_image_id** | **str**|  | 

### Return type

[**ImageResponse**](ImageResponse.md)

### Authorization

[oauth](../README.md#oauth), [personal_token](../README.md#personal_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

