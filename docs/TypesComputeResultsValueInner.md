# TypesComputeResultsValueInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instance_pricing** | [**SchemaComputePricingsRow**](SchemaComputePricingsRow.md) |  | [optional] 
**savings** | [**TypesSavings**](TypesSavings.md) |  | [optional] 
**vm** | [**GithubComBaselinehqGolangSharedTypesVM**](GithubComBaselinehqGolangSharedTypesVM.md) |  | [optional] 

## Example

```python
from pricing_api_client.models.types_compute_results_value_inner import TypesComputeResultsValueInner

# TODO update the JSON string below
json = "{}"
# create an instance of TypesComputeResultsValueInner from a JSON string
types_compute_results_value_inner_instance = TypesComputeResultsValueInner.from_json(json)
# print the JSON string representation of the object
print(TypesComputeResultsValueInner.to_json())

# convert the object into a dict
types_compute_results_value_inner_dict = types_compute_results_value_inner_instance.to_dict()
# create an instance of TypesComputeResultsValueInner from a dict
types_compute_results_value_inner_from_dict = TypesComputeResultsValueInner.from_dict(types_compute_results_value_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


