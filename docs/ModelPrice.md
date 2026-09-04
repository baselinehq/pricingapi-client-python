# ModelPrice


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context_limit** | **int** |  | [optional] 
**currency** | **str** |  | [optional] 
**effective_from** | **str** |  | [optional] 
**effective_to** | **str** |  | [optional] 
**fetched_at** | **str** |  | [optional] 
**host** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**modalities_input** | **List[str]** |  | [optional] 
**modalities_output** | **List[str]** |  | [optional] 
**model** | **str** |  | [optional] 
**model_id** | **str** |  | [optional] 
**open_weights** | **bool** |  | [optional] 
**output_limit** | **int** |  | [optional] 
**provider** | **str** |  | [optional] 
**publisher** | **str** |  | [optional] 
**raw_pricing_data** | **object** |  | [optional] 
**reasoning** | **bool** |  | [optional] 
**region** | **str** |  | [optional] 
**sku_price_id** | **str** |  | [optional] 
**source** | **str** |  | [optional] 
**source_url** | **str** |  | [optional] 
**structured_output** | **bool** |  | [optional] 
**tags** | **object** |  | [optional] 
**token_bucket** | **str** |  | [optional] 
**tool_call** | **bool** |  | [optional] 
**unit_price_per_mtok** | **float** |  | [optional] 

## Example

```python
from pricing_api_client.models.model_price import ModelPrice

# TODO update the JSON string below
json = "{}"
# create an instance of ModelPrice from a JSON string
model_price_instance = ModelPrice.from_json(json)
# print the JSON string representation of the object
print(ModelPrice.to_json())

# convert the object into a dict
model_price_dict = model_price_instance.to_dict()
# create an instance of ModelPrice from a dict
model_price_from_dict = ModelPrice.from_dict(model_price_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


