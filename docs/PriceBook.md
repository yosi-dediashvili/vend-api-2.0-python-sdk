# PriceBook

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Price book name. | 
**customer_group_id** | **str** | The ID of the customer group | 
**id** | **str** | Auto-generated object ID. | [optional] 
**valid_from** | **str** | The date when the price book becomes valid (active). | [optional] 
**valid_to** | **str** | The date when the price book becomes invalid (inactive). | [optional] 
**restrict_to_platform_key** | **str** | &#x60;\&quot;0\&quot;&#x60; - all platforms, &#x60;\&quot;1\&quot;&#x60; - in store, &#x60;\&quot;2\&quot;&#x60; - ecommerce. | [optional] 
**outlet_id** | **str** | The ID of an outlet for which the price book should be used.+ type: GENERAL (string) - Internal value. Safe to ignore. | [optional] 
**restrict_to_platform_label** | **str** | One of &#x60;In Store&#x60;, &#x60;Ecommerce&#x60;, &#x60;All Platforms&#x60;. | [optional] 
**customer_group** | [**CustomerGroup**](CustomerGroup.md) |  | [optional] 
**version** | **int** | Auto-incrementing object version number. | [optional] 
**deleted_at** | **str** | Deletion timestamp in UTC. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


