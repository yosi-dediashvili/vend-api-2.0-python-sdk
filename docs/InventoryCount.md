# InventoryCount

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**outlet_id** | **str** | The ID of the outlet in which the count is taking place. | 
**due_at** | **str** | The date for which the count is scheduled. | [optional] 
**show_inactive** | **bool** | Indicates whether inactive products should be included in the count. | [optional] 
**name** | **str** | The name of the inventory count | 
**status** | **str** | The status of the inventory count. One of: &#x60;STOCKTAKE_SCHEDULED&#x60;, &#x60;STOCKTAKE_IN_PROGRESS&#x60;, &#x60;STOCKTAKE_IN_PROGRESS_PROCESSED&#x60;, &#x60;STOCKTAKE_COMPLETE&#x60;. | 
**filters** | [**list[InventoryCountFilter]**](InventoryCountFilter.md) | An array of filter objects. Max 25. | [optional] 
**type** | **str** | Consignment type, for inventory counts always &#x60;STOCKTAKE&#x60; | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


