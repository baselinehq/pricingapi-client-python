# ModelPriceList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**providers** | [**List[ModelPrice]**](ModelPrice.md) |  | [optional] 

## Example

```python
from pricing_api_client.models.model_price_list import ModelPriceList

# TODO update the JSON string below
json = "{}"
# create an instance of ModelPriceList from a JSON string
model_price_list_instance = ModelPriceList.from_json(json)
# print the JSON string representation of the object
print(ModelPriceList.to_json())

# convert the object into a dict
model_price_list_dict = model_price_list_instance.to_dict()
# create an instance of ModelPriceList from a dict
model_price_list_from_dict = ModelPriceList.from_dict(model_price_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


