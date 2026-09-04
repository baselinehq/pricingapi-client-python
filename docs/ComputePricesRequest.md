# ComputePricesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entries** | [**List[ComputePrice]**](ComputePrice.md) |  | 

## Example

```python
from pricing_api_client.models.compute_prices_request import ComputePricesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ComputePricesRequest from a JSON string
compute_prices_request_instance = ComputePricesRequest.from_json(json)
# print the JSON string representation of the object
print(ComputePricesRequest.to_json())

# convert the object into a dict
compute_prices_request_dict = compute_prices_request_instance.to_dict()
# create an instance of ComputePricesRequest from a dict
compute_prices_request_from_dict = ComputePricesRequest.from_dict(compute_prices_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


