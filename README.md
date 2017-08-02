# vend-api-2
Early release of version 2.0 of the Vend API.

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 2.0
- Package version: 2.0.1
- Build package: io.swagger.codegen.languages.PythonClientCodegen
For more information, please visit [https://developers.vendhq.com](https://developers.vendhq.com)

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/vend/vend-api-2.0-python-sdk.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/vend/vend-api-2.0-python-sdk.git`)

Then import the package:
```python
import vend_api_2 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import vend_api_2
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import vend_api_2
from vend_api_2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth
vend_api_2.configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure API key authorization: personal_token
vend_api_2.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# vend_api_2.configuration.api_key_prefix['Authorization'] = 'Bearer'
# create an instance of the API class
api_instance = vend_api_2.BrandsApi()
brand_id = 'brand_id_example' # str | Valid brand ID.

try:
    # Get a single brand
    api_response = api_instance.get_brand_by_id(brand_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BrandsApi->get_brand_by_id: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://domain_prefix.vendhq.com/api/2.0*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*BrandsApi* | [**get_brand_by_id**](docs/BrandsApi.md#get_brand_by_id) | **GET** /brands/{brand_id} | Get a single brand
*BrandsApi* | [**list_brands**](docs/BrandsApi.md#list_brands) | **GET** /brands | List brands
*ConsignmentsApi* | [**adjust_inventory_item_count**](docs/ConsignmentsApi.md#adjust_inventory_item_count) | **POST** /consignments/{consignment_id}/products | Adjust the inventory item count
*ConsignmentsApi* | [**create_inventory_count**](docs/ConsignmentsApi.md#create_inventory_count) | **POST** /consignments | Create an inventory count
*ConsignmentsApi* | [**delete_consignment_by_id**](docs/ConsignmentsApi.md#delete_consignment_by_id) | **DELETE** /consignments/{consignment_id} | Delete a consignment
*ConsignmentsApi* | [**delete_item_from_inventory_count**](docs/ConsignmentsApi.md#delete_item_from_inventory_count) | **DELETE** /consignments/{consignment_id}/products/{product_id} | Delete an item from an inventory count
*ConsignmentsApi* | [**get_consignment_by_id**](docs/ConsignmentsApi.md#get_consignment_by_id) | **GET** /consignments/{consignment_id} | Get a single consignment
*ConsignmentsApi* | [**list_consignments**](docs/ConsignmentsApi.md#list_consignments) | **GET** /consignments | List consignments
*ConsignmentsApi* | [**list_products_by_consignment_id**](docs/ConsignmentsApi.md#list_products_by_consignment_id) | **GET** /consignments/{consignment_id}/products | List all products for a specific consignment
*ConsignmentsApi* | [**update_inventory_count_by_id**](docs/ConsignmentsApi.md#update_inventory_count_by_id) | **PUT** /consignments/{consignment_id} | Update an inventory count
*CustomerGroupsApi* | [**list_customer_groups**](docs/CustomerGroupsApi.md#list_customer_groups) | **GET** /customer_groups | List customer groups
*CustomersApi* | [**create_customer**](docs/CustomersApi.md#create_customer) | **POST** /customers | Create a new customer
*CustomersApi* | [**delete_customer_by_id**](docs/CustomersApi.md#delete_customer_by_id) | **DELETE** /customers/{customer_id} | Delete a customer
*CustomersApi* | [**get_customer_by_id**](docs/CustomersApi.md#get_customer_by_id) | **GET** /customers/{customer_id} | Get a single customer
*CustomersApi* | [**list_customers**](docs/CustomersApi.md#list_customers) | **GET** /customers | List customers
*CustomersApi* | [**update_customer_by_id**](docs/CustomersApi.md#update_customer_by_id) | **PUT** /customers/{customer_id} | Update a customer
*InventoryApi* | [**list_inventory_records**](docs/InventoryApi.md#list_inventory_records) | **GET** /inventory | List inventory records
*OutletProductTaxesApi* | [**list_outlet_product_taxes**](docs/OutletProductTaxesApi.md#list_outlet_product_taxes) | **GET** /outlet_taxes | List outlet product taxes
*OutletsApi* | [**get_outlet_by_id**](docs/OutletsApi.md#get_outlet_by_id) | **GET** /outlets/{outlet_id} | Get a single outlet
*OutletsApi* | [**list_outlets**](docs/OutletsApi.md#list_outlets) | **GET** /outlets | List outlets
*PaymentTypesApi* | [**list_payment_types**](docs/PaymentTypesApi.md#list_payment_types) | **GET** /payment_types | List payment types
*PriceBookProductsApi* | [**list_price_book_products**](docs/PriceBookProductsApi.md#list_price_book_products) | **GET** /price_book_products | List price book products
*PriceBooksApi* | [**create_price_book**](docs/PriceBooksApi.md#create_price_book) | **POST** /price_books | Create a price book
*PriceBooksApi* | [**get_price_bookby_id**](docs/PriceBooksApi.md#get_price_bookby_id) | **GET** /price_books/{price_book_id} | Get a single price book
*PriceBooksApi* | [**list_price_books**](docs/PriceBooksApi.md#list_price_books) | **GET** /price_books | List price books
*ProductImagesApi* | [**delete_product_image_by_id**](docs/ProductImagesApi.md#delete_product_image_by_id) | **DELETE** /product_images/{product_image_id} | Delete a product_image
*ProductImagesApi* | [**get_product_image_data_by_id**](docs/ProductImagesApi.md#get_product_image_data_by_id) | **GET** /product_images/{product_image_id} | Get a single product_image data
*ProductImagesApi* | [**set_image_position**](docs/ProductImagesApi.md#set_image_position) | **PUT** /product_images/{product_image_id} | Set image position
*ProductTypesApi* | [**get_product_type_by_id**](docs/ProductTypesApi.md#get_product_type_by_id) | **GET** /product_types/{product_type_id} | Get a single product type
*ProductTypesApi* | [**list_product_types**](docs/ProductTypesApi.md#list_product_types) | **GET** /product_types | ListProductTypes
*ProductsApi* | [**get_inventory_by_product_id**](docs/ProductsApi.md#get_inventory_by_product_id) | **GET** /products/{product_id}/inventory | Get inventory data for a single product
*ProductsApi* | [**get_product_by_id**](docs/ProductsApi.md#get_product_by_id) | **GET** /products/{product_id} | Get a single product
*ProductsApi* | [**list_products**](docs/ProductsApi.md#list_products) | **GET** /products | List products
*ProductsApi* | [**upload_image**](docs/ProductsApi.md#upload_image) | **POST** /products/{product_id}/actions/image_upload | Upload an image
*RegistersApi* | [**get_register_by_id**](docs/RegistersApi.md#get_register_by_id) | **GET** /registers/{register_id} | Get a single register
*RegistersApi* | [**list_registers**](docs/RegistersApi.md#list_registers) | **GET** /registers | List registers
*SalesApi* | [**get_sale_by_id**](docs/SalesApi.md#get_sale_by_id) | **GET** /sales/{sale_id} | Get a single sale
*SalesApi* | [**list_sales**](docs/SalesApi.md#list_sales) | **GET** /sales | List Sales
*SearchApi* | [**search**](docs/SearchApi.md#search) | **GET** /search | Search for resources
*SuppliersApi* | [**get_supplier_by_id**](docs/SuppliersApi.md#get_supplier_by_id) | **GET** /suppliers/{supplier_id} | Get a single supplier
*SuppliersApi* | [**list_suppliers**](docs/SuppliersApi.md#list_suppliers) | **GET** /suppliers | List suppliers
*TagsApi* | [**get_tag_by_id**](docs/TagsApi.md#get_tag_by_id) | **GET** /tags/{tag_id} | Get a single tag
*TagsApi* | [**list_tags**](docs/TagsApi.md#list_tags) | **GET** /tags | List tags
*TaxesApi* | [**list_taxes**](docs/TaxesApi.md#list_taxes) | **GET** /taxes | List taxes
*UsersApi* | [**get_user_by_id**](docs/UsersApi.md#get_user_by_id) | **GET** /users/{user_id} | Get a single user
*UsersApi* | [**list_users**](docs/UsersApi.md#list_users) | **GET** /users | List users


## Documentation For Models

 - [Brand](docs/Brand.md)
 - [BrandCollection](docs/BrandCollection.md)
 - [BrandResponse](docs/BrandResponse.md)
 - [BrandSample](docs/BrandSample.md)
 - [Consignment](docs/Consignment.md)
 - [ConsignmentCollection](docs/ConsignmentCollection.md)
 - [ConsignmentProductCollection](docs/ConsignmentProductCollection.md)
 - [ConsignmentResponse](docs/ConsignmentResponse.md)
 - [Customer](docs/Customer.md)
 - [CustomerBase](docs/CustomerBase.md)
 - [CustomerCollection](docs/CustomerCollection.md)
 - [CustomerGroup](docs/CustomerGroup.md)
 - [CustomerGroupCollection](docs/CustomerGroupCollection.md)
 - [CustomerResponse](docs/CustomerResponse.md)
 - [Image](docs/Image.md)
 - [ImagePosition](docs/ImagePosition.md)
 - [ImageResponse](docs/ImageResponse.md)
 - [ImageSample](docs/ImageSample.md)
 - [Inventory](docs/Inventory.md)
 - [InventoryCollection](docs/InventoryCollection.md)
 - [InventoryCount](docs/InventoryCount.md)
 - [InventoryCountFilter](docs/InventoryCountFilter.md)
 - [InventoryCountItem](docs/InventoryCountItem.md)
 - [InventoryCountItemRequest](docs/InventoryCountItemRequest.md)
 - [InventoryCountItemResponse](docs/InventoryCountItemResponse.md)
 - [LineItem](docs/LineItem.md)
 - [LineItemTaxComponent](docs/LineItemTaxComponent.md)
 - [Outlet](docs/Outlet.md)
 - [OutletCollection](docs/OutletCollection.md)
 - [OutletResponse](docs/OutletResponse.md)
 - [OutletTax](docs/OutletTax.md)
 - [OutletTaxCollection](docs/OutletTaxCollection.md)
 - [Payment](docs/Payment.md)
 - [PaymentType](docs/PaymentType.md)
 - [PaymentTypeCollection](docs/PaymentTypeCollection.md)
 - [PaymentTypeConfig](docs/PaymentTypeConfig.md)
 - [PriceBook](docs/PriceBook.md)
 - [PriceBookBase](docs/PriceBookBase.md)
 - [PriceBookCollection](docs/PriceBookCollection.md)
 - [PriceBookProduct](docs/PriceBookProduct.md)
 - [PriceBookProductCollection](docs/PriceBookProductCollection.md)
 - [PriceBookResponse](docs/PriceBookResponse.md)
 - [Product](docs/Product.md)
 - [ProductCollection](docs/ProductCollection.md)
 - [ProductResponse](docs/ProductResponse.md)
 - [ProductType](docs/ProductType.md)
 - [ProductTypeCollection](docs/ProductTypeCollection.md)
 - [ProductTypeResponse](docs/ProductTypeResponse.md)
 - [ProductTypeSample](docs/ProductTypeSample.md)
 - [Register](docs/Register.md)
 - [RegisterCollection](docs/RegisterCollection.md)
 - [RegisterResponse](docs/RegisterResponse.md)
 - [Sale](docs/Sale.md)
 - [SaleCollection](docs/SaleCollection.md)
 - [SaleResponse](docs/SaleResponse.md)
 - [SaleTax](docs/SaleTax.md)
 - [SearchResponse](docs/SearchResponse.md)
 - [Supplier](docs/Supplier.md)
 - [SupplierCollection](docs/SupplierCollection.md)
 - [SupplierResponse](docs/SupplierResponse.md)
 - [SupplierSample](docs/SupplierSample.md)
 - [Tag](docs/Tag.md)
 - [TagCollection](docs/TagCollection.md)
 - [TagResponse](docs/TagResponse.md)
 - [Tax](docs/Tax.md)
 - [TaxCollection](docs/TaxCollection.md)
 - [TaxRate](docs/TaxRate.md)
 - [User](docs/User.md)
 - [UserCollection](docs/UserCollection.md)
 - [UserImages](docs/UserImages.md)
 - [UserResponse](docs/UserResponse.md)
 - [VariantOption](docs/VariantOption.md)
 - [Version](docs/Version.md)


## Documentation For Authorization


## oauth

- **Type**: OAuth
- **Flow**: accessCode
- **Authorization URL**: https://secure.vendhq.com/connect
- **Scopes**: N/A

## personal_token

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Author

api@vendhq.com

