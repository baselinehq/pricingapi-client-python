# ComputePricePage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ComputePrice]**](ComputePrice.md) |  | [optional] 
**page** | [**Page**](Page.md) |  | [optional] 

## Example

```python
from pricing_api_client.models.compute_price_page import ComputePricePage

# TODO update the JSON string below
json = "{}"
# create an instance of ComputePricePage from a JSON string
compute_price_page_instance = ComputePricePage.from_json(json)
# print the JSON string representation of the object
print(ComputePricePage.to_json())

# convert the object into a dict
compute_price_page_dict = compute_price_page_instance.to_dict()
# create an instance of ComputePricePage from a dict
compute_price_page_from_dict = ComputePricePage.from_dict(compute_price_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


