# TypesComputeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include_metadata** | **bool** |  | [optional] 
**instance** | [**GithubComBaselinehqGolangSharedTypesInstance**](GithubComBaselinehqGolangSharedTypesInstance.md) |  | [optional] 
**predicates** | [**TypesPredicates**](TypesPredicates.md) |  | [optional] 
**usage** | [**GithubComBaselinehqGolangSharedTypesVM**](GithubComBaselinehqGolangSharedTypesVM.md) |  | [optional] 

## Example

```python
from pricing_api_client.models.types_compute_request import TypesComputeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TypesComputeRequest from a JSON string
types_compute_request_instance = TypesComputeRequest.from_json(json)
# print the JSON string representation of the object
print(TypesComputeRequest.to_json())

# convert the object into a dict
types_compute_request_dict = types_compute_request_instance.to_dict()
# create an instance of TypesComputeRequest from a dict
types_compute_request_from_dict = TypesComputeRequest.from_dict(types_compute_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


