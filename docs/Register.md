# Register

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Auto-generated object ID. | [optional] 
**name** | **str** | The Register name. | [optional] 
**outlet_id** | **str** | A valid ID of an Outlet that this register is associated with. | [optional] 
**ask_for_note_on_save** | **float** | &#x60;0&#x60; for **Never**, &#x60;1&#x60; for **On Save/Layby/Account/Return**, &#x60;2&#x60; for **Always**. | [optional] 
**print_note_on_receipt** | **bool** |  | [optional] 
**ask_for_user_on_sale** | **bool** |  | [optional] 
**show_discounts_on_receipts** | **bool** |  | [optional] 
**print_receipt** | **bool** | Indicates whether a receipt should be printed after a sale. | [optional] 
**email_receipt** | **bool** | Indicates whether a receipt should be emailed after a sale. | [optional] 
**invoice_prefix** | **str** | Invoice number prefix. | [optional] 
**invoice_suffix** | **str** | Invoice number suffix. | [optional] 
**invoice_sequence** | **float** | The numeric part of the last issued invoice. | [optional] 
**button_layout_id** | **str** | Register ID. | [optional] 
**is_open** | **bool** | Indicates if the Register is currently open. | [optional] 
**register_open_time** | **str** | Date/time when the register was open. Always in UTC. | [optional] 
**register_close_time** | **str** | Date/time when the register was closed. Null if currently open. | [optional] 
**register_open_sequence_id** | **str** | **internal** The ID of the current register closure object. | [optional] 
**cash_managed_payment_type_id** | **str** | **internal** The ID of the payment type used for cash management transactions in this regsiter. | [optional] 
**deleted_at** | **str** | Deletion timestamp in UTC. | [optional] 
**version** | **float** | Auto-incrementing object version number. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


