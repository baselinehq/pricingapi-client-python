# TypesCustomPricingResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entries** | [**List[SchemaComputePricingsRow]**](SchemaComputePricingsRow.md) |  | [optional] 
**status** | [**GithubComBaselinehqPricingapiPkgTypesStatus**](GithubComBaselinehqPricingapiPkgTypesStatus.md) |  | [optional] 

## Example

```python
from pricing_api_client.models.types_custom_pricing_response import TypesCustomPricingResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TypesCustomPricingResponse from a JSON string
types_custom_pricing_response_instance = TypesCustomPricingResponse.from_json(json)
# print the JSON string representation of the object
print(TypesCustomPricingResponse.to_json())

# convert the object into a dict
types_custom_pricing_response_dict = types_custom_pricing_response_instance.to_dict()
# create an instance of TypesCustomPricingResponse from a dict
types_custom_pricing_response_from_dict = TypesCustomPricingResponse.from_dict(types_custom_pricing_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


