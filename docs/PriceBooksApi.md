# vend_api_2.PriceBooksApi

All URIs are relative to *https://domain_prefix.vendhq.com/api/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_price_book**](PriceBooksApi.md#create_price_book) | **POST** /price_books | Create a price book
[**get_price_bookby_id**](PriceBooksApi.md#get_price_bookby_id) | **GET** /price_books/{price_book_id} | Get a single price book
[**list_price_books**](PriceBooksApi.md#list_price_books) | **GET** /price_books | List price books


# **create_price_book**
> PriceBookResponse create_price_book(body)

Create a price book

Creates a new price book.

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
api_instance = vend_api_2.PriceBooksApi(vend_api_2.ApiClient(configuration))
body = vend_api_2.PriceBookBase() # PriceBookBase | 

try: 
    # Create a price book
    api_response = api_instance.create_price_book(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PriceBooksApi->create_price_book: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PriceBookBase**](PriceBookBase.md)|  | 

### Return type

[**PriceBookResponse**](PriceBookResponse.md)

### Authorization

[oauth](../README.md#oauth), [personal_token](../README.md#personal_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_price_bookby_id**
> PriceBookResponse get_price_bookby_id(price_book_id)

Get a single price book

Returns a single price book with a requested ID

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
api_instance = vend_api_2.PriceBooksApi(vend_api_2.ApiClient(configuration))
price_book_id = 'price_book_id_example' # str | Valid price book ID.

try: 
    # Get a single price book
    api_response = api_instance.get_price_bookby_id(price_book_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PriceBooksApi->get_price_bookby_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **price_book_id** | **str**| Valid price book ID. | 

### Return type

[**PriceBookResponse**](PriceBookResponse.md)

### Authorization

[oauth](../README.md#oauth), [personal_token](../README.md#personal_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_price_books**
> PriceBookCollection list_price_books(after=after, before=before, page_size=page_size)

List price books

Returns a paginated list of price books

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
api_instance = vend_api_2.PriceBooksApi(vend_api_2.ApiClient(configuration))
after = 3.4 # float | The lower limit for the version numbers to be included in the response. (optional)
before = 3.4 # float | The upper limit for the version numbers to be included in the response. (optional)
page_size = 3.4 # float | The maximum number of items to be returned in the response. (optional)

try: 
    # List price books
    api_response = api_instance.list_price_books(after=after, before=before, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PriceBooksApi->list_price_books: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **after** | **float**| The lower limit for the version numbers to be included in the response. | [optional] 
 **before** | **float**| The upper limit for the version numbers to be included in the response. | [optional] 
 **page_size** | **float**| The maximum number of items to be returned in the response. | [optional] 

### Return type

[**PriceBookCollection**](PriceBookCollection.md)

### Authorization

[oauth](../README.md#oauth), [personal_token](../README.md#personal_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

