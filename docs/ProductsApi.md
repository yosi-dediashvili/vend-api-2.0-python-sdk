# vend_api_2.ProductsApi

All URIs are relative to *https://domain_prefix.vendhq.com/api/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_inventory_by_product_id**](ProductsApi.md#get_inventory_by_product_id) | **GET** /products/{product_id}/inventory | Get inventory data for a single product
[**get_product_by_id**](ProductsApi.md#get_product_by_id) | **GET** /products/{product_id} | Get a single product
[**list_products**](ProductsApi.md#list_products) | **GET** /products | List products
[**upload_image**](ProductsApi.md#upload_image) | **POST** /products/{product_id}/actions/image_upload | Upload an image


# **get_inventory_by_product_id**
> InventoryCollection get_inventory_by_product_id(product_id, after=after, before=before, page_size=page_size)

Get inventory data for a single product

Returns inventory data for a single product in all the outlets.

### Example 
```python
from __future__ import print_function
import time
import vend_api_2
from vend_api_2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vend_api_2.ProductsApi()
product_id = 'product_id_example' # str | Valid product ID.
after = 3.4 # float | The lower limit for the version numbers to be included in the response. (optional)
before = 3.4 # float | The upper limit for the version numbers to be included in the response. (optional)
page_size = 3.4 # float | The maximum number of items to be returned in the response. (optional)

try: 
    # Get inventory data for a single product
    api_response = api_instance.get_inventory_by_product_id(product_id, after=after, before=before, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->get_inventory_by_product_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| Valid product ID. | 
 **after** | **float**| The lower limit for the version numbers to be included in the response. | [optional] 
 **before** | **float**| The upper limit for the version numbers to be included in the response. | [optional] 
 **page_size** | **float**| The maximum number of items to be returned in the response. | [optional] 

### Return type

[**InventoryCollection**](InventoryCollection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_product_by_id**
> ProductResponse get_product_by_id(product_id)

Get a single product

Returns a single product object with a given ID.

### Example 
```python
from __future__ import print_function
import time
import vend_api_2
from vend_api_2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vend_api_2.ProductsApi()
product_id = 'product_id_example' # str | Valid product ID.

try: 
    # Get a single product
    api_response = api_instance.get_product_by_id(product_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->get_product_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| Valid product ID. | 

### Return type

[**ProductResponse**](ProductResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_products**
> ProductCollection list_products(after=after, before=before, deleted=deleted, page_size=page_size)

List products

Returns a paginated list of products.

### Example 
```python
from __future__ import print_function
import time
import vend_api_2
from vend_api_2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vend_api_2.ProductsApi()
after = 3.4 # float | The lower limit for the version numbers to be included in the response. (optional)
before = 3.4 # float | The upper limit for the version numbers to be included in the response. (optional)
deleted = true # bool | Indicates whether deleted items should be included in the response. (optional)
page_size = 3.4 # float | The maximum number of items to be returned in the response. (optional)

try: 
    # List products
    api_response = api_instance.list_products(after=after, before=before, deleted=deleted, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->list_products: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **after** | **float**| The lower limit for the version numbers to be included in the response. | [optional] 
 **before** | **float**| The upper limit for the version numbers to be included in the response. | [optional] 
 **deleted** | **bool**| Indicates whether deleted items should be included in the response. | [optional] 
 **page_size** | **float**| The maximum number of items to be returned in the response. | [optional] 

### Return type

[**ProductCollection**](ProductCollection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_image**
> ImageResponse upload_image(product_id, image)

Upload an image

Upload a binary file with an image to be used for a product. This request should be encoded as `multipart/form-data`.

### Example 
```python
from __future__ import print_function
import time
import vend_api_2
from vend_api_2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vend_api_2.ProductsApi()
product_id = 'product_id_example' # str | The ID of the product which the imaged should be associated with.
image = '/path/to/file.txt' # file | File to upload. Can be in `jpg` or `png` format.

try: 
    # Upload an image
    api_response = api_instance.upload_image(product_id, image)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->upload_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| The ID of the product which the imaged should be associated with. | 
 **image** | **file**| File to upload. Can be in &#x60;jpg&#x60; or &#x60;png&#x60; format. | 

### Return type

[**ImageResponse**](ImageResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

