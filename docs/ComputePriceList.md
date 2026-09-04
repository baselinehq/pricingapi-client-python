# ComputePriceList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**providers** | [**List[ComputePrice]**](ComputePrice.md) |  | [optional] 

## Example

```python
from pricing_api_client.models.compute_price_list import ComputePriceList

# TODO update the JSON string below
json = "{}"
# create an instance of ComputePriceList from a JSON string
compute_price_list_instance = ComputePriceList.from_json(json)
# print the JSON string representation of the object
print(ComputePriceList.to_json())

# convert the object into a dict
compute_price_list_dict = compute_price_list_instance.to_dict()
# create an instance of ComputePriceList from a dict
compute_price_list_from_dict = ComputePriceList.from_dict(compute_price_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


