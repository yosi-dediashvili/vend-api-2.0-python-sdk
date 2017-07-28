# vend_api_2.ConsignmentsApi

All URIs are relative to *https://domain_prefix.vendhq.com/api/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**adjust_inventory_item_count**](ConsignmentsApi.md#adjust_inventory_item_count) | **POST** /consignments/{consignment_id}/products | Adjust the inventory item count
[**create_inventory_count**](ConsignmentsApi.md#create_inventory_count) | **POST** /consignments | Create an inventory count
[**delete_consignment_by_id**](ConsignmentsApi.md#delete_consignment_by_id) | **DELETE** /consignments/{consignment_id} | Delete a consignment
[**delete_item_from_inventory_count**](ConsignmentsApi.md#delete_item_from_inventory_count) | **DELETE** /consignments/{consignment_id}/products/{product_id} | Delete an item from an inventory count
[**get_consignment_by_id**](ConsignmentsApi.md#get_consignment_by_id) | **GET** /consignments/{consignment_id} | Get a single consignment
[**list_consignments**](ConsignmentsApi.md#list_consignments) | **GET** /consignments | List consignments
[**list_products_by_consignment_id**](ConsignmentsApi.md#list_products_by_consignment_id) | **GET** /consignments/{consignment_id}/products | List all products for a specific consignment
[**update_inventory_count_by_id**](ConsignmentsApi.md#update_inventory_count_by_id) | **PUT** /consignments/{consignment_id} | Update an inventory count


# **adjust_inventory_item_count**
> InventoryCountItemResponse adjust_inventory_item_count(consignment_id, body)

Adjust the inventory item count

Increases or decreases the count for a specific product within the inventory count.

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
api_instance = vend_api_2.ConsignmentsApi(vend_api_2.ApiClient(configuration))
consignment_id = 'consignment_id_example' # str | Valid consignment ID.
body = vend_api_2.InventoryCountItemRequest() # InventoryCountItemRequest | 

try: 
    # Adjust the inventory item count
    api_response = api_instance.adjust_inventory_item_count(consignment_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConsignmentsApi->adjust_inventory_item_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consignment_id** | **str**| Valid consignment ID. | 
 **body** | [**InventoryCountItemRequest**](InventoryCountItemRequest.md)|  | 

### Return type

[**InventoryCountItemResponse**](InventoryCountItemResponse.md)

### Authorization

[oauth](../README.md#oauth), [personal_token](../README.md#personal_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_inventory_count**
> ConsignmentResponse create_inventory_count(body)

Create an inventory count

Creates a new consignment of type `STOCKTAKE`. Currently, this endpoint only supports creation of inventory counts (stock takes).

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
api_instance = vend_api_2.ConsignmentsApi(vend_api_2.ApiClient(configuration))
body = vend_api_2.InventoryCount() # InventoryCount | 

try: 
    # Create an inventory count
    api_response = api_instance.create_inventory_count(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConsignmentsApi->create_inventory_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InventoryCount**](InventoryCount.md)|  | 

### Return type

[**ConsignmentResponse**](ConsignmentResponse.md)

### Authorization

[oauth](../README.md#oauth), [personal_token](../README.md#personal_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_consignment_by_id**
> delete_consignment_by_id(consignment_id)

Delete a consignment

Deletes the consignment with the given ID.

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
api_instance = vend_api_2.ConsignmentsApi(vend_api_2.ApiClient(configuration))
consignment_id = 'consignment_id_example' # str | 

try: 
    # Delete a consignment
    api_instance.delete_consignment_by_id(consignment_id)
except ApiException as e:
    print("Exception when calling ConsignmentsApi->delete_consignment_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consignment_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[oauth](../README.md#oauth), [personal_token](../README.md#personal_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_item_from_inventory_count**
> delete_item_from_inventory_count(consignment_id, product_id)

Delete an item from an inventory count

Removes the count for a specific product from the inventory count.

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
api_instance = vend_api_2.ConsignmentsApi(vend_api_2.ApiClient(configuration))
consignment_id = 'consignment_id_example' # str | Valid consignment (inventory count) ID.
product_id = 'product_id_example' # str | The ID of a product included in the inventory count

try: 
    # Delete an item from an inventory count
    api_instance.delete_item_from_inventory_count(consignment_id, product_id)
except ApiException as e:
    print("Exception when calling ConsignmentsApi->delete_item_from_inventory_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consignment_id** | **str**| Valid consignment (inventory count) ID. | 
 **product_id** | **str**| The ID of a product included in the inventory count | 

### Return type

void (empty response body)

### Authorization

[oauth](../README.md#oauth), [personal_token](../README.md#personal_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_consignment_by_id**
> ConsignmentResponse get_consignment_by_id(consignment_id)

Get a single consignment

Returns a single consignment with the requested ID.

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
api_instance = vend_api_2.ConsignmentsApi(vend_api_2.ApiClient(configuration))
consignment_id = 'consignment_id_example' # str | Valid consignment ID.

try: 
    # Get a single consignment
    api_response = api_instance.get_consignment_by_id(consignment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConsignmentsApi->get_consignment_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consignment_id** | **str**| Valid consignment ID. | 

### Return type

[**ConsignmentResponse**](ConsignmentResponse.md)

### Authorization

[oauth](../README.md#oauth), [personal_token](../README.md#personal_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_consignments**
> ConsignmentCollection list_consignments(after=after, before=before, page_size=page_size)

List consignments

Returns a paginated list of consignments.

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
api_instance = vend_api_2.ConsignmentsApi(vend_api_2.ApiClient(configuration))
after = 3.4 # float | The lower limit for the version numbers to be included in the response. (optional)
before = 3.4 # float | The upper limit for the version numbers to be included in the response. (optional)
page_size = 3.4 # float | The maximum number of items to be returned in the response. (optional)

try: 
    # List consignments
    api_response = api_instance.list_consignments(after=after, before=before, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConsignmentsApi->list_consignments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **after** | **float**| The lower limit for the version numbers to be included in the response. | [optional] 
 **before** | **float**| The upper limit for the version numbers to be included in the response. | [optional] 
 **page_size** | **float**| The maximum number of items to be returned in the response. | [optional] 

### Return type

[**ConsignmentCollection**](ConsignmentCollection.md)

### Authorization

[oauth](../README.md#oauth), [personal_token](../README.md#personal_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_products_by_consignment_id**
> ConsignmentProductCollection list_products_by_consignment_id(consignment_id, after=after, before=before, page_size=page_size)

List all products for a specific consignment

Returns a collection of consignment products associated with the specified consignment.

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
api_instance = vend_api_2.ConsignmentsApi(vend_api_2.ApiClient(configuration))
consignment_id = 'consignment_id_example' # str | The ID of the consignment for which products should be listed.
after = 3.4 # float | The lower limit for the version numbers to be included in the response. (optional)
before = 3.4 # float | The upper limit for the version numbers to be included in the response. (optional)
page_size = 3.4 # float | The maximum number of items to be returned in the response. (optional)

try: 
    # List all products for a specific consignment
    api_response = api_instance.list_products_by_consignment_id(consignment_id, after=after, before=before, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConsignmentsApi->list_products_by_consignment_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consignment_id** | **str**| The ID of the consignment for which products should be listed. | 
 **after** | **float**| The lower limit for the version numbers to be included in the response. | [optional] 
 **before** | **float**| The upper limit for the version numbers to be included in the response. | [optional] 
 **page_size** | **float**| The maximum number of items to be returned in the response. | [optional] 

### Return type

[**ConsignmentProductCollection**](ConsignmentProductCollection.md)

### Authorization

[oauth](../README.md#oauth), [personal_token](../README.md#personal_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_inventory_count_by_id**
> ConsignmentResponse update_inventory_count_by_id(consignment_id, body)

Update an inventory count

Updates the inventory count with requested ID.

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
api_instance = vend_api_2.ConsignmentsApi(vend_api_2.ApiClient(configuration))
consignment_id = 'consignment_id_example' # str | Valid consignment ID.
body = vend_api_2.InventoryCount() # InventoryCount | 

try: 
    # Update an inventory count
    api_response = api_instance.update_inventory_count_by_id(consignment_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConsignmentsApi->update_inventory_count_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consignment_id** | **str**| Valid consignment ID. | 
 **body** | [**InventoryCount**](InventoryCount.md)|  | 

### Return type

[**ConsignmentResponse**](ConsignmentResponse.md)

### Authorization

[oauth](../README.md#oauth), [personal_token](../README.md#personal_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

