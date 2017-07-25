# User

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Auto-generated object ID. | 
**username** | **str** | User&#39;s username used for login. | 
**display_name** | **str** | Full user&#39;s name to be used for display in the UI. | [optional] 
**email** | **str** | User&#39;s email address. | [optional] 
**email_verified_at** | **str** | The timestamp of users email verification. | [optional] 
**restricted_outlet_id** | **str** | **deprecated** Use the &#x60;restricted_outlet_ids&#x60; instead. | [optional] 
**restricted_outlet_ids** | **list[str]** | A list of outlet IDs the user is associated with | [optional] 
**account_type** | **str** | User&#39;s account type. | 
**created_at** | **str** | Creation timestamp in UTC. | 
**updated_at** | **str** | Last update timestamp in UTC. | 
**deleted_at** | **str** | Deletion timestamp in UTC. | [optional] 
**seen_at** | **str** | The timestamp of the user&#39;s last activity in the system. | [optional] 
**target_daily** | **float** | Daily sales target for the user. | [optional] 
**target_weekly** | **float** | Weekly sales target for the user. | [optional] 
**target_monthly** | **float** | Monthly sales target for the user. | [optional] 
**version** | **int** | Auto-incrementing version number | 
**is_primary_user** | **bool** | Indicated whether this user is the primary user for the account. | 
**image_source** | **str** | URL of the default-sized user&#39;s avatar. | [optional] 
**images** | [**UserImages**](UserImages.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


