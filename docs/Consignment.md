# Consignment

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Auto-generated object ID. | [optional] 
**outlet_id** | **str** | A valid ID of an outlet where stock will be received. | [optional] 
**name** | **str** | Tue 29 Nov 2016 (string) - Consignment name. | [optional] 
**consignment_date** | **str** | 11-28T19:02:15+00:00 (timestamp) - Consignment creation date. | [optional] 
**due_at** | **str** | 11-30T19:08:541+00:00 (timestamp) - Due date. | [optional] 
**received_at** | **str** | 11-30T19:08:541+00:00 (timestamp) - The date when consignment was received. | [optional] 
**type** | **str** | One of &#x60;SUPPLIER&#x60;, &#x60;OUTLET&#x60;, &#x60;STOCKTAKE&#x60;, &#x60;RETURN&#x60;. | [optional] 
**status** | **str** | One of &#x60;OPEN&#x60;, &#x60;RECEIVED&#x60;, &#x60;SENT&#x60;, &#x60;STOCKTAKE&#x60;, &#x60;STOCKTAKE_SCHEDULED&#x60;, &#x60;STOCKTAKE_IN_PROGRESS&#x60;, &#x60;STOCKTAKE_IN_PROGRESS_PROCESSED&#x60;, &#x60;STOCKTAKE_COMPLETE&#x60;, &#x60;CLOSED&#x60;, &#x60;CANCELLED&#x60; | [optional] 
**supplier_id** | **str** | a valid supplier ID. | [optional] 
**source_outlet_id** | **str** | A valid ID of an outlet where stock will come from. **Stock transfers only**. | [optional] 
**supplier_invoice** | **str** | Supplier invoice number. | [optional] 
**reference** | **str** | Order number.+ &#x60;total_count_gain&#x60; (number) | [optional] 
**total_cost_gain** | **float** | The cost of items over the expected level. | [optional] 
**total_count_loss** | **float** | The number of items below the expected level. | [optional] 
**total_cost_loss** | **float** | The cost of items below the expected level. | [optional] 
**created_at** | **str** | Creation timestamp in UTC. | [optional] 
**updated_at** | **str** | Last update timestamp in UTC. | [optional] 
**deleted_at** | **str** | Deletion timestamp in UTC. | [optional] 
**version** | **int** | Auto-incrementing object version number. | [optional] 
**total_count_gain** | **float** | The number of items over the expected level. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


