# InventoryCountItem

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_id** | **str** | The ID of the product associated with this count item. | 
**product_sku** | **str** |  | [optional] 
**count** | **str** | Expected item count. | 
**received** | **str** | Observed item count. | 
**cost** | **str** | The cost of the item. | 
**is_included** | **bool** | Indicated whether the item was included via a filter. Can be &#x60;null&#x60;. For full count (no filters) always &#x60;true&#x60;. | [optional] 
**status** | **str** | The status of the item. One of: &#x60;PENDING&#x60;, &#x60;SUCCESS&#x60;. | 
**created_at** | **str** | The creation timestamp in UTC. | 
**updated_at** | **str** | Last update timestamp in UTC. | 
**deleted_at** | **str** | The deletion timestamp in UTC. | 
**version** | **float** | Auto-incrementing object version number. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


