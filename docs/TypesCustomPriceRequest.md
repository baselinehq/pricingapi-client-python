# TypesCustomPriceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entries** | [**List[SchemaComputePricingsRow]**](SchemaComputePricingsRow.md) |  | 

## Example

```python
from pricing_api_client.models.types_custom_price_request import TypesCustomPriceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TypesCustomPriceRequest from a JSON string
types_custom_price_request_instance = TypesCustomPriceRequest.from_json(json)
# print the JSON string representation of the object
print(TypesCustomPriceRequest.to_json())

# convert the object into a dict
types_custom_price_request_dict = types_custom_price_request_instance.to_dict()
# create an instance of TypesCustomPriceRequest from a dict
types_custom_price_request_from_dict = TypesCustomPriceRequest.from_dict(types_custom_price_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


