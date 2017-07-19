# vend_api_2.CustomersApi

All URIs are relative to *https://domain_prefix.vendhq.com/api/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_customer**](CustomersApi.md#create_customer) | **POST** /customers | Create a new customer
[**delete_customer_by_id**](CustomersApi.md#delete_customer_by_id) | **DELETE** /customers/{customer_id} | Delete a customer
[**get_customer_by_id**](CustomersApi.md#get_customer_by_id) | **GET** /customers/{customer_id} | Get a single customer
[**list_customers**](CustomersApi.md#list_customers) | **GET** /customers | List customers
[**update_customer_by_id**](CustomersApi.md#update_customer_by_id) | **PUT** /customers/{customer_id} | Update a customer


# **create_customer**
> CustomerResponse create_customer(body)

Create a new customer

Creates a new customer.

### Example 
```python
from __future__ import print_function
import time
import vend_api_2
from vend_api_2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vend_api_2.CustomersApi()
body = vend_api_2.CustomerBase() # CustomerBase | 

try: 
    # Create a new customer
    api_response = api_instance.create_customer(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->create_customer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CustomerBase**](CustomerBase.md)|  | 

### Return type

[**CustomerResponse**](CustomerResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_customer_by_id**
> delete_customer_by_id(customer_id)

Delete a customer

Deletes the customer with the requested ID.

### Example 
```python
from __future__ import print_function
import time
import vend_api_2
from vend_api_2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vend_api_2.CustomersApi()
customer_id = 'customer_id_example' # str | Valid customer ID.

try: 
    # Delete a customer
    api_instance.delete_customer_by_id(customer_id)
except ApiException as e:
    print("Exception when calling CustomersApi->delete_customer_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| Valid customer ID. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_customer_by_id**
> CustomerResponse get_customer_by_id(customer_id)

Get a single customer

Returns a single customer with a requested ID.

### Example 
```python
from __future__ import print_function
import time
import vend_api_2
from vend_api_2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vend_api_2.CustomersApi()
customer_id = 'customer_id_example' # str | Valid customer ID.

try: 
    # Get a single customer
    api_response = api_instance.get_customer_by_id(customer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->get_customer_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| Valid customer ID. | 

### Return type

[**CustomerResponse**](CustomerResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_customers**
> CustomerCollection list_customers(after=after, before=before, page_size=page_size)

List customers

Returns a paginated list of customers.

### Example 
```python
from __future__ import print_function
import time
import vend_api_2
from vend_api_2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vend_api_2.CustomersApi()
after = 3.4 # float | The lower limit for the version numbers to be included in the response. (optional)
before = 3.4 # float | The upper limit for the version numbers to be included in the response. (optional)
page_size = 3.4 # float | The maximum number of items to be returned in the response. (optional)

try: 
    # List customers
    api_response = api_instance.list_customers(after=after, before=before, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->list_customers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **after** | **float**| The lower limit for the version numbers to be included in the response. | [optional] 
 **before** | **float**| The upper limit for the version numbers to be included in the response. | [optional] 
 **page_size** | **float**| The maximum number of items to be returned in the response. | [optional] 

### Return type

[**CustomerCollection**](CustomerCollection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_customer_by_id**
> CustomerResponse update_customer_by_id(customer_id, body)

Update a customer

Updates the customer with the requested ID.

### Example 
```python
from __future__ import print_function
import time
import vend_api_2
from vend_api_2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vend_api_2.CustomersApi()
customer_id = 'customer_id_example' # str | Valid customer ID.
body = vend_api_2.CustomerBase() # CustomerBase | 

try: 
    # Update a customer
    api_response = api_instance.update_customer_by_id(customer_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->update_customer_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| Valid customer ID. | 
 **body** | [**CustomerBase**](CustomerBase.md)|  | 

### Return type

[**CustomerResponse**](CustomerResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

