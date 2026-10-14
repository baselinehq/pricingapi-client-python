# TypesRunnerShape


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**arch** | **str** |  | [optional] 
**cpu_cores** | **int** |  | [optional] 
**gpu_count** | **int** |  | [optional] 
**os** | **str** |  | [optional] 
**ram_gb** | **float** |  | [optional] 

## Example

```python
from pricing_api_client.models.types_runner_shape import TypesRunnerShape

# TODO update the JSON string below
json = "{}"
# create an instance of TypesRunnerShape from a JSON string
types_runner_shape_instance = TypesRunnerShape.from_json(json)
# print the JSON string representation of the object
print(TypesRunnerShape.to_json())

# convert the object into a dict
types_runner_shape_dict = types_runner_shape_instance.to_dict()
# create an instance of TypesRunnerShape from a dict
types_runner_shape_from_dict = TypesRunnerShape.from_dict(types_runner_shape_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


