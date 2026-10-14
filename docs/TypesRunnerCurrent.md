# TypesRunnerCurrent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cost** | **float** |  | [optional] 
**provider** | **str** |  | [optional] 
**sku** | **str** |  | [optional] 

## Example

```python
from pricing_api_client.models.types_runner_current import TypesRunnerCurrent

# TODO update the JSON string below
json = "{}"
# create an instance of TypesRunnerCurrent from a JSON string
types_runner_current_instance = TypesRunnerCurrent.from_json(json)
# print the JSON string representation of the object
print(TypesRunnerCurrent.to_json())

# convert the object into a dict
types_runner_current_dict = types_runner_current_instance.to_dict()
# create an instance of TypesRunnerCurrent from a dict
types_runner_current_from_dict = TypesRunnerCurrent.from_dict(types_runner_current_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


