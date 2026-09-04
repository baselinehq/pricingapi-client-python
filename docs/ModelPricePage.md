# ModelPricePage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ModelPrice]**](ModelPrice.md) |  | [optional] 
**page** | [**Page**](Page.md) |  | [optional] 

## Example

```python
from pricing_api_client.models.model_price_page import ModelPricePage

# TODO update the JSON string below
json = "{}"
# create an instance of ModelPricePage from a JSON string
model_price_page_instance = ModelPricePage.from_json(json)
# print the JSON string representation of the object
print(ModelPricePage.to_json())

# convert the object into a dict
model_price_page_dict = model_price_page_instance.to_dict()
# create an instance of ModelPricePage from a dict
model_price_page_from_dict = ModelPricePage.from_dict(model_price_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


