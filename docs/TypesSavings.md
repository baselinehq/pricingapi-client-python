# TypesSavings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount_per_hour** | **float** |  | [optional] 
**amount_per_month** | **float** |  | [optional] 
**amount_per_year** | **float** |  | [optional] 
**percentage** | **float** |  | [optional] 

## Example

```python
from pricing_api_client.models.types_savings import TypesSavings

# TODO update the JSON string below
json = "{}"
# create an instance of TypesSavings from a JSON string
types_savings_instance = TypesSavings.from_json(json)
# print the JSON string representation of the object
print(TypesSavings.to_json())

# convert the object into a dict
types_savings_dict = types_savings_instance.to_dict()
# create an instance of TypesSavings from a dict
types_savings_from_dict = TypesSavings.from_dict(types_savings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


