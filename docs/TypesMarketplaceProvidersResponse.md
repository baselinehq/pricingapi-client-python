# TypesMarketplaceProvidersResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**providers** | [**List[SchemaComputePricingsRow]**](SchemaComputePricingsRow.md) |  | [optional] 

## Example

```python
from pricing_api_client.models.types_marketplace_providers_response import TypesMarketplaceProvidersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TypesMarketplaceProvidersResponse from a JSON string
types_marketplace_providers_response_instance = TypesMarketplaceProvidersResponse.from_json(json)
# print the JSON string representation of the object
print(TypesMarketplaceProvidersResponse.to_json())

# convert the object into a dict
types_marketplace_providers_response_dict = types_marketplace_providers_response_instance.to_dict()
# create an instance of TypesMarketplaceProvidersResponse from a dict
types_marketplace_providers_response_from_dict = TypesMarketplaceProvidersResponse.from_dict(types_marketplace_providers_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


