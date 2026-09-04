# PublishedComputePrices


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ComputePrice]**](ComputePrice.md) |  | [optional] 

## Example

```python
from pricing_api_client.models.published_compute_prices import PublishedComputePrices

# TODO update the JSON string below
json = "{}"
# create an instance of PublishedComputePrices from a JSON string
published_compute_prices_instance = PublishedComputePrices.from_json(json)
# print the JSON string representation of the object
print(PublishedComputePrices.to_json())

# convert the object into a dict
published_compute_prices_dict = published_compute_prices_instance.to_dict()
# create an instance of PublishedComputePrices from a dict
published_compute_prices_from_dict = PublishedComputePrices.from_dict(published_compute_prices_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


