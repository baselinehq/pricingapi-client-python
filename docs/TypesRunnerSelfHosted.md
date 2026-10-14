# TypesRunnerSelfHosted


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**github_self_hosted_fee** | **bool** |  | [optional] 
**provider** | **str** |  | [optional] 
**region** | **str** |  | [optional] 

## Example

```python
from pricing_api_client.models.types_runner_self_hosted import TypesRunnerSelfHosted

# TODO update the JSON string below
json = "{}"
# create an instance of TypesRunnerSelfHosted from a JSON string
types_runner_self_hosted_instance = TypesRunnerSelfHosted.from_json(json)
# print the JSON string representation of the object
print(TypesRunnerSelfHosted.to_json())

# convert the object into a dict
types_runner_self_hosted_dict = types_runner_self_hosted_instance.to_dict()
# create an instance of TypesRunnerSelfHosted from a dict
types_runner_self_hosted_from_dict = TypesRunnerSelfHosted.from_dict(types_runner_self_hosted_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


