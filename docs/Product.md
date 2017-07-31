# Product

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Product name. | 
**handle** | **str** | Product handle. **Note:** Variants share the same handle. | 
**sku** | **str** | Product sku. **Note:** Should be unique, but it&#39;s not verified while posting. | 
**id** | **str** | Auto-generated object ID. | [optional] 
**source_id** | **str** | External reference ID. | [optional] 
**source_variant_id** | **str** | Secondary external reference ID. | [optional] 
**variant_parent_id** | **str** | This value is set if a Product is a variant of another Product. | [optional] 
**source** | **str** | Indicates the origin of the product. Can be USER, SYSTEM, SHOPIFY. | [optional] 
**active** | **bool** | Indicated whether the Product is active. | [optional] 
**has_inventory** | **bool** | Indicates whether inventory is being tracked for the Product. | [optional] 
**is_composite** | **bool** | Indicates whether the Product is a composite one. | [optional] 
**has_variants** | **bool** | Indicated whether product has variants. | [optional] 
**description** | **str** | A detailed description of the Product. **Note** Can contain HTML. | [optional] 
**supplier_code** | **str** | Supplier code. | [optional] 
**supply_price** | **float** | Default supply price, | [optional] 
**type** | [**ProductTypeSample**](ProductTypeSample.md) |  | [optional] 
**supplier** | [**SupplierSample**](SupplierSample.md) |  | [optional] 
**brand** | [**BrandSample**](BrandSample.md) |  | [optional] 
**variant_options** | [**list[VariantOption]**](VariantOption.md) | A list of variant option objects. | [optional] 
**categories** | [**list[Tag]**](Tag.md) | A list of tag objects. | [optional] 
**image_url** | **str** |  | [optional] 
**image_thumbnail_url** | **str** |  | [optional] 
**images** | [**list[ImageSample]**](ImageSample.md) | A list of image objects. | [optional] 
**created_at** | **str** | Creation timestamp in UTC. | [optional] 
**updated_at** | **str** | Last update timestamp in UTC. | [optional] 
**deleted_at** | **str** | Deletion timestamp in UTC. | [optional] 
**version** | **float** | Auto-incrementing object version number. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


