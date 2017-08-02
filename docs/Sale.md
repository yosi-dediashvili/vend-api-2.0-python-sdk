# Sale

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**outlet_id** | **str** | Valid outlet ID for the retailer. | [optional] 
**return_for** | **str** | Reference ID to a different sale if this sale was created as a return. | [optional] 
**total_price** | **float** | Sale total. | [optional] 
**total_tax** | **float** | Tax total. | [optional] 
**deleted_at** | **str** | Deletion timestamp in UTC. | [optional] 
**version** | **int** | Auto-incrementing object version number. | [optional] 
**taxes** | [**list[SaleTax]**](SaleTax.md) | Collection of taxes. | [optional] 
**register_id** | **str** | Valid register ID for the retailer. | [optional] 
**user_id** | **str** | Valid user ID for the retailer. | [optional] 
**status** | **str** | Sale status. One of: CLOSED, SAVED, ONACCOUNT, ONACCOUNT_CLOSED, LAYBY, LAYBY_CLOSED. VOIDED ??? | [optional] 
**line_items** | [**list[LineItem]**](LineItem.md) | A collection of line items. | [optional] 
**payments** | [**list[Payment]**](Payment.md) | Collection of payments. | [optional] 
**customer_id** | **str** | Valid customer ID for the retailer. | [optional] 
**invoice_number** | **str** | Invoice number which if provided, should use the prefix and suffix defined for the register. | [optional] 
**invoice_sequence** | **float** | Optionally provided value. | [optional] 
**note** | **str** | Sale Note. | [optional] 
**short_code** | **str** | 6 character code used in the loyalty system. ??? | [optional] 
**sale_date** | **str** | Sale timestamp in UTC. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


