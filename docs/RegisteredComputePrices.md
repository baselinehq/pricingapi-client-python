# RegisteredComputePrices


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entries** | [**List[ComputePrice]**](ComputePrice.md) |  | [optional] 
**status** | [**RegistrationStatus**](RegistrationStatus.md) |  | [optional] 

## Example

```python
from pricing_api_client.models.registered_compute_prices import RegisteredComputePrices

# TODO update the JSON string below
json = "{}"
# create an instance of RegisteredComputePrices from a JSON string
registered_compute_prices_instance = RegisteredComputePrices.from_json(json)
# print the JSON string representation of the object
print(RegisteredComputePrices.to_json())

# convert the object into a dict
registered_compute_prices_dict = registered_compute_prices_instance.to_dict()
# create an instance of RegisteredComputePrices from a dict
registered_compute_prices_from_dict = RegisteredComputePrices.from_dict(registered_compute_prices_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


