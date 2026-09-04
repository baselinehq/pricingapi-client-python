# ModelPricesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entries** | [**List[ModelPrice]**](ModelPrice.md) |  | 

## Example

```python
from pricing_api_client.models.model_prices_request import ModelPricesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ModelPricesRequest from a JSON string
model_prices_request_instance = ModelPricesRequest.from_json(json)
# print the JSON string representation of the object
print(ModelPricesRequest.to_json())

# convert the object into a dict
model_prices_request_dict = model_prices_request_instance.to_dict()
# create an instance of ModelPricesRequest from a dict
model_prices_request_from_dict = ModelPricesRequest.from_dict(model_prices_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


