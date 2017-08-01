# vend_api_2.SearchApi

All URIs are relative to *https://domain_prefix.vendhq.com/api/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**search**](SearchApi.md#search) | **GET** /search | Search


# **search**
> SearchResponse search(type, order_by=order_by, order_direction=order_direction, page_size=page_size, offset=offset, id=id, id2=id2, deleted=deleted, status=status, invoice_number=invoice_number, customer_id=customer_id, user_id=user_id, outlet_id=outlet_id, date_from=date_from, date_to=date_to, sku=sku, sku2=sku2, supplier_id=supplier_id, supplier_id2=supplier_id2, brand_id=brand_id, brand_id2=brand_id2, tag_id=tag_id, tag_id2=tag_id2, product_type_id=product_type_id, product_type_id2=product_type_id2, variant_parent_id=variant_parent_id, variant_parent_id2=variant_parent_id2, customer_code=customer_code, first_name=first_name, last_name=last_name, company_name=company_name, phone=phone, mobile=mobile, email=email)

Search

This endpoint enables seaching for a few types of entities (currently sales, products and customers) by a number of different attributes associated with them. The description for every query parameter indicates which type of object the parameter can be used to search for.

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
api_instance = vend_api_2.SearchApi(vend_api_2.ApiClient(configuration))
type = 'type_example' # str | The enity type to search for. One of: `sales`, `products`, `customers`.
order_by = 'order_by_example' # str | The attribute used to sort items returned in the response. (optional)
order_direction = 'order_direction_example' # str | Sorting direction. One of: `asc`, `desc`. (optional)
page_size = 56 # int | The maximum number of objects to be included in the response, currently limited to 10000. (optional)
offset = 56 # int | The number of objects to be \"skipped\" for the response. Used for pagination. (optional)
id = 'id_example' # str | The `id` of the object to be included in the response. (optional)
id2 = 'id_example' # str | The `id` of the object to be excluded from the response. (optional)
deleted = true # bool | Indicated whether deleted objects should be included in the response. (optional)
status = 'status_example' # str | **SALES** Status of the sale to find. Can be used multiple times to search for objects with different values of this parameter. (optional)
invoice_number = 'invoice_number_example' # str | **SALES** Invoice number of the sale. (optional)
customer_id = 'customer_id_example' # str | **SALES** The `ID` of the customer associated with the sales. (optional)
user_id = 'user_id_example' # str | **SALES** The `ID` of the user associated with the sales. (optional)
outlet_id = 'outlet_id_example' # str | **SALES** The `ID` of the outlet associated with the sales. (optional)
date_from = 'date_from_example' # str | **SALES** Lower limit for the sale date. (optional)
date_to = 'date_to_example' # str | **SALES** The `ID` Upper limit for the sale date. (optional)
sku = 'sku_example' # str | __PRODUCTS__ The SKU of products to include in the search. Can be used multiple times to search for objects with different values of this parameter. (optional)
sku2 = 'sku_example' # str | __PRODUCTS__ The SKU of products to exclude from the search. Can be used multiple times to search for objects with different values of this parameter. (optional)
supplier_id = 'supplier_id_example' # str | __PRODUCTS__ The ID of the supplier associated with the product to include in the search. Can be used multiple times to search for objects with different values of this parameter. (optional)
supplier_id2 = 'supplier_id_example' # str | __PRODUCTS__ The ID of the supplier associated with the product to exclude from the search. Can be used multiple times to search for objects with different values of this parameter. (optional)
brand_id = 'brand_id_example' # str | __PRODUCTS__ The ID of the brand associated with the product to include in the search. Can be used multiple times to search for objects with different values of this parameter. (optional)
brand_id2 = 'brand_id_example' # str | __PRODUCTS__ The ID of the brand associated with the product to exclude from the search. Can be used multiple times to search for objects with different values of this parameter. (optional)
tag_id = 'tag_id_example' # str | __PRODUCTS__ The ID of the tag associated with the product to include in the search. Can be used multiple times to search for objects with different values of this parameter. (optional)
tag_id2 = 'tag_id_example' # str | __PRODUCTS__ The ID of the brand associated with the product to exclude from the search. Can be used multiple times to search for objects with different values of this parameter. (optional)
product_type_id = 'product_type_id_example' # str | __PRODUCTS__ The ID of the product type associated with the product to include in the search. Can be used multiple times to search for objects with different values of this parameter. (optional)
product_type_id2 = 'product_type_id_example' # str | __PRODUCTS__ The ID of the product type associated with the product to exclude from the search. Can be used multiple times to search for objects with different values of this parameter. (optional)
variant_parent_id = 'variant_parent_id_example' # str | __PRODUCTS__ The ID of the variant parent product associated with the product to include in the search. Can be used multiple times to search for objects with different values of this parameter. (optional)
variant_parent_id2 = 'variant_parent_id_example' # str | __PRODUCTS__ The ID of the variant parent product associated with the product to exclude from the search. Can be used multiple times to search for objects with different values of this parameter. (optional)
customer_code = 'customer_code_example' # str | **CUSTOMERS** The `customer_code` associated with the customer to find. (optional)
first_name = 'first_name_example' # str | **CUSTOMERS** The `first_name` for the customers to find. (optional)
last_name = 'last_name_example' # str | **CUSTOMERS** The `last_name` for the customers to find. (optional)
company_name = 'company_name_example' # str | **CUSTOMERS** The `company_name` for the customers to find. (optional)
phone = 'phone_example' # str | **CUSTOMERS** The `phone_number` for the customer(s) to find. (optional)
mobile = 'mobile_example' # str | **CUSTOMERS** The `mobile` phone number for the customer(s) to find. (optional)
email = 'email_example' # str | **CUSTOMERS** The `email` for the customer(s) to find. (optional)

try: 
    # Search
    api_response = api_instance.search(type, order_by=order_by, order_direction=order_direction, page_size=page_size, offset=offset, id=id, id2=id2, deleted=deleted, status=status, invoice_number=invoice_number, customer_id=customer_id, user_id=user_id, outlet_id=outlet_id, date_from=date_from, date_to=date_to, sku=sku, sku2=sku2, supplier_id=supplier_id, supplier_id2=supplier_id2, brand_id=brand_id, brand_id2=brand_id2, tag_id=tag_id, tag_id2=tag_id2, product_type_id=product_type_id, product_type_id2=product_type_id2, variant_parent_id=variant_parent_id, variant_parent_id2=variant_parent_id2, customer_code=customer_code, first_name=first_name, last_name=last_name, company_name=company_name, phone=phone, mobile=mobile, email=email)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The enity type to search for. One of: &#x60;sales&#x60;, &#x60;products&#x60;, &#x60;customers&#x60;. | 
 **order_by** | **str**| The attribute used to sort items returned in the response. | [optional] 
 **order_direction** | **str**| Sorting direction. One of: &#x60;asc&#x60;, &#x60;desc&#x60;. | [optional] 
 **page_size** | **int**| The maximum number of objects to be included in the response, currently limited to 10000. | [optional] 
 **offset** | **int**| The number of objects to be \&quot;skipped\&quot; for the response. Used for pagination. | [optional] 
 **id** | **str**| The &#x60;id&#x60; of the object to be included in the response. | [optional] 
 **id2** | **str**| The &#x60;id&#x60; of the object to be excluded from the response. | [optional] 
 **deleted** | **bool**| Indicated whether deleted objects should be included in the response. | [optional] 
 **status** | **str**| **SALES** Status of the sale to find. Can be used multiple times to search for objects with different values of this parameter. | [optional] 
 **invoice_number** | **str**| **SALES** Invoice number of the sale. | [optional] 
 **customer_id** | **str**| **SALES** The &#x60;ID&#x60; of the customer associated with the sales. | [optional] 
 **user_id** | **str**| **SALES** The &#x60;ID&#x60; of the user associated with the sales. | [optional] 
 **outlet_id** | **str**| **SALES** The &#x60;ID&#x60; of the outlet associated with the sales. | [optional] 
 **date_from** | **str**| **SALES** Lower limit for the sale date. | [optional] 
 **date_to** | **str**| **SALES** The &#x60;ID&#x60; Upper limit for the sale date. | [optional] 
 **sku** | **str**| __PRODUCTS__ The SKU of products to include in the search. Can be used multiple times to search for objects with different values of this parameter. | [optional] 
 **sku2** | **str**| __PRODUCTS__ The SKU of products to exclude from the search. Can be used multiple times to search for objects with different values of this parameter. | [optional] 
 **supplier_id** | **str**| __PRODUCTS__ The ID of the supplier associated with the product to include in the search. Can be used multiple times to search for objects with different values of this parameter. | [optional] 
 **supplier_id2** | **str**| __PRODUCTS__ The ID of the supplier associated with the product to exclude from the search. Can be used multiple times to search for objects with different values of this parameter. | [optional] 
 **brand_id** | **str**| __PRODUCTS__ The ID of the brand associated with the product to include in the search. Can be used multiple times to search for objects with different values of this parameter. | [optional] 
 **brand_id2** | **str**| __PRODUCTS__ The ID of the brand associated with the product to exclude from the search. Can be used multiple times to search for objects with different values of this parameter. | [optional] 
 **tag_id** | **str**| __PRODUCTS__ The ID of the tag associated with the product to include in the search. Can be used multiple times to search for objects with different values of this parameter. | [optional] 
 **tag_id2** | **str**| __PRODUCTS__ The ID of the brand associated with the product to exclude from the search. Can be used multiple times to search for objects with different values of this parameter. | [optional] 
 **product_type_id** | **str**| __PRODUCTS__ The ID of the product type associated with the product to include in the search. Can be used multiple times to search for objects with different values of this parameter. | [optional] 
 **product_type_id2** | **str**| __PRODUCTS__ The ID of the product type associated with the product to exclude from the search. Can be used multiple times to search for objects with different values of this parameter. | [optional] 
 **variant_parent_id** | **str**| __PRODUCTS__ The ID of the variant parent product associated with the product to include in the search. Can be used multiple times to search for objects with different values of this parameter. | [optional] 
 **variant_parent_id2** | **str**| __PRODUCTS__ The ID of the variant parent product associated with the product to exclude from the search. Can be used multiple times to search for objects with different values of this parameter. | [optional] 
 **customer_code** | **str**| **CUSTOMERS** The &#x60;customer_code&#x60; associated with the customer to find. | [optional] 
 **first_name** | **str**| **CUSTOMERS** The &#x60;first_name&#x60; for the customers to find. | [optional] 
 **last_name** | **str**| **CUSTOMERS** The &#x60;last_name&#x60; for the customers to find. | [optional] 
 **company_name** | **str**| **CUSTOMERS** The &#x60;company_name&#x60; for the customers to find. | [optional] 
 **phone** | **str**| **CUSTOMERS** The &#x60;phone_number&#x60; for the customer(s) to find. | [optional] 
 **mobile** | **str**| **CUSTOMERS** The &#x60;mobile&#x60; phone number for the customer(s) to find. | [optional] 
 **email** | **str**| **CUSTOMERS** The &#x60;email&#x60; for the customer(s) to find. | [optional] 

### Return type

[**SearchResponse**](SearchResponse.md)

### Authorization

[oauth](../README.md#oauth), [personal_token](../README.md#personal_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

