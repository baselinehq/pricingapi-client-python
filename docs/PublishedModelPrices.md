# PublishedModelPrices


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ModelPrice]**](ModelPrice.md) |  | [optional] 

## Example

```python
from pricing_api_client.models.published_model_prices import PublishedModelPrices

# TODO update the JSON string below
json = "{}"
# create an instance of PublishedModelPrices from a JSON string
published_model_prices_instance = PublishedModelPrices.from_json(json)
# print the JSON string representation of the object
print(PublishedModelPrices.to_json())

# convert the object into a dict
published_model_prices_dict = published_model_prices_instance.to_dict()
# create an instance of PublishedModelPrices from a dict
published_model_prices_from_dict = PublishedModelPrices.from_dict(published_model_prices_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


