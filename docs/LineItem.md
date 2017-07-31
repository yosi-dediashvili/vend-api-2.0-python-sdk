# LineItem

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tax_id** | **str** | ??? | [optional] 
**discount_total** | **float** | Total discount for the line item. | [optional] 
**is_return** | **bool** | Indicates whether this line item is a return from another sale (referenced by &#x60;return_for&#x60; on the main sale object). | [optional] 
**cost** | **float** | Unit cost for the line item. | [optional] 
**cost_total** | **float** | Total cost for the line item. | [optional] 
**price_total** | **float** | Total price for the line item. | [optional] 
**tax** | **float** | Unit tax for the line item. **deprecated** ??? | [optional] 
**tax_total** | **float** | Total tax value. | [optional] 
**product_id** | **str** | Valid product ID. | [optional] 
**quantity** | **float** | Quantity of product units included in the sale. | [optional] 
**price** | **float** | Unit price for the product. | [optional] 
**tax_components** | [**list[LineItemTaxComponent]**](LineItemTaxComponent.md) | Collection of tax components associated with the line item. | [optional] 
**discount** | **float** | Discount. ??? Unit? Should that be even posted? | [optional] 
**loyalty_value** | **float** | The value that should be added to associated customer&#39;s loyalty balance. | [optional] 
**price_set** | **bool** | Indicates whether the price was set manually. Using &#x60;true&#x60; means that the value will never be refreshed from the price book when reloaded (sale retrieved from parked sales). | [optional] 
**sequence** | **float** | Order of the line item in the sale. | [optional] 
**note** | **str** | Line item note. | [optional] 
**status** | **str** | Line item status. ??? | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


